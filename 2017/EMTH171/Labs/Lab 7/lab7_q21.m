% EMTH171
% Some other stuff

clear
clc

t0 = 1;
x0 = 0.1;
y0 = 0.5;

f = @(t0,x0,y0) y0*t0;
g = @(t0,x0,y0) x0-y0;

f(t0,x0,y0)
g(t0,x0,y0)