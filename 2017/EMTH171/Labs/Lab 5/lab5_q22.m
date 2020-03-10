function [ evens ] = evenElements( array )
%UNTITLED Summary of this function goes here
%   Detailed explanation goes here

evens = [];

for x = array
    if mod(x,2) == 0
        evens(x) = x;
    end
end
end


