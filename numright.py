class right:
    def pat1(self,n):
        for i in range(1,n+1):
            for j in range(1,i+1):
                print(j,end='')
            print()
if __name__ == "__main__":
    n = int(input("enter no of rows: "))
    num = right()
    num.pat1(n)