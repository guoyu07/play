package main

import (
	"fmt"
)

func main() {
	var i, j int = 1, 2
	k := 3 // can use := for short declaration only in functions, ps: only
	c, python, java := true, false, "no"
	fmt.Println(i, j, k, c, python, java)
}
