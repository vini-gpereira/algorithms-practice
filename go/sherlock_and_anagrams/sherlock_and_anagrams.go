package main

import (
	"fmt"
	"sort"
	"strings"
)

type Runes []rune

func (r Runes) Len() int           { return len(r) }
func (r Runes) Swap(i, j int)      { r[i], r[j] = r[j], r[i] }
func (r Runes) Less(i, j int) bool { return r[i] < r[j] }

func sherlockAndAnagrams(s string) int32 {
	counts := make(map[string]int32)
	var anagrams int32 = 0
	l := len(s)

	for i := 1; i < l; i++ {
		for j := 0; j < (l - i + 1); j++ {
			sub := s[j:(j + i)]
			sub = sortString(sub)
			value, ok := counts[sub]

			if ok {
				counts[sub] = value + 1
			} else {
				counts[sub] = 1
			}
		}
	}

	for _, count := range(counts) {
		anagrams += numberOfPairs(count)
	}

	return int32(anagrams)
}

func sortString(s string) string {
	split := strings.Split(s, "")
	sort.Strings(split)
	return strings.Join(split, "")
}

func numberOfPairs(count int32) int32 {
	return count * (count - 1) / 2
}

func main() {
	s := "ifailuhkqq"
	result := sherlockAndAnagrams(s)
	fmt.Println(result)
}
