function [ omega,origVelocity,origDisplacement ] = calculateDataStep(omega,origVelocity,origDisplacement,tdelta,beta,current)
%calculateDataStep: This function is what we use to save retyping the same code over and over again
% It calculates the new velocities and outputs them to be used in the next
% iteration
% Initialise variables
g = 9.81;	% Gravitational constant m/sec/sec
% Car constants
m = 760;		% Mass in kg
Jmotor = 25.5;      % Motor moment of intertia in kg.m^2
Jwheel = 10.0;      % Drive wheel moment of intertia in kg.m^2
fd0 = 180;		% Static (& low speed) drag force in N
km = 0.5;
rmotorS = 0.1; rwheelS = 0.15; rwheel = 0.25;	% Radii in m
ratios = rmotorS / rwheelS * rwheel; %Converts rad/s to mp/s
% Parameters of the road fof task 0 and 1
sina = sin (atan (-10 / 1000)); 
% Car parameterrs
Tm = current * km;   % Fixed motor torque in N.m while current is applied
Jef = Jmotor + (rmotorS / rwheelS)^2 * (Jwheel + rwheel^2 * m); % Effective moment of intertia in kg.m^2
fload = fd0 + m * g * sina;

% The calculations that are iteratively done each loop
dwdt = 1 / Jef * (Tm - (ratios * (fload + (beta * origVelocity ^ 2))));
omegaNew = omega + tdelta * dwdt;
velocityNew = omegaNew * ratios;
displacementNew = origDisplacement + tdelta * (origVelocity + velocityNew)/2;
omega = omegaNew;
origVelocity = velocityNew;  
origDisplacement = displacementNew;     
end

