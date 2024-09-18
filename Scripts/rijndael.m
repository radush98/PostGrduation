%function S1=rijndael(input, r)

% input='3243f6a8885a308d313198a2e0370734'
% input='0123456789ABCDEF0123456789ABCDEF'
r=10;

% binInput=randsrc(1,256,[0, 1;0.15, 0.85]);
% inputMatrix = reshape(binInput, [32, 8]);
TOTAL = [];

for counter=1:1:10000
    
disp(counter)
 
input = [];

for i=1:1:length(inputMatrix)
   input = [input; binaryVectorToHex((inputMatrix(i,1:8)))]; 
end

%Генерация раундовых ключей
K=['2b'; '7e'; '15'; '16'; '28'; 'ae'; 'd2'; 'a6'; 'ab'; 'f7'; '15'; '88'; '09'; 'cf'; '4f'; '3c'];
K=['00'; '11'; '22'; '33'; '44'; '55'; '66'; '77'; '88'; '99'; 'AA'; 'BB'; 'CC'; 'DD'; 'EE'; 'FF'];
w=KeyExpansion(K);
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


%Преобразование входной строки в матрицу состояний
k1=1; k2=2; S=zeros(4);
for j=1:4
    for i=1:4
    S(i,j)=hex2dec(input(k1:k2));
    k1=k1+2; k2=k2+2;
    end
end
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


%AddRoundKey
S=AddRoundKey(S,w,0);
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

%Цикл шифрования
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
enthropy = [];

for i=1:r
%SubBytes
S=SubBytes(S);
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

%ShiftRows
S=ShiftRows(S);
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

%MixColumns
S=MixColumns(S);
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

%AddRoundKey
S=AddRoundKey(S,w,i);

res = [];
for i=1:1:length(S)
    res = [res , de2bi(S(i),8)];
end

P=[1-sum(res)/length(res) sum(res)/length(res)];
E=-P(1)*log2(P(1))-P(2)*log2(P(2));
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
enthropy = [enthropy, E];
end

TOTAL = [TOTAL; enthropy];
end
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

% disp(enthropy);
% 
% S=dec2hex(S);
% S1='';
% for i=1:16
%     S1=strcat(S1,S(i,:));
% end



