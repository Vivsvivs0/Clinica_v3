import streamlit as st
import pandas as pd
from views import View
import datetime
import time

class ManterConsultaUI:
    def main():
        st.header("Manter Consulta")
        tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])
        with tab1: ManterConsultaUI.listar()
        with tab2: ManterConsultaUI.inserir()
        with tab3: ManterConsultaUI.atualizar()
        with tab4: ManterConsultaUI.excluir()
    def listar():
        if len(View.consulta_listar()) > 0:
            dic = []
            for obj in View.consulta_listar(): dic.append(obj.to_json())
            df = pd.DataFrame(dic)
            st.dataframe(df)
        else:
            st.write("Nenhuma consulta cadastrada")
    def inserir():
        data = st.text_input("Data da consulta DD/MM/AAAA HH\:MM")
        medico = st.selectbox("Medico", View.medico_listar())
        paciente = st.selectbox("Paciente", View.paciente_listar())
        if st.button("Inserir"):
             data = datetime.datetime.strptime(data, "%d/%m/%Y %H:%M")
             View.consulta_inserir("True", data, paciente.get_id(), medico.get_id())
             st.success("Consulta inserida com sucesso")
             time.sleep(2)
             st.rerun()
    def atualizar():
        consulta = View.consulta_listar()
        if len(consulta) == 0:
            st.write("Nenhuma consulta cadastrada")
        else:
            op = st.selectbox("Atualização de consulta", consulta)
            data = st.text_input("Nova data da consulta DD/MM/AAAA HH\:MM")
            medico = st.selectbox("Novo medico", View.medico_listar())
            paciente = st.selectbox("Novo paciente", View.paciente_listar())
            if st.button("Atualizar"):
                data = datetime.datetime.strptime(data, "%d/%m/%Y %H:%M")
                View.consulta_atualizar(op.get_id(), "True", data, paciente.get_id(), medico.get_id())
                st.success("Consulta atualizada com sucesso")
                time.sleep(2)
                st.rerun()
    def excluir():
        op = st.selectbox("Exclusão de horários", View.consulta_listar())
        if st.button("Excluir"):
            View.consulta_excluir(op.get_id())
            st.success("Consulta excluída com sucesso")
            time.sleep(2)
            st.rerun()