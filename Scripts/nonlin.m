function dis=nonlin(a)
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
%Нахождения расстояний Хэмминга
h1=2*N+1;
for h=1:2*N
    if h1 ~=h
    dish(h)=sum(affin1(h1,:)~=affin1(h,:));
    else
        dish(h)=NaN;
    end
end
dis=min(dish);
end