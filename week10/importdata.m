experiment = importdata('radioactivedecay.dat')
t=experiment.data(:,1);
N=experiment.data(:,2);
figure(42)
plot(t,N,'.b')