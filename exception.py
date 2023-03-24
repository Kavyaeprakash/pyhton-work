try:
    f=open('sample.txt','a')
    f.write('open text file')
    f.close()
except FileNotFoundError:
    print('file not found')
except IOError:
    print('not writable')
else:
    print('succesfully write to the file')
finally:
    print('execution compleated')

