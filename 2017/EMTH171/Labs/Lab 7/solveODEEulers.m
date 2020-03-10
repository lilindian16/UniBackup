function [ tArray, xArray ] = solveODEEulers( f,t0,x0,tf,h )
%UNTITLED2 Summary of this function goes here
%   Detailed explanation goes here
% Something here

% Set up variables
timeArray(1) = t0;
xArray(1) = x0;
count = 2;

for x=t0+h:h:tf    
    x0 = x0 + h * f(t0,x0);
    t0 = t0 + h;
    timeArray(count) = t0;
    xArray(count) = x0;
    count = count + 1;
end

tArray = timeArray;
xArray;


end

