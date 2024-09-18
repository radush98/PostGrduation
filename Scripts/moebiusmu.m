function u = moebiusmu(n)
%MOEBIUSMU Moebius function.
%   MOEBIUSMU(N) returns the corresponding mu value of N according to the
%   Moebius mu function.
%
%   The Moebius mu function is used in number theory and combinatorics. It
%   was first introduced by August Ferdinand Moebius in 1831. The function
%   is denoted by the Greek lowercase letter mu(n).
%   mu(n) is defined for all strictly positive natural numbers n and
%   returns values in {-1,0,1}.
%   mu(n) is defined as follows:
%   mu(n) = 0       if n is not a square-free integer
%   mu(n) = 1       if n = 1
%   mu(n) = (-1)^k  if n is square-free with k prime factors
%   The function is multiplicative, i.e. mu(ab) = mu(a)mu(b) when a and b
%   are coprime.
%
%   See also FACTOR.

%   2006/07/10, v1.0, Adrian Schumacher

if numel(n)~=1, error('MATLAB:moebiusmu:NonScalarInput','N must be a scalar.'); end
if (n < 1) || (floor(n) ~= n)
  error('MATLAB:moebiusmu:InputNotPosIntGrZero', 'N must be a positive integer greater than 0.'); 
end
p = factor(n);
N = hist([0 p],max(p)+1);
r = sum(N(2:end) > 1);

if (n == 1)
    u = 1;
elseif (r > 0)
    u = 0;
else
    k = sum(N(2:end) > 0);
    u = (-1)^k;
end
