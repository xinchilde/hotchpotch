'''
    python学习第二个例子：利用input函数实现一个分配水果任务
'''

# 接受用户的输入
print('''
---分配水果游戏---
有三个选项(输入1、2或者3)：
1：给小明 2：给小红 3：喂狗
''')
x = input()
print(type(x))
x = int(x)

# 判断
if x == 1:
    print('给小明吃苹果！')
elif x == 2:
    print('给小红吃香蕉！')
else:
    print('丢了喂狗！')