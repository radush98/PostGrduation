function degree=ANF256(out)
%��������� ������� ��������������
L1=[1 0; 1 1];
L2=kron(L1,L1);
L4=kron(L2,L2);
L8=kron(L4,L4);

%��������� ������������ �������� ������� � ������� ��������������
a=mod(L8*out',2)';

%������������ ��������� �����
for i=1:256
lin(i,1:8)=bitget(i-1, 1:8);
end


%���������� ������������ ������
k=1;
for i=1:256
    if a(i)==1
        term(k,:)=lin(i,:);
        k=k+1;
    end
end
degree=max(sum(term,2));



end
