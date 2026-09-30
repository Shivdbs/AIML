data=True
line=1
word="python"
with open("sample.txt","r") as f:
    while data:
        print(f.read())
        data = f.readline()

        if(word in data):
            print(f"{word} found at line {line}")
            break
        print(data)
        line+=1

