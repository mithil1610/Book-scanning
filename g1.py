f = open("d_tough_choices.txt", "r")
a = f.readline().split(' ')
a[-1] = a[-1].strip()
for i in range(0, len(a)): 
    a[i] = int(a[i])

totalBooks = a[0]
totalLibraries = a[1]
totalDays = a[2]

b=f.readline().split(' ')
b[-1] = b[-1].strip()
for i in range(0, len(b)): 
    b[i] = int(b[i])

bookscore = [0]*totalBooks
for i in range(0, totalBooks):
    bookscore[i] = int(b[i])


class Library:
    def __init__(self, books, signtime, bookday,booksavail):
        self.books = books
        self.signtime = signtime
        self.bookday = bookday
        self.booksAvail= booksavail
        self.booksDone=False
        self.scannedbooks=[]
    
    def signingUp(self):
        self.signtime-=1
        
    def my(self):
        print(self.books,self.signtime, self.bookday,self.booksAvail,self.booksDone,self.scannedbooks)










#Libraries priority vise sorting
def sorto(val):
    return val.books/val.bookday

#books score vise sorting
def scoresort(val):
    return val[1]
    
#Libraries which are signed needs to be scanned
def scanBooks(ith,signedUp):
    #print(str(ith))
    for i in signedUp:
        if(i.booksDone):
            if i in ongoing:
                ongoing.pop(0)
            continue
        for _ in range(i.bookday):
            k=0
            while True:
                if(k>=i.books):
                        i.booksDone=True
                        break
                elif i.booksAvail[k][0] not in Donebooks:
                    Donebooks.append(i.booksAvail[k][0])
                    i.scannedbooks.append(i.booksAvail[k][0])
                    #print(str(ith)+"thday",i.booksAvail[k][0])
                    break
                k+=1      
    
# totalBooks,totalLibraries,totalDays= map(int,input().split())
# bookscore= list(map(int,input().split()))



# libraries=[]
# for i in range(n_libs):
#     b,s,bd= f.readline().split(' ')
#     bd = bd.strip()
#     b,s,bd=int(b), int(s), int(bd)
#     print(b)
#     print(s)
#     print(bd)
#     e = f.readline().split(' ')
#     e[-1] = e[-1].strip()
#     for i in range(0, len(e)): 
#         e[i] = int(e[i])
#     print(e)
#     libraries.append(Library(b, s, bd, e))

# f.close()



libraries=[]
for i in range(totalLibraries):
    b,s,bd= f.readline().split(' ')
    bd = bd.strip()
    b,s,bd=int(b), int(s), int(bd)
    e = f.readline().split(' ')
    e[-1] = e[-1].strip()
    for i in range(0, len(e)):
        e[i] = int(e[i])
    bs = []
    for i in e:
        bs.append([i, bookscore[i]])
    # bs=[[i,bookscore[i]] for i in list(map(int,input().split()))]
    bs.sort(key = scoresort, reverse = True)
    libraries.append(Library(b,s,bd,bs))

f.close()

#main Logic 
lOrder=libraries[:]
libraries.sort(reverse=True,key=sorto)
#print(*[i.my() for i in libraries])
scanningLib=0
ongoing=[]
signedUp=[]
Donebooks=[]
libraryOrder=[]
ongoing.append(libraries[0])
#starting days
for i in range(totalDays+1):
    for item in ongoing:
        if(scanningLib>=totalLibraries):
            break
        if lOrder.index(item) not in libraryOrder:
            libraryOrder.append(lOrder.index(item))
        if i>0:
            item.signingUp()
        if item.signtime<=0:
            if(item not in signedUp):
                signedUp.append(item)
            if ongoing[-1] in signedUp:
                if(scanningLib<totalLibraries-1):
                    scanningLib+=1
                    if libraries[scanningLib] not in ongoing:
                        ongoing.append(libraries[scanningLib])
                scanBooks(i,signedUp)
    #print(str(i)+"thday ",scanningLib)
o = open("myfile4.txt", "w")
o.write(str(len(signedUp))+"\n")

#print(len(signedUp))
for i in range(len(libraryOrder)):
    if len(lOrder[libraryOrder[i]].scannedbooks)==0: continue
    o.write(' '.join(map(str,(libraryOrder[i],len(lOrder[libraryOrder[i]].scannedbooks))))+"\n")
    sb=' '.join(map(str,lOrder[libraryOrder[i]].scannedbooks))
    o.write(str(sb)+"\n")
    # print(libraryOrder[i],len(lOrder[libraryOrder[i]].scannedbooks))
    # print(*lOrder[libraryOrder[i]].scannedbooks,sep=' ')

o.close()
#print(*[i.my() for i in signedUp])
#print (libraries[1].scannedbooks)
#print((libraryOrder))
#print(len(signedUp))
#print(Donebooks)