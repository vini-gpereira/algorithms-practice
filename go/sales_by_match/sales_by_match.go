package main

import "fmt"

func sockMerchant(n int32, ar []int32) int32 {
	var pairs int32 = 0
	socks := make(map[int32]int32)
	for i := range ar {
		sock := ar[i]
		_, ok := socks[sock]
		if ok {
			socks[sock]++
			if socks[sock] % 2 == 0 {
				pairs++
			}
		} else {
			socks[sock] = 1
		}
	}
	return pairs
}

func main() {
	var n int32 = 9
	ar := []int32{10, 20, 20, 10, 10, 30, 50, 10, 20}
	pairs := sockMerchant(n, ar)
	fmt.Println(pairs)
	n = 7
	ar = []int32{1, 2, 1, 2, 1, 3, 2}
	pairs = sockMerchant(n, ar)
	fmt.Println(pairs)
}
