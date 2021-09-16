import os

searchText = str(input("Type text what you want to search : "))
withAbsPath = str(input("Want to include absolute path? y=yes, n=no : "))
listPath = []

def searchProcess(path):
    os.chdir(path)
    lists = os.listdir()
    for data in lists:
        if os.path.isdir(data):
            searchProcess(data)
        if os.path.isfile(data):
            b = open(data, 'r')
            if searchText in b.read():
                listPath.append(os.path.abspath(data) if withAbsPath == 'y' else data)

searchProcess(os.curdir)
print(f"There are {len(listPath)} path that contains text you searched for")
for path in listPath:
    print("- " + path)
