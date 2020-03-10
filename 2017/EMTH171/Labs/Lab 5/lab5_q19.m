% EMTH171
% Anonymous handles with arrays

clear
clc

fHandle = @(x) 2 .* x .^ 3 - 4 .* x + 2;
inVal = [1 2 3];

fHandle(inVal)

