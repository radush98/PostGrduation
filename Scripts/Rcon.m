function out=Rcon(in)
in=in-1;
if in==0
    out='01000000';
elseif in==1
    out='02000000';
elseif in==2
    out='04000000';
elseif in==3
    out='08000000';
elseif in==4
    out='10000000';
elseif in==5
    out='20000000';
elseif in==6
    out='40000000';
elseif in==7
    out='80000000';
elseif in==8
    out='1b000000';
elseif in==9
    out='36000000';
elseif in==10
    out='6c000000';
elseif in==11
    out='d8000000';
elseif in==12
    out='ab000000';
elseif in==13
    out='4d000000';
elseif in==14
    out='9a000000';
end
															
end
