package main

import (
	"fmt"
)

func countingValleys(steps int32, path string) int32 {
	var valleys int32 = 0
	level := 0
	lastLevel := 0
	for _, step := range path {
		lastLevel = level
		if string(step) == "D" {
			level--
		} else {
			level++
		}
		if lastLevel < 0 && level == 0 {
			valleys++
		}
	}
	return valleys
}

func main() {
	var steps int32 = 8
	path := "UDDDUDUU"
	valleys := countingValleys(steps, path)
	fmt.Println(valleys)
}
