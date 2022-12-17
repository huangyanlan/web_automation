def creatGenerator():
    mylist = range(3)

    for i in mylist:
        yield i*i
        print("循环内打印")
    # yield mylist
    print("循环外打印")
if __name__ =='__main__':
    mygennerator = creatGenerator()
    print(f"函数返回值类型{type(mygennerator)}")

    for i in mygennerator:
        print(i)
        print("胡呼呼呼")
