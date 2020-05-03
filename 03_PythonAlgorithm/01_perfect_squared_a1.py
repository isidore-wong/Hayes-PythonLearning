# _*_ coding:utf-8 _*_
import math

"""
@author: Isidore
@email: 616132717@qq.com
@file: 01_perfect_squared
@time: 2020/05/01 22:15
"""

"""
1.问题描述：给定一个正整数n，找到若干个完全平方数(例如：1,4,9，…)，使得它们的和等于n，完全平方数的个数最少
2.问题示例：给出n=12，返回3，因为12=4+4+4；给出13，返回2，因为13=4+9.
3.方法1--回溯法，采用暴力枚举，会因为过度递归求解，超出时间限制，枚举出所有可能，得到个数最少的一个
4.具体思考见Markdown--01_perfect_squared.md
"""

class Solution(object):
    def numSquares(self, n):
        # 列举出整数n内的所有平方数
        square_nums = [i ** 2 for i in range(1, int(math.sqrt(n)+1))]

        def minNumSquare(k):
            # 使用递归法找到平方数的个数
            if k in square_nums:
                return 1
            min_num = float('inf')

            # 在所有可能的组合中找到个数最少的组合
            for square in square_nums:
                if k < square:
                    break
                new_num = minNumSquare(k - square) + 1
                min_num = min(min_num, new_num)
            return min_num

        return minNumSquare(n)


if __name__ == '__main__':
    n = int(input('请输入一个正整数n：'))
    n_so = Solution()
    print("结果是：", n_so.numSquares(n))