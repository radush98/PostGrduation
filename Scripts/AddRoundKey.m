function out=AddRoundKey(S,w,r);

Nb=4;
out=zeros(4);

for c=1:4
out(1,c)=bi2de(xor(de2bi(S(1,c),8), de2bi(hex2dec(w(r*Nb+c, 1:2)),8)));
out(2,c)=bi2de(xor(de2bi(S(2,c),8), de2bi(hex2dec(w(r*Nb+c, 3:4)),8)));
out(3,c)=bi2de(xor(de2bi(S(3,c),8), de2bi(hex2dec(w(r*Nb+c, 5:6)),8)));
out(4,c)=bi2de(xor(de2bi(S(4,c),8), de2bi(hex2dec(w(r*Nb+c, 7:8)),8)));
end

% end





