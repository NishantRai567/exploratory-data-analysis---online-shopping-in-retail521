# exploratory-data-analysis---online-shopping-in-retail521
The aim of this project is to conduct exploratory data analysis as part of a large retail company on a dataset of online shopping website activity. With the increasing popularity of online shopping, this dataset provides valuable insights into consumer behaviour.

## Project Details

1. The first stage of the project involves creating the required python classes to extract the online shopping data from the cloud and save it as a csv file.
2. The next step involves performing an exploratory data anlysis(EDA) on the customer_activity dataset. The main objective is to gain a deeper understanding of the data and identify any patterns that may exist. This involves cleaning the data to identify any missing values or incoreectly formatted data. Next, statistical techniques will be applied to gain insight on the data's distribution and visualisation techniques will be used to identify patterns/trends.
3. Now that the dataset has been transformed, the final stage will be to gain deeper insights into the data to identify any patterns/trends that weren't visible by the previous analysis.This will allow management to make more informed decisions about changes to the website and marketing strategies.

## Installation instructions
- Use git clone in the terminal to copy exploratory-data-analysis---online-shopping-in-retail521 from remote to local repository

```bash
git clone https://github.com/NishantRai567/exploratory-data-analysis---online-shopping-in-retail521.git
```

## Usage instructions
- To extract the online shopping dataset, navigate to the db_utils.py and run the python file to extract the dataset from the RDS AWS databse and save it as a csv file

```python
if __name__ == '__main__':
  credentials_dict=get_credentials()
  db_connector=RDSDataBaseConnector(credentials_dict)
  db_connector.extract_from_database(credentials_dict)
  customer_activity=db_connector.create_dataframe()
  save_as_csv(customer_activity)
  dataframe=load_to_dataframe()
```

```bash
python db_utils.py
```
- Next, navigate to the eda.ipynb notebook to run the code containing the EDA for this dataset
- Finally, navigate to the analysis.ipynb notebook to run the code for the in depth analysis of the dataset

## Licensce information
- This project is licesned under the terms of the MIT license

