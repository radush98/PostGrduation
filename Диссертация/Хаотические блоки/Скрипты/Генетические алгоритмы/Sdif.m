function mx=Sdif(a)

s=max(size(a));

o=zeros(s,log2(s));
F=zeros(log2(s),s);
for i=1:s
    o(i,:)=de2bi(a(i),log2(s));
end

for i=1:log2(s)
F(i,:)=o(:,i)';
end

for i=1:log2(s)
    mx(i,:)=differential(F(i,:));
end
mx=(mx');

