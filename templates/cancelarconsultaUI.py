import time
import streamlit as st
import pandas as pd
from views import View

class CancelarConsultaUI:
  def main():
    st.header("Cancelar Consulta")
    CancelarConsultaUI.cancelar()

  def cancelar():
    consulta = st.selectbox("Consulta escolhida", View.consulta_listar_paciente(View.paciente_listar_id(st.session_state["id_paciente"])))
    if st.button("Cancelar"):
      View.consulta_excluir(consulta.get_id())
      st.success("Consulta cancelada com sucesso")
      time.sleep(2)
      st.rerun()
