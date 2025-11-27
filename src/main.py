from src.utils import math_s, sort_s, struct_s

def main():
    while True:
        c = input().lower()
        match c:
            case "exit":
                break
            case "math":
                math_s()
            case "sort":
                sort_s()
            case "struct":
                struct_s()
            case _:
                print("Неизвестная команда")


if __name__ == "__main__":
    main()
