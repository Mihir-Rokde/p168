class bookshelf:
    def __init__(self,name,author,price,publishing_year):
        self.bn=name
        self.ba=author
        self.bp=price
        self.bpy=publishing_year
    def addb(self):
        print("Book name : "+self.bn)
        print("Book author : "+self.ba)
        print("Book price : "+str(self.bp))
        print("Book was published in : "+str(self.bpy))
        print("Book added")
    def ysp(self):
        yap=2020-self.bpy
        print("This book was published "+str(yap)+"Years ago")
b1=bookshelf("Harry Potter","Jk Rowling",1928,1997)
b1.addb()
b1.ysp()
b2=bookshelf("horrid Henry","Francesca Simon",440,2020)
b2.addb()
b2.ysp()