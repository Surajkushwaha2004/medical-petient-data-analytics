import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

filename = "my_medical_examination.csv" 
df = pd.read_csv(filename)

df["BMI"] = df["weight"] / ((df["height"] / 100) ** 2)
df["overweight"] = (df["BMI"] > 25).astype(int)
df.drop("BMI", axis=1, inplace=True)

df["cholesterol"] = (df["cholesterol"] > 1).astype(int)
df["gluc"] = (df["gluc"] > 1).astype(int)

def draw_cat_plot():
    df_cat = pd.melt(
        df,
        id_vars=['cardio'],
        value_vars=['active', 'alco', 'cholesterol', 'gluc', 'overweight', 'smoke']
    )
    df_cat = df_cat.groupby(['cardio', 'variable', 'value']).size().reset_index(name='total')

    cat_plot = sns.catplot(
        data=df_cat,
        kind='bar',
        x='variable',
        y='total',
        hue='value',
        col='cardio'
    )

    cat_plot.set_axis_labels("Variable", "Total")
    cat_plot.set_titles("Cardio = {col_name}")

    fig = cat_plot.fig
    fig.savefig('catplot.png')
    print("📊 Saved categorical plot as 'catplot.png'")
    plt.show()

def draw_heat_map():
    df_heat = df[
        (df['ap_lo'] <= df['ap_hi']) &
        (df['height'] >= df['height'].quantile(0.025)) &
        (df['height'] <= df['height'].quantile(0.975)) &
        (df['weight'] >= df['weight'].quantile(0.025)) &
        (df['weight'] <= df['weight'].quantile(0.975))
    ]

    corr = df_heat.corr()
    mask = np.triu(np.ones_like(corr, dtype=bool))

    fig, ax = plt.subplots(figsize=(12, 10))
    sns.heatmap(
        corr,
        mask=mask,
        annot=True,
        fmt=".1f",
        center=0,
        square=True,
        linewidths=0.5,
        cbar_kws={"shrink": 0.5},
        ax=ax
    )
    fig.savefig('heatmap.png')
    print("📊 Saved heatmap as 'heatmap.png'")
    plt.show()

draw_cat_plot()
draw_heat_map()
