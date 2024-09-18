function result=add2(a,b)

for i=1:max(size(a))
    result(i)=bi2de(bitxor(de2bi(a(i),256), de2bi(b(i),256)));
end

end