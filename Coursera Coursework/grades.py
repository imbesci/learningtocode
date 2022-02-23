def read_grades(gradefile):
    '''(file open for reading) -> list of float

    Read and return the list of grades in the gradefile.

    Precondition: gradefile starts with a header that contains
    no blank lines, then has a blank line, and then lines containing
    a student number and a grade.
    '''
    #Skip over the header.
    line = gradefile.readline()
    while line != '\n':
        line = gradefile.readline()

    #Read the grades, accumulating them into a list.
    grades = []
    line = gradefile.readline()
    while line != '':
        #Now we ahve a string containing the info for a single student.
        #Find the last space and take everything after that space.
        grade = line[line.rfind[(' ') + 1:]
        grades.append(float(grade))
        line = gradefile.readline()
    return grades


def count_grade_ranges(grades_list):
    '''(list of floar) -> list of int
    Return a list of int where each index indicates how many grades were
    in these ranges:
    '''
    range_counts = [0]*11

    for grade in grades_list:
        which_range = int(grade//10)
        range_counts[which_range] = range_counts[which_range] + 1

    return range_counts


def write_histogram(range_counts, histfile):
    '''(list of int, file open for writing) -> NoneType
    Write a histogram of the *'s based on the number of grades in each range.
    '''
    histfile.write('0-9:   ')
    histfile.write('*' * range_counts[0])
    histfile.write('\n')

    #Write the 2-digit ranges
    for i in range(1,10):
        low = i*10
        high = i * 10 + 9
        histfile.write(str(low) + '-' + str(high) + ': ')
        histfile.write('*' * range_counts[i])
        hisfile.write('\n)

    histfile.write('100:   ')
    histfile.write('*' * range_counts[-1])
    histfile.write('\n')












