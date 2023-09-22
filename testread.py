with open('log.txt','r',encoding='utf-8') as file:
    text = file.readlines()
    #print(text)
    
for r in text:
    print(r.strip().split(','))