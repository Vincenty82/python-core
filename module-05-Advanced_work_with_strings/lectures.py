# s = "This is a string"
# s = s.removeprefix("dupa")
# print(len(s))
# s = s.center(18, "-")
# print(s)

# value = 100
# print(f"value = {value:b}")

with open("hello.txt", "r") as file:
    file.seek(2, 2)
    ch = file.read(1)
    print(ch)
