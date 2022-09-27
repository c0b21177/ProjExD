import random
import datetime

alphabet = 26
quiz_chars = 10
time = 2
abs = 2

def quiz(Alpha):
    chars = random.sample(Alpha,quiz_chars)
    print("対象文字:" , end="")


    for i in sorted(chars):
        print(i , end=" ")
    print()
    print("表示文字:" , end="")
    van_chars = random.sample(chars,abs)


    for i in chars:
        if i not in van_chars:
            print(i, end=" ")
    print()
    print("欠損文字：", van_chars)
    return van_chars

def ans(van_chars):
    num = int(input("消えた文字は何文字でしょうか？"))
    if num != abs:
        print("ざんねん！")
    else:
        print("正解！　では何が欠損しているでしょうか？")

        
        for i in range(time):
            M = input(f"{i+1}文字目")
            
            if M not in van_chars:
                print("不正解！ざんねん！")
                return False
            else:
                van_chars.remove(M)
        else:
            print("正解！すごい！")
            return True
        return False

if __name__ == "__main__":
    Alpha = [chr(i+65) for i in range(alphabet)]
    
quiz()
ans()
