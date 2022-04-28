
file_name = "./infile.txt"
infile = open(file_name, "r")
names = [line.rstrip() for line in infile]
# print("names: ", names)

# infile.close()

# def main():
#     display_with_forloop(file_name)
#     print()
#     display_with_forloop()

# def display_with_forloop(file_name):
#     infie = open(file_name, "r")
#     for line in infile:
#         print(line, ends="")
#     infile.closed()


# def display_with_forloop(file_name):
#     infile = open(file_name, "r")
#     items = [line.rstrip() for line in infile]
#     print("items: ", items)
#     infile.closed()



# def open_file(file_name, mode):
#     return open(file_name, mode)

# main()

def main():
    save_to_outfile()

def open_file(file_name, mode):
    return open(file_name, mode)

def save_to_outfile(file_name):
    outfile = open_file("./outfile.txt", "w")    
    for name in names:
        if "Doe" not in name:
            print("Name to be persisted: ", name) 
            outfile.write(name + "\n")   
    else:
        print("Names to be exclude: ", name)
    outfile.close()

main()