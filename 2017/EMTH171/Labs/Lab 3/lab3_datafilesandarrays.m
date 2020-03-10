clear
clc

dataFilename = 'RainfallChCh2011.csv';
dataArray = load(dataFilename);


% Put columns in separate arrays

dayNum = dataArray(:,1);
dailyRainfall = dataArray(:,5);

plot(dayNum,dailyRainfall)