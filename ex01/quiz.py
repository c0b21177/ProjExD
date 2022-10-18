import random

Q = ["サザエの旦那の名前は？", "カツオの妹の名前は？", "タラオはカツオから見てどんな関係？"]
A = [["マスオ", "ますお"], ["ワカメ", "わかめ"], ["甥っ子", "おいっこ", "甥", "おい"]]

num = random.randint(0,2)

def quiz():
    print("問題:" + Q[num])
    Ans = input("回答:")
    if Ans in A[num]:
        print("正解！！")
    else:
        print("不正解！！")

quiz()
