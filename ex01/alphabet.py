import random
import datetime

Alpha = []
quiz_chars = 10
van_chars = []

for i in range(26):
    Alpha.append(chr(i + 65))

def quiz():
    chars = random.sample(Alpha,quiz_chars)
    print("対象文字:" , end="")
    for i in sorted(chars):
        print(i , end=" ")
    print()
    print("表示文字:" , end="")
    van_chars = random.sample(chars,2)
    for i in chars:
        if i not in van_chars:
            print(i, end=" ")
    print()
    print("欠損文字：", van_chars)

def ans():
    num = int(input("消えた文字は何文字でしょうか？"))
    if num == 2:
        print("正解！　では何が欠損しているでしょうか？")
    else:
        print("ざんねん！")
        
        for i in range(2):
            M = input(f"{i+1}文字目")
            if M not in van_chars:
                print("不正解！ざんねん！")
        else:
            print("正解！すごい！")
    
quiz()
ans()
