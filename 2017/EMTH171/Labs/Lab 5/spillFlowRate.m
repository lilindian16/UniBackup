% EMTH171
% Function to find the flow rate blah blah blah
% Some more blah blah blah
function [ fSpill ] = spillFlowRate( currentHeight, maxHeight, constant, length )
% The returned units are in m^3 per s
% Harambe balh blah blah
% Blah blah peace blah

if currentHeight <= 0
    fSpill = 0;
else
    fSpill = constant * length * (abs(currentHeight - maxHeight)) ^ 1.5;
end

end

