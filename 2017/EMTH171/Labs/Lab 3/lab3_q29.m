% EMTH171/MATH170
% Part of a script to calculate and store
% terms in a power series 

clear
clc

x = 0.1; 
nTerms = 5; % number of terms
factorialSum = 2;
termsArray(1) = (x * 2);

% Start on the for loop
for ii = 2 : 1 : nTerms
    multiplier = (2 * ii - 1);
    factorialSum = factorialSum * (multiplier + 1) * multiplier;
    result = x ^ ii * factorialSum;
    termsArray(ii) = result;
    
end

% display arrays of terms
disp(termsArray);
