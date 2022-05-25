class MinhaClasse():
    pass
    
    def __str__(self) -> str:
        return f'<Instância de ({self.__class__.__name__}) \nID : {id(self)}>'


if __name__ == '__main__':
    mc = MinhaClasse()
    print(mc)