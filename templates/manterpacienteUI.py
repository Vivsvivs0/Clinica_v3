import streamlit as st
import pandas as pd
from views import View
import time

class ManterPacienteUI:
    def main():
        st.header("Manter Paciente")
        tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])
        with tab1: ManterPacienteUI.listar()
        with tab2: ManterPacienteUI.inserir()
        with tab3: ManterPacienteUI.atualizar()
        with tab4: ManterPacienteUI.excluir()
    def listar():
        if len(View.paciente_listar()) > 0:
            dic = []
            for obj in View.paciente_listar(): dic.append(obj.to_json())
            df = pd.DataFrame(dic)
            st.dataframe(df)
        else:
            st.write("Nenhum paciente cadastrado")
    def inserir():
        nome = st.text_input("Nome do paciente")
        fone = st.text_input("Fone do paciente")
        email = st.text_input("Email do paciente")
        senha = st.text_input("Senha do paciente")
        if st.button("Inserir"):
             View.paciente_inserir(nome, fone, email, senha)
             st.success("Paciente inserido com sucesso")
             time.sleep(2)
             st.rerun()
    def atualizar():
        pacientes = View.paciente_listar()
        if len(pacientes) == 0:
            st.write("Nenhum paciente cadastrado")
        else:
            op = st.selectbox("Atualização de paciente", pacientes)
            nome = st.text_input("Novo nome do paciente", op.get_nome())
            fone = st.text_input("Novo fone do paciente", op.get_fone())
            email = st.text_input("Novo email do paciente", op.get_email())
            senha = st.text_input("Nova senha do paciente", op.get_senha())
            if st.button("Atualizar"):
                View.paciente_atualizar(op.get_id(), nome, fone, email, senha)
                st.success("Paciente atualizado com sucesso")
                time.sleep(2)
                st.rerun()
                
    def excluir():
        op = st.selectbox("Exclusão de pacientes", View.paciente_listar())
        if st.button("Excluir"):
            View.paciente_excluir(op.get_id())
            st.success("Paciente excluído com sucesso")
            time.sleep(2)
            st.rerun()