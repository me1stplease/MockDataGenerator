def Properties(st, dtype):
    if dtype == "Name":
        ntype = st.selectbox(
            'Type: ',
            ('Full Name', 'First', 'Last'))
        st.write(ntype)
    if dtype == "Phone":
        plen = st.text_input('Length : ', '10')
        st.write(plen)



