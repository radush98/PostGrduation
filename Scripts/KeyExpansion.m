function w=KeyExpansion(K)
w='';
Nk=4;
Nb=4;
Nr=10;

temp='';
i=0;

while(i<Nk)
    w(i+1,:)=[K(4*i+1,:), K(4*i+1+1,:), K(4*i+2+1,:), K(4*i+3+1,:)];
    i=i+1;
end

i=Nk;

while(i<Nb*(Nr+1))
    temp=w(i-1+1, :);
    if (mod(i, Nk)==0)
        temp=dec2hex(bi2de(xor(de2bi(hex2dec(SubWord(RotWord(temp))),32),de2bi(hex2dec(Rcon(i/Nk)), 32))), 8);
    else
        if (Nk>6 && mod(i,Nk)==4)
            temp=SubWord(temp);
        end
    end
    w(i+1,:)=dec2hex(bi2de(xor(de2bi(hex2dec(w(i-Nk+1,:)),32), de2bi(hex2dec(temp),32))),8);
    i=i+1;
end

end
        