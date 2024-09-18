function L=Lmx(k)
L=[1 0; 1 1];
for i=2:k
    L=[L zeros(2^(i-1)); L L];
end
end