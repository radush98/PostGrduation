clear;
n=8;

neprivod=zeros(1,n+1);
pervoobraz=zeros(1,n+1);

%������������ ������� ��������
k=1;
k1=1;
for i=2^n:(2^(n+1))-1
    test=gfprimck(de2bi(i,n+1), 2);
    
    if test==0 %������� �������������
        neprivod(k,:)=de2bi(i,n+1);
        k=k+1;
    end
    
    if test==1 %������� ������������� �������������
        pervoobraz(k1,:)=de2bi(i,n+1);
        k1=k1+1;
    end
end

