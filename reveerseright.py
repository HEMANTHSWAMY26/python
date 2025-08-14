class right:
    def pat1(self,n):
        for i in range(n):
            for j in range(n-i):
                print('*',end='')
            print()
if __name__ == "__main__":
    n = int(input("enter no of rows: "))
    num = right()
    num.pat1(n)