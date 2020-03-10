% EMTH171
% Comment

clear
clc

% Start variables

startValue = 1;
stopValue = 5;
stepValue = 1;
nTerms = 0;

% Start for loop

for ii = startValue : stepValue : stopValue
    answer = ii ^ 2;
    nTerms = nTerms + answer
end
