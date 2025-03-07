from mypackages import classone, classtwo


def main():
    obj1 = classone.classone()
    obj2 = classtwo.classtwo()

    print(obj1.print_message1())
    print(obj2.print_message2())


main()
