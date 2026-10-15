"""Pattern printing
Run: python patterns.py
"""


def right_triangle(n):
    for i in range(1, n + 1):
        print("* " * i)


def inverted_triangle(n):
    for i in range(n, 0, -1):
        print("* " * i)


def pyramid(n):
    for i in range(1, n + 1):
        print(" " * (n - i) + "* " * i)


def diamond(n):
    for i in range(1, n + 1):
        print(" " * (n - i) + "* " * i)
    for i in range(n - 1, 0, -1):
        print(" " * (n - i) + "* " * i)


def number_triangle(n):
    for i in range(1, n + 1):
        print(" ".join(str(j) for j in range(1, i + 1)))


def floyd(n):
    num = 1
    for i in range(1, n + 1):
        for _ in range(i):
            print(num, end=" ")
            num += 1
        print()


def hollow_square(n):
    for i in range(n):
        for j in range(n):
            if i in (0, n - 1) or j in (0, n - 1):
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()


if __name__ == "__main__":
    patterns = {
        "1": ("Right triangle", right_triangle),
        "2": ("Inverted triangle", inverted_triangle),
        "3": ("Pyramid", pyramid),
        "4": ("Diamond", diamond),
        "5": ("Number triangle", number_triangle),
        "6": ("Floyd's triangle", floyd),
        "7": ("Hollow square", hollow_square),
    }
    for key, (name, _) in patterns.items():
        print(f"{key}. {name}")

    choice = input("Choose pattern: ").strip()
    if choice in patterns:
        n = int(input("Enter number of rows: "))
        print()
        patterns[choice][1](n)
    else:
        print("Invalid choice.")
