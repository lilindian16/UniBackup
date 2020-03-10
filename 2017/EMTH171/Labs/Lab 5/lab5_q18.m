% EMTH171
% Anonymous functions handles

clear
clc

fHandle = @(x) x ^ 2 + 2 * x + 1;

inVal = 5;

fHandle(inVal)