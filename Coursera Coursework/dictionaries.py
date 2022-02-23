fruit_to_color = {'watermelon': 'green', 'pomegranate': 'red',
'peach': 'orange', 'cherry': 'red', 'pear': 'green',
'banana': 'yellow', 'plum': 'purple', 'orange': 'orange'}

# Invert fruit_to_color
color_to_fruit = {}
for fruit in fruit_to_color:
    color = fruit_to_color[fruit]


    #if color is not already a key in the accumulator,
    # add color: [fruit] as an entry
    if not (color in color_to_fruit):
        color_to_fruit[color] = [fruit]
    #otherwise, if append fruit to existing list.
    else:
        color_to_fruit[color].append(fruit)

def read_grades(gtadefile)
    ''' (file open for reading) -> dict of (float : list of str)

    Read the grades from the gradefile and return a dictionary where each grade is
    a key and each value is the list of ids of students who got that grade.

    Precondition: gradefile starts with a header that contains no blank lines,
    then has a blank line, and then lines containing a number and a grade.
    '''
    #skip over the header
    line = gradefile.readline()
    while line != '\n':
        line = gradefile.readline()

    #read the grades, accumulting them into a dict
    grade_to_ids = {}
    line = gradefile.readline()

    while line != '':

        student_id = line[:4]
        grade = float(line[4:].strip())

        if grade not in grade_to_ids:
            grade_to_ids[grade] = [student_id]
            
        else:
            grade_to_ids[grade].append(student_id)

        line = gradefile.readline()

    return grade_to_ids


        
