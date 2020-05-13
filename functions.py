import pandas as pd


def filter_df(dfs, cols):
    df_int = pd.DataFrame(columns=cols)

    for i in range(0, len(dfs)):
        df = pd.DataFrame(dfs[i].Data)
        df["Latitude"] = dfs[i].Latitude
        df["Longitude"] = dfs[i].Longitude

        df_int = df_int.append(df, ignore_index=True)

    return df_int


def create_datetime(df):
    df['Datetime'] = pd.to_datetime(df.Data, format="%Y-%m-%dT%H:%M:%S.%fZ")

    return df

def convert_date(dfs):
    dfs['year'] = dfs.Datetime.dt.year
    dfs['month'] = dfs.Datetime.dt.month
    dfs['day'] = dfs.Datetime.dt.day
    dfs['hour'] = dfs.Datetime.dt.hour
    dfs['minute'] = dfs.Datetime.dt.minute
    dfs['second'] = dfs.Datetime.dt.second
    dfs['day_of_week'] = dfs.Datetime.dt.dayofweek

    dfs.drop(["Data"], axis=1, inplace=True)

    return dfs


def append_dfs(dfs):
    df_int = pd.DataFrame(columns=dfs[0].columns)

    for i in range(0, len(dfs)):
        df_int = df_int.append(dfs[i], ignore_index=True)

    return df_int


def create_df_animated(df):
    df_day = []
    df_hour = []
    df_num = []
    lat = []
    longi = []

    for day in range(1, 18):
        df_day_month = df.loc[df["day"] == day]
        for hour_pico in range(0, 24):
            df_month_pico = df_day_month.loc[df_day_month["hour"] == hour_pico]
            df_day.append(day)
            df_hour.append(hour_pico)
            df_num.append(int(len(df_month_pico)))
            lat.append(df_day_month["Latitude"])
            longi.append(df_day_month["Longitude"])

    dic_cols = {"day_week": df_day, "hour": df_hour, "num_pass": df_num, "lat": lat, "long": longi}
    df_animated = pd.DataFrame(data=dic_cols)

    return df_animated

