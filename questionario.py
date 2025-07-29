
import streamlit as st
import pandas as pd
from datetime import datetime
import os

st.set_page_config(page_title="Pesquisa Amazonas 2025", layout="wide")
st.title("📋 Pesquisa Eleitoral Amazonas 2025")

with st.form("formulario"):

    st.header("🧍‍♂️ BLOCO 1 – Dados Sociodemográficos")
    municipio = st.selectbox("1. Município", ["Manaus", "Itacoatiara", "Iranduba", "Parintins"])
    bairro = st.text_input("2. Bairro onde mora")
    idade = st.number_input("3. Idade", min_value=16, max_value=100)
    sexo = st.radio("4. Sexo", ["Masculino", "Feminino", "Outro", "Prefere não dizer"])
    escolaridade = st.selectbox("5. Escolaridade", [
        "Analfabeto(a)", "Ensino Fundamental incompleto", "Ensino Fundamental completo",
        "Ensino Médio incompleto", "Ensino Médio completo", "Ensino Superior incompleto",
        "Ensino Superior completo", "Pós-graduação"
    ])
    renda = st.selectbox("6. Renda familiar mensal", [
        "Até 1 salário mínimo", "De 1 a 2 salários mínimos", "De 2 a 5 salários mínimos",
        "Acima de 5 salários mínimos", "Prefere não responder"
    ])

    st.header("🏛️ BLOCO 2 – Avaliação de Governo")
    avaliacao_estado = st.radio("7. Como você avalia o governo estadual?", ["Ótimo", "Bom", "Regular", "Ruim", "Péssimo", "NS/NR"])
    avaliacao_federal = st.radio("8. Como você avalia o governo federal?", ["Ótimo", "Bom", "Regular", "Ruim", "Péssimo", "NS/NR"])
    aprovacao_prefeito = st.radio("9. Você aprova a administração do prefeito?", ["Aprova", "Desaprova", "Não sabe / Não respondeu"])
    avaliacao_prefeito = st.radio("10. Como avalia a gestão do prefeito?", ["Ótima", "Boa", "Regular", "Ruim", "Péssima", "NS/NR"])

    area_melhorou = st.selectbox("11. Área que mais melhorou", [
        "Saúde", "Educação", "Transporte", "Limpeza pública", "Segurança", "Assistência social",
        "Asfaltamento", "Turismo", "Revitalização do centro", "Limpeza de igarapés",
        "Cultura e eventos", "Esporte e lazer", "Habitação", "Atendimento nos órgãos públicos", "Nenhuma", "Outra"
    ])
    area_precisa = st.selectbox("12. Área que mais precisa de melhorias", [
        "Saúde", "Educação", "Transporte", "Limpeza pública", "Segurança", "Assistência social",
        "Asfaltamento", "Turismo", "Revitalização do centro", "Limpeza de igarapés",
        "Cultura e eventos", "Esporte e lazer", "Habitação", "Atendimento nos órgãos públicos", "Nenhuma", "Outra"
    ])
    caracteristicas = st.multiselect("13. Três principais características desejadas para o futuro governador", [
        "Ser de centro", "De esquerda", "De direita", "Honesto", "Conservador",
        "Progressista", "De família", "Com passado limpo", "Experiente"
    ])
    voto_prefeitura = st.radio("14. Em quem votou para prefeito (apenas Manaus)?", ["David Almeida", "Capitão Alberto Neto", "Branco/Nulo", "NS/NR"])

    st.header("🗳️ BLOCO 3 – Governo do Estado")
    voto_espontaneo_gov = st.text_input("15. Se a eleição para governador fosse hoje, em quem você votaria? (Espontânea)")
    cenario1_gov = st.radio("16. Cenário 1", ["David Almeida", "Omar Aziz", "Maria do Carmo", "Sargento Salazar", "Branco/Nulo", "NS/NR"])
    cenario2_gov = st.radio("17. Cenário 2", ["David Almeida", "Omar Aziz", "Maria do Carmo", "Branco/Nulo", "NS/NR"])
    cenario3_gov = st.radio("18. Cenário 3", ["Omar Aziz", "David Almeida", "Capitão Alberto Neto", "Branco/Nulo", "NS/NR"])
    cenario4_gov = st.radio("19. Cenário 4", ["David Almeida", "Omar Aziz", "Sargento Salazar", "Branco/Nulo", "NS/NR"])
    cenario5_gov = st.radio("20. Cenário 5", ["Omar Aziz", "Tadeu de Souza", "Maria do Carmo", "Branco/Nulo", "NS/NR"])

    st.header("🗳️ BLOCO 4 – Senado")
    voto_espontaneo_sen = st.text_input("21. Se a eleição para senador fosse hoje, em quem votaria? (Espontânea)")
    cenario1_sen = st.selectbox("22. Cenário 1", ["Eduardo Braga", "Wilson Lima", "Capitão Alberto Neto", "Plínio Valério", "Marcos Rotta", "Marcelo Ramos", "Sargento Salazar", "Branco/Nulo", "NS/NR"])
    cenario2_sen = st.selectbox("23. Cenário 2", ["Eduardo Braga", "Wilson Lima", "Capitão Alberto Neto", "Plínio Valério", "Marcos Rotta", "Marcelo Ramos", "Branco/Nulo", "NS/NR"])
    cenario3_sen = st.selectbox("24. Cenário 3", ["Eduardo Braga", "Wilson Lima", "Plínio Valério", "Sargento Salazar", "Marcos Rotta", "Marcelo Ramos", "Branco/Nulo", "NS/NR"])

    st.header("🚫 BLOCO 5 – Rejeição")
    rejeicao_gov = st.multiselect("25. Em quem NÃO votaria para governador?", ["David Almeida", "Omar Aziz", "Maria do Carmo", "Tadeu de Souza", "Sargento Salazar", "Capitão Alberto Neto", "NS/NR"])
    rejeicao_sen = st.multiselect("26. Em quem NÃO votaria para senador?", ["Eduardo Braga", "Wilson Lima", "Capitão Alberto Neto", "Plínio Valério", "Marcos Rotta", "Marcelo Ramos", "Sargento Salazar", "NS/NR"])

    st.header("👨‍⚖️ BLOCO 6 – Deputado Federal")
    voto_espontaneo_dep = st.text_input("27. Em quem votaria para deputado federal? (Espontânea)")
    voto_estimulado_dep = st.selectbox("28. Em qual dessas opções votaria?", [
        "Adail Filho", "Alfredo Nascimento", "Amom Mandel", "Arthur Neto", "Átila Lins", "Carlos Almeida", "Coronel Menezes",
        "Fausto Júnior", "Fernanda Aryel Almeida", "Gedeão Amorim", "Jesus Alves", "João Carlos", "Jorge Oliveira", "Luiz Castro",
        "Pauderney Avelino", "Ricardo Nicolau", "Roberto Cidade", "Sargento Salazar", "Saullo Vianna", "Serafim Corrêa",
        "Sidney Leite", "Silas Câmara", "Thaysa Lippy", "Vanda Witoto", "Zé Ricardo"
    ])

    st.header("🇧🇷 BLOCO 7 – Presidente")
    voto_presidente = st.radio("29. Se a eleição para presidente fosse hoje, em quem votaria?", ["Lula", "Michelle Bolsonaro", "Branco/Nulo", "NS/NR"])

    enviar = st.form_submit_button("Enviar resposta")

