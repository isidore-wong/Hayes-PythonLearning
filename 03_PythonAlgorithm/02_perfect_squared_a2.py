# _*_ coding:utf-8 _*_
import math

"""
@author: Isidore
@email: 616132717@qq.com
@file: 02_perfect_squared_a2
@time: 2020/05/02 0:10
"""

"""
1.问题描述：给定一个正整数n，找到若干个完全平方数(例如：1,4,9，…)，使得它们的和等于n，完全平方数的个数最少
2.问题示例：给出n=12，返回3，因为12=4+4+4；给出13，返回2，因为13=4+9
3.方法二--采用和方法一思维类似的动态规划法，动态规划中不用重复计算中间解，解决方法一递归中堆栈溢出的问题的一个思路就是使用
动态规划（DP）技术，该技术建立在重用中间解的结果来计算终解的思想之上
3.具体思考见Markdown--01_perfect_squared.md
"""


class Solution(object):
    def numSquares(self, n):
        square_nums = [i ** 2 for i in range(0, int(math.sqrt(n))+1)]
        dp = [float('inf')] * (n + 1)
        dp[0] = 0

        for i in range(1, n + 1):
            for square in square_nums:
                if i < square:
                    break
                dp[i] = min(dp[i], dp[i - square] + 1)
        return dp[-1]

if __name__ == '__main__':
    n = int(input('请输入一个正整数n：'))
    n_so = Solution()
    print("结果是：", n_so.numSquares(n))