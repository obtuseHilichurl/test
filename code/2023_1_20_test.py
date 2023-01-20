# print(1,2,3,4,sep="\\",end="!\n")#sep为中间间隔，默认为空格。end为末尾，默认为空行
# print('{0:.3f}'.format(1.0/3,1))#自动计算并保留三位小数
# print('{1:.3f}'.format(1.0/3,1))#用第二个数字
# print('{00001:.3f}'.format(1.0/3,1))# 自动转化数字
# print('{0:_^11}'.format('hello'))# 使用下划线填充文本，并保持文字处于中间位置, 使用 (^) 定义 '___hello___'字符串长度为 11
# print('{name} wrote {book}'.format(name='Swaroop', book='A Byte of Python'))# {}内还可填变量名
# print("hello\
# world")#末尾的\表示下行继续，python的普通代码都能这么用(但不能用在函数名，变量名等等里边)
# print\
#     ("你好")
# print("hello\tworld")#转义字符
# print(r"hello\tworld")#原始字符串