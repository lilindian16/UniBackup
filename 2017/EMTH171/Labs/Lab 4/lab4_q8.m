% EMTH171
% Comparing two variables

clear
clc

% Start variables

a= 0.0001;
b = 0.00011;
tol = 0.0001;

% Check the values against tolerance

checkValues = (b > tol) | (a > tol)