function a=s2n(b)
[g1, g2]=size(b);
a=zeros(g1,g2);
for i=1:g1
    for j=1:g2
    if b(i,j)=='1'
        a(i,j)=1;
    elseif b(i,j)=='0'
        a(i,j)=0;
    end
    end
end
end
        