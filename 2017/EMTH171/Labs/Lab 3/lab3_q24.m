% Plotting arrays
% EMTH171

clear
clc

% Start Variables

arrayX = [0: pi/16: 2*pi];
arrayY = sin(arrayX);

% Plot graphs

plot(arrayX,arrayY)
title('Plotting a sine curve') % add a title
xlabel('x') % x axis label
ylabel('sin(x)') % y axis label
