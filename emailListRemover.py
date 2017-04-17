
def remove(address):
    address=address+'\n'
    target = open("emailList.txt", "r")
    lines = target.read()
    print("Remove " + address)
    if address in lines:
        newlines = lines.replace(address, '')
        target.close()
        target = open("emailList.txt", "w")
        target.write(newlines)


