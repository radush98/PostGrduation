q=3;
n=5;

v=divisor(n);
neprivod=0;
for i=1:max(size(v))
neprivod=neprivod + (moebiusmu(v(i))*q^(n/v(i)));
end
neprivod=neprivod/n;
primitive=totient((q^n)-1)/n;

neprivod
primitive
