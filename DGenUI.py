import streamlit as st
from PropComp import Properties as prop

global datatype
global columnName
with st.container():
    col1, col2, col3 = st.columns(3)

    with col1:
        datatype = st.selectbox(
            'Data Type: ',
            ('Name', 'Phone', 'Email'))
        st.write(datatype)

    with col2:
        columnName = st.text_input('Attribute Name: ', 'Text')
        st.write(columnName)

    with col3:
        prop(st, datatype)

