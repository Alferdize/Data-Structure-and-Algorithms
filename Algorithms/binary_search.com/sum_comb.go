package main


func solve(nums []int) int {
    // Write your code here
    M := 1000000007
    var total int
    N := len(nums)
    for i in 0 to N{
        n := nums[i]
        total += (i+1) * (N-i) *n
    }
    return total % M
}
