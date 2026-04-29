from data_cleaning import load_and_clean_data
from visualization import (
    plot_overall_trend,
    plot_covid_impact,
    plot_statewise,
    plot_seasonal,
    plot_top_states
)

# File paths
path1 = 'data/unemployment_india.csv'
path2 = 'data/unemployment_covid.csv'

# Load cleaned data
df = load_and_clean_data(path1, path2)
plot_top_states(df)
# Basic info
print(df.head())
print(df.describe())

# Run visualizations
plot_overall_trend(df)
plot_covid_impact(df)
plot_statewise(df)
plot_seasonal(df)