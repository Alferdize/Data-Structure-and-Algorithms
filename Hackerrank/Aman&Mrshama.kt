fun main() {
    var t = readLine()!!.toInt()
    var count = 0
    while (t-- > 0) {
        val (r, x) = readLine()!!.split(" ").map { it.toInt() }
        if (((44 * r) / 7) <= (100 * x)) {
            count++
        }
    }
    println(count)
}