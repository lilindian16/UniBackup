% EMTH171
% Something here

clear
clc

a=3;
b=4;
dx = 2*10^(-1);

f = @(x) 22-3*x.^2;

x=a:dx:b
y=f(x)