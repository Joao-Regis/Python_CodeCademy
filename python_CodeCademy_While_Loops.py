all_students = ["Alex", "Briana", "Cheri", "Daniele", "Dora", "Minerva", "Alexa", "Obie", "Arius", "Loki"]
students_in_poetry = []

print('length of poetry = ' + str(len(students_in_poetry)))
print('\n')

while len(students_in_poetry) < 6:
  print('length of poetry before append = ' + str(len(students_in_poetry)))
  students_in_poetry.append(all_students.pop())
  print(students_in_poetry)
  print('length of poetry after append = ' + str(len(students_in_poetry)))
  print('\n')