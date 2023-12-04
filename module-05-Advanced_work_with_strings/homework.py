# ZADANIE 1

def real_len(text):
    count = 0
    special_signs = ["\n", "\f", "\r", "\t", "\v"]
    for chr in text:
        if chr not in special_signs:
            count += 1
            print(chr, end=", ")
    print(f"count = {count}")
    return count

# WYWOLANIA

if __name__ == "__main__":
    real_len("Alex\nKd\\fe23\t\f\v.\r")