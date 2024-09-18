% %ÿ»‘– –≈…Õƒ¿À Rigndael_1.m
pol=gfprimfd(7,'all',2);
pole=gftuple([-1:2^7-2]',7);
[tp,expform]=gftuple(pole,7);
A=[1:128]';
Pole=[A,expform,pole];
c=gfmul(23,45,pole);
pole(c,:);
gfpretty(pole(c,:));
a1=0;a2=0;
for i=1:128
Vektor9(i,:)=[1,pole(i,:),1];
 ck=gfprimck(Vektor9(i,:));
   if ck==0
     a1=a1+1;
     neprivod(a1,:)=Vektor9(i,:);
   else
        if ck==1
     a2=a2+1;
     pervoobraz(a2,:)=Vektor9(i,:);
 end
end
end
neprivod
pervoobraz

