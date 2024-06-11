class Filme:
    def __init__(self,nome,ano,duracao):
        self.nome=nome.tittle()
        self.ano=ano
        self.duracao=duracao
        self._likes = 0
    @property
    def likes(self):
        return self._likes
     
    def dar_likes(self):
        self.likes+=1
        
    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self):
        self._nome=nome    
        
class Serie:
    def __init__(self,nome,ano,temporadas):
        self.nome=nome
        self.ano=ano
        self.temporadas=temporadas
        self.likes = 0
        
filme1=Filme('Rasputia',2015,133)
filme1.dar_likes()
print(f'Nome: {filme1.nome} - Ano: {filme1.ano} Duração: {filme1.duracao}')
serie1=Serie('Greys Anatomy',2005,20)
print(f'Nome: {serie1.nome} - Ano: {serie1.ano} Temporadas: {serie1.temporadas}')