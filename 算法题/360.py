
s=input()
d={}
# for i in range(len(s)):
#     for j in range(i,len(s)):
#         if s[i:j+1] in d:
#             d[s[i:j+1]]+=1
#         else:
#             d[s[i:j+1]]=1
# print(max(d.values()))
for i in range(len(s)):
    if s[i] in d:
        d[s[i]]+=1
    else:
        d[s[i]]=1
print(max(d.values()))

# count ={}
# for i in set(s):
#     count[i]=s.count(i)
# print(count)
# # print(max(count.items(),key=lambda x:x[1])[0]）
# max_value=max(count.values())
# l=[]
# for k,v in count.items():
#     if v==max_value:
#         print(k)