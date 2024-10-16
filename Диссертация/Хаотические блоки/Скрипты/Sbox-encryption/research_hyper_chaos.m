clear
a=imread('test.jpg');
a=a(1:900, 1:1800, :);
S256=[0    1   71  167  216  114  224   62   54   95  146   78   56   35  129   26  131  160  222  144  170   61  157  173   14  151  193   19  103   22  136   48  233  251   40  209  185  196   36   87  164  195   72  137   96   86  108  237  141   82  236   32  119  219  205  132  208  112  139   38   34   80   12  171  125  133  247  210   10  153  115   16  105   83   49   73    9  172  220   11   41  113  249   67   18   89  101  184   24  223  155  188   27   84  124  204  100  197  154  149   59  206    8  156  212   66  255  127  116  250   33  109   52  194   28  130  235  242  135  229  134  177   20   63    3  143  227  231   88  192  102   76  244  142  186  122  140  104   97   37  213  248    4  166   93  150  221  152   75   42   85  128   69  147   43   30   55   65  203   99   77   23   91  202  121  218  217   17  138   44   81   57   94   64   46  111    6  187  254  252  239  179   47   50  207  169   21  225   31   74   51  110   25  145  118  120  168   58   98   90  199  162  189  148    2  245   39   45   53  165  158  163  246  200  214  215   29  161  176  228   79   68   92   15   13   60  190  183    7  123  174  182  243  180  178  106  232  117  126  253  175  191  107  238    5   70  198  159  201  211  234  181  241  226  240  230];
S243=[0 1    2  163  210  240   83  120  150  217   57   60   70  104  200   80  115  142  110   30   33   40  194  221   50  154  178  235   98   37   19   58  216   20  218   62  183   29  117  114   21  143  149  140  136  106   88  172  198  103   24  207  229  202  119   74  184   10   31  109   11  108   35  176  101  167  144  161  134  153   12  179   96  234   55  214  191  196  219  193   15  241  212    6  112  188  180  175   46   99  169  186  111  182  170  113   72  118   28   89  105   64  155   49   13  100   45  165   61   59   18   92   84   95   39   16  192   38   97   54    7  211  162  127  204  233  129  123  157  126  238  205  208  201   68  195   44  215  189  213   43  220   17   41   66  203  228  197  190   42    8  164  242   69   25  102  239  128  232  230  209   67  122    3  151  107  171   65  224   90   94  166   47  174  173   87   63  199   26   71   86  222   93   36   56  236   91  223   85  138  148   76  116   79   22  135   77  147   48  177   14  133   53  145  124  131  226   51  132  160    4  121   82  139   75  137   32    9   34   78  141   23  181  187  168  231  206  237  146   52  159  225  158  125   73   27  185  227  130  156    5   81  152];

S256inv=[1    2  205  125  143  245  177  229  103   77   69   80   63  225   25  224   72  168   85   28  123  187   30  162   89  193   16   93  115  217  156  189   52  111   61   14   39  140   60  207   35   81  150  155  170  208  175  183   32   75  184  191  113  209    9  157   13  172  198  101  226   22    8  124  174  158  106   84  222  153  246    3   43   76  190  149  132  161   12  221   62  171   50   74   94  151   46   40  129   86  200  163  223  145  173   10   45  139  199  160   97   87  131   29  138   73  236  243   47  112  192  176   58   82    6   71  109  238  195   53  196  165  136  230   95   65  239  108  152   15  116   17   56   66  121  119   31   44  169   59  137   49  134  126   20  194   11  154  204  100  146   26  148   70   99   91  104   23  211  248   18  218  202  212   41  210  144    4  197  186   21   64   78   24  231  241  219  122  235  182  234  252  232  228   88   37  135  178   92  203  227  242  130   27  114   42   38   98  247  201  214  249  164  159   96   55  102  185   57   36   68  250  105  141  215  216    5  167  166   54   79  147   19   90    7  188  254  127  220  120  256  128  237   33  251  117   51   48  244  181  255  253  118  233  133  206  213   67  142   83  110   34  180  240  179  107];
S243inv=[1    2    3  164  211  241   84  121  151  218   58   61   71  105  201   81  116  143  111   31   34   41  195  222   51  155  179  236   99   38   20   59  217   21  219   63  184   30  118  115   22  144  150  141  137  107   89  173  199  104   25  208  230  203  120   75  185   11   32  110   12  109   36  177  102  168  145  162  135  154   13  180   97  235   56  215  192  197  220  194   16  242  213    7  113  189  181  176   47  100  170  187  112  183  171  114   73  119   29   90  106   65  156   50   14  101   46  166   62   60   19   93   85   96   40   17  193   39   98   55    8  212  163  128  205  234  130  124  158  127  239  206  209  202   69  196   45  216  190  214   44  221   18   42   67  204  229  198  191   43    9  165  243   70   26  103  240  129  233  231  210   68  123    4  152  108  172   66  225   91   95  167   48  175  174   88   64  200   27   72   87  223   94   37   57  237   92  224   86  139  149   77  117   80   23  136   78  148   49  178   15  134   54  146  125  132  227   52  133  161    5  122   83  140   76  138   33   10   35   79  142   24  182  188  169  232  207  238  147   53  160  226  159  126   74   28  186  228  131  157    6   82  153];

