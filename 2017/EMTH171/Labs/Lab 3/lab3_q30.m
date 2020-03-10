% EMTH171
% Even harder partial sums, arrays and factorials

clear
clc

% Start variables

x = 1.6;
nTerms = 5;
factorial = 1;
termsArray = zeros(1, nTerms);
termsArray(1) = x ^ 2 / 1;
sum = 2.56;

% Start for loop

for ii = 2 : 1 : nTerms
    multiplier = (2 * ii - 1);
    factorial = factorial * (multiplier - 1) * multiplier;
    numerator = ((-1) ^ (ii + 1)) * (x ^ (2 * ii));
    result = numerator / factorial;
    termsArray(ii) = sum + result;
end

disp(termsArray)
    
    