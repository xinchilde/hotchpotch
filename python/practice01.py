'''
    python开始学习第一例：利用分支模拟用户登录
    注意：input函数相当于java里面的Scanner类,当input接受的是字符串
'''
# 定义正确的用户名和密码
ACCOUNT = 'admin'
PASSWORD = '654321'

# 接收用户输入的账户信息
print('请输入用户名：')
temp_account = input()

print('请输入密码：')
temp_password = input()

# 校验结果
if not(temp_account and temp_password):
    print('用户名或者密码不能为空!')
elif temp_account != ACCOUNT:
    print('用户名或密码不正确！')
elif temp_password != PASSWORD:
    print('用户名或密码不正确！')
else:
    print('恭喜你通过验证！！！')
