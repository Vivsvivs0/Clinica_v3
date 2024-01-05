import streamlit as st
import pandas as pd
from views import View

class ConsultasMesUI:
  def main():
    st.header("Consultas do Mês")
    ConsultasMesUI.listar()

  def listar():
    if len(View.consulta_listar_mes()) != 0:
      dic = []
      for obj in View.consulta_listar_mes(): dic.append(obj.to_json())
      df = pd.DataFrame(dic)
      st.dataframe(df)
    else:
      st.write("Não há consultas marcadas esse mês")