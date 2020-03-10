% EMTH171
% Something here

clear
clc

t0 = 1;
x0 = 0.1;
y0 = 0.5;
h = 0.1;
tf = 1.5;

f = @(t0,x0,y0) y0*t0;
g = @(t0,x0,y0) x0-y0;
count = 2;
xArray(1) = x0;
yArray(1) = y0;
tArray(1) = t0;

for ii = t0:h:tf-h
    x0 = x0 + h*f(t0,x0,y0);
    y0 = y0 + h*g(t0,x0,y0);
    tArray(count) = t0;
    xArray(count) = x0;
    yArray(count) = y0;
    count = count + 1;
    t0 = t0 + h;
end
tArray
xArray
yArray
