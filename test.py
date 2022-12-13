
def third():
    print("Hello")
    n = int(input())
    n = n + n
    try:
        if n == 1:
            5 / 0
        elif n == 2:
            int("dsgfsd")    #ValueError
        else:
            a + b            #NameError
        print("Hello!")
    except (ZeroDivisionError, ValueError,  NameError) as exc:
        print("exception was handled...")
        print(exc)
        print(repr(exc))
        print(exc.args)


    print("end third")




def second():
    print("begin second")
    third()
    print("end second")

def first():
    print("begin first")
    second()
    print("end  first")


def main():
    print("begin main")
    first()
    print("end main")

main()