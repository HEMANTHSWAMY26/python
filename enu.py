"""
fruits  = ["apple", "banana", "cherry"]
prices  = [80, 30, 120]
stocks  = [50, 75, 20]

for fruits , prices , stocks in zip ((fruits,prices,stocks)):
    print( fruits,"-","$","(",stocks,"pcs)")
"""

for row in range(1,4):
    for col in range(1,4):
        print(f"{(row),(col)}",end = " ")
        