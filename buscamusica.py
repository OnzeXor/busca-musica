class Musica:
    def __init__(self,titulo,compositor,ano):
        self.titulo = titulo
        self.compositor = compositor
        self.ano = ano
class Buscador:
    def busca_por_titulo(self,playlist,titulo):
        for i in range(len(playlist)):
            if playlist[i].titulo == titulo:
                return i
        return -1
    def vamos_buscar(self):
        playlist = [Musica('Principia','Emicida', 2019),
                    Musica('Going Home','Yun Li',2022),
                    Musica('Beautiful Boy','John Lennon',1980)]
        onde_achou = self.busca_por_titulo(playlist,'Principia')

        if onde_achou == -1:
            print('a musica não está na playlist')
        else:
            preferida = playlist[onde_achou]
            print(preferida.titulo, preferida.compositor, preferida.ano, sep=', ')

j=Buscador()
j.vamos_buscar()
