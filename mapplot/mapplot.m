hold off;
opts = detectImportOptions('C:\Users\carl\Downloads\NEIGHBORS.csv');
m = readtable('C:\Users\carl\Downloads\NEIGHBORS.csv', opts);
geoscatter(m.neighbor_lat(100:end), m.neighbor_lon(100:end), 80, m.SNR(100:end), '.');
geobasemap streets;
