% EMTH171
% Explain somehting hererererere
% Eerererererererer
function [ result ] = finiteDerivativeApprox( f, x )
%UNTITLED3 Summary of this function goes here
%   Detailed explanation goes here
h = 1 * 10 ^ (-6);

result = (f(x + h) - f(x)) / h;


end

