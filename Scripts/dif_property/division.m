function r=division(a,b)

a1=a;


%��������� ����� � ������������
for i=max(size(b)):-1:1
    if b(i)==0
        b(i)=[];
    else
        break;
    end
end

%��������� ����� � ����������
for i=max(size(a)):-1:1
    if a(i)==0
        a(i)=[];
    else
        break;
    end
end


[nul da]=size(a);
[nul db]=size(b);

if da>db

while max(size(a))>=max(size(b))
[nul da1]=size(a);
pribl=b; 
while max(size(pribl))~=max(size(a))
    pribl=conv(pribl, [0 1]);
end
%��������� �� ������� ���������
el=0; pribl1=pribl;
    while pribl1(end)~=a(end)
for i=1:da1
pribl1(i)=mul2(el,pribl(i));
end
el=el+1;
    end


%���������
r=add2(a,pribl1);
if r==0
    break;
end
%��������� �����
for i=max(size(r)):-1:1
    if r(i)==0
        r(i)=[];
    else
        break;
    end
end

%������� ������
a=r;

end

r=[r, zeros(1, max(size(a1))-max(size(r)))];

%���� ������� ��������� �����
elseif da==db
 el=0; 
pribl=zeros(1,da);
    
if b(1)==a(1) 
pribl=b;
end

    
    while pribl(end)~=a(end)
for i=1:da
pribl(i)=mul2(el,b(i));
end
el=el+1;
    end

%���������
r=add2(a,pribl);
r=[r, zeros(1, max(size(a1))-max(size(r)))];
%���� ������m �������� ������
elseif da<db

    r=a;   
    if da==0
        r=0;
    end   
r=[r, zeros(1, max(size(a1))-max(size(r)))];    
end
end

