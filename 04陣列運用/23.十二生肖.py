#23.十二生肖
y = {
    0:"rat",
    1:"ox",
    2:"tiger",
    3:"rabbit",
    4:"dragon",
    5:"snake",
    6:"horse",
    7:"sheep",
    8:"monkey",
    9:"rooster",
    10:"dog",
    11:"pig"
}
n = int(input())
n = (n - 2008)%12
print(y[n])
#前面的語法