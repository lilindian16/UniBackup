% EMTH171
% Some other stuff here

clear
clc
clear all

% Start variables

g = @(x) 1/3 - (3.*x./4);
dg = @(x) -3/4;
h = @(x) 2*sin(x.^2);
dh = @(x) 4.*x*cos(x.^2);
x = -1;
N = 20;
tol = 0.1;



f = @(x)  g(x)-h(x);
d = @(x) dg(x)-dh(x);

myArray(1) = x;
count = 2;

residualArray(1) = abs(0 - f(x));
differenceArray = zeros(1, N);
tol = 1* 10 ^(-2);

% Start for loop

for ii = 1 : N
     x = x - (f(x) / d(x));
     myArray(count) = x;
     residualArray(count) = abs(0 - f(x));
     differenceArray(ii) = abs(myArray(count) - myArray(count - 1));
     if abs(f(x)) < tol & abs(myArray(count) - myArray(count-1)) < tol
         break
     end
     
     count = count + 1;
     
end

final = myArray(length(myArray))
g(x)


