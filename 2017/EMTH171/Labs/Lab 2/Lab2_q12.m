% EMTH171
% Sums the integers from 13 to 56 (inclusive)

clear
clc

% Set up variables
startValue = 13;
stopValue = 56;
stepValue = 1;

total = 0;

% Start for loop

for ii = startValue : stepValue : stopValue
    total = total + ii;
end
total

