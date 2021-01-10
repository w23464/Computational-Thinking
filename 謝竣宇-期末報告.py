print('你好，很高興為你服務')
while True:
    q=input('請問有訂位嗎?A.有 B.沒有 C.我只是來參觀的')
    if q=='A':
       name = input('請問您的大名')
       print('你好', name, ', 這邊請')
       while True:
           w = input('想吃什麼套餐呢?A.牛排 B.魚排 C.萊豬')
           if w=='A':
               print('我們的牛排都一律是五分熟，若不敢吃太生的，建議選魚排或是萊豬套餐')
               break
           if w=='B':
               print('我們的魚排是採用挪威空運的鮭魚，很好吃的喔!')
               break
           if w=='C':
               print('萊豬是加了大量的萊克多巴胺，肉質非常軟嫩，再加上主廚精緻的料理是我們店裡最受歡迎的套餐')
               break
    if q=='B':
        while True:
            e = input('我們目前室內的座位都滿了，請問要做室外嗎?A.要 B.不要')
            if e=='A':
                print('好的這邊請')
                while True:
                    r = input('想吃什麼套餐呢?A.牛排 B.魚排 C.萊豬')
                    if r=='A':
                        print('我們的牛排都一律是五分熟，若不敢吃太生的，建議選魚排或是萊豬套餐')
                        break
                    if r=='B':
                        print('我們的魚排是採用挪威空運的鮭魚，很好吃的喔!')
                        break
                    if r=='C':
                        print('萊豬是加了大量的萊克多巴胺，肉質非常軟嫩，再加上主廚精緻的料理是我們店裡最受歡迎的套餐')
                        break
                        
                   
            if e=='B':
                print('謝謝惠顧，歡迎下次再來')
                break
    if q=='C':
        print('不好意思，我們餐廳不提供參觀，歡迎下次來消費')
        break
    


        
        