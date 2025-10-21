class Canal:
    '''
    __init__ = Metodo contrutor | self = Si mesmo
    '''
    def __init__(self, nome, descricao, inscritos):
        self.nome = nome
        self.descricao = descricao
        self.inscritos = inscritos
        self.videos = []
        self.playlists:list[Playlist] = []
    
    def inscrever(self, quantidade=1):
        self.inscritos += quantidade

    def postar(self, video):
        if video in self.videos:
            print("Esse video ja foi postado")
            return 
        
        self.videos.append(video)
        
    def info_playlists(self):
        for playlist in self.playlists:
            print(playlist.nome)
            playlist.info_videos()

    def adicionar_playlist(self, playlist):
        if playlist not in self.playlists:
            self.playlists.append(playlist)
        else:
            print("Essa playlist ja foi adicionada")

    def remover_playlist(self, playlist):
        if playlist in self.playlists:
            self.playlists.remove(playlist)
        else:
            print("Esta Playlist nao foi criada")


class CanalEmpresarial(Canal):
    '''
    "_" so pode alterar algo dentro da classe, nao fora
    '''
    def __init__(self, nome, descricao, inscritos):
        super().__init__(nome, descricao, inscritos)
        self._equipe = []


    @property # <- Decorador pra indicar que algo é uma propriedade
    def equipe(self):
        return self._equipe
    
    
    def adicionar_membro_equipe(self, membro):
        if membro not in self._equipe:
            self._equipe.append(membro)
        else:
            print(f"O membro {membro} ja esta na equipe")

    
    def remover_membro_equipe(self, membro):
        if membro in self._equipe:
            self._equipe.remove(membro)
        else:
           print(f"O membro {membro} nao esta na equipe") 

class Video:
    def __init__(self, titulo, descricao):
        self.titulo = titulo
        self.descricao = descricao

        self.visualizacoes = 0
        self.likes = 0
        self.deslikes = 0
        self.comentarios = []

    def __repr__(self):
        return f"<{self.titulo}>" # <- Para retornar um "objeto"

    def assistir(self):
        self.visualizacoes += 1

    def gostei(self):
        self.likes += 1

    def nao_gostei(self):
        self.deslikes += 1

    def comentar(self, comentario):
        self.comentarios.append(comentario)

    def info(self):
        print(f"""Titulo: {self.titulo}
Descriçao: {self.descricao}
{self.visualizacoes} Visualizaçoes
{self.likes} Likes {self.deslikes} Deslikes
{self.descricao}\n""")


class Playlist:
    def __init__(self, nome):
        self.nome = nome

        self.videos:list[Video] = []

    def adicionar_video(self, video):
        if video not in self.videos:
            self.videos.append(video)
        else:
            print(f"O video {video} ja esta na playlist!")

    def remover_video(self, video):
        if video in self.videos:
            self.videos.remove(video)
        else:
            print(f"O video {video} nao esta na playlist!")

    def info_videos(self):
        for video in self.videos:
            video.info()
        

canal_moonteiro = Canal("Moonteiro", "Journey", 1)
canal_lancode = Canal("Lancode", "Codigos e gatos", 34000)
canal_duolingo = CanalEmpresarial("duolingo", "ingres", 500000)

video_poo = Video("Python objetos", "Aprenda agora")
video_discordpy = Video("Aprenda Discord", "Aiai")
playlist_programacao = Playlist("Programacao")
playlist_programacao.adicionar_video(video_poo)
playlist_programacao.adicionar_video(video_discordpy)

video_minecraft = Video("Jogando minezin", "mine")
video_eldenring = Video("Jogano Elden Ring", "Elden Ring")
playlist_games = Playlist("Games")
playlist_games.adicionar_video(video_minecraft)
playlist_games.adicionar_video(video_eldenring)


canal_lancode.adicionar_playlist(playlist_games)
canal_lancode.adicionar_playlist(playlist_programacao)



canal_lancode.postar(video_poo)
canal_lancode.postar(video_discordpy)

canal_lancode.info_playlists()











# print(canal_duoling._equipe) # <- da pra remover o parentese "canal_duolingo.equipe()"

# print(f"Membros atuais: {canal_duolingo._equipe}")
# canal_duolingo.adicionar_membro_equipe("Jose")
# print(f"Membros atuais: {canal_duolingo._equipe}")
# canal_duolingo.adicionar_membro_equipe("Bob")
# canal_duolingo.remover_membro_equipe("Jose")
# canal_duolingo.adicionar_membro_equipe("Jorge")
# print(f"Membros atuais: {canal_duolingo._equipe}")
