#读文件，得到所有四级词汇
def getWord(line):
    newlist = []
    wlist = line.split(' ')
    for x in wlist:
        if x != '':
            newlist.append(x)
    return newlist[0]

f = open('C:/Users/yllzxzyq/Desktop/1.txt','r',encoding='utf-8')
dic={}
i=0
for line in f.readlines():
    if line !='\n':
        word=list(getWord(line))
        flist=list(word)
        flist.sort()
        finger=""
        for z in flist:
            finger+=z
        if finger in dic:
            dic[finger][i]=word
        else:
            dic[finger]={}
            dic[finger][i]=word
        i+=1

for value in dic.values():
    if len(value)>1:
        print(value)

#
#for line in f.readlines():
#    try:                                              
#        words.append(getWord(line))
#    except:
#        #print(line)
#        pass

#
#for word in words:
#    li=list(word)
#    li.sort()
#    finger="".join(li)
#    if finger in dic:
#        dic[finger].append(word)
#    else:
#        dic[finger]=[word]


#for x in dic.values():
#    if len(x)>=2:
#        print(x)
#对比指纹，编入词典
#查找词典中leg(value[])>1,并输出

