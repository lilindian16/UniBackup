function [ origDisplacement ] = distanceFunction(beta, alpha)
%origDisplacement: This function takes a drag co-efficient and angle and
%outputs the total distance traveled by the car. Car details are given already

% Initialise variables
g = 9.81;	% Gravitational constant m/sec/sec
% Car constants
m = 760;		% Mass in kg
Jmotor = 25.5;      % Motor moment of intertia in kg.m^2
Jwheel = 10.0;      % Drive wheel moment of intertia in kg.m^2
fd0 = 180;		% Static (& low speed) drag force in N
km = 0.5;
rmotorS = 0.1; rwheelS = 0.15; rwheel = 0.25;	% Radii in m
% Parameters of the road for Task 0 and Simulation parameters
current = 650;		% Fixed motor current in A
sina = sin (alpha);     % sin(alpha) for 10 m down every km along
tdelta = 1.0;   % Time step in seconds
totCap = 38 * 5 * 3600; % Total capacity of the battery

% Calculate derived quantities
Tm = current * km;   % Fixed motor torque in N.m while current is applied
Jef = Jmotor + (rmotorS / rwheelS)^2 * (Jwheel + rwheel^2 * m); % Effective moment of intertia in kg.m^2
ratios = rmotorS / rwheelS * rwheel;  
% Initialise iterated variables
omega = 0;
dt = 0;
origVelocity = 0;
dtcons = 1; 
origDisplacement = 0;
r_wind = 0;
index = 1;

while dt < 30
    dwdt = 1 / Jef * (Tm - (ratios * (fd0 + (m * g * sina) + r_wind)));
    omegaNew = omega + tdelta * dwdt; % New acceleration
    velocityNew = omegaNew * ratios; % New velocity
    r_wind =(beta * velocityNew .^ 2); % New wind resistance
    displacementNew = origDisplacement + tdelta * (origVelocity + velocityNew)/2; % New distance
    omega = omegaNew;
    origVelocity = velocityNew; % Update arrays
    origDisplacement = displacementNew; %
    Varray(index) = origVelocity; %
    Darray(index) = origDisplacement; %
    index = index + 1;
    dt = dt + 1;
end
usedC = current * dt;
percentageLeft = usedC/totCap * 100;
remainingCapPercentage = 100 - percentageLeft;
Irequired =  (ratios * (fd0 + m * g * sina + beta * origVelocity.^2)) / km;

while remainingCapPercentage > 0 
    Tm = Irequired * km;
    dwdt = 1 / Jef * (Tm - (ratios * (fd0 + m * g * sina + (beta * origVelocity .^ 2))));
    omegaNew = omega + tdelta * dwdt;
    velocityNew = omegaNew * ratios;
    displacementNew = origDisplacement + tdelta * (origVelocity + velocityNew)/2;
    omega = omegaNew;
    origVelocity = velocityNew;
    origDisplacement = displacementNew;
    usedC = usedC + Irequired * dtcons;
    percentageLeft = usedC/totCap * 100;
    remainingCapPercentage = 100 - percentageLeft;
    Varray(index) = origVelocity;
    Darray(index) = origDisplacement;
    index = index + 1;
end
%----------Plotting----------%
figure(1)
plot (0:tdelta:tdelta * (index - 2), Varray)
grid on
figure(2)
plot (0:tdelta:tdelta * (index - 2), Darray)
grid on
end
