% EMTH171
% Something here

clear;clc

x0 = 4;
c = -5;
t0 = 0;
tf = 5;
h = 0.02;

f = @(t0,x0) 1/x0^3+t0^2+tanh(2*t0)+c;

for ij = t0:h:tf-h
    x0 = x0 + h*f(t0,x0);
    t0 = t0 +h;
end
x0