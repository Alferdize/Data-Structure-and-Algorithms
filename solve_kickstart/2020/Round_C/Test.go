package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

func main() {
	scanner := bufio.NewScanner(os.Stdin)
	scanner.Split(bufio.ScanWords)
	scanner.Scan()
	testcasesNumber, _ := strconv.Atoi(scanner.Text())

	for i := 0; i < testcasesNumber; i++ {
		var N []int
		scanner.Scan()
		n, _ := strconv.Atoi(scanner.Text())
		scanner.Scan()
		p, _ := strconv.Atoi(scanner.Text())
		for j := 0; j < n; j++ {
			scanner.Scan()
			num, err := strconv.Atoi(scanner.Text())
			if err != nil {
				fmt.Println("Some random err")
			}
			N = append(N, num)
		}
		fmt.Printf("Case #%d: %d\n", i+1, solver(N, p))

	}
}

func getMaxVal(arr []int) int {
	res := arr[0]
	for _, val := range arr {
		if val > res {
			res = val
		}
	}
	return res
}

func solver(N []int, P int) int {
	var added []int = make([]int, len(N))
	newN := countSort(N)
	added[0] = newN[0]
	for idx := 1; idx < len(N); idx++ {
		added[idx] = added[idx-1] + newN[idx]
	}

	minS := helper(newN, added, P, len(newN)-1)
	for start := len(newN) - 2; start >= 0; start-- {

		if start-P >= -1 {
			curr := helper(newN, added, P, start)
			if curr < minS && curr > 0 {
				minS = curr
			}
		}

	}
	return minS
}

func helper(N []int, added []int, P, idx int) int {
	res := P*N[idx] - added[idx]
	if idx-P >= 0 {
		res += added[idx-P]
	}
	return res
}

func countSort(N []int) []int {
	k := getMaxVal(N)
	count := make([]int, k+1)
	for _, val := range N {
		count[val]++
	}
	for i := 1; i < k+1; i++ {
		count[i] = count[i] + count[i-1]
	}
	result := make([]int, len(N))
	for j := 0; j < len(N); j++ {
		result[count[N[j]]-1] = N[j]
		count[N[j]] = count[N[j]] - 1
	}
	return result
}
