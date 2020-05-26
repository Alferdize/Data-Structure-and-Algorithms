fun main(){
val N = readLine()!!.toInt()
var total = 0
var m = N/5;
var b = N%5;
if(b==0)
println(m);
else
println(m+1);
}