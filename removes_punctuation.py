file=open("1.txt",'r')
sentence=file.read()
punctuations = '''!()‘-[]{};:’'"\,<>./?؟@#$%^&*_~۔'''#This code defines punctuation
#This code removes the punctuation
no_punct = "" 
for char in sentence:
    if char not in punctuations:
        no_punct = no_punct + char

no_punct1 =(str.lower (no_punct))
file=open("saad.txt",'w')
file.write(no_punct1)
#print(no_punct1)
