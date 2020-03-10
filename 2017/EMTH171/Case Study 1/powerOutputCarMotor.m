clear
clc


x=0:8000;

f=@(x) (440.*(pi.*x./30))-0.44*((pi.*x./30).^2);
plot(x,f(x)/1000)
xlabel('Engine speed (rpm)')
ylabel('Power output (kw)')
title('Car motor power output')
grid on