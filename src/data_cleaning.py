import pandas as pd

def load_and_clean_data(path1, path2):
    # Load datasets
    df1 = pd.read_csv(path1)
    df2 = pd.read_csv(path2)

    # Combine datasets
    df = pd.concat([df1, df2], ignore_index=True)

    # Clean column names (remove spaces)
    df.columns = df.columns.str.strip()

    # Rename columns (important for consistency)
    df.rename(columns={
        'Estimated Unemployment Rate (%)': 'Unemployment_Rate',
        'Estimated Employed': 'Employed',
        'Estimated Labour Participation Rate (%)': 'Labour_Participation_Rate'
    }, inplace=True)

    # Convert Date column
    df['Date'] = pd.to_datetime(df['Date'], dayfirst=True)
    
    # Drop only important missing values
    df.dropna(subset=['Date', 'Unemployment_Rate'], inplace=True)

    return df