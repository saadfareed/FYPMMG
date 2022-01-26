def bracketscore(sentence):
    number=0
    for i in sentence:
        #print(i)
        #print(len(i))
        if (i=='(' or i=='[' or i==']' or i==')'):
            number=number+1
    
    number=number/2
    number=number**0.5
    number=1/number
    return number

sentence="(I am a boy(saad).i am student(computer science))"
print(bracketscore(sentence))
