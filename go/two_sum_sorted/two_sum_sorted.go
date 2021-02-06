package main

import "fmt"

func twoSumSorted(numbers []int, target int) []int {
	left := 0
	right := len(numbers) - 1

	for left < right {
		sum := numbers[left] + numbers[right]

		if sum > target {
			right--
		} else if sum < target {
			left++
		} else {
			return []int{left, right}			
		}
	}

	return []int{-1, -1}
}

func main() {
	numbers := []int{2, 7, 11, 15}
	target := 9
	res := twoSumSorted(numbers, target)
	fmt.Println(res)
}
