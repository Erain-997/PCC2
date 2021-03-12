def fn():
    try:
        for i in range(10):
            if i >3:
                print('随机数字是：',i)
                raise Exception("数字大于3了")#自定义异常用raise抛出异常
    except Exception as ret:
        print(ret)
fn()