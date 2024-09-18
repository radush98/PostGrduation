clear
clc

% Ïîñòğîåíèå S-ÁËÎÊÀ RIJNDAL
m=8; N=2^m; f=283; % ÍÅÏĞÈÂÎÄÈÌÛÅ ÏÎËÈÍÎÌÛ
disp(f);
a=gf(0:N-1, m, f); % İËÅÌÅÍÒÛ ÏÎËß Â ËÅÊÑÈÊÎÃĞÀÔÈ×ÅÑÊÎÌ ÏÎĞßÄÊÅ
k=a(1);



for i=2:N
k(i)=a(2)/a(i); % ÍÀÕÎÆÄÅÍÈÅ ÎÁĞÀÒÍÛÕ ÅËÅÌÅÍÒÎÂ
end

%-------------------------------
a1=double(k.x); 
%-------------------------------
distrib=zeros(1,8);
for vector=0:255

  r=dec2base(vector,16,2);  
    
m=['f8'; '7c'; '3e'; '1f'; '8f'; 'c7'; 'e1'; r];
m=de2bi(base2dec(m,16));


for i=1:256
    b(i)=bi2de(rem((m*de2bi(a1(i),8)')',2));
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
    distrib(8)= distrib(8)+1;
elseif max(size(find(mx(:,8)'>=128)))==7
    distrib(7)= distrib(7)+1;
elseif max(size(find(mx(:,8)'>=128)))==6
    distrib(6)= distrib(6)+1;
elseif max(size(find(mx(:,8)'>=128)))==5
    distrib(5)= distrib(5)+1;
elseif max(size(find(mx(:,8)'>=128)))==4
    distrib(4)= distrib(4)+1;
elseif max(size(find(mx(:,8)'>=128)))==3
    distrib(3)= distrib(3)+1;
elseif max(size(find(mx(:,8)'>=128)))==2
    distrib(2)= distrib(2)+1;
elseif max(size(find(mx(:,8)'>=128)))==1
    distrib(1)= distrib(1)+1;
end

end

