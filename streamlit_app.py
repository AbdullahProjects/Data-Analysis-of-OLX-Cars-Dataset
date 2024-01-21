import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import seaborn as sns
from wordcloud import WordCloud
# these are python files
import preprocessing, helper



# import dataset
df = pd.read_csv("Dataset/OLX_cars_dataset00.csv")
# preprocess it 
df = preprocessing.preprocess_dataset(df)

# setting title and icon of streamlit app
st.set_page_config(page_title="Data Analysis OLX Cars Dataset", page_icon="CarImg.png")
# streamlit sidebar
st.sidebar.image("https://github.com/AbdullahKhanKakar/My-Dataset-Collection/blob/main/Image.jpg?raw=true")
st.sidebar.title("OLX Cars Data Analysis")
user_menu = st.sidebar.radio(
    "Select an option:",
    ("Overall Analysis" ,"Brand-wise Analysis", "Model-wise Analysis", "City-wise Analysis")
)
st.sidebar.markdown("---")
st.sidebar.markdown("##### Dataset Available on Kaggle: 'https://www.kaggle.com/datasets/abdullahkhanuet22/olx-cars-dataset'")
# user selection
if user_menu=="Overall Analysis":
    # 1. top statistics
    st.title("Top Statistics")
    col1, col2= st.columns(2)
    with col1:
        st.subheader("Rows")
        st.markdown(f"##### {df.shape[0]}")
    with col2:
        st.subheader("Columns")
        st.markdown(f"##### {df.shape[1]}")

    col1, col2= st.columns(2)
    with col1:
        st.subheader("Total Sellers")
        st.markdown(f"##### {len(df['Ad ID'].unique().tolist())}")
    with col2:
        st.subheader("Car Brands")
        st.markdown(f"##### {len(df['Make'].unique().tolist())}")
    
    col1, col2= st.columns(2)
    with col1:
        st.subheader("Total Models")
        st.markdown(f"##### {len(df['Model'].unique().tolist())}")
    with col2:
        st.subheader("Years Range")
        st.markdown(f"##### {df['Year'].min()} - {df['Year'].max()}")
    
    col1, col2= st.columns(2)
    with col1:
        st.subheader("KM's Driven Range")
        n_df = df.rename(columns={"KM's driven":"KM driven"})
        st.markdown(f"##### {n_df['KM driven'].min()} - {n_df['KM driven'].max()}")
    with col2:
        st.subheader("Prices Range")
        st.markdown(f"##### {df['Price'].min()} - {df['Price'].max()}")

    # 2. Car Companies Distribution
    st.title("Car Companies(Brands) Distribution")
    fig = px.histogram(df, x="Make", color="Make")
    fig.update_layout(xaxis_title="Car Company", yaxis_title="Counts")
    st.plotly_chart(fig)

    # 3. Most Frequent Models
    st.title("Top 20 Most Frequent Models")
    most_frequent_models = df["Model"].value_counts().reset_index().head(20)
    fig = px.bar(most_frequent_models, x="Model", y="count", color="Model")
    fig.update_layout(xaxis_title="Most Frequent Models", yaxis_title="Counts")
    st.plotly_chart(fig)

    # 4. Prices Distribution
    st.title("Price Distribution with KDE")
    fig, ax = plt.subplots()
    ax = sns.histplot(df['Price'], kde=True, color='skyblue', bins=10)
    ax.set_xlabel('Price')
    ax.set_ylabel('Count')
    st.pyplot(fig)

    # 5. Years Distribution
    st.title("Years Distribution")
    df_sorted_years = df.sort_values(by="Year")
    fig = px.histogram(df_sorted_years, x="Year", color="Year")
    fig.update_layout(xaxis_title="Year", yaxis_title="Count")
    st.plotly_chart(fig)

    # 6. Fuel Type Distribution
    st.title("Fuel Type Distribution")
    table_df = df["Fuel"].value_counts().reset_index(name="Count") # showing table also
    st.table(table_df)
    fig = px.pie(df, names="Fuel", hole=0.5, opacity=0.82)
    st.plotly_chart(fig)

    # 7. Transmission Distribution
    st.title("Transmission Distribution")
    table_df = df["Transmission"].value_counts().reset_index(name="Count") # showing table also
    st.table(table_df)
    fig = px.pie(df, names="Transmission", hole=0.5, opacity=0.82)
    st.plotly_chart(fig)

    # 8. Car Documents Distribution
    st.title("Car Documents Distribution")
    table_df = df["Car documents"].value_counts().reset_index(name="Count") # showing table also
    st.table(table_df)
    fig = px.pie(df, names="Car documents", hole=0.5, opacity=0.82)
    st.plotly_chart(fig)

    # 9. Assembly Distribution
    st.title("Assembly Distribution")
    table_df = df["Assembly"].value_counts().reset_index(name="Count") # showing table also
    st.table(table_df)
    fig = px.pie(df, names="Assembly", hole=0.5, opacity=0.82)
    st.plotly_chart(fig)

    #10.  Condition Distribution
    st.title("Condition Distribution")
    table_df = df["Condition"].value_counts().reset_index(name="Count") # showing table also
    st.table(table_df)
    fig = px.pie(df, names="Condition", hole=0.5, opacity=0.82)
    st.plotly_chart(fig)

    # 11. Word Cloud of Car Features
    st.title("Car Features WordCloud")
    wordcloud = WordCloud(width=1000, height=600, background_color='black').generate(' '.join(df["Car Features"]))
    # plot wordcloud with matplotlib
    fig, ax = plt.subplots()
    ax.imshow(wordcloud, interpolation='bilinear')
    ax.axis('off')
    st.pyplot(fig)

    # 12. Brand-wise Car Sales Across Years
    st.title("Brand-wise Sales Across Years")
    brands_over_years = helper.brands_sales_over_years(df)
    st.table(brands_over_years)
    # visualize it
    st.subheader("Visualization:")
    fig = px.line(brands_over_years, x='Years', y='Brands', markers=True, color_discrete_sequence=px.colors.qualitative.Set2)
    fig.update_layout(xaxis_title='Year', yaxis_title='Car Brands')
    st.plotly_chart(fig) 

    # 13. Models Across Years
    st.title("Model-wise Sales Across Years")
    models_over_years = helper.models_sales_over_years(df)
    st.table(models_over_years)
    # visualize it
    st.subheader("Visualization:")
    fig = px.line(models_over_years, x='Years', y='Models', markers=True, color_discrete_sequence=px.colors.qualitative.Set2)
    fig.update_layout(xaxis_title='Year', yaxis_title='Car Models')
    st.plotly_chart(fig)

    # 14. Top 12 Cities where sellers are more
    st.title("Top 12 Cities Where More Sellers Exist")
    more_sellers_df = helper.cities_where_more_sellers(df)
    more_sellers_df = more_sellers_df.head(12)
    st.table(more_sellers_df)
    # visualize it
    st.subheader("Visualization:")
    fig = px.line(more_sellers_df, x="Seller City", y="count", markers=True, color_discrete_sequence=px.colors.qualitative.Set2)
    fig.update_layout(xaxis_title="Cities", yaxis_title="Sellers Count")
    st.plotly_chart(fig)

    # 15. Highest Price Car Brands
    st.title("Top 10 Highest Price Cars")
    highest_prices = df[df["Price"]==5000000][["Ad ID","Make","Model","Year","Price","KM's driven","Seller Location"]].sort_values(by="Price").reset_index(drop=True)
    st.dataframe(highest_prices.head(10))

    # 16. Lowest Price Car Brands
    st.title("Top 10 Lowest Price Cars")
    lowest_prices = df[df["Price"]<=350000][["Ad ID","Make","Model","Year","Price","KM's driven","Seller Location"]].sort_values(by="Price").reset_index(drop=True)
    st.dataframe(lowest_prices.head(10))

    # 17. Mean Prices
    st.title("Brands-wise Mean of Prices")
    mean_prices = df.groupby(["Make"])["Price"].mean().reset_index().sort_values(by="Price").reset_index(drop=True)
    st.table(mean_prices)
    # visualize it
    fig = px.line(mean_prices, x='Make', y='Price', markers=True, color_discrete_sequence=px.colors.qualitative.Set2)
    fig.update_layout(xaxis_title="Car Brands", yaxis_title="Mean Price")
    st.plotly_chart(fig)

    # 18. Mean KM's Driven
    st.title("Brands-wise Mean of KM's Driven")
    mean_distances = df.groupby(["Make"])["KM's driven"].mean().reset_index().sort_values(by="KM's driven").reset_index(drop=True)
    st.table(mean_distances)
    # visualize it
    fig = px.line(mean_distances, x='Make', y="KM's driven", markers=True, color_discrete_sequence=px.colors.qualitative.Set2)
    fig.update_layout(xaxis_title="Car Brands", yaxis_title="Mean Distance Covered")
    st.plotly_chart(fig)

    # Relationship between Year, Price, KM's driven
    st.title("Year vs Price vs KM's driven")
    fig1 = px.scatter_3d(df, x="Year", y="Price", z="KM's driven", color="KM's driven", color_continuous_scale='Viridis')
    st.plotly_chart(fig1)

    # Relationship between Year, Price, KM's driven on the basis of Transmission
    st.title("Year vs Price vs KM's driven highlighted Transmission")
    fig2 = px.scatter_3d(df, x="Year", y="Price", z="KM's driven", color="Transmission", color_discrete_sequence=px.colors.qualitative.Set1)
    st.plotly_chart(fig2)

    # Relationship between Year, Price, KM's driven on the basis of Car Documents
    st.title("Year vs Price vs KM's driven highlighted Car Documents")
    fig3 = px.scatter_3d(df, x="Year", y="Price", z="KM's driven", color="Car documents", color_discrete_sequence=px.colors.qualitative.Set2)
    st.plotly_chart(fig3)

    # Relationship between Year, Price, KM's driven on the basis of Assembly
    st.title("Year vs Price vs KM's driven highlighted Assembly")
    fig4 = px.scatter_3d(df, x="Year", y="Price", z="KM's driven", color="Assembly", color_discrete_sequence=px.colors.qualitative.Set3)
    st.plotly_chart(fig4)


