package main
 
import "fmt"
 
func main(){
    
    var n int
    
    fmt.Scan(&n)
    
    d := n/5
    
    if n%5==0{
        
         fmt.Println(d)
    }else{
        
         fmt.Println(d+1)
    }
    
    
}