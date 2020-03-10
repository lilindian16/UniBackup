% EMTH171
% Sum even numbers in a given range

clear
clc

% Set up variables
startValue = 12;
stopValue = -7;
stepValue = -2;

% Start for loop
total = 0;
for ii = startValue : stepValue : stopValue
    total = total + ii;
end
total
