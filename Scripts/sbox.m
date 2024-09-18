clear
N=8

a=gf(0:2^N-1, N,283)
k=a(1);
for i=2:2^N
k(i)=a(2)/a(i);
end

S=double(k.x);
F=de2bi(S);
% 
% a=F(:,8)';
% H=hadamard(4);
% a=(-1).^mod([H(1,:) H(2,:) H(3,:) H(4,:)]-1,3);
% 
% N=max(size(a));
% n=log2(N);
% %Создание аффинного кода
% %Формирование линейного когда
% for i=1:N
% lin(i,1:n)=bitget(i-1, 1:n);
% end
% affin=mod(lin*lin',2);
% %Формирование аффинного кода    
% affin1=[affin; mod(affin+1,2); a]; 
% %Нахождения расстояний Хэмминга
% h1=2*N+1;
% for h=1:2*N
%     if h1 ~=h
%     dish(h)=correlat(affin1(h1,:),affin1(h,:));
%     else
%         dish(h)=NaN;
%     end
% end
% dis=max(abs(dish));
% disp(dis);