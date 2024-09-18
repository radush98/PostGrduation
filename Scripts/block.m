function bl=block(in)

in1=[in, in];

bl=0;

for i=1:max(size(in))
    if in1(i)~=in1(i+1)
        bl=bl+1;
    end
            
end




end