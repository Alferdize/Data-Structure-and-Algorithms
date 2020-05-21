package main
var dirs = [][]int{{1,0},{-1,0},{0,-1},{0,1}}
func dfs(i, j int, memo, matrix [][]int) int {
    if memo[i][j] != 0 {
        return memo[i][j]
    }
    res := 0
    for _,d := range dirs {
        x,y:=d[0]+i,d[1]+j
        if x< 0 || y<0||x>=len(memo)||y>=len(memo[0]) || matrix[x][y] <= matrix[i][j] {
            continue
        }
        subres := dfs(x,y,memo, matrix)
        if subres > res {
            res = subres
        }
    }
    res++
    memo[i][j] = res
    return res
}
func solve(matrix [][]int) int {
    // Write your code here
    n, m := len(matrix), len(matrix[0])
    memo := make([][]int, n)
    for i:=0;i<n;i++ {
        memo[i] = make([]int, m)
    }
    res := 0
    for i:=0;i<n;i++ {
        for j:=0;j<m;j++ {
            if memo[i][j] == 0 {
                r := dfs(i,j,memo,matrix)
                if r>res {res=r}
            }
        }
    }
    return res
}