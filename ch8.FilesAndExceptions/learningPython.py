from pathlib import Path

path = Path('ch8.FilesAndExceptions/learning_Python.txt')
contents = path.read_text()

print(contents.replace('Python', 'C'))

# py_strings = ''
# for line in contents :
#     py_strings += line

# print(py_strings)

for line in contents.splitlines() :
    print(line)