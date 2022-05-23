import os

__names = [
    "deck_test.py",
]

def main():
    print(os.getcwd())
    for name in __names:
        os.system(f"python -m unittest Deck/tests/{name} -v")

if __name__ == "__main__":
    main()
