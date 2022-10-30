#7-1
message=input('what car do you need to rent?')
print('Let me see if i can find you a '+message)

#7-2
message=input('how many people are eating there?')
message=int(message)
if message>=8:
    print('no empty table')
else:
    print('come in')

#7-3
message=input('please input a number')
if int(message)%10 == 0:
    print('this number is a x0')
else:
    print('this number is not a x0 ')

#7-4
prompt='\nplease enter pizza ingredients'
prompt+="\nenter 'quit' to end the prohram"
active=True
while active:
    message=input(prompt)
    if message=='quit':
        active=False
    else:
        print('we will add the ingredients'+message)

#7-5
prompt='please enter your age'
prompt+="\nenter 'quit' to end"
while True:
    age=input(prompt)
    if age=='quit':
        break
    else:
        if int(age)<=3:
            print('free')
        elif int(age)>3 and int(age)<=12:
            print('10')
        else:
            print('15')

#7-7
#while True
#print('1')

#7-8
sandwich_orders=['s1','s2','s3']
finshed_sandwiches=[]
while sandwich_orders:
    ms=sandwich_orders.pop()
    print('I make your '+ms+' sandwich')
    finshed_sandwiches.append(ms)
print('finsh_sandwiches:')
for s in finshed_sandwiches:
    print(s)

#7-9
sandwich_orders=['s1','pastrami','s2','pastrami','s3','pastrami']
print('the pastrami is sold out')
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
print(sandwich_orders)

#7-10
responses={}
active=True
while active:
    name=input("what's your name?")
    response=input("if you could visit one place in the world,where would you go?")
    responses[name]=response
    repeat=input("would you like let another person respond?(yes/no) ")
    if repeat=='no':
        active=False
print("\n----end----")
for key,value in responses.items():
    print(key+' want to go '+value)
