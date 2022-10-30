#8-1
def display_message():
    print('function')
display_message()

#8-2
def favorite_book(title):
    print('one of my favorite books is '+title)
favorite_book('Alice in wonderland')

#8-3
def make_shirt(size,words):
    print('the shirt \nsize: '+size+'\nwords: '+words)
make_shirt('m','python')

#8-4
def make_shirt1(size='T',words='I love Python'):
    print('the shirt \nsize: '+size+'\nwords: '+words)
make_shirt1()
make_shirt1(size='m')
make_shirt1('m','i love python')

#8-5
def decribe_city(name,country='china'):
    print(name+' is in '+country)
decribe_city('xian')
decribe_city('sjz')
decribe_city('tokoy','japan')

#8-6
def city_country(name,country):
    result=name+', '+country
    return result
n=[city_country('n1','c1'),city_country('n2','c2'),city_country('n3','c3')]
for c in n:
    print(c)

#8-7
def make_album(singer,album,song=''):
    if song:
        p={'singer':singer,'album':album,'song':song}
    else:
        p={'singer':singer,'album':album}
    return p

print(make_album('s1','a1'))
print(make_album('s2','a2'))
print(make_album('s3','a3',song='9'))

#8-8
def make_album(singer,album,song=''):
    if song:
        p={'singer':singer,'album':album,'song':song}
    else:
        p={'singer':singer,'album':album}
    return p
while True:
    print('please input a singer and the album')
    print('input q to end the program')
    s = input('singer:')
    a = input('album:')
    g = input('song:')
    if s == 'q' or a == 'q' or g == 'q':
        break
    n1 = make_album(s, a, g)
    print(n1)

#8-9
def show_magicians(magician):
    for n in magician:
        print(n)
magician=['m1','m2','m3']
show_magicians(magician)

#8-10
def make_great(magician):
    n=len(magician)
    i=0
    while i<n:
        magician[i]='the great '+magician[i]
        i=i+1
make_great(magician)
show_magicians(magician)

#8-11
def make_magician(magician,a):
   n=len(magician)
   i=0
   while i<n:
       a.append("The great "+magician[i])
       i=i+1
a=[]
make_great(magician[:],a)
show_magicians(a)
print(magician)

#8-12
def sand(*toppings):
    print('user put these toppings:')
    print(toppings)
sand('a')
sand('a','b')

#8-13
def build_profile(first,last,**user_info):
    profile={}
    profile['first_name']=first
    profile['last_name']=last
    for key,value in user_info.items():
        profile[key]=value
    return profile
user_profile=build_profile('l','h',food='f1',school='s1',country='c1')
print(user_profile)

#8-14
def car_info(manufacturer,model,**car_info):
    info={}
    info['manufactuer']=manufacturer
    info['model']=model
    for key,value in car_info.items():
        info[key]=value
    return info
car=car_info('subaru','outback',color='blue',two_package=True)
print(car)




