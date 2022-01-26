output=[]
file=open("1.txt",'r')
happy=file.read()
import re
sentence=re.split('۔|؟|\n',happy)
#saad=['saad is my name.',"fareed is my lastname.",'sadi is my nick name','saad happy birthday.']
#print(len(saad))
for i in sentence:
    #print(i)
    a=sentence.index(i)
    sa=output.append(a)
#print(output)
mid=max(output)-min(output)
mid=int(mid/2)
print(mid)
for i in range(mid-5,mid+5):
    print(sentence[i])