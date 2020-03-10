% EMTH171
% Using all to compare errors

clear
clc

f = @(x) exp(2*x);
xMin = 2;
xMax = 5;
trueValue = (exp(2*5)/2)-(exp(2*2)/2);
for N = 10:200
    dx = (xMax-xMin)/N;
    [trapInt]=trapRule(f,xMin,xMax,dx);
    [lhInt]=leftHandRule(f,xMin,xMax,dx);
    [rhInt]=rightHandRule(f,xMin,xMax,dx);
    trapRes(N-9) = abs(trueValue-trapInt);
    lhRes(N-9) = abs(trueValue-lhInt);
    rhRes(N-9) = abs(rhInt-trueValue);
end
plot(10:200,trapRes,10:200,lhRes,10:200,rhRes)