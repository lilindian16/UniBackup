% EMTH171
% Plotting some weird graph

clear
clc

fHandle = @mean;
maxNData = 1000;

resultArray = zeros(1,maxNData);

for x = 1 : maxNData
    myArray = rand(1,x);
    resultArray(x) = fHandle(myArray);
end

xAxis = 1 : 1 : maxNData;
figure
plot(xAxis, resultArray)

title('Data summary using mean');
xlabel('Number of data values');
ylabel('mean');



