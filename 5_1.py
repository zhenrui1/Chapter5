
file_name = "./infile.txt"
infile = open(file_name, "r")
names = [line.rstrip() for line in infile]
print("names: ", names)

infile.close()

def main():
    display_with_forloop(file_name)
    print()
    display_with_forloop()

def display_with_forloop(file_name):
    infie = open(file_name, "r")
    for line in infile:
        print(line, ends="")
    infile.closed()


def display_with_forloop(file_name):
    infile = open(file_name, "r")
    items = [line.rstrip() for line in infile]
    print("items: ", items)
    infile.closed()


main()