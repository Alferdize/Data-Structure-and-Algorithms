package main
import "fmt"
 
func main() {
    var d int
    fmt.Scanf("%d", &d)
    tof := 0
    for i:= 0;i<d;i++ {
        var r, x int
        fmt.Scanf("%d %d", &r, &x)
        cap := 100 * x
        circum := 2 * 22 * r / 7
        if cap >= circum {
            tof++
        }
        
    }
    fmt.Println(tof)
}