class ReaderL:
    __spisok = []
    def __init__(self, name):
        self.name = name
    def take(self, kname):
        if len(self.__spisok) < 2:
            self.books.append(kname)
        else:
            print('Error') #больше книг брать нельзя
    
    def zdat_b (self, kname):
        if kname in self.__spisok:
            self. __spisok.remove(kname)
        else:
            print('Error') #такой книги больше нет

class Matrix:
    def __init__(self, x):
        self.x = x
        if len(x) == 0:
            print('Error')
        else:
            y = len(x[0])
            for i in x[1:]:
                if len(i) != y:
                    break
                else:
                    self.matrix = x
                    self.valid = True

    def trans(self):
        if  not (self.val):
            return 'Error'
        else:
            for i in range(len(self.matrix)):
                for j in range(len(self.matrix[i])):   
                    if i != j:
                        self.matrix[i][j], self.matrix[j][i] = self.matrix[j][i], self.matrix[i][j]
                        





