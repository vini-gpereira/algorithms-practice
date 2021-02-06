package main

import "fmt"

func twoSum(numbers []int, target int) []int {
	storage := make(map[int]int)

	for i, num := range numbers {
		complement := target - num
		idx, ok := storage[complement]

		if ok {
			return []int{idx, i}
		} 

		storage[num] = i
	}

	return []int{-1, -1}
}

func main() {
	numbers := []int{3, 2, 7}
	target := 10
	res := twoSum(numbers, target)
	fmt.Println(res)
}