# importar pacotes e setar configurações de plots
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from functions import *
import plotly.express as px
import random


sns.set_style()

dfx = pd.read_csv("/home/saulomaia/Documentos/mobit/SCOPS_OBFUSCATED_PASSAGES.tsv", sep='\t')
sensores = dfx.Local

all_dfs = []

random_lats = [-7.104860, -4.520079, -6.893017, -11.235091, -11.986047, -6.270331, -6.838615, -5.943062]
random_long = [-50.653080, -40.372369, -45.039618, -43.358975, -49.971897, -45.709057, -38.337954, -42.751896]

print("[INFO] Generate the dataframes of each sensor")
for s in range(0, len(sensores.unique())):
    df_local = dfx.loc[((dfx['Local'] == sensores.unique()[s]))]
    df_local.Latitude = random_lats[s]
    df_local.Longitude = random_long[s]
    all_dfs.append(df_local)

all_filter_dfs = []

print("[INFO] Filterings ...")
for r in range(0, len(all_dfs)):

    dfs_filter = filter_df(all_dfs[r])
    df_datetime = create_datetime(dfs_filter)
    dfs_convert_time = convert_date(df_datetime)
    df_animated = create_df_animated(dfs_convert_time)
    all_filter_dfs.append(df_animated)

join_df = append_dfs(all_filter_dfs)
join_df = join_df.replace(0, 1)


fig = px.scatter_geo(join_df,
                     lat="lat", lon="long",
                     color="num_pass",
                     hover_name="day_week",
                     text="num_pass",
                     size="num_pass",
                     animation_frame="day_week",
                     animation_group="hour",
                     scope="south america",
                     #projection="natural earth",
                     width=700, height=700,
                     #center={"lat": -4.795678, "lon": -40.717659},
                     labels={"hour": "Hour of the day", "num_pass": "Number of Passes", "day_week": "Day of the Month"},
                     size_max=25
                     )
fig.show()
