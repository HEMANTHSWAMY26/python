"""
date = int(input("enter the day"))
mon = str(input("enter the mon"))
yr = int(input("enter yr"))
print (" your dob is: ",date,"-",mon,"-",yr)
print("month is: ", mon)
"""

month = ["jan","feb","mar","april","may","june","july"]
dob = input("enter the dob in the format of dd-mm-year: ")
indx = int(dob[3:5])-1
urs_mnth = (month[indx])
print("your bd mnth is: ", urs_mnth)


