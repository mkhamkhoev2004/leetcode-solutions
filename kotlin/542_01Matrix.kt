// Time Complexity: O(m * n)
// Space complexity: O(m * n)

import java.util.*

class Solution {
    fun updateMatrix(mat: Array<IntArray>): Array<IntArray> {
        val m = mat.size
        val n = mat[0].size
        val dist = Array(m) { IntArray(n) { Int.MAX_VALUE } }
        val queue: Queue<Pair<Int, Int>> = LinkedList()
        
        for (i in 0 until m) {
            for (j in 0 until n) {
                if (mat[i][j] == 0) {
                    dist[i][j] = 0
                    queue.offer(i to j)
                }
            }
        }
        
        val dirs = arrayOf(-1 to 0, 1 to 0, 0 to -1, 0 to 1)
        
        while (queue.isNotEmpty()) {
            val (x, y) = queue.poll()
            for ((dx, dy) in dirs) {
                val nx = x + dx
                val ny = y + dy
                if (nx in 0 until m && ny in 0 until n) {
                    if (dist[nx][ny] > dist[x][y] + 1) {
                        dist[nx][ny] = dist[x][y] + 1
                        queue.offer(nx to ny)
                    }
                }
            }
        }
        
        return dist
    }
}