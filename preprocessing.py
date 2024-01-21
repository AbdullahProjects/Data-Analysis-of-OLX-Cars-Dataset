import pandas as pd

# constructing new column of city
def constructing_city(col):
    location = col.split(",")
    if len(location)==2:
        return location[1].strip()
    else:
        return None
    

def preprocess_dataset(df):
    df["Seller City"] = df["Seller Location"].apply(constructing_city)
    # drop unnecessary columns
    df.drop(columns=["Car Name","Description","Images URL's","Car Profile"], inplace=True)
    # drop duplicated rows
    df.drop_duplicates(inplace=True)
    # drop null values
    df.dropna(inplace=True)

    return df
    