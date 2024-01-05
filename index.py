from templates.entrarUI import EntrarUI
from templates.manterpacienteUI import ManterPacienteUI
from templates.mantermedicoUI import ManterMedicoUI
from templates.manterconsultaUI import ManterConsultaUI
from templates.minhasconsultasUI import MinhasConsultasUI
from templates.solicitarconsultaUI import SolicitarConsultaUI
from templates.confirmarconsultaUI import ConfirmarConsultaUI
from templates.remarcarconsultaUI import RemarcarConsultaUI
from templates.cancelarconsultaUI import CancelarConsultaUI
from templates.consultasmesUI import ConsultasMesUI
from templates.editarperfilUI import EditarPerfilUI
from templates.abrircontaUI import AbrirContaUI
from views import View

import streamlit as st

class IndexUI:

  def menu_visitante():
    op = st.sidebar.selectbox("Menu", ["Login", "Abrir Conta"])
    if op == "Login": EntrarUI.main()
    if op == "Abrir Conta": AbrirContaUI.main()

  def menu_admin():
    op = st.sidebar.selectbox("Menu", ["Manter Consultas", "Manter Pacientes", "Manter Médicos", "Consultas do Mês", "Confirmar Consultas", "Editar Perfil"])
    if op == "Manter Consultas": ManterConsultaUI.main()
    if op == "Manter Pacientes": ManterPacienteUI.main()
    if op == "Manter Médicos": ManterMedicoUI.main()
    if op == "Consultas do Mês": ConsultasMesUI.main()
    if op == "Confirmar Consultas": ConfirmarConsultaUI.main()
    if op == "Editar Perfil": EditarPerfilUI.main()


  def menu_paciente():
    op = st.sidebar.selectbox("Menu", ["Minhas Consultas", "Solicitar Consulta", "Remarcar Consulta", "Cancelar Consulta", "Editar Perfil"])
    if op == "Minhas Consultas": MinhasConsultasUI.main()
    if op == "Solicitar Consulta": SolicitarConsultaUI.main()
    if op == "Remarcar Consulta": RemarcarConsultaUI.main()
    if op == "Cancelar Consulta": CancelarConsultaUI.main()
    if op == "Editar Perfil": EditarPerfilUI.main()

  def btn_logout():
    if st.sidebar.button("Logout"):
      del st.session_state["id_paciente"]
      del st.session_state["paciente_nome"]
      st.rerun()

  def sidebar():
    if "id_paciente" not in st.session_state:
      IndexUI.menu_visitante()   
    else:
      st.sidebar.write("Bem-vindo(a), " + st.session_state["paciente_nome"])
      if st.session_state["paciente_nome"] == "admin": IndexUI.menu_admin()
      else: IndexUI.menu_paciente()
      IndexUI.btn_logout()  

  def main():
    View.paciente_admin()
    IndexUI.sidebar()

IndexUI.main()