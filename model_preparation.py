import pandas as pd
from sklearn.preprocessing import LabelEncoder

def prepare_data():
    df = pd.read_csv("processed_data.csv")

    le_city = LabelEncoder()
    df['City'] = le_city.fit_transform(df['City'])

    le_target = LabelEncoder()
    df['AQI_Bucket'] = le_target.fit_transform(df['AQI_Bucket'])

    X = df.drop('AQI_Bucket', axis=1)
    y = df['AQI_Bucket']

    return X, y


if __name__ == "__main__":
    X, y = prepare_data()
    print("Features shape:", X.shape)
    print("Target shape:", y.shape)