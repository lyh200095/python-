#3-1
name=['lin','chang','wu']
print(name[0])
print(name[1])
print(name[2])

#3-2
print(name[0]+' how are you')
message=' how are you'
print(name[1]+message)
print(name[2]+message)

#3-3
ty=['bike','car','sub']
sth="I would like to own a "
print(sth+ty[0])
print(sth+ty[1])
print(sth+ty[2])

#3-4
person=['sun','wu','da','tu']
print('welcome to my party '+person[0])
print('welcome to my party '+person[1])
print('welcome to my party '+person[2])
print('welcome to my party '+person[3])

#3-5
print(person[2]+' can not come')
person[2]='yao'
print('welcome to my party '+person[0])
print('welcome to my party '+person[1])
print('welcome to my party '+person[2])
print('welcome to my party '+person[3])

#3-6
print('I find a big table')
person.insert(0,'wang')
person.insert(2,'jia')
person.append('di')
print('welcome to my party '+person[0])
print('welcome to my party '+person[1])
print('welcome to my party '+person[2])
print('welcome to my party '+person[3])
print('welcome to my party '+person[4])
print('welcome to my party '+person[5])
print('welcome to my party '+person[6])

#3-7
print("I am sorry, I only can invite two person")
print("sorry I can't invite you"+person.pop())
print("sorry I can't invite you"+person.pop())
print("sorry I can't invite you"+person.pop())
print("sorry I can't invite you"+person.pop())
print("sorry I can't invite you"+person.pop())
print("welcome to my party"+person[0])
print("welcome to my party"+person[1])
del person[0]
del person[0]
print(person)

#3-8
travel=['xinjiang','maerdaifu','weinisi','xianggelila','sanya']
print(travel)
print(sorted(travel))
print(travel)
print(sorted(travel,reverse=True))
print(travel)
travel.reverse()
print(travel)
travel.reverse()
print(travel)
travel.sort()
print(travel)
travel.sort(reverse=True)
print(travel)

#3-9
print(len(person))

#3-10
like=['shoubiao','bailu','baoma','changbaishan']
print(like)
print(sorted(like))
like.sort(reverse=True)
print(like)
like.insert(2,'work')
like.append('black')
print(like)
del like[1]
like.pop()
print(like)

#3-11
error=['s1','s2']
print(error[1])





