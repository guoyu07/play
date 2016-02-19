package main

import (
	"fmt"
	"math"
)

func main() {
	fmt.Println(math.pi) // cannot refer to math.pi like there, because first-letter capitalized can be exported
}
