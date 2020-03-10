% EMTH171 Case Study 1
% Exercise 1: Electric motor pulling a sled
% Daniel Wadsworth and Jaime Sequeira
clear; clc; close all
 
% Set up variables, constants and power equations
theta = pi/4;           % Angle of incline (Radians)
gravConst = 9.81;       % Gravity constant (m/s^2)
rGB = 20;               % Gearbox ratio
alphaCons = 1;          % Alpha constant for finding power output of motor (Ws^2/rad^2)
betaCons = 100*pi;      % Beta constant for finding power output of motor (rad/s)
radiusPulley = 0.5;     % Radius of the pulley (m)
massCombined = 1000;    % Mass of the sled and load (kg)
cFriction = 0.2;        % Coefficient of friction used
 
% Function handles to deal with amount of power demanded and output by the system (all in watts)
 
outputEngine = @(v) alphaCons*((betaCons*rGB*v/radiusPulley)-...
    (rGB^2*v.^2/radiusPulley^2));                        
weightPower = @(v) massCombined*gravConst*sin(theta)*v;  
frictionPower = @(v) cFriction*massCombined*gravConst*cos(theta)*v;
totalPowerDemanded = @(v) weightPower(v) + frictionPower(v);   
 
f = @(v) totalPowerDemanded(v) - outputEngine(v);            
 
% Setting anonymous functions for derivatives of the functions above
derivOutput = @(v) alphaCons*((betaCons*rGB/radiusPulley)-...
    (2*rGB^2*v/radiusPulley^2));     
derivWeight = @(v) massCombined*gravConst*sin(theta);        
derivFriction = @(v) cFriction*massCombined*gravConst*cos(theta);
                         
d = @(v) derivWeight(v) + derivFriction(v) - derivOutput(v);  
 
% Plotting graph for engine power output against engine speed (rpm)
degreesToRadians = pi/30;                           % Convert angles to SI
enginePower = @(omega) (alphaCons*betaCons*omega)-(alphaCons*omega.^2);
omega = 0:3000;
plot(omega,enginePower(omega*degreesToRadians))
xlabel('Shaft speed (rpm)'); ylabel('Power output from motor (W)');grid on
 
 
% Plotting graph for all powers in w against v in m/s
v=0:0.001:12;                       % Creating data for the x axis
figure(2), plot(v,outputEngine(v),v,weightPower(v), ...
    v,frictionPower(v),v,totalPowerDemanded(v))
legend('Motor Output (W)', 'Gradient Power (W)', 'Friction Power (W)', 'Total Power Demand (W)')
ylim([0 40000]);
xlabel('Sled speed (m/s)');ylabel('Power (W)');grid on
 
% Iterating to find the roots using Newton's method
N = 50;                                     % Max number of iterations
root=2;                                     % The initial guess
velocityArray(1) = root;                    % Create array for v used
tol = 1* 10 ^(-4);                          % Tolerance for iterations
residualArray(1) = abs(0 - f(root));         
differenceArray = zeros(1, N);
             
for x=1:N
    root = root - (f(root)/d(root));        % Newton's method formula
    velocityArray(x+1) = root;               
    residualArray(x) = abs(0 - f(x));        
    differenceArray(x) = abs(velocityArray(x+1) - velocityArray(x));
    if abs(f(root)) < tol & abs(velocityArray(x+1) -...
 velocityArray(x)) < tol                % Checks if root is found
        break
    end
end
 
% Plotting convergence (v against f(v))
figure(3)
xAxis = 0:1:length(velocityArray)-1;
plot(xAxis,velocityArray)
xlabel('Number of iterations'), ylabel('v in m/s')
grid on; xticks([0:(length(velocityArray))])
 
% Plotting power against the number of iterations
figure(4)
xAxis = 0:1:length(velocityArray)-1;
plot(xAxis,f(velocityArray)),
xlabel('Number of iterations'), ylabel('f(v) in Watts')
grid on; xticks([0:length(velocityArray)])
