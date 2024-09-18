function [dif, f_e]=differential(f)


N=max(size(f));


%Формирование полного кода
num=0:N-1;
code=de2bi(num);

error=zeros(log2(N));
%Вектор ошибки
for i=0:nextpow2(N)-1
error(i+1,:)=de2bi(2^i,log2(N));
end

   
%Вычисление производных
for j=1:log2(N)
for i=1:N
    code_e(i,:)=xor(code(i,:), error(j,:));
end
    num_e=bi2de(code_e);
    f_e(j,:)=f(num_e+1);
    dif(j)=sum(xor(f,f_e(j,:)));
end

end