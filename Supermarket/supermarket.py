class Supermarket:
    def __init__ (self,filepath) ->None:
        self.filepath = filepath
        return None
    
    def loadProduct(self) :
        product = []
        try:
            filehandle = open(self.filepath, "r", encoding='UTF-8')
            file = filehandle.readline()
            for row in file:
                number = int(row['number'])

        except Exception as err:
            print(f"Faild to read file '{self.filepath}' .")
            print(err)
            exit(-1)


if __name__ == "__main__":
    app = Supermarket()