function [cor, distance]=cor_mx(a)

[a1,a2]=size(a);
%Формирование входного слова
in(1)=0;
for i=2:a2
    in(i)=in(i-1)+1;
end


for k=1:a2
    u(k,1:log2(a2))=dec2bin(a(k),log2(a2));
    v(k,1:log2(a2))=dec2bin(in(k),log2(a2));
end

%Цикл определения коэфициента корреляции
cor=zeros(log2(a2),log2(a2));
    for i=1:log2(a2)
       
           for j=1:log2(a2)
           
               for k=1:a2
                 if(double(u(k,i)) ~= double(v(k,j))) 
                    cor(i,j)=cor(i,j)+1;
                 end
               end
           end
    end
    

 for i=1:log2(a2)
    for j=1:log2(a2)
        cor(i,j)=1-(cor(i,j)/(a2/2));
    end
end       
cor=fliplr(cor);
cor=flipud(cor);

end