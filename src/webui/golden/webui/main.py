from typing import Any
from threading import Timer
from urllib.parse import urljoin

import pandas as pd
import requests
import streamlit as st

from golden.webui.configuration import Configuration

config = Configuration()



st.title('Golden ui')
cont = st.container()

if btn := cont.button('Pay'):
    res = requests.get(urljoin(config.api_url, '/pay'), timeout=30)
    obj = cont.write('Payed! ' + res.text)
    def empty() -> None:
        st.rerun()
    Timer(1, empty).run()

st.divider()


@st.cache_data(ttl=5)
def get_data() -> Any:
    try:
        return requests.get(urljoin(config.api_url, '/payments'), timeout=30).json()
    except requests.JSONDecodeError:
        return {'data':[], 'columns':[]}

json = get_data()
df = pd.DataFrame(json['data'], columns=json['columns'])

st.dataframe(df)
