# class Stack():   #定义类
# 	def __init__(self):  #产生一个空的容器
# 		self.__list = []
# 	def push(self, item):  #入栈
# 		self.__list.append(item)
# 	def pop(self):  #出栈
# 		return self.__list.pop()
# 	def speek(self):  #返回栈顶元素
# 		return self.__list[-1]
# 	def is_empty(self):  #判断是否已为空
# 		return not self.__list
# 	def size(self):  #返回栈中元素个数
# 		return len(self.__list)
#
# if __name__ == '__main__':
# 	s = Stack()
# 	c = 1
# 	s.push('a')
# 	s.push('b')
# 	s.push(c)
# 	print('size:' + str(s.size()))
# 	print('speek:' + str(s.speek()))
# 	print(s.pop())
# 	print(s.pop())
# 	print(s.pop())
# 	print('size:' + str(s.size()))


class Solution(object):
    def largestRectangleArea(heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        res = 0
        stack = list()
        heights = [0] + heights + [0]

        for i in range(len(heights)):
            while stack and heights[stack[-1]] > heights[i]:
                top = stack.pop()
                res = max(res, (i - stack[-1] - 1) * heights[top])

            stack.append(i)
        print(res)
        return res

Solution.largestRectangleArea([2,1,2,3,1,3])