% EMTH171
% Drag force calculation for different velocities

clear 
clc

% Fixed parameters
rho = 1 * 10 ^ (-6); %density of air kg/m^3
areaBody = 1; %reference area m^2

% Info from experiment
Fe = 2 * 10 ^ 4; %drag force N
Ve = 100; %velocity in mph ( Needs to be changed to SI units!!!

%Calculate CD

CD = 2 * Fe / (rho * areaBody * (Ve * 0.447)^ 2);

% Calculate drag force for v = 20, 40 etc in mph
for v = 0 : 20 : 197
        F = CD * rho * areaBody * (v * 0.447)^ 2 / (2)
end



