% EMTH171
% Something here

clear
clc

temp = 100;
t0 = 0;
ta = 20;
targetTemp = 40;
h = 0.01;
r = 0.043;
tf = 80;
f = @(t0,temp) -r*temp*ta;

for j = t0:h:tf
    temp = temp + h*f(t0,temp);
    t0 = t0 + h;
    if temp == targetTemp
        break
    end    
end
temp

