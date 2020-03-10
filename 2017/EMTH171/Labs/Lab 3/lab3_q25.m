% EMTH171
% Dealing with loding data into arrays

clear
clc

% Open the file and load the data

dataFilename = 'AIRNZ.csv';
inFile = load(dataFilename);

% Split the data into appropriate variables

dayNumArray = inFile(:,1);
sharePriceArray = inFile(:,2);