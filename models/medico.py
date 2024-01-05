import json
from models.modelo import Modelo


class Medico:
  def __init__(self, id, nome, fone, email):
    self.__id = id
    self.__nome = nome
    self.__fone = fone
    self.__email = email

  def get_id(self): return self.__id
  def get_nome(self): return self.__nome
  def get_fone(self): return self.__fone
  def get_email(self): return self.__email

  def set_id(self, id): self.__id = id
  def set_nome(self, nome): self.__nome = nome
  def set_fone(self, fone): self.__fone = fone
  def set_email(self, email): self.__email = email

  def __eq__(self, x):
    if self.__id == x.__id and self.__nome == x.__nome and self.__fone == x.__fone and self.__email == x.__email:
      return True
    return False

  def __str__(self):
    return f"{self.__id} - {self.__nome} - {self.__fone} - {self.__email}"
  
  def to_json(self):
    return {
      'id': self.__id,
      'nome': self.__nome,
      'fone': self.__fone,
      'email': self.__email
    }


class NMedico(Modelo):

  @classmethod
  def abrir(cls):
    cls.objetos = []
    try:
      with open("medicos.json", mode="r") as arquivo:
        medicos_json = json.load(arquivo)
        for obj in medicos_json:
          aux = Medico(obj["_Medico__id"], 
                        obj["_Medico__nome"], 
                        obj["_Medico__fone"],
                        obj["_Medico__email"])
          cls.objetos.append(aux)
    except FileNotFoundError:
      pass

  @classmethod
  def salvar(cls):
    with open("medicos.json", mode="w") as arquivo:
      json.dump(cls.objetos, arquivo, default=vars)
