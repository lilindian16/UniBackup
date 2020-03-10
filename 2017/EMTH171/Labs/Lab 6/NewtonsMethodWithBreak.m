% Here is some 
% explanation of what
% this function actually does

function [ rootsArray ] = NewtonsMethodWithBreak( guess, func, der, N, tol)
%UNTITLED4 Summary of this function goes here
%   Detailed explanation goes here

myArray(1) = guess;
residualArray(1) = abs(0 - func(guess));

for ii = 1 : N
    
    guess = guess - (func(guess)/der(guess));
    myArray(ii + 1) = guess;
    residualArray(ii + 1) = abs(0 - func(guess));
    differenceArray(ii) = abs(myArray(ii + 1) - myArray(ii));
     if abs(func(guess)) < tol & abs(myArray(ii + 1) - myArray(ii)) < tol
         break
     end
      
   
end

rootsArray = myArray;
end
