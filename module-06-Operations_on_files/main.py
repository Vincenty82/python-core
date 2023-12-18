with open("test.txt", "w+", encoding = "utf-16") as test_file:
    test_file.write("H")
    test_file.seek(0)
    print(ord(test_file.read(1)))