function [ lhInt ] = leftHandRule( f,xMin,xMax,dx )
%UNTITLED2 Summary of this function goes here
%   Detailed explanation goes here

totalArea = 0;
for jj = xMin + dx:dx:xMax
    area = (jj - (jj - dx)) * f(jj-dx);
    totalArea = totalArea + area;
end
lhInt = totalArea;  
end

