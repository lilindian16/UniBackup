% EMTH171
% Something here

clear
clc

f = @(x) 22 - 3*x.^2;
xMin = -6;
xMax = 4;
dx = 0.01;

totalArea = 0;
for jj = xMin + dx:dx:xMax
    area = (jj - (jj - dx)) * f(jj-dx);
    totalArea = totalArea + area;
end
totalArea
    