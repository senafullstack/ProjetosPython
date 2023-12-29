import os
from django.conf import settings
from PIL import Image
from datetime import datetime
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
class Arquivos:
    
    @staticmethod
    def salvar_imagem(imagem, diretorio_destino):
        if imagem and imagem.name:
            
            img = Image.open(imagem)
            caminho_completo = os.path.join(settings.MEDIA_ROOT, diretorio_destino, imagem.name)
            img.save(caminho_completo)
            return imagem.name
        else:
            return "sem_foto.png" 
        
class ValidadorUtil:
    @staticmethod
    def validar_data(data_str, formato='%d/%m/%Y'):
        if data_str:
            try:
                datetime.strptime(data_str, formato)
                return True  # A data é válida
            except ValueError:
                return False  # A data é inválida
        return False  # A string de data está vazia

    @staticmethod
    def validar_email(email):
        try:
            validate_email(email)
            return True  # O e-mail é válido
        except ValidationError:
            return False  # O e-mail é inválido
        
    @staticmethod    
    def converter_para_data(data_str):
        if data_str is None:
            return None
        if data_str:
            try:
                return datetime.strptime(data_str, '%d/%m/%Y')
            except ValueError:
                return None
        return None
