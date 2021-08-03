import json

import pandas as pd

# link to etoro instrument list
# https://colab.research.google.com/drive/1i8LaoQG3O0tEnJov5AqlErn27C-p5Oi1?usp=sharing#scrollTo=iz_u4S-NYq83
# running this will download the etoro_stocks.csv which will be parsed to etoro_stocks.json

etoro_stocks = pd.read_csv("etoro_stocks.csv", sep=';', encoding='utf-16')
etoro_stocks.sort_values("name", inplace=True)

# For now we will just be filtering out the exchange and industry values
etoro_stocks["exchange"].replace("-", "", inplace=True)
etoro_stocks["industry"].replace("-", "", inplace=True)

instrument_types = sorted(etoro_stocks["instrument type"].unique())

etoro_instruments = dict()
for i in instrument_types:
    instrument_key = i.lower()
    etoro_instruments[instrument_key] = dict()
    sub_df = etoro_stocks.loc[etoro_stocks["instrument type"] == i]

    for i, row in sub_df.iterrows():
        # if row["name"] == "Algorand":
        #     a = 1
        instrument_dict = {"symbol": row["symbol"]}
        if row["exchange"]:
            instrument_dict["exchange"] = row["exchange"]
        if row["industry"]:
            instrument_dict["industry"] = row["industry"]
        etoro_instruments[instrument_key][row["name"]] = instrument_dict

with open('etoro_instruments.json', 'w') as fp:
    json.dump(etoro_instruments, fp, indent=4)
