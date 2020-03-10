% EMTH171
% Something here
clear
clc

% Initialise variables
g = 9.81;	% Gravitational constant m/sec/sec
% Car constants
m = 760;		% Mass in kg
Jmotor = 25.5;      % Motor moment of intertia in kg.m^2
Jwheel = 10.0;      % Drive wheel moment of intertia in kg.m^2
fd0 = 180;		% Static (& low speed) drag force in N
beta = 0.31;    % Wind resistance factor in N / (m/sec)^2			
km = 0.5;		% Motor factor in N.m per amp
rmotorS = 0.1;	
rwheelS = 0.15;	
rwheel = 0.25;	% Radii in m

% Parameters of the road for Task 0
% Simulation parameters
current = 100;		% Fixed motor current in A
tf = 100;       % Time in seconds when the current is switched off
sina = sin (atan (-10 / 1000));     % sin(alpha) for 10 m down every km along
tdelta = 1.0;   % Time step in seconds
% Calculate derived quantities
Tm = current * km;   % Fixed motor torque in N.m while current is applied
Jef = Jmotor + (rmotorS / rwheelS)^2 * (Jwheel + rwheel^2 * m); % Effective moment of intertia in kg.m^2
N = tf / tdelta + 1;
vLinear = zeros (1, N);
distanceArray = zeros (1, N);
% Initial conditions (standing start)
omega = 0;       % Initial omega_m ('om')
origVelocity = 0;        % Speed along road in m/sec
origDisplacement = 0;        % Distance along road from start in m
fload = fd0 + m * g * sina;
index = 1;

% Task 0 (a) straight forward calculation for ditance traveled with integration
% Angular velocity changed to linear * time^2 / 2 
distanceInt = 1 / Jef * (Tm - (rmotorS / rwheelS * rwheel * fload))* rmotorS / rwheelS * rwheel * 100^2 / 2


for t = tdelta:tdelta:tf
    dwdt = 1 / Jef * (Tm - (rmotorS / rwheelS * rwheel * fload))  % Function for constant acceleration of motor
    omegaNew = omega + tdelta * dwdt;    % Estimate om by Euler's method
    velocityNew = omegaNew * rmotorS / rwheelS * rwheel; % Estimate u at end of step
    displacementNew = origDisplacement + tdelta * (origVelocity + velocityNew)/2; % Estimate s at end of step by trapezoidal integration
    vLinear(index) = origVelocity;
    distanceArray(index) = origDisplacement;
    index = index + 1;
    omega = omegaNew; % Advance to next time step
    origVelocity = velocityNew;     %
    origDisplacement = displacementNew;     %
end

distanceArray

% Recompute the (fixed) motor acceleration with no motor torque
Tm = 0;
dwdt = (Tm - rmotorS / rwheelS * rwheel * fload) / Jef;

while (velocityNew > 0)
   % Estimate the state at the end of the time step (n = 'next')
   omegaNew = omega + tdelta * dwdt;    % Estimate om by Euler's method
   velocityNew = omegaNew * rmotorS / rwheelS * rwheel;      % Estimate u at end of step
   displacementNew = origDisplacement + tdelta * (origVelocity + velocityNew)/2; % Estimate s at end of step by trapezoidal integration
   vLinear(index) = origVelocity;
   distanceArray(index) = origDisplacement;
   index = index + 1;
   omega = omegaNew;   		% Advance to next time step
   origVelocity = velocityNew;     		%
   origDisplacement = displacementNew;     		%
   t = t + tdelta;	%
end

% figure(1)
% plot ([0:tdelta:tdelta * (index - 2)], vLinear)
% title('Task 0 (b): Velocity of car(m/s) against time(s)')
% xlabel('Time (s)')
% ylabel('Velocity(m/s)')
% grid on
% 
% figure(2)
% plot ([0:tdelta:tdelta * (index - 2)], distanceArray)
% title('Task 0 (b): Distance traveled by car(m) against time(s)')
% xlabel('Time(s)')
% ylabel('Distance traveled(m)')
% grid on

% Part C which takes wind resistance into account
omega = 0;
origDisplacement = 0;
t = 0;
velocityNew = 0;
index = 1;
Tm = current * km;

for t = tdelta:tdelta:tf
    dwdt = 1 / Jef * (Tm - (rmotorS / rwheelS * rwheel * (fload + (beta * origVelocity ^ 2))));  % Function for changing acc of motor
    omegaNew = omega + tdelta * dwdt;    % Estimate om by Euler's method
    velocityNew = omegaNew * rmotorS / rwheelS * rwheel; % Estimate u at end of step
    displacementNew = origDisplacement + tdelta * (origVelocity + velocityNew)/2; % Estimate s at end of step by trapezoidal integration
    vLinearWind(index) = origVelocity;
    distanceArrayWind(index) = origDisplacement;
    index = index + 1;
    omega = omegaNew;   % Advance to next time step
    origVelocity = velocityNew   %
    origDisplacement = displacementNew;     %
end

Tm = 0; % No torque provided by motor when current is turned off

while (velocityNew > 0)
   dwdt = 1 / Jef * (Tm - (rmotorS / rwheelS * rwheel * (fload + (beta * origVelocity ^ 2))));
   % Estimate the state at the end of the time step (n = 'next')
   omegaNew = omega + tdelta * dwdt;    % Estimate new omega by Euler's method
   velocityNew = omegaNew * rmotorS / rwheelS * rwheel;      % Estimate new linear velocity at end of step
   displacementNew = origDisplacement + tdelta * (origVelocity + velocityNew)/2; % Estimate deisplacement at end of step by trapezoidal integration
   vLinearWind(index) = origVelocity;
   distanceArrayWind(index) = origDisplacement;
   index = index + 1;
   omega = omegaNew;   		% Advance to next time step
   origVelocity = velocityNew;     		%
   origDisplacement = displacementNew;     		%
   t = t + tdelta;	%
end

t

figure(3)
plot ([0:tdelta:tdelta * (index - 2)], vLinearWind)
title('Task 0 (c): Velocity of car in m/s')
xlabel('Time(s)')
ylabel('Velocity(m/s)')
grid on

figure(4)
plot ([0:tdelta:tdelta * (index - 2)], distanceArrayWind)
title('Task 0 (c): Distance traveled in m')
xlabel('Time(s)')
ylabel('Distance traveled by car(m)')
grid on

% % Task 1 (a)
% omega = 0;
% origDisplacement = 0;
% t = 0;
% omegaNew = 0;
% velocityNew = 0;
% displacementNew = 0;
% index = 1;
% current = 125;
% Tm = current * km;
% 
% 
% %Calculating current required to maintain this velocity
% kmh2mps = 100/360;
% current = (rmotorS / rwheelS * rwheel * (fload + (beta * (100*kmh2mps) ^ 2)) /km);
% dwdt = 1 / Jef * ((current*km) - (rmotorS / rwheelS * rwheel * (fload + (beta * 100*kmh2mps ^ 2))));
% 
% totalCap = 38 * 5; % Max current produced in one hour
% dcapdt = totalCap * 3600;
%     
