import streamlit as st
import pandas as pd
from views import View

class ConfirmarConsultaUI:
  def main():
    st.header("Confirmar Consulta")
    ConfirmarConsultaUI.confirmar()

  def confirmar():
    consultas = View.consulta_nao_confirmada()
    if len(consultas) != 0:
      dic = []
      for obj in consultas: dic.append(obj.__dict__)
      df = pd.DataFrame(dic)
      st.dataframe(df)
    else:
      st.write("Não há consultas não confirmadas")
    consulta = st.selectbox("Consulta escolhida", View.consulta_nao_confirmada())
    if st.button("Confirmar"):
      View.consulta_atualizar(consulta.get_id(), "True", consulta.get_data(), consulta.get_id_paciente(), consulta.get_id_medico())
      st.success("Consulta confirmada com sucesso")