% EMTH171
% Jaime Sequeira and ...
% Case study 1
% Graph to plot the power output of motor

clear
clc
clear all

x = 0:3000;
f = @(x) 314.16.*(pi.*x./30)-(pi.*x./30).^2;
plot(x,f(x))

