# x=43
# if x % 2:
#     print("odd")
# else:
#     print("even")

# y=0
# msg = "0123456789"
# for x in msg:
#     print(x)
#     y += 1
# print(y)

# for _ in range(10):
#     print("Hello world")

# counter = 0
# while counter < 10:
#     print("Hello world")
#     counter += 1

# x=42
# result=""
# while x != 0:
#     rem = str(x %2)
#     x //= 2                # x = x // 2
#     result = rem + result
# print(result)

# from math import log2, floor

# x = 65535
# bits = floor(log2(x)) + 1
# result=""
# for _ in range(bits):
#     rem = str(x % 2)
#     x //= 2  # x = x // 2
#     result = rem + result
# print(result)

print("This program will conver decimal to bin")
while True:
    try:
        value = input("Input non-negative integer: ")
        if value == "exit":  # back door exit
            break
        x = int(value)
    except ValueError as error:
        print(f"{error}. Try again")
        continue
    except Exception:
        print("\nI CANNOT DO THAT DAVE\n")
        break
    except KeyboardInterrupt:
        print("\nExiting program ...")
        break
    
    # Check if nuber is negative

    if x >= 0:                          # If positive, use bin()
        result = bin(x)
    else:                               # If negative flip all bits
        x = x * -1                          # Reverse the sign
        result = ""
        while x != 0:
            bit = (x % 2)
            bit = 1 - bit                   # Reverse the bit 0 to 1 and 1 to 0
            x //= 2                
            result = str(bit) + result        

    print(f"Binary value: {result}")
    answer = input("Do you want to try again? Y/N ")
    while answer not in ["Y", "y", "N", "n"]:
        print(f"Unrecognized command '{answer}', use Y/N")
        answer = input("Do you want to try again? Y/N ")
    if answer in ["N", "n"]:
        break
