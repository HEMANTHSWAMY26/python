class solution:
    def pattern(self):
        num = int(input("enter the num: "))
        if(num>0):
            for i in range(num):
                for j in range(num):
                    print("*",end=" ")              
                print()

if __name__ == "__main__":
    sol = solution()
    sol.pattern()
