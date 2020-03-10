% EMTH171/MATH170
% script to print values of sin(x)

clear
clc

startValue = pi;
stopValue = 5*pi/4;
stepValue = 0.2;
% ** uncomment and complete the definition of stepValue below ** %
% stepValue = ??;

% ********* add your code to complete the question ********* %
for ii = startValue : stepValue : stopValue
    sin(ii)
end
