clear
clc

g = @(x) (1 / 3) - (3 .* x / 4);
h = @(x) 2 .* sin(x .^ 2);


figure(1)
x = -2 : 0.1 : 4;
plot(x,g(x),x,h(x))
