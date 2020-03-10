% EMTH171
% Something here

clear
clc

s=load('VariableDensityRodData12.csv');
distanceOrigin = s(:,1);
density = s(:,2).*1000;
area = s(:,3).*0.0001;

for j = 0:len(