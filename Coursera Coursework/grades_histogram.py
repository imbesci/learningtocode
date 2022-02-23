import tkinter.filedialog
import grades

a1_filename = tkinter.filedialog.askopenfilename()
a1_file = open(a1_filename, 'r')

a1_histfilename = tkinter.filedialog.asksaveasfilename()
a1_hist = open(a1_histfilename, 'w')

#Read the grades into a list
grades = grades.read_grades(a1_file)

#Count the grades per range.
range_count = grades.count_grade_ranges(grades)

#Write the histogram to the file
grades.write_histogram(range_counts, a1_histfile)

a1_file.close()
a1_hist.close()
