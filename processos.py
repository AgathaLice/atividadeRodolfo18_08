
class Processo():
    
    def __init__(self, id, nome, cpu, user, memoria):
        self.id = id
        self.nome = nome
        self.cpu = cpu
        self.user = user
        self.memoria = memoria
        self.estado = "INÍCIO"
        self.comeco = True
    
    def getId(self) -> int | None:
        return self.id
    
    def setId(self, id) -> None:
        self.id = id
        return None
    
    def getNome(self) -> int | None:
        return self.nome
    
    def setNome(self, nome) -> None:
        self.nome = nome
        return None
    
    def getCpu(self) -> int | None:
        return self.cpu
    
    def setCpu(self, cpu) -> None:
        self.cpu = cpu
        return None
    
    def getUser(self) -> int | None:
        return self.user
    
    def setUser(self, user) -> None:
        self.user = user
        return None
    
    def getMemoria(self) -> int | None:
        return self.memoria
    
    def setMemoria(self, memoria) -> None:
        self.memoria = memoria
        return None
    
    def getEstado(self) -> str | None:
        return self.estado
    
    def setEstado(self, estado) -> None:
        self.estado = estado
        return None

    def getComeco(self):
        return self.comeco
    
    def setComeco(self, comeco: bool):
        self.comeco = comeco
        return None