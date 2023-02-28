#Return values VS printing values

#Returning values
def get_full_name(first,last):
    """When we return values, we need a variable assigned to the function call to store the return value"""
    full_name = first + ' ' + last
    return full_name.title()

musician = get_full_name('jimi', 'hendrix')
print(musician)


#Printing values
def get_full_name(first,last):
    """Return a nearly formatted full name"""
    full_name = first + ' ' + last
    print(full_name.title()) 

get_full_name('jimi', 'hendrix')

#Returning a Dictionary

def build_person(first,last):
    '''Return a dictionary with info about a person'''
    person = {'First' : first, 'Last' : last}
    return person

musician = build_person('Gary','Kasparov')
print(musician)

#Returning a Dictionary with Default values

def build_person(first,last='Doe'):
    '''Return a dictionary with info about a person'''
    person = {'First' : first, 'Last' : last}
    return person

musician = build_person('John')
print(musician)

#Returning a Dictionary with Optional values

def build_person(first,last,age=None):
    '''Return a dictionary with info about a person'''
    person = {'First' : first, 'Last' : last}
    if age:
        person['Age'] = age
    return person

musician = build_person('Fabrizio','Modena',44)
print(musician)
musician1 = build_person('Marcelo','Firenze')
print(musician1)
