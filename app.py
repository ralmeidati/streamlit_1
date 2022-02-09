#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import numpy as np
import streamlit as st
import plotly.express as px
#import plotly.express == 5.5.0

df = pd.read_csv('covid-variants.csv')

df.head(2)


df['location'].unique()


paises = list(df['location'].unique())


variantes = list(df['variant'].unique())


data = list(df['location'].unique())


df['date'] = pd.to_datetime(df['date'], format = '%Y-%m-%d')


pais = st.sidebar.selectbox('Escolha o país', ['Todos'] + paises)


variante = st.sidebar.selectbox('Escolha a variante', ['Todas'] + variantes)


if (pais != 'Todos'):
    st.header('Mostrando resultado de '+ pais)
    df = df[df['location'] == pais]
else:
    st.header('Mostrando resultado para todos os paises')


if (variante != 'Todas'):
    st.subheader('Mostrando resultado para variante '+ variante)
    df = df[df['variant'] == variante]
else:
    st.subheader('Mostrando resultado para todas as variantes')


dfShow = df.groupby(by = ['date']).sum()


fig = px.line(dfShow, x=dfShow.index, y = 'num_sequences')
fig.update_layout(title='Casos diários de COVID-19')
st.plotly_chart(fig, use_container_width=True)

