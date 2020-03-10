% EMTH171
% ODE and euler's formula

clear
clc

% Set up variables
k = -5*10^(-4);
f = @(t0,c) k*t0*c;
c = 55;
h = 1*10^(-2);
t0 = 0;


for x = 0:h:32
    c = c+h*f(t0,c);
    t0 = t0 + h;
end
c
    