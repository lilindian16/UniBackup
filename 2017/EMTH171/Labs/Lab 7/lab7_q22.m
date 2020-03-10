% EMTH171
% Something here

clear
clc

t0 = 0;
x0 = 0.2;
y0 = 0.7;

f = @(t0,x0,y0) 3*y0-2*x0*y0;
g = @(t0,x0,y0) 4*x0*y0-7*x0;

f(t0,x0,y0)
g(t0,x0,y0)