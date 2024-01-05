from models.paciente import Paciente, NPaciente
from models.medico import Medico, NMedico
from models.consulta import Consulta, NConsulta
import datetime
import streamlit as st


class View:
  def paciente_listar():
    return NPaciente.listar()
  
  def paciente_listar_id(id):
    return NPaciente.listar_id(id)

  def paciente_inserir(nome, fone, email, senha):
    paciente = Paciente(0, nome, fone, email, senha)
    NPaciente.inserir(paciente)

  def paciente_atualizar(id, nome, fone, email, senha):
    paciente = Paciente(id, nome, fone, email, senha)
    NPaciente.atualizar(paciente)
    
  def paciente_excluir(id):
    paciente = Paciente(id, "", "", "", "")
    NPaciente.excluir(paciente)    

  def paciente_admin():
    for paciente in View.paciente_listar():
      if paciente.get_nome() == "admin": return
    View.paciente_inserir("admin", "999999999", "admin", "admin")

  def paciente_login(email, senha):
    for paciente in View.paciente_listar():
      if paciente.get_email() == email and paciente.get_senha() == senha:
        return paciente
    return None

  def consulta_listar():
    return NConsulta.listar()

  def consulta_listar_paciente(paciente):
    r = []
    for horario in View.consulta_listar():
      if horario.get_id_paciente() == paciente.get_id():
        r.append(horario)
    return r
  
  def consulta_listar_mes():
    r = []
    hoje = datetime.datetime.today()
    for horario in View.consulta_listar():
      if hoje.month == horario.get_data().month and hoje.year == horario.get_data().year and horario.get_confirmado() == "True":
        r.append(horario)
    return r 

  def consulta_nao_confirmada():
    consultas = []

    for consulta in View.consulta_listar():
      if consulta.get_confirmado() == "False":
        consultas.append(consulta)

    return consultas
  
  def consulta_listar_id(id):
    return NConsulta.listar_id()

  def consulta_inserir(confirmado, data, id_paciente, id_medico):
    NConsulta.inserir(Consulta(0, confirmado, data, id_paciente, id_medico))

  def consulta_atualizar(id, confirmado, data, id_paciente, id_medico):
    consulta = Consulta(id, confirmado, data, id_paciente, id_medico)
    NConsulta.atualizar(consulta)

  def consulta_excluir(id):
    NConsulta.excluir(Consulta(id, "", "", 0, 0))
    
  def consulta_solicitados():
    r = []
    for obj in NConsulta.listar_nao_confirmados():
      if obj.get_id_paciente(): r.append(obj)
    return r
  
  def medico_listar():
    return NMedico.listar()
  
  def medico_listar_id(id):
    return NMedico.listar_id(id)
  
  def medico_inserir(nome, fone, email):
    medico = Medico(0, nome, fone, email)
    NMedico.inserir(medico)

  def medico_atualizar(id, nome, fone, email):
    medico = Medico(id, nome, fone, email)
    NMedico.atualizar(medico)
    
  def medico_excluir(id):
    medico = Medico(id, "", "", "")
    NMedico.excluir(medico)

  def medico_disponivel(medico, data):
    for con in View.consulta_listar():
      if con.get_id_medico() == medico.get_id():
          fim = con.get_data() + datetime.timedelta(minutes=15)
          if con.get_data() <= data and data <= fim:
            return False
    return True