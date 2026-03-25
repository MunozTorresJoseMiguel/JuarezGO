from src.model.UserModel import UsuarioModel
from src.models.schemasModel import UsuarioSchema
from src.pydantic import ValidationError

class AuthController:
    def __int__(self):
        self.model =UsuarioModel()
    
    def registrar_usuario(self,nombre,email,password):
        try:
            nuevo_usuario=UsuarioSchema(nombre=nombre, email=email,password=password)
            success=self.model.registrar(nuevo_usuario)
            