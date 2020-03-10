% EMTH171 Case study 2 Task 0 and 1
% This script uses calculateDataStep function to find distances traveled by car
clear,clc

%Initial conditions (standing start)
index = 1;
omega = 0;       % Initial omega_m ('om')
origVelocity = 0;        % Speed along road in m/sec
origDisplacement = 0;        % Distance along road from start in m
tdelta = 1;                 % Step size for Euler's method
tf = 100;                   % Time when the current is turned off
% Start task 0(b)
for t = 1:tdelta:tf
    beta = 0; current = 100;  % Set wind resistance and current
    [omega,origVelocity,origDisplacement] = calculateDataStep(omega,origVelocity,origDisplacement,tdelta,beta,current);
    vLinear(index) = origVelocity;
    distanceArray(index) = origDisplacement;
    index = index + 1;
end
%Continues the calculation until the car stops
while (origVelocity > 0)
   current = 0; beta = 0;
   [omega,origVelocity,origDisplacement] = calculateDataStep(omega,origVelocity,origDisplacement,tdelta,beta,current);
   vLinear(index) = origVelocity;
   distanceArray(index) = origDisplacement;
   index = index + 1;
end
%----------Plotting-------%
figure(1)
plot ([0:tdelta:tdelta * (index - 2)], vLinear)
title('Task 0 (b): Velocity of car(m/s) against time(s)')
xlabel('Time (s)'), ylabel('Velocity(m/s)')
grid on
figure(2)
plot ([0:tdelta:tdelta * (index - 2)], distanceArray)
title('Task 0 (b): Distance traveled by car(m) against time(s)')
xlabel('Time(s)'), ylabel('Distance traveled(m)')
grid on

% Task 0(c) and reset all iterated values
omega = 0;
origVelocity = 0;
origDisplacement = 0;
index = 1;
beta = 0.31;     % Co-efficient of drag
current = 100;
for t = 1:tdelta:tf
    [omega,origVelocity,origDisplacement] = calculateDataStep(omega,origVelocity,origDisplacement,tdelta,beta,current);
    vLinearWind(index) = origVelocity;
    distanceArrayWind(index) = origDisplacement;
    index = index + 1;
end
current = 0;    % Current is switched off
while (origVelocity > 0)
   [omega,origVelocity,origDisplacement] = calculateDataStep(omega,origVelocity,origDisplacement,tdelta,beta,current);
   vLinearWind(index) = origVelocity;
   distanceArrayWind(index) = origDisplacement;
   index = index + 1;
end
%-----------Plotting---------%
figure(3)
plot ([0:tdelta:tdelta * (index - 2)], vLinearWind)
title('Task 0 (c): Velocity of car in m/s')
xlabel('Time(s)'), ylabel('Velocity(m/s)')
grid on
figure(4)
plot ([0:tdelta:tdelta * (index - 2)], distanceArrayWind)
title('Task 0 (c): Distance traveled in m')
xlabel('Time(s)'), ylabel('Distance traveled by car(m)')
grid on

% Start task 1 and reinitialise iterated values
omega = 0;
origVelocity = 0;
origDisplacement = 0;
index = 1;
beta = 0.31;
while origVelocity < (100 * 1000 / 3600)
    current = 100;
    [omega,origVelocity,origDisplacement] = calculateDataStep(omega,origVelocity,origDisplacement,tdelta,beta,current);
    vLinearWindNew(index) = origVelocity;
    distanceArrayWindNew(index) = origDisplacement;
    index = index + 1;
end
current = 114.8818; % Current required to maintain current origVelocity
while origDisplacement < 100
    [omega,origVelocity,origDisplacement] = calculateDataStep(omega,origVelocity,origDisplacement,tdelta,beta,current);
    vLinearWindNew(index) = origVelocity;
    distanceArrayWindNew(index) = origDisplacement;
    index = index + 1;
end
%----------Plotting-----------%
figure(5)
plot ([0:tdelta:tdelta * (index - 2)], vLinearWindNew)
title('Task 0 (c): Velocity of car in m/s')
xlabel('Time(s)'), ylabel('Velocity(m/s)')
grid on
figure(6)
plot ([0:tdelta:tdelta * (index - 2)], distanceArrayWindNew)
title('Task 0 (c): Distance traveled in m')
xlabel('Time(s)'), ylabel('Distance traveled by car(m)')
grid on