import streamlit as st
import pandas as pd
from views import View
import datetime

class SolicitarConsultaUI:
    def main():
        st.header("Solicitar consulta")
        SolicitarConsultaUI.solicitar()
    def solicitar():
        if len(View.medico_listar()) > 0:
            medico = st.selectbox("Médico desejado", View.medico_listar())
            data = st.text_input("Data em formato DD/MM/AAAA HH\:MM")
            if st.button("Solicitar"):
              data = datetime.datetime.strptime(data, "%d/%m/%Y %H:%M")
              if View.medico_disponivel(medico, data):
                View.consulta_inserir("False", data, st.session_state["id_paciente"], medico.get_id())
                st.success("Consulta solicitada com sucesso, aguarde confirmação")
              else:
                 st.error("Médico ocupado no horário selecionado")
        else:
            st.write("Nenhum médico disponível para consultas")