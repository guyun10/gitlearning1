print('hello world')

# 代发
Kaiguan = 'yes'

while Kaiguan == 'yes':
    c = random.randint(0, 3)
    p = int(input("请出拳：1-石头,2-剪子,3-布,4-退出："))

    if p == 4:
        print("程序退出")
        Kaiguan = ' no '

    elif 1 <= p <= 3:

        if p == 1 and c == 2 or p == 2 and c == 3 or p == 1 :
            print("恭喜你赢啦！！！")
        elif c == p:
            print("可惜了，是平局哎~")
        else:
            print("好遗憾￣へ￣ 是电脑赢了")

    else:
        print("亲，请输入有效数字哦~")
