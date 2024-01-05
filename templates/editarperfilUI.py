import streamlit as st
from views import View

class EditarPerfilUI:
    def main():
        st.header("Atualizar perfil")
        EditarPerfilUI.atualizar()

    def atualizar():
        op = View.paciente_listar_id(st.session_state["id_paciente"])
        nome = "admin"
        if op.get_nome() != "admin":
            nome = st.text_input("Informe o novo nome", op.get_nome())
        fone = st.text_input("Informe o novo fone", op.get_fone())
        email = st.text_input("Informe o novo e-mail", op.get_email())
        senha = st.text_input("Informe a nova senha")
        if st.button("Atualizar"):
            id = op.get_id()
            View.paciente_atualizar(id, nome, fone, email, senha)
            st.success("Perfil atualizado com sucesso")