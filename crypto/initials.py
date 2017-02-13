def get_initials (fullname):
    initial = ""
    mynamelist = []
    mynamelist = fullname.split(" ")
    for eachname in mynamelist:
        initial = initial + eachname[0]
    return initial.upper()

#print(get_initials("Mangala Shenoy"))
#print(get_initials("Ozzie Smith"))
#print(get_initials("bonnie blair"))
#print(get_initials("George"))
#print(get_initials("Daniel Day Lewis"))
#print(get_initials("Vinod Shenoy H.N"))
