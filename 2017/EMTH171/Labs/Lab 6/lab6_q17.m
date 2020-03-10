% EMTH171
% Script use NewtonsMethodWithBreak function
% fix required 
 
clear 
clc 
 
% ----------------------- variables -------------------- 
% function to find root of 
f = @(x) cos(7*x) + x/3; 
% derivative of f 
d = @(x) -7*sin(7*x) + 1/3; 
 
% ------------------- Newtons method ----------------- 
x = -3; % first guess 
N = 20; % number of iterations 
tol = 1e-4;
 
rootsArray = NewtonsMethodWithBreak( x, f, d, N , tol); 

finalRoot = rootsArray(end);

% display final root found
fprintf('Root found %.4f\n', finalRoot);

% Sanity check:  what is f(x) at this approx?
fValue = f(finalRoot);
fprintf('f(final root)= %.4f\n', fValue);