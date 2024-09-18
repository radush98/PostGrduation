function out=polymult(a,b)

da=max(size(a));
db=max(size(b));

out=zeros(1,da+db-1);
for k=1:da+db-1
    j=1;
while (k-j+1)>=1
    if k-j+1<=db && j<=da
   out(k)=add2(out(k),mul2(a(j),b(k-j+1)));
    end
   j=j+1;
end

end

end