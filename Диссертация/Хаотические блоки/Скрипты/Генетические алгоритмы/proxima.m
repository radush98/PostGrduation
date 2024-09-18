clear

box=0:255;

population=50;
step=10000;

for i=1:population
   b(i,:)=box; 
end

% load b

for i=1:step
   
    %Generation
    for j=population+1:2*population
       ch1=round(255*rand(1));
       ch2=round(255*rand(1));
        b(j,:)=b(j-50,:);
        temp=b(j-50,ch1+1);
        b(j,ch1+1)=b(j-50,ch2+1);
        b(j,ch2+1)=temp;
    end
    
    %Destruction
    parfor j=1:2*population
        D(j)=sum(sum(abs(Sdif(b(j,:))-128*ones(8))));
        if D(j)==0
            disp(b(j,:));
        end
    end
    
    [a u]=sort(D);
    
    b(u(51:100),:)=[];
    
    disp([i min(D)]);
    
end