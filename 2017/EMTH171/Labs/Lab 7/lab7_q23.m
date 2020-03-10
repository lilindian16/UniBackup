% EMTH171
% Something here

clear
clc

t0 = 1;
x0 = 0.1;
y0 = 0.5;
h = 0.1;

f = @(t0,x0,y0) y0*t0;
g = @(t0,x0,y0) x0-y0;

t = t0 + h
x = x0 + h*f(t0,x0,y0)
y = y0 + h*g(t0,x0,y0)
