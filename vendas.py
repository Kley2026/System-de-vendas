import streamlit as st
import pandas as pd
import plotly.express as px

st.write('# SISTEMA DE VENDAS')

tabela = pd.read_csv('vendas.csv')

st.sidebar.write('## Cadastrar venda')
data = st.sidebar.date_input('Data')
vendedor = st.sidebar.selectbox('Vendendor', ['Hosana', 'Lucca', 'Kleyvon'])
produto = st.sidebar.selectbox('Produto', ['Celular', 'Notebook', 'Computador', 'Fone'])
quantidade = st.sidebar.number_input('Quantidade', step=1)
valor = st.sidebar.number_input('Valor')
botao = st.sidebar.button('Cadastrar venda')

if botao:
    nova_venda = [data, vendedor, produto, quantidade, valor]
    tabela.loc[len(tabela)] = nova_venda
    tabela.to_csv('vendas.csv', index=False)
    st.success('Venda cadastrada!')

st.dataframe(tabela)

st.write('# VENDAS CADASTRADAS')
st.dataframe(tabela)

st.write('# DASHBOARD')
soma = tabela['valor'].sum()
st.metric('Faturamento total', f'R$ {soma}')

grafico = px.bar(tabela, x='vendedor', y='valor', color='produto')
st.plotly_chart(grafico)

grafico2 = px.pie(tabela, names='produto', values='valor')
st.plotly_chart(grafico2)
