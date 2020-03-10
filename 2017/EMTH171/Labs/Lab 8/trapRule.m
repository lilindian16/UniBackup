function [ integral ] = trapRule( f,a,b,dx )
%UNTITLED Summary of this function goes here
%   Detailed explanation goes here
% EMTH171
% Something here
integral = 0;
for ii = a+dx:dx:b-dx
    integral = integral + 2*f(ii);
end
integral = (integral + f(a) + f(b)) * (dx/2);

end

