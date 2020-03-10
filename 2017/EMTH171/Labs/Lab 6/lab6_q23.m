% EMTH171
% Some more bollocks

clear
clc

x = 3;


start = -10;
stop = -1;

for j = start:stop
    for ii = 1:5
        c = j;
        f = @(x) 10*x.^2 - 10 .* x + 0.1*sinh(x) + c;
        d = @(x) 20*x - 10 + 0.1 * cosh(x);
        x = x - f(x)/d(x);
    end
    cArray(j+11) = x;
end

figure(1)
xAxis = 1:length(cArray);
plot(xAxis,cArray)