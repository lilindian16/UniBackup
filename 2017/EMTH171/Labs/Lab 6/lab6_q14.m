% EMTH171
% Finally using Newton's method

clear
clc

% Start variables

f = @(x)  2 .* x .^ 4 - x .^ 3 - 4 .* x .^ 2 + 3.* x - (2 / 5);
d = @(x) 8 .* x .^ 3 - 3.* x .^ 2 - 8.* x + 3;
x = 2;
N = 20;


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

final = myArray(length(myArray));
iterations = count - 1;
if abs(f(x)) < tol & abs(myArray(count) - myArray(count-1)) < tol
    disp('Convergence has been reached')
else
    disp('Convergence has not been reached')
end






