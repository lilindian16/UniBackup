% EMTH171
% Extreme factorials

clear
clc

% Start variables

x = 0.6;
nTerms = 20;

% Start for loop
term = 1;
sum = 1;

for n = 1 : 1 : nTerms 
    numerator = (-1) ^ n * x ^ (2 * n);
    term = term * 2 * n * (2 * n - 1);
    sum = sum + (numerator / term);
    term
   
end
cos(sum)
