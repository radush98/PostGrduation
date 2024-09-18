%Нахождение аффиного кода
a=zeros(256,8);
X=[0,0,0,0,0,0,0,0];
for h=1:256
    a(h,1:8)=X(1:8);
for j=1:8
           
        if X(j)~=1
            X(j)=X(j)+1;
            for k=1:j-1
                X(k)=0;
            end
            break;
        else
            X(h,j)=0;
        end       
end
end
a1=a;
affin=rem(a*a1',2);

%Вычислитель компонентных функций
for i=1:256
    outb(i,1:8)=dec2bin(b(i),8);
end

F1=outb(:,8);
F2=outb(:,7);
F3=outb(:,6);
F4=outb(:,5);
F5=outb(:,4);
F6=outb(:,3);
F7=outb(:,2);
F8=outb(:,1);

F1=str2num(F1);
F1=F1';

F2=str2num(F2);
F2=F2';

F3=str2num(F3);
F3=F3';

F4=str2num(F4);
F4=F4';

F5=str2num(F5);
F5=F5';

F6=str2num(F6);
F6=F6';

F7=str2num(F7);
F7=F7';

F8=str2num(F8);
F8=F8';


affin1=affin;
affin1=vertcat(affin1, F1);
affin1=vertcat(affin1, F2);
affin1=vertcat(affin1, F3);
affin1=vertcat(affin1, F4);
affin1=vertcat(affin1, F5);
affin1=vertcat(affin1, F6);
affin1=vertcat(affin1, F7);
affin1=vertcat(affin1, F8);

for h1=1:264
for h=1:264
    if h1 ~=h
    dish(h)=hamming_dis(affin1(h1,:), affin1(h,:));
    end
end
dis1(h1)=min(dish);
end

rd=min(dis1);


%Свойства цикличности
%Формирование входного слова
in(1)=0;
for i=2:256
    in(i)=in(i-1)+1;
end

in1=in
out=zeros(1,256);
k=0;

while(sum(eq(in1,out))/256 ~=1)
 %Цикл замены
 for i=1:256
     out(i)=x(in(i)+1);
 end
 
in=out
k=k+1;

end
