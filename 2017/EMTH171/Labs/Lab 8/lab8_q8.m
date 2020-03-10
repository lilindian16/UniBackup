% EMTH171
% Something here

clear
clc

f = @(x) sin(x)/3;
a = 0;
b = pi;
dx = 1e-2;
x=a:dx:b;
sum = 0;
for j = a+dx:dx:b-dx
    sum = sum + f(j);
end
sum

