#5-1
car = 'subaru'
print("\ncar == 'subaru'? I predict True.")
print(car == 'subaru')
print("car == 'audi'?I predict Flase.")
print(car == 'audi')

#5-2
car='Audi'
print(car=='Car')
print(7!=8)
print('car' == 'Car'or'li'=='li')
print('car' == 'Car'and'li'=='li')
cat=['a','b','c']
print('a' in cat)
print('c' not in cat)

#5-3
alien_color='green'
if alien_color=='green':
    print("you get 5 point")
alien_color='red'
if alien_color=='green':
    print('you get 5 point')

#5-4
alien_color='green'
if alien_color=='green':
    print('you get 5 point')
else:
    print('you get 10 point')
alien_color='red'
if alien_color=='green':
    print('you get 5 point')
else:
    print('you get 10 point')

#5-5
alien_color='green'
if alien_color=='green':
    print('you get 5 point')
elif alien_color=='red':
    print('you get 10 point')
else:
    print('you get 15 point')

#5-6
age=16
if age<=2:
    print('baby')
elif age>=2 and age<=4:
    print('learn to walk')
elif age>=4 and age<=13:
    print('child')
elif age>=13 and age<=20:
    print('teenager')
elif age>=20 and age<=65:
    print('adult')
else:
    print('old people')

#5-7
favorite_fruits=['apple','pear','bananas']
if 'apple' in favorite_fruits:
    print("you really like apple")
if 'pear' in favorite_fruits:
    print("you really like pear")
if 'strawberry' in favorite_fruits:
    print("you really like strawberry")
if 'bananas' in favorite_fruits:
    print("you really like bananas")
if 'orange' in favorite_fruits:
    print("you really like orange")

#5-8
users=['admin','u1','u2','u3','u4']
for user in users:
    if user=='admin':
        print('hello admin,would you like to see a status report?')
    else:
        print("hello "+user+' thank you for logging in again')

#5-9
users=[]
if users:
    for user in users:
        if user=='admin':
            print('hello admin,would you like to see a status report?')
        else:
            print("hello " + user + ' thank you for logging in again')
else:
    print('we need to find some users')

#5-10
current_users=['u1','u2','u3','u4','u5']
new_users=['u4','u5','u6','u7','u8']
for new_user in new_users:
    if new_user in current_users:
        print(new_user+' has already been used,please input another one')
    else:
        print(new_user+' is not being used')

#5-11
nums=list(range(1,10))
for num in nums:
    if num==1:
        print(str(num)+'st')
    elif num==2:
        print(str(num)+'nd')
    elif num==3:
        print(str(num)+'rd')
    else:
        print(str(num)+'th')


