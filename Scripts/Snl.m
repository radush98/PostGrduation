function [out]=Snl(in)

s=max(size(in));

out=zeros(s,log2(s));   
F=zeros(log2(s),s);
for i=1:s
    out(i,:)=de2bi(in(i),log2(s));
end

for i=1:log2(s)
F(i,:)=out(:,i)';
end


for i=1:log2(s)
    n(i)=nonlin(F(i,:));
%     [xexs, deg1(i)]=ANF(F(i,:));
end

out=min(n);
% deg=min(deg1(i));