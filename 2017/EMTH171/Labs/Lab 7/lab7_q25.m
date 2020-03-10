% ENTH171
% Something here as well

clear;clc

t0 = 0;
tf = 15;
h = 0.01;
m0 = 1;
e0 = 1;

m = @(t0,m0,e0) 2/3*m0-4/3*m0*e0;
e = @(t0,m0,e0) -e0+m0*e0;
mArray(1)= m0;
eArray(1) = e0;
tArray(1) = t0;
count = 2;
for j = t0:h:tf-h
    tArray(count) = t0;
    m0 = m0 + h*m(t0,m0,e0);
    mArray(count) = m0;
    e0 = e0 + h * e(t0,m0,e0);
    eArray(count) = e0;
    count = count +1;
    t0 = t0 + h;
end

plot(tArray,mArray,tArray,eArray)

