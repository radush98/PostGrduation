function [R nl]=correlatis32(a)
N=max(size(a));
n=log2(N);
%Создание аффинного кода
%Формирование линейного когда
for i=1:N
lin(i,1:n)=bitget(i-1, 1:n);
end
affin=mod(lin*lin',2);
%Формирование аффинного кода    
affin1=[affin; mod(affin+1,2); a];

%Вычислитель компонентных функций
for i=1:N
    outb(i,1:n)=dec2bin(a(i),n);
end

k=1;
for i=n:-1:1
F(k,:)=s2n(outb(:,i));
nl(k)=nonlin(F(k,:));
k=k+1;
end

for i=1:n
    for j=1:N
        R(i,j)=(2*sum(F(i,:)==affin1(j,:))-N)/N;
    end
end

nl=max(nl);
