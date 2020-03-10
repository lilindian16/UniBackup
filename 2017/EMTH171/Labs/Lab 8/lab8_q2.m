% EMTH171
% Refresher on dot operators

clear
clc

% add a line below to define an anonymous function f
% as specified in the question

f = @(x) x.^2;
xArray = 1: 0.2 : 2;
yArray = f(xArray);

fprintf('%.4f\n', yArray);