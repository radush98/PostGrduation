function [xexs, degree]=ANF(out)

s=max(size(out));

%Генерация матрицы преобразования
L=Lmx(log2(s));

%Матричное произведение входящий матрицы и матрицы преобразования
a=mod(L*out',2)';

%Формирование линейного кода
for i=1:s
lin(i,1:log2(s))=bitget(i-1, 1:log2(s));
end


%Вычисление существующих термов
k=1;
for i=1:s
    if a(i)==1
        term(k,:)=lin(i,:);
        k=k+1;
    end
end
degree=max(sum(term,2));

%Формирование строки
if a(1)==1
xexs='1+';
term(1,:)=[];
elseif a(1)==0
    xexs='';
end

[s1 s3]=size(term);

for j=1:s1
xex=find(term(j,:)==1);
%Преобразование в строку


for i=1:max(size(xex))
    xexs=strcat(xexs, strcat('x',num2str(xex(i))));
end

xexs=strcat(xexs, '+');

end
    
if xexs(end)=='+'
   xexs(end)=[];
end


