# file = open('5juli/File/note2.txt', 'x')
# file.write('hello world')
# file.close()

file = open('5juli/File/note3.txt', 'w')
file.write('baris ke-1\n')
file.write('baris ke-2\n')
file.write('baris ke-3\nbaris ke-4')
file.close()

file = open('5juli/File/note.txt', 'a')
file.write('baris append 1\nbaris append 2\n')
file.close()

file = open('5juli/File/note4.txt', 'a')
file.write('baris append 1\nbaris append 2\n')
file.close()

file = open('5juli/File/note4.txt', 'r')
print(file.read())
file.close()


