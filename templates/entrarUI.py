import streamlit as st
from views import View
import time

class EntrarUI:
  def main():
    st.header("Entrar no Sistema")
    EntrarUI.entrar()
  def entrar():
    email = st.text_input("Informe o e-mail")
    senha = st.text_input("Informe a senha")
    if st.button("Login"):
      paciente = View.paciente_login(email, senha) 
      if paciente is not None:
        st.success("Login realizado com sucesso")
        st.success("Bem-vindo(a), " + paciente.get_nome())
        st.session_state["id_paciente"] = paciente.get_id()
        st.session_state["paciente_nome"] = paciente.get_nome()
        time.sleep(1)
        st.rerun()
      else:
        st.error("Usuário ou senha inválido(s)")