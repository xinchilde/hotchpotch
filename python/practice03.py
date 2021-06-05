'''
    python学习第三个例子：利用while模拟升级效果
'''

# while循环
print('while循环')
count = 1;
while count < 18:
    if count < 6:
        print('吭呲~吭呲~埋头补兵中......') 
    elif count < 13:
        if count % 3 == 0:
            print('拆个塔~~~')
        if count % 3 == 1:
            print('打个野~~~')
        if count % 3 == 2:
            print('抢个头~~~')
    else:
        print('参团大战中......')
    count+=1
    print('叮~恭喜你，成功升级！当前等级：' + str(count))

print('恭喜你，获取飞升~')



# while-else 循环
print('while-else 循环')
count = 1;
while count < 18:
    if count < 6:
        print('吭呲~吭呲~埋头补兵中......') 
    elif count < 13:
        if count % 3 == 0:
            print('拆个塔~~~')
        if count % 3 == 1:
            print('打个野~~~')
        if count % 3 == 2:
            print('抢个头~~~')
    else:
        print('参团大战中......')
    count+=1
    print('叮~恭喜你，成功升级！当前等级：' + str(count))
else:
    print('恭喜你，获取飞升~')
