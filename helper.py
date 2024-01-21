import pandas as pd



# Cities where more sellers exist
def cities_where_more_sellers(df):
    dataset = df["Seller City"].value_counts().reset_index()
    return dataset

# brands(companies) over years
def brands_sales_over_years(df):
    group_years = df.groupby(["Year"])["Make"] # group years 
    unique_years = sorted(df["Year"].unique().tolist()) # get unique years from dataset
    companies = []
    for year in unique_years: # get_group of particular year from 'group_years' line by line and then get unique cars companies in that year and finally, append it in new list
        companies.append(len(group_years.get_group(year).unique().tolist()))

    dataset = pd.DataFrame({ # create dataset in which we have year and it corresponding car companies
        "Years": unique_years,
        "Brands": companies
    })
    return dataset

# models over years
def models_sales_over_years(df):
    group_years = df.groupby(["Year"])["Model"] # group years 
    unique_years = sorted(df["Year"].unique().tolist()) # get unique years from dataset
    models = []
    for year in unique_years: # get_group of particular year from 'group_years' line by line and then get unique cars companies in that year and finally, append it in new list
        models.append(len(group_years.get_group(year).unique().tolist()))

    dataset = pd.DataFrame({ # create dataset in which we have year and it corresponding car companies
        "Years": unique_years,
        "Models": models
    }) 
    return dataset



