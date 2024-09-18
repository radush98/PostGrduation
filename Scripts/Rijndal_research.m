clear
clc
% ÈÑÑËÅÄÎÂÀÍÈÅ ÐÀÂÍÎÌÅÐÍÎÑÒÈ ÊÎÐÐÅËßÖÈÈ 
% Ïîñòðîåíèå S-ÁËÎÊÀ RIJNDAL
 m=8; 
N=2^m; 
f=273; % ÍÅÏÐÈÂÎÄÈÌÛÅ ÏÎËÈÍÎÌÛ
a=gf(0:N-1, m); % ÝËÅÌÅÍÒÛ ÏÎËß Â ËÅÊÑÈÊÎÃÐÀÔÈ×ÅÑÊÎÌ ÏÎÐßÄÊÅ
k=a(1);
for i=2:N
k(i)=a(2)/a(i); % ÍÀÕÎÆÄÅÍÈÅ ÎÁÐÀÒÍÛÕ ÅËÅÌÅÍÒÎÂ
end

%-------------------------------
a=double(k.x); 
nonlin(a)
%-------------------------------

% for i=1:256
%     out(i,:)=de2bi(a(i),8);
% end
% 
% F(1,:)=out(:,1)';
% F(2,:)=out(:,2)';
% F(3,:)=out(:,3)';
% F(4,:)=out(:,4)';
% F(5,:)=out(:,5)';
% F(6,:)=out(:,6)';
% F(7,:)=out(:,7)';
% F(8,:)=out(:,8)';


% %Èññëåäîâàíèå öèêëè÷åñêèõ ñäâèãîâ
% 
% %Ïîëó÷åíèå öèêëè÷åñêèõ ñäâèãîâ
% cycl=cell(8, 256); k=1;
% for i=1:8
%     for j=1:256
%         cycl{i,j}=circshift(F(i,:), [0,j]);
%     end
% end
% 
% %Èçìåðåíèå ñòåïåíåé íåëèíåéíîñòè
% 
% for i=1:8
%     for j=1:256
%         deg(j)=ANF256(cycl{i,j});
%     end
%     [a0 b0]=size(find(deg==0));
%     [a1 b1]=size(find(deg==1));
%     [a2 b2]=size(find(deg==2));
%     [a3 b3]=size(find(deg==3));
%     [a4 b4]=size(find(deg==4));
%     [a5 b5]=size(find(deg==5));
%     [a6 b6]=size(find(deg==6));
%     [a7 b7]=size(find(deg==7));
%     [a8 b8]=size(find(deg==8));
%     o(i,:)=[b0, b1, b2, b3, b4, b5, b6, b7, b8];
% end
% 
% %Èçó÷åíèå áëî÷íîé ñòðóêòóðû
% for i=1:8
%     bl(i)=block(F(i,:));
% end
% bl=bl';
% 
% bl1=zeros(1,9);
% for i=1:8
%     temp=block1(F(i,:));
%     [u1 u2]=size(bl1);
%     s=max(size(temp));
%     if s>u2
%         for l=u2:s
%             bl1(:,l)=0;
%         end
%     end
%     
%     if s<u2
%         for l=s:u2
%             temp(l)=0;
%         end
%     end
%     
%     bl1(i,:)=temp;
% end
% 
% [u1 u2]=size(bl1);
% y=1:u2;
% bl1=[y; bl1];
% 
% 
% [0 1 2 3 4 5 6 7 8 ;o];
% bl1; mean(bl)
% disp(max(bl));
% disp(min(bl));
