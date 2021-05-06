def scope_test():
    def do_local():
        spam = "local spam"
        print("In do_local function:", spam)

    def do_nonlocal():
        nonlocal spam
        print("Current nonlocal spam value:", spam)
        spam = "nonlocal spam"

    def do_global():
        global spam
        print("Current global spam value:", spam)
        spam = "global spam"

    spam = "test spam"
    do_local()
    print("After local assignment:", spam)
    do_nonlocal()
    print("After nonlocal assignment:", spam)
    do_global()
    print("After global assignment:", spam)

spam = "my_spam"
scope_test()
print("In global scope:", spam)