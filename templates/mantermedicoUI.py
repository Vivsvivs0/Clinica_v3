import streamlit as st
import pandas as pd
from views import View
import time

class ManterMedicoUI:
    def main():
        st.header("Manter Medico")
        tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])
        with tab1: ManterMedicoUI.listar()
        with tab2: ManterMedicoUI.inserir()
        with tab3: ManterMedicoUI.atualizar()
        with tab4: ManterMedicoUI.excluir()
    def listar():
        if len(View.medico_listar()) > 0:
            dic = []
            for obj in View.medico_listar(): dic.append(obj.to_json())
            df = pd.DataFrame(dic)
            st.dataframe(df)
        else:
            st.write("Nenhum médico cadastrado")    
    def inserir():
        nome = st.text_input("Nome do médico")
        fone = st.text_input("Fone do médico")
        email = st.text_input("Email do médico")
        if st.button("Inserir"):
             View.medico_inserir(nome, fone, email)
             st.success("Médico inserido com sucesso")
             time.sleep(2)
             st.rerun()
    def atualizar():
        medicos = View.medico_listar()
        if len(medicos) == 0:
            st.write("Nenhum médico cadastrado")
        else:
            op = st.selectbox("Atualização de médico", medicos)
            nome = st.text_input("Novo nome do médico", op.get_nome())
            fone = st.text_input("Novo fone do médico", op.get_fone())
            email = st.text_input("Novo email do médico", op.get_email())
            if st.button("Atualizar"):
                View.medico_atualizar(op.get_id(), nome, fone, email)
                st.success("Médico atualizado com sucesso")
                time.sleep(2)
                st.rerun()
    def excluir():
        op = st.selectbox("Exclusão de médicos", View.medico_listar())
        if st.button("Excluir"):
            View.medico_excluir(op.get_id())
            st.success("Médico excluído do sistema")
            time.sleep(2)
            st.rerun()