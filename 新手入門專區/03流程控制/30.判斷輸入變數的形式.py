#30.判斷輸入變數的形式
n = input()
try:
    i =int(n)
    print("int")
except ValueError:
    try:
        f = float(n)
        print("float")
    except ValueError:
        if len(n)==1:
            print("char")
        else:
            print("string")
#try-except是一組程式，當裡面的程式出錯時，可以根據不同的錯誤形式延伸後續指令
#ValueError：值的型別對，但內容不合法
#TypeError：型別錯了
#IndexError：存取超出範圍
#KeyError：查不到指定的Key