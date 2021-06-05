'''
    python学习第四个例子：利用for实现数据的遍历
    注意：for和while一样，可以单独使用，也可以结合else使用
'''

# 定义一个数组
a = [110,119,120,12315,13123,10001,10010,10086]

# 使用for循环数组，类似与java里面的foreach（也称增强for循环）
for x in a:
    print(x)
else:
    print('循环结束')


# for循环结合 continue 和 break （注意：执行break之后，else也不执行）
print("结合'continue'和'break'使用")
for x in a:
    if x == 120:
        continue
    if x == 13123:
        break
    print(x)
else:
    print('循环结束')

# for循环之：指定执行次数
print("for循环之：指定执行次数,类似java里面的 fori ==> for(int i = 0;i<10;i++)")
for x in range(1,10):
    print(x)