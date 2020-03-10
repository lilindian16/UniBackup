% EMTH171
% Handles and other things

clear
clc

fHandle = @mean;
maxNData = 5;
resultArray = zeros(1,maxNData);

for x = 1 : maxNData
    myArray = rand(1,x);
    resultArray(x) = fHandle(myArray);
end
resultArray
    