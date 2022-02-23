

def student_info(*args, **kwargs):
    print(args)
    print(kwargs)



subjects = ['Math', 'Art']
info = {'name': 'john', 'age': 25}



student_info(*subjects, **info)