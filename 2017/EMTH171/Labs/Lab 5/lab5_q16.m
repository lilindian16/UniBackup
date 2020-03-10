% EMTH171/MATH170
% demonstrate function handles with plotting and fminbnd

clear
clc
close all

fHandle = @wiggleFun; % handle for function f

x = pi/6;
minx = -pi; 
maxx = pi;

% Evaluate f at x
y = fHandle(x) % find and display y = f(x)

% arrays for plotting
xArray = minx : pi/64 : maxx;
yArray = fHandle(xArray);

figure(1) % plot them
plot(xArray, yArray)

% Find x such that f(x) is a minimum of f in specified interval 
fmin_x = fminbnd(fHandle, minx, maxx) % find and display minimising x