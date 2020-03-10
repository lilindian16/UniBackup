%EMTH171
%Jaime Sequeira trials

clear
clc

% Start varaiables
nTerms = 5;
startValue = 2;
stepValue = 1;

% For loop starts here. This calculates the factorial sums for each number

partialsum = 1 %
partialSum = 1;

for x = startValue : stepValue : nTerms
    multiplier = (2 * x - 1);
    partialsum = partialsum * (multiplier - 1) * multiplier;
    partialSum = partialSum + partialsum
end


    
    