if user_menu == "Brand-wise Analysis":
    st.title("Brand-wise Analysis")

    # select the brand
    brands = sorted(df["Make"].unique().tolist())
    selected_company = st.selectbox("Select a Brand:", brands)
   
    # filter the brand
    brands_df = df[df["Make"]==selected_company]
    # Statistics
    st.header(f"'{selected_company}' Top Statistics")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.subheader("Total Models")
        st.markdown(f"##### {len(brands_df['Model'].unique().tolist())}")
    with col2:
        st.subheader("Total Sellers")
        st.markdown(f"##### {len(brands_df['Ad ID'].unique().tolist())}")
    with col3:
        st.subheader("Seller Cities Count")
        st.markdown(f"##### {len(brands_df['Seller City'].unique())}")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.subheader("Years Range")
        st.markdown(f"##### {brands_df['Year'].min()} - {brands_df['Year'].max()}")
    with col2:
        st.subheader("KM's Driven Range")
        n_df = brands_df.rename(columns={"KM's driven":"KM driven"})
        st.markdown(f"##### {n_df['KM driven'].min()} - {n_df['KM driven'].max()}")
    with col3:
        st.subheader("Prices Range")
        st.markdown(f"##### {brands_df['Price'].min()} - {brands_df['Price'].max()}")

    # 1. visualize the Models Distribtion
    st.title(f"{selected_company} Models Distribution")
    fig = px.histogram(brands_df, x="Model", color="Model")
    fig.update_layout(xaxis_title="Given Brand Models", yaxis_title="Counts")
    st.plotly_chart(fig)

    # 2. Mean of Prices
    st.title(f"{selected_company} Models Mean Prices")
    mean_distances = brands_df.groupby(["Model"])["Price"].mean().reset_index().sort_values(by="Price")
    st.table(mean_distances)
    # visualize it
    fig = px.line(mean_distances, x='Model', y="Price", markers=True, color_discrete_sequence=px.colors.qualitative.Set2)
    fig.update_layout(xaxis_title="Car Brands", yaxis_title="Mean Prices")
    st.plotly_chart(fig)

    # 3. Mean of KM's driven distances
    st.title(f"{selected_company} Models Mean KM's driven distances")
    mean_distances = brands_df.groupby(["Model"])["KM's driven"].mean().reset_index().sort_values(by="KM's driven")
    st.table(mean_distances)
    # visualize it
    fig = px.line(mean_distances, x='Model', y="KM's driven", markers=True, color_discrete_sequence=px.colors.qualitative.Set2)
    fig.update_layout(xaxis_title="Car Brands", yaxis_title="Mean Distance Covered")
    st.plotly_chart(fig)

    # 4. Prices Distribution
    st.title("Price Distribution with KDE")
    fig, ax = plt.subplots()
    ax = sns.histplot(brands_df['Price'], kde=True, color='skyblue', bins=10)
    ax.set_xlabel('Price')
    ax.set_ylabel('Count')
    st.pyplot(fig)

    # 5. Years Distribution
    st.title(f"{selected_company} Models Years Distribution")
    df_sorted_years = brands_df.sort_values(by="Year")
    fig = px.histogram(df_sorted_years, x="Year", color="Year")
    fig.update_layout(xaxis_title="Year", yaxis_title="Count")
    st.plotly_chart(fig)

    # 6. Fuel Type Distribution
    st.title(f"{selected_company} Models Fuel Type Distribution")
    table_df = brands_df["Fuel"].value_counts().reset_index(name="Count") # showing table also
    st.table(table_df)
    fig = px.pie(brands_df, names="Fuel", hole=0.5, opacity=0.82)
    st.plotly_chart(fig)

    # 7. Transmission Distribution
    st.title(f"{selected_company} Models Transmission Distribution")
    table_df = brands_df["Transmission"].value_counts().reset_index(name="Count") # showing table also
    st.table(table_df)
    fig = px.pie(brands_df, names="Transmission", hole=0.5, opacity=0.82)
    st.plotly_chart(fig)

    # 8. Car Documents Distribution
    st.title(f"{selected_company} Models Car Documents Distribution")
    table_df = brands_df["Car documents"].value_counts().reset_index(name="Count") # showing table also
    st.table(table_df)
    fig = px.pie(brands_df, names="Car documents", hole=0.5, opacity=0.82)
    st.plotly_chart(fig)

    # 9. Assembly Distribution
    st.title(f"{selected_company} Models Assembly Distribution")
    table_df = brands_df["Assembly"].value_counts().reset_index(name="Count") # showing table also
    st.table(table_df)
    fig = px.pie(brands_df, names="Assembly", hole=0.5, opacity=0.82)
    st.plotly_chart(fig)

    # 10. Word Cloud of Car Features
    st.title(f"{selected_company} Models Car Features WordCloud")
    wordcloud = WordCloud(width=1000, height=600, background_color='black').generate(' '.join(brands_df["Car Features"]))
    # plot wordcloud with matplotlib
    fig, ax = plt.subplots()
    ax.imshow(wordcloud, interpolation='bilinear')
    ax.axis('off')
    st.pyplot(fig)

    # 11. Models Across Years
    st.title("Model-wise Sales Across Years")
    models_over_years = helper.models_sales_over_years(brands_df)
    st.table(models_over_years)
    # visualize it
    st.subheader("Visualization:")
    fig = px.line(models_over_years, x='Years', y='Models', markers=True, color_discrete_sequence=px.colors.qualitative.Set2)
    fig.update_layout(xaxis_title='Year', yaxis_title='Car Models')
    st.plotly_chart(fig)

    # 12. Top 5 Cities where sellers are more
    st.title(f"Top 5 Cities Where More Sellers Exist of {selected_company} Models")
    more_sellers_df = helper.cities_where_more_sellers(brands_df)
    more_sellers_df = more_sellers_df.head(5)
    st.table(more_sellers_df)
    # visualize it
    st.subheader("Visualization:")
    fig = px.line(more_sellers_df, x="Seller City", y="count", markers=True, color_discrete_sequence=px.colors.qualitative.Set2)
    fig.update_layout(xaxis_title="Cities", yaxis_title="Sellers Count")
    st.plotly_chart(fig)

    # 13. Highest Price Car Brands
    st.title(f"Top 5 Highest Price Cars in {selected_company}")
    highest_prices = brands_df.sort_values(by="Price", ascending=False).head(5).reset_index(drop=True)[["Ad ID","Make","Model","Year","Price","KM's driven","Seller Location"]].sort_values(by="Price").reset_index(drop=True)
    st.dataframe(highest_prices.head(5))

    # 14. Lowest Price Car Brands
    st.title(f"Top 5 Lowest Price Cars in {selected_company}")
    lowest_prices = brands_df.sort_values(by="Price").head(5).reset_index(drop=True)[["Ad ID","Make","Model","Year","Price","KM's driven","Seller Location"]].sort_values(by="Price").reset_index(drop=True)
    st.dataframe(lowest_prices.head(5))

    # 15. Relationship between Year, Price, KM's driven
    st.title("Year vs Price vs KM's driven")
    fig1 = px.scatter_3d(brands_df, x="Year", y="Price", z="KM's driven", color="KM's driven", color_continuous_scale='Viridis')
    st.plotly_chart(fig1)

        
