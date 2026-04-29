import matplotlib.pyplot as plt
import seaborn as sns

def plot_overall_trend(df):
    plt.figure(figsize=(10,5))
    sns.lineplot(x='Date', y='Unemployment_Rate', data=df)
    plt.title("Overall Unemployment Trend")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


def plot_covid_impact(df):
    covid_df = df[df['Date'] >= '2020-03-01']

    plt.figure(figsize=(10,5))
    sns.lineplot(x='Date', y='Unemployment_Rate', data=covid_df, color='red')
    plt.title("COVID-19 Impact on Unemployment")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


def plot_statewise(df):
    if 'Region' in df.columns:
        top_states = df.groupby('Region')['Unemployment_Rate'].mean().sort_values(ascending=False).head(10)

        top_states.plot(kind='bar')
        plt.title("Top 10 States by Unemployment Rate")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()


def plot_seasonal(df):
    df['Month'] = df['Date'].dt.month

    plt.figure(figsize=(8,5))
    sns.boxplot(x='Month', y='Unemployment_Rate', data=df)
    plt.title("Monthly (Seasonal) Trends")
    plt.tight_layout()
    plt.show()
    
def plot_top_states(df):
    top_states = df.groupby('Region')['Unemployment_Rate'].mean().sort_values(ascending=False).head(5)

    top_states.plot(kind='bar')
    plt.title("Top 5 Most Affected States")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()