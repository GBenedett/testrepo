import imp
from pathlib import Path

path = Path()
#path = Path("ecommerce")
#print(path.mkdir()) #to create a directory
#print(path.rmdir()) #to remove a directory
#print(path.glob('*.py')) #to search file or directory, if I put a * mean everything, it is also possible search some extension 

for file in path.glob('*.py'):
    print(file)