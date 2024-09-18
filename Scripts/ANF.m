function [xexs, degree]=ANF(out)

s=max(size(out));

%��������� ������� ��������������
L=Lmx(log2(s));

%��������� ������������ �������� ������� � ������� ��������������
a=mod(L*out',2)';

%������������ ��������� ����
for i=1:s
lin(i,1:log2(s))=bitget(i-1, 1:log2(s));
end


%���������� ������������ ������
k=1;
for i=1:s
    if a(i)==1
        term(k,:)=lin(i,:);
        k=k+1;
    end
end
degree=max(sum(term,2));

%������������ ������
if a(1)==1
xexs='1+';
term(1,:)=[];
elseif a(1)==0
    xexs='';
end

[s1 s3]=size(term);

for j=1:s1
xex=find(term(j,:)==1);
%�������������� � ������


for i=1:max(size(xex))
    xexs=strcat(xexs, strcat('x',num2str(xex(i))));
end

xexs=strcat(xexs, '+');

end
    
if xexs(end)=='+'
   xexs(end)=[];
end


