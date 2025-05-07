def preprocess(df):
    df["Sex"] = df["Sex"].map({"male": 0, "female": 1})
    df["Embarked"] = df["Embarked"].map({"S": 0, "C": 1, "Q": 2})
    df = df.fillna(df.median(numeric_only=True))
    return df