if enviar:
    resposta = {
        "Data": datetime.now(), "Município": municipio, "Bairro": bairro, "Idade": idade, "Sexo": sexo,
        "Escolaridade": escolaridade, "Renda": renda, "Avaliação Estado": avaliacao_estado, "Avaliação Federal": avaliacao_federal,
        "Aprovação Prefeito": aprovacao_prefeito, "Avaliação Prefeito": avaliacao_prefeito,
        "Área Melhorou": area_melhorou, "Área Melhorar": area_precisa, "Características": ", ".join(caracteristicas),
        "Voto Prefeitura": voto_prefeitura, "Voto Espontâneo Gov": voto_espontaneo_gov,
        "Cenário 1 Gov": cenario1_gov, "Cenário 2 Gov": cenario2_gov, "Cenário 3 Gov": cenario3_gov,
        "Cenário 4 Gov": cenario4_gov, "Cenário 5 Gov": cenario5_gov,
        "Voto Espontâneo Sen": voto_espontaneo_sen, "Cenário 1 Sen": cenario1_sen, "Cenário 2 Sen": cenario2_sen,
        "Cenário 3 Sen": cenario3_sen, "Rejeição Gov": ", ".join(rejeicao_gov), "Rejeição Sen": ", ".join(rejeicao_sen),
        "Voto Espontâneo Dep": voto_espontaneo_dep, "Voto Estimulado Dep": voto_estimulado_dep,
        "Voto Presidente": voto_presidente
    }

    arquivo = "respostas_pesquisa_amazonas.xlsx"
    if os.path.exists(arquivo):
        df_existente = pd.read_excel(arquivo)
        df_novo = df_existente.append(resposta, ignore_index=True)
    else:
        df_novo = pd.DataFrame([resposta])

    df_novo.to_excel(arquivo, index=False)
    st.success("✅ Resposta registrada com sucesso!")
