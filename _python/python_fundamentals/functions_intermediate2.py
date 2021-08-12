
#1

x = [ [5,2,3], [10,8,9] ]
x[1][0]=15
print(x) 
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
students[0].update({'last_name':'Bryant'})
print(students)
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
sports_directory['soccer'][0]='Andre'
print(sports_directory['soccer'])


z = [ {'x': 10, 'y': 20} ]
z[0].update(y=30)
print(z)

#2
students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

def iterateStudents(list):
        for x in list:
            first_name = x['first_name']
            last_name =x['last_name']
            string = f'first_name - {first_name}, last_name - {last_name}'
            print(string)
iterateStudents(students)


#3
def iterateDictionary2(key_name,some_list):
    for x in some_list:
        key = x[key_name]
        print(key)

iterateDictionary2('first_name',students)
iterateDictionary2('last_name',students)

#4
dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printInfo(some_dict):
    for x in some_dict:
        count = 0
        for name in some_dict[x]:
            count+=1
        print(count, x)
        for name in some_dict[x]:
            print(name)    
printInfo(dojo)
