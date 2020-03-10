% EMTH171
% Plotting functions to find roots

clear
clc
clear all

% Set up variables
f = @(x) 2 .* x.^4 - x .^ 3 - 4 .* x .^2 + 3 .* x - (2 / 5);

xMin = -2;
xMax = 2;
xStep = 0.1;

xArray = xMin : xStep : xMax;
yArray = f(xArray);

figure(1)
plot(xArray, yArray)