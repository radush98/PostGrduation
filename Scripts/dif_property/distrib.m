function d=distrib(a)

d=zeros(1,8);
b=zeros(1,256);

for vector=0:255

  r=vector;  
    
m=[248; 124; 62; 31; 143; 199; 225; r];
m=de2bi(m);


for i=1:256
    b(i)=bi2de(rem((m*de2bi(a(i),8)')',2));
end

o=zeros(256,8);
F=zeros(8,256);
for i=1:256
    o(i,:)=de2bi(b(i),8);
end


F(1,:)=o(:,1)';
F(2,:)=o(:,2)';
F(3,:)=o(:,3)';
F(4,:)=o(:,4)';
F(5,:)=o(:,5)';
F(6,:)=o(:,6)';
F(7,:)=o(:,7)';
F(8,:)=o(:,8)';

for i=1:8
    mx(i,:)=differential(F(i,:));
end
mx=mx';

if max(size(find(mx(:,8)'>=128)))==8
    d(8)= d(8)+1;
elseif max(size(find(mx(:,8)'>=128)))==7
    d(7)= d(7)+1;
elseif max(size(find(mx(:,8)'>=128)))==6
    d(6)= d(6)+1;
elseif max(size(find(mx(:,8)'>=128)))==5
    d(5)= d(5)+1;
elseif max(size(find(mx(:,8)'>=128)))==4
    d(4)= d(4)+1;
elseif max(size(find(mx(:,8)'>=128)))==3
    d(3)= d(3)+1;
elseif max(size(find(mx(:,8)'>=128)))==2
    d(2)= d(2)+1;
elseif max(size(find(mx(:,8)'>=128)))==1
    d(1)= d(1)+1;
end

end
d=rot90(rot90(d));
end