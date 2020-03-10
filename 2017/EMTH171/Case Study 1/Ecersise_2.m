% Case study part two
% Car motor power 
clc; clear; close all;
% Initilizing variables      	(Units)
mass = 1500;                	%(kg)
drag_coefficient = 0.30;    	%unitless
frontal_area =  2.0;        	%(m^2)
rolling_resistance = 0.010; 	%unitless
wheel_radius = 0.205;       	%(m)
alpha = 420;                	%(ws/rad)
beta = 0.440;               	%(ws^2/rad^2)
drive_ratio = 3.50;         	%unitless
gear_ratio = 0.80;          	%unitless
gravity = 9.81;             	%(m/s^2)
air_density = 1.2;          	%(kg/m^3)
K = wheel_radius / (drive_ratio * gear_ratio);  %(m)
% Variables that change for each case
degrees2radians = 2*pi/360; 	% constant for unit conversion
theta = 0;                  	%(rad)- initial gradient angle
theta = theta * degrees2radians;% puts theta in desired unit of radians
acceleration = 1;           	% (m/s^2)initial value of acceleration

% Information for plotting first graph
to_rpm = 60 / (2*pi);         % Converts m/s into rpm
watt2kW = 1/1000;           
omega = 1:733;              
engine_power_rpm = ((alpha .* omega) - (beta .* omega.^2));
figure(1)
plot(omega*to_rpm, engine_power_rpm*watt2kW)
ylim([0,120])
xlim([0,8000])
xlabel('Engine speed/rpm')
ylabel('Power output/kW')
grid on
 
%function handles (all units in watts):
power_to_overcome_drag = @(v) drag_coefficient * frontal_area ./ 2 .* air_density .* v.^3;
gravity_component = @(v) mass .* gravity .* sin(theta).* v;
power_to_overcome_rr = @(v) rolling_resistance .* mass .* gravity .* cos(theta) .* v;
max_speed = @(v) mass .* acceleration .* v;
engine_power = @(v) ((alpha .* v ./ K) - (beta .* v.^2 ./ K .^ 2));
power_to_overcome_gradient = @(v) mass * gravity * sin(theta) * v;
acceleration_power = @(v) mass * acceleration * v;
total_power_demand = @(v) gravity_component(v) + power_to_overcome_drag(v) + power_to_overcome_rr(v) + acceleration_power(v);
 
% information for plotting power vs speed
v = 0:100;
figure(2)
v_kph = v * 3.6; % converts m/s to km/h
watt2kW = 1/1000; % conversion of watts to kilowatts

plot(v, engine_power(v)*watt2kW, ...
	v, power_to_overcome_drag(v)*watt2kW, ...
	v, power_to_overcome_rr(v)*watt2kW, ...
	v, power_to_overcome_gradient(v)*watt2kW, ...
	v, acceleration_power(v)*watt2kW, ...
	v, total_power_demand(v)*watt2kW)
legend('Engine power','Drag power','Rolling resistance', ...
    	'Gradient climing power','Acceleration power','Total power demand')
xlabel('Vehicle speed (m/s)')
ylabel('Aggregate Power Output (kW)')
ylim([0,120])
xlim([0,80])
grid on
 
%engine power is:
f = @(v) power_to_overcome_drag(v) + gravity_component(v) + power_to_overcome_rr(v) ...
	+ max_speed(v) - engine_power(v);
 
% derivatives function handles
d_power_to_overcome_drag = @(v) 3 .* drag_coefficient .* frontal_area ./ 2 .* air_density .* v.^2;
d_gravity_component = @(v) mass .* gravity .* sin(theta);
d_power_to_overcome_rr = @(v) rolling_resistance .* mass .* gravity .* cos(theta);
d_max_speed = @(v) mass .* acceleration;
d_engine_power = @(v) ((alpha ./ K) - (2 .* beta .* v ./ K .^ 2));
 
d = @(v) d_power_to_overcome_drag(v) + d_gravity_component(v) + d_power_to_overcome_rr(v) ...
	+ d_max_speed(v) - d_engine_power(v);
 
%initilizing variabels for Newtons Method
N = 20;                               %max number of iterations
x = 21;                               %set up initial guess
tol = 1*exp(-4);
 
%initilizing arrays for Newtons Method
roots_array = zeros();
error_array = zeros();
change_array = zeros();
roots_array(1) = x;
error_array(1) = abs(f(x));
  
%iterations of Newtons Method
for ii = 1: N
	x = x - f(x)/d(x);
	roots_array(ii+1) = x;
	error_array(ii+1) = abs(f(x));
	change_array(ii) = abs(x - roots_array(ii));
	if error_array(ii+1) < tol && change_array(ii) < tol
    	break
	end
end

%plot of approximate roots
figure(3)
plot(0:ii, roots_array)
title('Convergence plot: V vs number of iterations')
xlabel('Number of iterations')
xticks(0: length(roots_array))
ylabel('velocity (m/s)')
grid on
 
%plot of power
figure(4)
plot(0:ii, f(roots_array))
title('Power f(v) vs number of iterations')
xlabel('Number of iterations')
ylabel('f(v) in Watts')
xticks(0: length(roots_array))
ylim = 100;
grid on
