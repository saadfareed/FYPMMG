import numpy
final = []
result=[]
file=open("1.txt",'r')
inputText=file.read()
sentence=inputText
sentlen=len(sentence)
#print(sentlen)
sentence=sentence.split('۔')

def sentencelen(sentence):
    for i in sentence:
        ilen=len(i)
        alpha=ilen**0.5
        alpha=1/alpha
        results=alpha
        results=final.append(results)
        maximum=max(final)
    for x in final:
        fin=x/maximum
        saad=result.append(fin)
        
sentencelen(sentence)
sort_index = numpy.argsort(result)
#print(sort_index)
for i in range(int(len(sort_index)*.2)):
    print(sentence[i])
