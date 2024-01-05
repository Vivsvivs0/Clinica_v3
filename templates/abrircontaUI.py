import streamlit as st
from views import View

class AbrirContaUI:
  def main():
    st.header("Abrir Conta no Sistema")
    AbrirContaUI.abrirconta()
  
  def abrirconta():
    nome = st.text_input("Informe o nome")
    fone = st.text_input("Informe o fone")
    email = st.text_input("Informe o e-mail")
    senha = st.text_input("Informe a senha")
    if st.button("Cadastrar"):
      View.paciente_inserir(nome, fone, email, senha)
      st.success("Conta criada com sucesso")