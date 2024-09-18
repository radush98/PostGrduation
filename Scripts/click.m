clear;
fid=fopen('gogol_n_v__mertvye_dushi.txt');
i=1;
line='';
        while 1
            tline = fgetl(fid);
            if ~ischar(tline), break, end
            line=strcat(line,tline);
        end
        fclose(fid);

line1=lower(line); %Нижний регистр
l=double(line1);
k=1;
for i=1:max(size(l))
    if l(i)>=1072 && l(i)<=1103
        l1(k)=l(i);
        k=k+1;
    end
end
l3=l1-1071-1;
%hist(l3, 1:33);

%Запоковка текста пакетами по 5 бит
binary=dec2bin(l3,5);
binary_line='';
k=1; k1=5;
for i=1:max(size(binary))
binary_line(k:k1)=binary(i,1:5);
k=k+5;
k1=k1+5;
end

hx=bin2hex(binary_line);

%Разрезание строки чисел на сегменты по 8 символов
k=1; k1=32;
for i=1:max(size(hx))
    if k1>max(size(hx))
        break;
    end
    hx1(i,:)=hx(k:k1);
    k=k+32; k1=k1+32;
end
    
for e=10:10
    
%Шифрование по AES

crypto='';
for i=1:max(size(hx1))
    S=rijndael(hx1(i,:),e); 
    crypto=strcat(crypto, S);
end

%Обработка шифрованного текста
chip=crypto;
chip_h=zeros(1);
k=1;
k1=1;
k2=2;
for i=1:max(size(chip))
    if k2>=max(size(chip))
        break;
    end
    chip_h(k)=hex2dec(chip(k1:k2));
    k=k+1;
    k1=k1+3;
    k2=k2+3;
end

chip_b=dec2bin(chip_h, 8);
k=1; k1=8;
for i=1:max(size(chip_b))
chip_b_line(k:k1)=chip_b(i,1:8);
k=k+8;
k1=k1+8;
end

chip_r=zeros(1);
k1=1; k2=5;
k=1;
for i=1:max(size(chip_b_line))
    if k2>=max(size(chip_b_line))
        break;
    end
chip_r(k)=bin2dec(chip_b_line(k1:k2));
k=k+1; k1=k1+5; k2=k2+5;
end

chip_r=chip_r+1;
subplot(1,1,1)
hist((chip_r-1), 0:35);
grid on;
xlabel('Літера');
ylabel('Частота');

end