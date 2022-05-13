def dec1(func1):
    def nowexec():
        print("Exection now")
        func1()
        print("Executed")
    return nowexec


@dec1
def who_is_harry():
    print("Good")
    
who_is_harry()