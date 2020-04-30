# #include "solution.hpp"
# #include <bits/stdc++.h>
# using namespace std;
# int sum(int n) {
#     return (n*n+n)/2;
# }
# int Solution::solve(int n) {
#     int res = 0;
#     for (int i = 2; sum(i) <= n; ++i) {
#         if (n%i == sum(i)%i) ++res;
#     }
#     return ++res;
# };