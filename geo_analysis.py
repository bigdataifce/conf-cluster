# importar pacotes e setar configurações de plots
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from functions import *
import plotly.express as px
import plotly.offline as py

sns.set_style()

dfx = pd.read_csv("SCOPS_OBFUSCATED_PASSAGES.tsv", sep='\t')
sensores = dfx.Local

passagens_sensor_1 = dfx.loc[((dfx['Local'] == sensores[0]))]
passagens_sensor_2 = dfx.loc[((dfx['Local'] == sensores[1]))]

dfs_filter = filter_df([passagens_sensor_1, passagens_sensor_2], cols=["Data", "Latitude", "Longitude"])
df_datetime = create_datetime(dfs_filter)
dfs_convert_time = convert_date(df_datetime)
df_animated = create_df_animated(dfs_convert_time)

df = px.data.gapminder()
fig = px.scatter_geo(df_animated,
                     lat="lat", lon="long",
                     color="num_pass",
                     hover_name="day_week",
                     text="num_pass",
                     size="num_pass",
                     animation_frame="day_week",
                     animation_group="hour",
                     scope="south america",
                     #width=800, height=800,
                     labels={"hour": "Hour of the day", "num_pass": "Number of Passes", "day_week": "Day of the Month"},
                     size_max=50)
fig.show()
py.plot(fig, filename='file.html')

