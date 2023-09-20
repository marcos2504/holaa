class Buscaminas:
    def __init__(self,rows,cols,bombs):
        self.board =[['' for _ in range(rows)] for _ in range(cols)]
       
    def show(self):
        pass
        #  for x  in range (8):
        #     for y in range(8):
        #         if self.board[x][y] =='B':
        #              self.board[x][y] == 'F'
                
                    

    def win(self):
        return True
    def lose(self):
        return True
    def question(self,movs):
        pass