S256inv=S256inv-1;
S243inv=S243inv-1;

%Map1
%Map1
x=0.7;

g=4;

e1=(1/2) - sqrt((1/4)- floor(g/4)/g);

e2=(1/2) + sqrt((1/4)- floor(g/4)/g);

N=2*3*8388608;
k=1;

for i=1:N
    
    if g<=4
        x(i+1)=g*x(i)*(1-x(i));
    else
        
        if x(i)>=e1 && x(i)<=e2
            x(i+1)=mod(g*x(i)*(1-x(i)),1)/mod(g/4,1);
        else
            x(i+1)=mod(g*x(i)*(1-x(i)),1);
        end
    end
    
    if x(i)>=0.1 && x(i)<=0.6
        y(k)=x(i);
        y(k)=mod(y(k)*10^10,1);
        
        
        if y(k)>=0.5
            y(k)=1;
        else
            y(k)=0;
        end
        
        k=k+1;
    else
        continue
    end
end

k=1;
y1=zeros(1,2*8388608, 'uint8');
for i=1:8:2*8388608
   
    y1(k)=uint8(bi2de(y(i:i+7)));
    k=k+1; 
    
end


%Encrypt
%Round 1
k=1;
for i=1:9:900
    for j=1:9:1800
        
        block=a(i:i+8, j:j+8, :);
        
        %S-box
        for l=1:243
            block(l)=S256(double(block(l))+1);
        end
        
        %P-box
        block=reshape(block(S243+1),[9,9,3]);
        
        b(i:i+8, j:j+8, :)=block;
        
    end
end

%XOR
for l=2:4860000
    b(l)=bitxor(b(l), b(l-1));
    b(l)=bitxor(b(l), y1(k));
    k=k+1;
end

%Round 2

for i=1:9:900
    for j=1:9:1800
        
        block=b(i:i+8, j:j+8, :);
        
        %S-box
        for l=1:243
            block(l)=S256(double(block(l))+1);
        end
        
        %P-box
        block=reshape(block(S243+1),[9,9,3]);
        
        b(i:i+8, j:j+8, :)=block;
        
    end
end

%XOR
k=1;
for l=2:4860000
    b(l)=bitxor(b(l), b(l-1));
    b(l)=bitxor(b(l), y1(k));
    k=k+1;
end



figure(1)
imshow(a)

figure(2)
imshow(b)


% %Decrypt
% c=b;
% %Round 2
% %XOR
% k=1;
% for l=2:4860000
%     c(l)=bitxor(b(l), b(l-1));
%     c(l)=bitxor(c(l), y1(k));
%     k=k+1;
% end
% 
% for i=1:9:900
%     for j=1:9:1800
%         
%         block=c(i:i+8, j:j+8, :);
%         
%         %P-box
%         block=reshape(block(S243inv+1),[9,9,3]);
%         
%         %S-box
%         for l=1:243
%             block(l)=S256inv(double(block(l))+1);
%         end
%         
% 
%         
%         c(i:i+8, j:j+8, :)=block;
%         
%     end
% end
% 
% 
% 
% 
% %Round 1
% %XOR
% k=1;
% b=c;
% for l=2:4860000
%     c(l)=bitxor(b(l), b(l-1));
%     c(l)=bitxor(c(l), y1(k));
%     k=k+1;
% end
% 
% 
% k=1;
% for i=1:9:900
%     for j=1:9:1800
%         
%         block=c(i:i+8, j:j+8, :);
%         
%         %P-box
%         block=reshape(block(S243inv+1),[9,9,3]);
%         
%         %S-box
%         for l=1:243
%             block(l)=S256inv(double(block(l))+1);
%         end
%         
% 
%         
%         c(i:i+8, j:j+8, :)=block;
%         
%     end
% end








