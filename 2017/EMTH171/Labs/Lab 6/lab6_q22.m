% EMTH171
% Some more bollocks

clear
clc

x = 3;
c = -1;

f = @(x) 10*x.^2 - 10 .* x + 0.1*sinh(x) + c;
d = @(x) 20*x - 10 + 0.1 * cosh(x);

for ii = 1:5
    x = x - f(x)/d(x);
end

x
