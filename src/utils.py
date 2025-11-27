from math_ import fact, fact_recurs,fibb,fibb_recurs
from sort import bobble, qsort,count,radix,heapy, bucket_s
from stract_ import Stack
from stract_ import Queue

def math_s():
    while True:
        c = input().lower()
        match c:
            case "back":
                break
            case "fact" | "fact_rec" | "fibb" | "fibb_rec":
                try:
                    n = int(input())
                    match c:
                        case "fact":
                            r = fact(n)
                            print(r)
                        case "fact_rec":
                            r = fact_recurs(n)
                            print(r)
                        case "fibb":
                            r = fibb(n)
                            print(r)
                        case "fibb_rec":
                            r = fibb_recurs(n)
                            print(r)
                except:
                    print("Ошибка")
            case _:
                print("Неизвестная команда")


def sort_s():
    while True:
        c = input().lower()
        match c:
            case "bakc":
                break
            case "bobble" | "qsort" | "count" | "radix" | "bucket" | "heapy":
                try:
                    n = input()
                    if c == "bucket":
                        a = list(map(float, n.split()))
                    else:
                        a = list(map(int, n.split()))
                    print("Исходный массив", a)

                    match c:
                        case "bobble":
                            res = bobble(a, len(a))
                        case "qsort":
                            res = qsort(a, 0, len(a) - 1)
                        case "count":
                            res = count(a, len(a))
                        case "radix":
                            res = radix(a, len(a))
                        case "bucket":
                            res = bucket_s(a, len(a))
                        case "heapy":
                            res = heapy(a, len(a))
                    print("Отсортированный", res)
                except:
                    print("Ошибка")
            case _:
                print("Неизвестная команда")


def struct_s():
    st = Stack()
    qe = Queue()
    while True:
        c = input().lower()
        match c:
            case "back":
                break
            case "stack":
                stack_s(st)
            case "queue":
                queue_s(qe)
            case _:
                print("Неизвестная команда")


def stack_s(st):
    while True:
        print(st.size_)
        st.print_()
        c = input().lower()
        match c:
            case "back":
                break
            case "push":
                try:
                    a = int(input())
                    st.push(a)
                except:
                    print("Ошибка")
            case "pop":
                a = st.pop()
                if a is not None:
                    print(a)
                else:
                    print("Cтек пуст")
            case "top":
                a = st.top()
                if a is not None:
                    print(a)
                else:
                    print("Cтек пуст")
            case "mini":
                a = st.mini()
                if a is not None:
                    print(a)
                else:
                    print("Cтек пуст")
            case _:
                print("Неизвестная команда")


def queue_s(q):
    while True:
        print(q.size_)
        q.print_()
        c = input().lower()
        match c:
            case "back":
                break
            case "enqueue":
                try:
                    a = int(input())
                    q.enqueue(a)
                except:
                    print("Ошибка")
            case "dequeue":
                a = q.dequeue()
                if a is not None:
                    print(a)
                else:
                    print("очередь пуста")
            case "front":
                a = q.front()
                if a is not None:
                    print(a)
                else:
                    print("очередь пуста")
            case _:
                print("Неизвестна яоперация")


