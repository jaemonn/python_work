# fhand = open('freecodecamp/sample.txt')
# count = 0
# for line in fhand :
#     count = count + 1
# print('Line count:', count)

# searching through a file
# fhand = open('freecodecamp/sample.txt')
# for line in fhand :
#     line = line.strip()
#     if line.endswith('Mond') :
#         print(line)

# prompt a file name
fname = input("Enter file name: ")
fhand = open(fname)
print(fhand)