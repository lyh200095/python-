#6-1
person1={'first_name':'li','last_name':'xue','age':'22','city':'shenyang'}
print(person1)

#6-2
fn={'n1':'1','n2':'2','n3':'3','n4':'4','n5':'5'}
print('n1 '+fn['n1']+' this is your fn?')
print('n2 '+fn['n2']+' this is your fn?')
print(fn['n3']+' this is your fn?')
print(fn['n4']+' this is your fn?')
print(fn['n5']+' this is your fn?')

#6-3,6-4
bc={'for':'xunhuan','list':'liebiao','array':'shuzu','dist':'zidian','print':'shuchu'}
for key,value in bc.items():
    print(key+value)

#6-5
hg={'nile':'egypt','cj':'china','mssp':'american'}
for key,value in hg.items():
    print('The '+key.title()+' run through '+value.title())
for key in hg:
    print(key)
for value in hg.values():
    print(value)

#6-6
favorite_languages={'jen':'python','sarah':'c','edward':'ruby','phil':'python'}
people=['jen','sarah','raby','phik']
for key,value in favorite_languages.items():
    if key in people:
        print(key+' thank you' )
    else:
        print(key+' please join us')


#6-7
person1={'first_name':'li','last_name':'xue','age':'22','city':'shenyang'}
person2={'first_name':'li','last_name':'xue','age':'22','city':'shenyang'}
person3={'first_name':'li','last_name':'xue','age':'22','city':'shenyang'}
person=[person1,person2,person3]
for p in person:
    print(p)

#6-8
cat={'name':'cat','type':'t1','owner':'p1'}
dog={'name':'dog','type':'t2','owner':'p2'}
pig={'name':'pig','type':'t3','owner':'p3'}
bird={'name':'bird','type':'t4','owner':'p4'}
pets=[cat,dog,pig,bird]
for pet in pets:
    print(pet)

#6-9
favorite_places={'x':['x1','x2','x3'],'y':['y1','y2','y3'],'z':['z1','z2','z3']}
for key,values in favorite_places.items():
    print(key.title()+'like:')
    for value in values:
        print(value)

#6-10
n1=[1,2]
n2=[3,4]
n3=[4,5]
fn={'p1':n1,'p2':n2,'p3':n3}
for key,values in fn.items():
    print(key+' like')
    for value in values:
        print(value)

#6-11
cities={
    'xian':{
        'country':'c1',
        'population':'p1',
        'about':'a1'
         },
    'changsha':{
        'country':'c2',
        'population':'p2',
        'about':'a2'
        },
    }
for key,values in cities.items():
    print(key)
    for key1,values1 in values.items():
        print(key1+values1)

