import streamlit as st
import pandas as pd
from views import View
import datetime

class RemarcarConsultaUI:
  def main():
    st.header("Remarcar Consulta")
    RemarcarConsultaUI.remarcar()

  def remarcar():
    consulta = st.selectbox("Consulta escolhida", View.consulta_listar_paciente(View.paciente_listar_id(st.session_state["id_paciente"])))
    data = st.text_input("Nova data DD/MM/AAAA HH\:MM")
    if st.button("Remarcar"):
      data = datetime.datetime.strptime(data, "%d/%m/%Y %H:%M")
      View.consulta_atualizar(consulta.get_id(), "False", data, st.session_state['id_paciente'], consulta.get_id_medico())
      st.success("Consulta atualizada com sucesso")