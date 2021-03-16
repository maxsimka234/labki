def longest_sentence(text):
    sentence_list=[]
    sentence_=[]
    i=0
    while i in range(len(text)):
        
        if(i>0):
            if(text.count(text[i])>2):
                sentence_.append(text[i])
                   
            elif(text.count(text[i-1])>2) and (text.count(text[i])<2):
                sentence_list.append(sentence_[:])
                sentence_.clear()
        else:
            if(text.count(text[i])>2):
                sentence_.append(text[i])
        i+=1           
    max_sentence_len=len(sentence_list[0])
    max_sentence=sentence_list[0]
    for i in sentence_list:
        if (len(i)>max_sentence_len):
            max_sentence_len=len(i)
            max_sentence=i
    return max_sentence


import random

dictionary1=('Бесплатный сервис Google позволяет мгновенно переводить слова, фразы и веб-страницы с английского более чем на 100 языков и обратно').split()
dictionary2=('Яндекс.Переводчик — синхронный перевод для 99 языков, подсказки при наборе, словарь с транскрипцией, произношением и примерами').split()
dictionary3=('Перево́дчик специалист, занимающийся переводом, то есть созданием письменного или устного текста на определённом языке').split()
print("рандомна фраза : "+dictionary1[random.randint(0,len(dictionary1)-1)]+" "+dictionary2[random.randint(0,len(dictionary2)-1)]+" "+dictionary3[random.randint(0,len(dictionary3)-1)]+"\n")

f = open("text.txt","r")
text=(f.read())
print('кількість символів з пробілами:',len(text))
print('кількість символів без пробілів:',len(text)-text.count(' '))
print('кількість слів : ',len(text.split()))
print('кількість унікальних слів : ',len(set(text.split())))
print(longest_sentence(text.split()))



f.close()