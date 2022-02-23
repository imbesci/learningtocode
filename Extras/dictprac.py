student = {'name': 'John', 'age': 25, 'courses':'Compsci'}

student.update({'name': 'Jane', 'age': 26, 'phone': '555-5555'})

#dict.update({dict of things to update}) will update the dictionary. it will update already existign key value pairs and add new ones if needed
#dict.items() #returns the keys and values in a list, each key value pair is a tuple
#dict.get('key') returns a value from the key specified


for key, value in student.items():
    print(key, value)


