% EMTH171
% Finding all the even numbers in array
function [ resultArray ] = evenElements( array )
%UNTITLED Summary of this function goes here
%   Detailed explanation goes here
% Even more detail here 

fHandle = @(x) mod(x,2);
resultArray = fHandle(array);

end

