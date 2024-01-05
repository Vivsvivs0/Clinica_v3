import streamlit as st
import pandas as pd
from views import View

class MinhasConsultasUI:
  def main():
    st.header("Minhas Consultas")
    MinhasConsultasUI.listar()

  def listar():
    paciente = View.paciente_listar_id(st.session_state["id_paciente"])

    if len(View.consulta_listar_paciente(paciente)) != 0:
      dic = []
      for obj in View.consulta_listar_paciente(paciente): dic.append(obj.to_json())
      df = pd.DataFrame(dic)
      st.dataframe(df)
    else:
      st.write("Você nao possui consultas marcadas")