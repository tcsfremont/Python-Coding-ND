import sys

for index in range(len(sys.argv)):
    
    if sys.argv[index] == '_':

        sys.argv[index] = input("Enter a word")
sys.argv.pop(0)
result = ' '.join(sys.argv)
print(result)
print( sys.argv)
