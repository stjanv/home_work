from operator import itemgetter
import collections
list1 = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]
#task1


def swap(list1):
    list1_index_x = 2
    list1_index_y = 3
    list1[list1_index_x], list1[list1_index_y] = list1[list1_index_y], list1[list1_index_x]
    return list1
print(swap(list1))


#task2



def mutka(list1):
    list3=[]
    for i in range(len(list1)):
        list3.append(bin(i))
    return list3


def mutka2(list2):
    list3 = []
    for i in list2:
        calk = 0
        for j in i:
            if j == '1':
                calk += 1
        if calk >= 2 and calk % 2 == 0:
            list3.append(i)
    return list3


def mutka3(list3,list1,list2):
    summ=0
    for i in list3:
        for j in list2:
            if i ==j :
                summ+=list1[list2.index(j)]
    return summ*list1[len(list1)-1]



list2 = mutka(list1)
print(list2)
list3=mutka2(list2)
print(list3)
print(mutka3(list3,list1,list2))


#task 3


a = input()
def check_for_registry(a):
    g = True
    for i in a:
        if i.isupper():
            g = False
    return g
def check_for_cheet(a):
    k = 0
    n = 0
    for i in a:
        if i.isdigit():
            k += 1
        else:
            n += 1
    if k % 2 == 0 and n % 2 == 1:
        return True
    else:
        return False
def check(a: str):
    if len(a) > 4 and check_for_registry(a) and check_for_cheet(a):
        print('Pass is successful')
    else:
        print('Pass is incorrect')
print(check_for_registry(a))
print(check_for_cheet(a))
check(a)

#task4
autos = [

    {"brand": "Ford", "model": "Mustang", "year": 1964, "price": 4000},

    {"brand": "Ford", "model": "Mondeo", "year": 1999, "price": None},

    {"brand": "Ford", "model": "Fiesta", "year": 2003, "price": 4200},

    {"brand": "Nissan", "model": "Primera", "year": 1997, "price": 3100},

    {"brand": "BMW", "model": "X3", "year": 2001, "price": 5000},

    {"brand": "Nissan", "model": None, "year": 1964, "price": None},

    {"brand": "VW", "model": "Passat", "year": 1996, "price": 1200},

    {"brand": "BMW", "model": "X5", "year": 2010, "price": 7500},

    {"brand": "Renault", "model": "Megane", "year": 1999, "price": 2300}

]

def change(autos):
    for i in autos:
        if i['price'] == None:
            i['price'] = 0
    return autos

def dis_change(autos):
    for i in autos:
        if i['price']==0:
            i['price']=None
    return autos

def by_key(autos):
    for i in range(len(autos)):
        for j in range(len(autos)):
            if  autos[i]['price']<autos[j]['price']:
                autos[i],autos[j]=autos[j],autos[i]
    return autos

autos=change(autos)
autos=sorted(autos, key=lambda x: x['price'])[::-1]
autos=dis_change(autos)
print(autos)

autos=change(autos)
print(autos)
autos=by_key(autos)[::-1]
print(dis_change(autos))




