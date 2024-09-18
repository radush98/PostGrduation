function c=correlat(a,b)

v=sum(a.*b)-(sum(a)*sum(b))/length(a);
u=(sum(a.*a)-(sum(a)^2)/length(a))*(sum(b.*b)-(sum(b)^2)/length(b));
c=v/sqrt(u);