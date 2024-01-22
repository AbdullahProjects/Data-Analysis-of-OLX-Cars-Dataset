# Data Analysis of OLX-Cars Dataset

Welcome to the project of Data Analysis of OLX Cars Dataset. This project is designed to get useful insights from dataset. The [OLX Cars dataset](https://www.kaggle.com/datasets/abdullahkhanuet22/olx-cars-dataset) is avaiable on Kaggle, I personally scraped it using BeautifulSoup and Requests Libraries in Python. 

## Live Demo:

See Project in Streamlit Webapp: https://data-analysis-olx-cars-dataset.streamlit.app/

## About this Project:

### Motivation:

Today each company or business generating whole amount of data whether from its services or from products. These companies want to grow their income and profit. That's why they need suggestions to do something that will really benefit their company revenues. These suggestions can only get from hidden patterns of data. Data Analytics demand is growing day by day. Also, for building Machine Learning Models, it is important to first analyze the data that help us to find and remove unnecessary columns or rows for enhancing the performance of Model.

### Dataset I used?

[OLX Cars dataset](https://www.kaggle.com/datasets/abdullahkhanuet22/olx-cars-dataset): Contains 9000+ records of used cars in Pakistan that owners want to sale.

### Tools:

I use following tools to develop this whole project:

- Jupyter Notebook
- Streamlit
- Pandas
- Matplotlib
- Seaborn
- Plotly
- WordCloud (for analyzing text column)

### Project Development Steps:

1. **Download Dataset:** Download the dataset from Kaggle.
2. **Preprocessing:** Cleaning the dataset, Feature Construction and Removing Unnecessary Columns.
3. **Perform Analysis on Jupyter Notebook:** I first try to analyze roughly on Jupyter Notebook, then create Streamlit Webapp for better user interctions.
4. **Analyzing Dataset into 3 categories:** This step helps to analyze data more effeciently.
   - **Step 1:** Overall Analysis
   - **Step 2:** Brands-wise Analysis
   - **Step 3:** Model-wise Analysis
   - **Step 4:** City-wise Analysis
5. **Create Streamlit Webapp:** After analyzing whole dataset, finally I create Streamlit Webapp for better user interactions.

### Learning Outcomes:

- Handle and Clean Dataset for Analysis.
- Capability to understand dataset.
- Selecting right visuals for analyzing data.
- Better command on visualization tools such as Seaborn, Plotly.
- Able to create beautiful Streamlit Webapp.
- Identifying and Resolving errors from project development to deployment.
- Project Deployment
- Project Organizing
- Continous Learning


### How to Run on Your Machine

1. **Clone the Repository:** Download all files and folders from this repository.
2. **Create Virtual Environment:**
   ```bash
   py -3 -m venv virtualEnv
3. **Run this command:**
   ```bash
   pip freeze > requirements.txt
4. **Finally start the streamlit app:** Run the following command on command terminal.
   ```bash
   streamlit run streamlit_app.py
