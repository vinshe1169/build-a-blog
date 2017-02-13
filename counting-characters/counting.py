text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc accumsan sem ut ligula scelerisque sollicitudin. Ut at sagittis augue. Praesent quis rhoncus justo. Aliquam erat volutpat. Donec sit amet suscipit metus, non lobortis massa. Vestibulum augue ex, dapibus ac suscipit vel, volutpat eget massa. Donec nec velit non ligula efficitur luctus."
countchars = {}
for i in range(len(text)):
    k = text[i]
    if countchars.has_key(k):
        countchars[k] =  countchars[k]  + 1
    else:
        countchars[k] = 1
#keylist = list(countchars.keys())
#keylist.sort()
#print(keylist)
for eachitem in countchars:
    print(eachitem,countchars[eachitem])

#print(countchars)
