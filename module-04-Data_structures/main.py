# import sys
# from pathlib import Path

def save_to_file(path, *sample_args):   # <-- Definiujesz funkcję o nazwie "save_to_file" która będzie przyjmowała jako pierwszy argument ścieżkę do pliku w zmiennej "path".
                                        #     Potem kolejne argumenty,nie zależnie ile ich będzie, sa zapisywane do listy "sample_args".
                                        #     * oznacza - tworz listę z każdego kolejnego argumentu sopóki się nie skończą.
                                        #     ** oznacza - tworz słownik i po kolei zapisuj, w tej kolejnosci, klucz a potem wartosc dopóki nie skończą się argumenty. 
    with open(path, "w") as file:       # <-- Otwórz plik wskazany na wejściu do funkcji w zmiennej "path" z parametrem "w" czyli write. "w" - pozwala to tworzyć nowe i edytować istniejące pliki.
                                        #     Tak otwarty plik na czas trwania "with" przypisujesz do zmiennej "file".
        for arg in sample_args:         # <-- Potem iterujesz po elemntach listy "sample_args" i przypisujesz je do zmiennej "arg".
            file.write(str(arg) + "\n") # <-- Tu tak na prawde dopiero zaczyna sie zapisywanie do pliku.
                                        #     Dla każdego elemntu z listy zmienna "arg" jest zamieniana na string i wraz ze znakiem następnej lini zapisywana do pliku wskazanego przez zmienną "file"
if __name__ == "__main__":
    save_to_file("test.txt", 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "test")
    
    # path = Path("G:/Python/goit/python_group_3")
    # print(path.is_dir())
    
    # for arg in sys.argv:
    #     print(arg)

    # val_1 = int(sys.argv[1])
    # val_2 = int(sys.argv[2])

    # print(val_1 + val_2)

    # path = Path(sys.argv[1])

    # for p in path.iterdir():
    #     print(p)
    exit