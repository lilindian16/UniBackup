% EMTH171
% Something here

clear
clc

f = @(x) x.^3;
a = -2;
b = 1;
dx = 1e-2; 
sum = 0;
for ii = a+dx:dx:b-dx
    sum = sum + 2*f(ii);
end
sum = (sum + f(a) + f(b)) * (dx/2)