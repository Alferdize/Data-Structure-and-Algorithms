#include "solution.hpp"
#include <bits/stdc++.h>
using namespace std;
/**
 * class Tree {
 *   public:
 *     int val;
 *     Tree *left;
 *     Tree *right;
 * };
 */
bool sym(Tree* a,Tree* b)
{
if(!a and !b)return true;
if(!a or !b)return false;
return a->val==b->val and sym(a->left,b->right)and sym(a->right,b->left );
}
bool Solution::solve(Tree* root) {
return sym(root,root);
};