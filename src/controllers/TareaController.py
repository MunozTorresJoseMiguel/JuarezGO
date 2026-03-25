from src.models.TareaModel import TareaModel

class TareaController:
    def_init_(self):
        self.model = TareaModel()
        
    def obtener_lista(self,id_usuario):
        return self.model.lista_por_usuario(id_usuario)
    def guardar_nueva(self,id_usuario,titulo,desc,prio,clas):
        if not titulo:
            return False, "El titulo es Obligatorio"
        
        self.model.crear(id_usuario,titulo,desc,prio,clas)
        return True, "Tarea guardada"
    