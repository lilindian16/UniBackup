% EMTH171 Case Study One Exercise 1
% Daniel Wadsworth and Jaime Sequeira

clear; clc; close all

% Set up variables, constants and power equations
theta = pi/4;             % Angle of incline (Radians)
gravity = 9.81;           % Gravity constant (m/s^2)
rGB = 20;                 % Gearbox ratio
alphaCons = 1;            % Alpha constant for finding power output of motor (Ws^2/rad^2)
betaCons = 100*pi;        % Beta constant for finding power output of motor (rad/s)
radiusPulley = 0.5;       % Radius of the pulley (m)
massCombined = 1000;      % Mass of the sled and load (kg)
cFriction = 0.2;          % Coefficient of friction used

% Function handles to deal with amount of power for certain aspects to rig
outputEngine = @(v) alphaCons*((betaCons*rGB*v/radiusPulley)-...
    (rGB^2*v.^2/radiusPulley^2));                           % Power output by engine (W)
weightPower = @(v) massCombined*gravity*sin(theta)*v;     % Power required to overcome weight
frictionPower = @(v) cFriction*massCombined*gravity*...   % Power to overcome friction
    cos(theta)*v; 
totalPowerDemanded = @(v) weightPower(v) + frictionPower(v);   % Total power demanded
f = @(v) totalPowerDemanded(v) - outputEngine(v);              % Power demanded - output power

% Setting anonymous functions for derivatives of the functions above
derivOutput = @(v) alphaCons*((betaCons*rGB/radiusPulley)-...  % Derivative of the output fucntion
    (2*rGB^2*v/radiusPulley^2));        
derivWeight = @(v) massCombined*gravity*sin(theta);          % Derivative of the weight function
derivFriction = @(v) cFriction*massCombined*gravity*...      % Derivative of the friction funciton
    cos(theta);                           
d = @(v) derivWeight(v) + derivFriction(v) - derivOutput(v);   % Derivative of whole system

% Plottting graphs
v=0:0.001:12;                                % Creating data for the x axis
figure(1), plot(v,outputEngine(v),v,weightPower(v)...
    ,v,frictionPower(v),v,totalPowerDemanded(v))
legend('Motor Output (W)', 'Gradient Power (W)', 'Friction Power (W)', 'Total Power Demand (W)')
ylim = 100000;,title('Power demanded and output from the system')
xlabel('Sled speed (m/s)'),ylabel('Power (W)'),grid on

% Iterating to find the roots using Newton's method
N = 50;                                       % Maximum number of iterations
root=2;                                       % Sets up the intial guess
velocityArray(1) = root;                      % This is the first guess ie iteration 1
tol = 1* 10 ^(-4);                            % Tolerance for difference between two values
residualArray(1) = abs(0 - f(root));          % These arrays are set up for 
differenceArray = zeros(1, N);                % checking if the tolerance has been met
for x=1:N
    root = root - (f(root)/d(root));          % Newton's method formula
    velocityArray(x+1) = root;                % Puts all root gueses into array
    residualArray(x) = abs(0 - f(x));         % Calculates distance from root
    differenceArray(x) = abs(velocityArray(x+1) - velocityArray(x));
    if abs(f(root)) < tol & abs(velocityArray(x+1) - velocityArray(x)) < tol % Checks if root is found
        break
    end
end

% Plotting convergence (v against f(v))
figure(2)
xAxis = 0:1:length(velocityArray)-1;,plot(xAxis,velocityArray)
title('Convergence plot: V versus number of iterations')
xlabel('Number of iterations'), ylabel('v in m/s')
grid on, xticks([0:(length(velocityArray))])

% Plotting power against the number of iterations
figure(3)
xAxis = 0:1:length(velocityArray)-1;,plot(xAxis,f(velocityArray)),
title('Power f(v) versus number of iterations')
xlabel('Number of iterations'), ylabel('f(v) in Watts')
grid on, xticks([0:length(velocityArray)])

% EMTH 171 Case study exercise 2

%initilizing variables      	(Units)
mass = 1500;                	%(kg)
drag_coefficient = 0.30;    	%unitless
frontal_area =  2.0;        	%(m^2)
rolling_resistance = 0.010; 	%unitless
wheel_radius = 0.205;       	%(m)
alpha = 420;                	%(ws/rad)
beta = 0.440;               	%(ws^2/rad^2)
drive_ratio = 3.50;         	%unitless
gear_ratio = 0.80;          	%unitless
air_density = 1.2;          	%(kg/m^3)
K = wheel_radius / (drive_ratio * gear_ratio);  %(m)
 
degrees2radians = 2*pi/360; 	% constant for unit conversion
theta = 0;                  	%(rad)- initial gradient angle
theta = theta * degrees2radians;% puts theta in desired unit of radians
acceleration = 1;           	% (m/s^2)initial value of acceleration
 
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
figure(1)
v_kph = v * 3.6; % converts m/s to km/h
watt2kW = 1/1000; % conversion of watts to kilowatts
 
plot(v, engine_power(v)*watt2kW, ...
	v, power_to_overcome_drag(v)*watt2kW, ...
	v, power_to_overcome_rr(v)*watt2kW, ...
	v, power_to_overcome_gradient(v)*watt2kW, ...
	v, acceleration_power(v)*watt2kW, ...
	v, total_power_demand(v)*watt2kW)
legend('Engine power', ...
    	'Drag power', ...
    	'Rolling resistance', ...
    	'Gradient climing power', ...
    	'Acceleration power', ...
    	'Total power demand')
xlabel('Vehicle speed (m/s)')
ylabel('Aggregate Power Output (kW)')
xlim([0,80])
ylim= ([0 10])
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
N = 20;
x = 21;
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
 
% disp('Number of iterations');
% ii;
 
 
roots_array
error_array;
change_array;
 
 
 
 
%plot of approximate roots
figure(2)
plot(0:ii, roots_array)
title('Convergence plot: V vs number of iterations')
xlabel('Number of iterations')
xticks(0: length(roots_array))
ylabel('velocity (m/s)')
grid on
 
%plot of power
figure(3)
plot(0:ii, f(roots_array))
title('Power f(v) vs number of iterations')
xlabel('Number of iterations')
ylabel('f(v) in Watts')
xticks(0: length(roots_array))
ylim = 100;
grid on
 
 
f(roots_array);
 
% some testing stuff
% figure(7)
% plot(roots_array)
%  
% xmin = -10;
% xmax = 100;
% xstep = 0.1;
%  
% xarray = xmin: xstep: xmax;
% yarray = f(xarray);
% figure(8)
% title(func2str(f));
% plot(xarray,yarray);
% %ylim([-10,10]);
% grid on;
% xlabel = ('just an array');
% ylabel = ('function of array');
