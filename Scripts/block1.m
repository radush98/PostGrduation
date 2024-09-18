function c=block1(in)

in1=[in, in];

bl=0;

for i=1:max(size(in))
    if in1(i)~=in1(i+1)
        bl=bl+1;
    end
            
end

u=1; k=1;
C=cell(1,bl);
for i=1:max(size(in))
    if in1(i)~=in1(i+1)
       C{1,u}=in1(k:i);
        u=u+1;
        k=i+1;
    end
            
end

%Исследование блочной структуры
for i=1:bl
    dlinu(i)=max(size(C{1,i}));
end

c=hist(dlinu, 1:max(dlinu));

end