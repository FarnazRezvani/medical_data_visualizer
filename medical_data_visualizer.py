import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("C:/Users/SAM-Tech/Desktop/freecode camp/medical_data_visualizer/medical_examination.csv")


df["overweight"] = (df["weight"] / (df["height"] / 100) ** 2 > 25).astype(int)
print(df.head()) 


df["cholesterol"] = df["cholesterol"].apply(lambda X:0 if X==1 else 1)
df["gluc"] = df["gluc"].apply(lambda X:0 if X==1 else 1)
print(df.head()) 


df_cat = pd.melt(df, id_vars=["cardio"], value_vars=["cholesterol", "gluc", "smoke", "alco", "active", "overweight"])
df_cat = df_cat.rename(columns={"variable" : "variable" , "value" : "result"})

df_cat = df_cat.groupby(["variable", "result" , "cardio"], as_index= False).size()
df_cat = df_cat.rename(columns={"size" : "total"})
print(df_cat.head())


def draw_cat_plot():
    plot = sns.catplot(
        data=df_cat,
        kind="bar",
        x="variable",
        y="total",
        hue="result",
        col="cardio",
        height=5,
        aspect=1
    )
    plot.set_axis_labels("variable", "total") 
    fig = plot.fig
    return fig

fig = draw_cat_plot()
plt.show()


df_heat = df[
    (df["ap_lo"] <= df["ap_hi"]) &
    (df["height"] >= df["height"].quantile(0.025)) &
    (df["height"] <= df["height"].quantile(0.975)) &
    (df["weight"] >= df["weight"].quantile(0.025)) &
    (df["weight"] <= df["weight"].quantile(0.975)) 
]
corr = df_heat.corr()
print(corr)


mask = np.triu(np.ones_like(corr, dtype=bool))

def draw_heat_map():
    fig, ax = plt.subplots(figsize=(10, 10))
    sns.heatmap(
        corr,
        mask=mask,
        annot=True,
        fmt=".1f",
        cmap="coolwarm",
        square=True,
        cbar_kws= {"shrink" : 0.5}
    )
    return fig

fig = draw_heat_map()
plt.show()