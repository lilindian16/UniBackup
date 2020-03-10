% EMTH171
% Calculating product of numbers in a range

clear
clc

% Set up variables
startValue = 3;
stopValue = 9;
stepValue = 1;
product = 1;

% Start for loop
for ii = startValue : stepValue : stopValue
    product = product * ii;
end
product