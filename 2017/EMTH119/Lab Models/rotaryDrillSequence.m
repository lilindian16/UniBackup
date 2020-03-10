% EMTH119
% Rotary drill sequence

clear
clc


x = 0.2;
count = 1;
for ii = 1:0.001:2
    
    if x <= 1/4
        x = x +1 - 3*sqrt(2*x/3);
        xArray(count) = x;
        count = count + 1;
    else
        x = x + 0.5 -1.5*sqrt((4*x-1)/3);
        xArray(count) = x;
        count = count + 1;
    end
end

xaxis = 1:0.0001:2;

plot(xaxis,x)
