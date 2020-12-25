d = {}

while True:
    print("")
    print('1. 建立字彙表')
    print('2. 列出全部單字')
    print('3. 英翻中')
    print('4. 中翻英')
    print('5. 測驗學習結果')
    print('6. 離開系統')
    
    select = int(input('請輸入選項:'))
    
    if select==1:
        while True:
            e = input('請輸入英文單字(輸入0退出):') 
            if e == '0':
                break
            c = input('請輸入中文單字:')
            d [c] = e
    elif select==2:
        for key,value in d.items():
            print(key,value)
    elif select==3:
        e1 = input('請輸入英文:')
        for key,value in d.items():
            if value == e1:
                print(key)
    elif select==4:
        c1 = input('請輸入中文:')
        for key in d.keys():
            if c1 == key:
                print(d[c1])
    elif select==5:
        r=0
        for key,value in d.items():
            T = input('請輸入' + key + '的英文:')
            if T == value:
                r=r+1
                print('答對了!現在答對'+ str(r)+'題')
            else:
                print('答錯了!現在答對'+ str(r)+'題')
        print('總共' + str(len(d)) + '題,'+'答對' + str(r) + '題')        
    elif select==6:
        break
    else:
        print('wrong input')
        
    
                
        