if user_menu == "Model-wise Analysis":
        st.title("Model-wise Analysis")

        # select the brand
        brands = sorted(df["Make"].unique().tolist())
        selected_company = st.selectbox("Select a Brand:", brands)
        
        st.subheader("Select Model to see in which cities that Model is Saled")
        brands_df = df[df["Make"] == selected_company]
        models_df = brands_df["Model"].unique().tolist()
        selected_model = st.selectbox("Select a Model:", models_df)
        
        cities = brands_df[brands_df["Model"]==selected_model]["Seller City"].value_counts().reset_index(name="Count")
        st.table(cities)
        # visualize it
        st.subheader("Line Plot")
        fig = px.line(cities, x="Seller City", y="Count", markers=True, color_discrete_sequence=px.colors.qualitative.Set2)
        fig.update_layout(xaxis_title="Cities", yaxis_title=f"{selected_model} Cities Count")
        st.plotly_chart(fig)

        st.subheader("Bar Plot")
        fig = px.bar(cities, x="Seller City", y="Count", color="Seller City")
        fig.update_layout(xaxis_title="Cities", yaxis_title=f"{selected_model} Cities Count")
        st.plotly_chart(fig)


if user_menu == "City-wise Analysis":
        st.title("City-wise Analysis")
        # select the city
        cities = sorted(df["Seller City"].unique().tolist())
        selected_city = st.selectbox("Select a City:", cities)

        cities_df = df[df["Seller City"] == selected_city]

        # Distribution of Brands in given city
        st.header(f"Brands Distribution in {selected_city}")
        brands_distribution = cities_df["Make"].value_counts().reset_index(name="Counts")
        fig = px.bar(brands_distribution, x="Make", y="Counts", color="Make")
        st.plotly_chart(fig)

        # st.subheader("Select Model to see in which cities that Model is Saled")
        st.header(f"Models Distribution in {selected_city}")
        models_of_city = cities_df["Model"].value_counts().reset_index(name="Count")
        st.table(models_of_city)
        # visualize it
        st.subheader("Line Plot")
        fig = px.line(models_of_city, x="Model", y="Count", markers=True, color_discrete_sequence=px.colors.qualitative.Set2)
        fig.update_layout(xaxis_title="Cities", yaxis_title="Models Count")
        st.plotly_chart(fig)

        st.subheader("Bar Plot")
        fig = px.bar(models_of_city, x="Model", y="Count", color="Model")
        fig.update_layout(xaxis_title="Cities", yaxis_title="Models Count")
        st.plotly_chart(fig)
