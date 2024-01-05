import json
import datetime
from models.modelo import Modelo

class Consulta:
  def __init__(self, id, confirmado, data, id_paciente, id_medico):
    self.__id = id
    self.__confirmado = confirmado
    self.__data = data
    self.__id_paciente = id_paciente
    self.__id_medico = id_medico

  def get_id(self): return self.__id
  def get_confirmado(self): return self.__confirmado
  def get_data(self): return self.__data
  def get_id_paciente(self): return self.__id_paciente
  def get_id_medico(self): return self.__id_medico

  def set_id(self, id): self.__id = id
  def set_confirmado(self, confirmado): self.__confirmado = confirmado
  def set_data(self, data): self.__data = data
  def set_id_paciente(self, id_paciente): self.__id_paciente = id_paciente
  def set_id_medico(self, id_medico): self.__id_medico = id_medico

  def _eq_(self, x):
    if self._id == x.id and self.confirmado == x.confirmado and self.data == x.data and self.id_medico == x.id_medico and self.id_paciente == x._id_paciente:
      return True
    return False

  def __str__(self):
    return f"{self.__id} - {self.__confirmado} - {self.__data.strftime('%d/%m/%Y %H:%M')} - {self.__id_paciente} - {self.__id_medico}"

  def to_json(self):
    return {
      'id': self.__id,
      'confirmado': self.__confirmado,
      'data': self.__data.strftime('%d/%m/%Y %H:%M'),
      'id_paciente': self.__id_paciente,
      'id_medico': self.__id_medico}


class NConsulta(Modelo):

  """   @classmethod 
  def listar_nao_confirmados(cls):
    cls.abrir()
    r = []
    for con in NConsulta.listar():
      if not con.get_confirmado:
        r.append(con)
    return r """

  @classmethod
  def abrir(cls):
    cls.objetos = []
    try:
      with open("consultas.json", mode="r") as arquivo:
        consultas_json = json.load(arquivo)
        for obj in consultas_json:
          aux = Consulta(
            obj["id"], obj["confirmado"],
            datetime.datetime.strptime(obj["data"], "%d/%m/%Y %H:%M"),
            obj["id_paciente"], obj["id_medico"])
          cls.objetos.append(aux)
    except FileNotFoundError:
      pass

  @classmethod
  def salvar(cls):
    with open("consultas.json", mode="w") as arquivo:
      json.dump(cls.objetos, arquivo, default=Consulta.to_json, indent=4)
