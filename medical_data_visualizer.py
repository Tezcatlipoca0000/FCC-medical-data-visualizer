import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Import data
df = pd.read_csv('medical_examination.csv')

# Add 'overweight' column
bmi = df['weight'] / (df['height'] / 100) ** 2
df['overweight'] = bmi.apply(lambda x: 0 if x < 26 else 1)

# Normalize data by making 0 always good and 1 always bad. If the value of 'cholesterol' or 'gluc' is 1, make the value 0. If the value is more than 1, make the value 1.
df['cholesterol'] = df['cholesterol'].apply(lambda x: 0 if x == 1 else 1)
df['gluc'] = df['gluc'].apply(lambda x: 0 if x == 1 else 1)

# Draw Categorical Plot
def draw_cat_plot():
    # Create DataFrame for cat plot using `pd.melt` using just the values from 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.
    df_cat = df.melt(id_vars=['cardio'], value_vars=['active', 'alco', 'cholesterol', 'gluc', 'overweight', 'smoke'])


    # Group and reformat the data to split it by 'cardio'. Show the counts of each feature. You will have to rename one of the columns for the catplot to work correctly.
    #df_cat = None
    

    # Draw the catplot with 'sns.catplot()'
    sns.catplot(data=df_cat, kind='count', x='variable', hue='value', col='cardio')


    # Get the figure for the output
    fig = sns.catplot(data=df_cat, kind='count', x='variable', hue='value', col='cardio')


    # Do not modify the next two lines
    fig.savefig('catplot.png')
    return fig


# Draw Heat Map
def draw_heat_map():
    # Clean the data
    df = df[df['ap_lo'] <= df['ap_hi']]
    df = df[df['height'] >= df['height'].quantile(0.025)]
    df = df[df['height'] <= df['height'].quantile(0.975)]
    df = df[df['weight'] >= df['weight'].quantile(0.025)]
    df = df[df['weight'] <= df['weight'].quantile(0.975)]
    df_heat = df.copy()

    # Calculate the correlation matrix
    corr = df_heat.corr()

    # Generate a mask for the upper triangle
    mask = np.triu(corr)



    # Set up the matplotlib figure
    fig, ax = sns.heatmap(corr, mask=mask, annot=True, fmt='.1f', center=0, vmax=0.3)

    # Draw the heatmap with 'sns.heatmap()'
    sns.heatmap(corr, mask=mask, annot=True, fmt='.1f', center=0, vmax=0.3)


    # Do not modify the next two lines
    fig.savefig('heatmap.png')
    return fig
