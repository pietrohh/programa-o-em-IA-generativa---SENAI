import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression

st.header('Previsão de Vendas')

#dados: [Investimento em marketing] = Faturamento
dados_vendas = pd.DataFrame({
    'Investimento': [100,200,300,400,500,600],
    'Faturamento': [1200,2500,3200,4800,5100,6300]
})

#objetivo: previsão de FATURAMENTO baseado nos investimentos

modelo_faturamento = LinearRegression() 

modelo_faturamento.fit(dados_vendas[['Investimento']], dados_vendas['Faturamento'])

#previsão
investimento = st.number_input('Investimento em marketing', min_value=0)
if st.button('Prever Faturamento'):
    faturamento_previsto = modelo_faturamento.predict([[investimento]])
    st.write(f'Faturamento previsto: {faturamento_previsto[0]:.2f}')
    
