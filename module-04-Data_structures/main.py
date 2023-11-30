

import sys
from pathlib import Path

if __name__ == "__main__":
    # path = Path("G:/Python/goit/python_group_3")
    # print(path.is_dir())
    
    # for arg in sys.argv:
    #     print(arg)

    # val_1 = int(sys.argv[1])
    # val_2 = int(sys.argv[2])

    # print(val_1 + val_2)

    path = Path(sys.argv[1])

    for p in path.iterdir():
        print(p)