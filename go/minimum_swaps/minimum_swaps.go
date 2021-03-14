package main

import (
    "fmt"
)

// Complete the minimumSwaps function below.
func minimumSwaps(arr []int32) int32 {
	var swaps int32 = 0
	var i int32 = 0
	var num int32

	for i < int32(len(arr)) {
		num = arr[i]
		if (num - 1) != i {
			arr[num - 1], arr[i] = arr[i], arr[num - 1]
			swaps++
		} else {
			i++
		}
	}

	return swaps
}

func main() {
	arr := []int32{2, 3, 4, 1, 5}
	swaps := minimumSwaps(arr)
	fmt.Println(swaps)
}
