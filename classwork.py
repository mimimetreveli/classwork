#1
with open("randomfile","w") as obj:
    obj.write("vovinvoin")
with open("randomfile") as obj:
    s=obj.read()
    print(s)
    print(len(s))
with open("randomfile","a") as obj:
    obj.write("hey!")
with open("randomfile",encoding="utf-8") as obj, open("new_file","w",encoding="utf-8") as file:
    file.write(obj.read())
with open("randomfile",encoding="utf-8") as obj, open("new_file",encoding="utf-8") as file,open("newest_file","w") as file2:
    file2.write(obj.read()+file.read())
with open("randomfile") as obj:
    print(obj.read().upper())
with open("data","a") as obj:
    x="1vd"
    while x!="0":
        x=input()
        obj.write(x)
        obj.write("\n")
with open("file1") as obj, open("new_info","w") as file:
    arr=[]
    for line in obj:
        arr.append(line)
    s=""
    for i in arr:
        s+=i.strip()
    file.write(s)