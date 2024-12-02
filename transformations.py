import missingno as msno
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from statsmodels.graphics.gofplots import qqplot
import numpy as np
from sklearn.preprocessing import PowerTransformer

class DataTransform:
    
    def convert_to_timedelta(self,df):
       df['administrative_duration']=pd.to_timedelta(df['administrative_duration'], unit='s')
       df['informational_duration']=pd.to_timedelta(df['informational_duration'], unit='s')
       df['product_related_duration']=pd.to_timedelta(df['informational_duration'], unit='s')
       return df

    def convert_to_categorical(self,df):
        columns_to_convert=['administrative','product_related','month','operating_systems','browser','region','traffic_type','visitor_type']
        for col in columns_to_convert:
           df[col]=df[col].astype('category')
        return df
    
    def convert_to_numeric(self,df):
        columns_to_convert=['administrative','administrative_duration','product_related','product_related_duration','informational_duration']
        for col in columns_to_convert:
            df[col]=pd.to_numeric(df[col])
        return df
    
    def impute_nulls(self,df):
       for col in df.select_dtypes(include=['number']).columns:
            df[col]=df[col].fillna(df[col].median())
       for col in df.select_dtypes(include=['category']).columns:
            mode_value=df[col].mode()[0]
            df[col]=df[col].fillna(mode_value)
       return df
   
    def drop_rows(self,df):
       df=df.dropna(subset='operating_systems')
       return df
    
    def correct_skew(self,df):
        numeric_columns=['informational','bounce_rates','exit_rates','page_values']
        for col in numeric_columns:
         if col in ['bounce_rates','exit_rates']:
            df[col]=df[col].map(lambda i: np.log(i) if i > 0 else 0)
         else:
             pt = PowerTransformer(method='yeo-johnson', standardize=True)
             data=df[col]
             data=data.values.reshape((len(data),1))
             df[col]=pt.fit_transform(data)
    
    def remove_outliers(self,df):
         columns=['administrative','administrative_duration','informational','informational_duration','product_related','product_related_duration','bounce_rates','exit_rates','page_values']
         df_cleaned=df.copy()
         for col in columns:
            Q1 = df[col].quantile(0.25)
            Q3 = df[col].quantile(0.75)
            IQR = Q3 - Q1
            lower_bound = Q1 - 1.5 * IQR
            upper_bound = Q3 + 1.5 * IQR
            df_cleaned = df_cleaned[(df_cleaned[col] >= lower_bound) & (df_cleaned[col] <= upper_bound)]
         return df_cleaned
         

        
             
            

    
class DataFrameinfo:

   def describe_columns(self,df):
       return df.dtypes
   
   def extract_statistics(self,df):
       mean=df.mean(numeric_only=True)
       median=df.median(numeric_only=True)
       std=df.std(numeric_only=True)
       return print("Mean:\n",mean.to_dict()),print("Median:\n",median.to_dict()),print("Std:\n",std.to_dict())
   
   def count_distinct_values(self,df):
        value_counts_dict={}
        for col in df:
           value_counts_dict[col]=df[col].value_counts().to_dict
        return value_counts_dict
    
   def get_shape(self,df):
       message=print(f"Dataframe has {df.shape[0]} rows and {df.shape[1]} columns")
       return message
   
   def percentage_nulls(self,df):
        percentage_of_nulls=df.isnull().mean()
        return percentage_of_nulls
   
   def no_of_nulls(self,df):
       return df.isnull().sum()
   
   
       

class Plotter:

 def generate_plot(self,df):
        return msno.bar(df)

 def create_histogram(self,df):
     numeric_columns=['informational','bounce_rates','exit_rates','page_values']
     f = pd.melt(df, value_vars=numeric_columns)
     g = sns.FacetGrid(f, col="variable", col_wrap=2, sharex=False, sharey=False)
     g.map(sns.histplot, "value", kde=True)
     g.set_axis_labels("Value", "Frequency")
     g.set_titles("{col_name}")
     g.tight_layout()
     plt.show()

 def create_qq_plot(self,df):
    numeric_columns=['informational','bounce_rates','exit_rates','page_values']
    for col in numeric_columns:
      qq_plot = qqplot(df[col] , scale=1 ,line='q', fit=True)
      plt.title(f"q-q plot for {col}")
      plt.show()

 def visualise_outliers(self,df):
     columns=['administrative','administrative_duration','informational','informational_duration','product_related','product_related_duration','bounce_rates','exit_rates','page_values']
     fig,axs=plt.subplots(3,3,figsize=(15,15))
     for i, col in enumerate(columns):
       ax = axs[i // 3, i % 3]
       df.boxplot(column=col,ax=ax)
       ax.set_title(f'Boxplot of {col}')
     plt.tight_layout()
     plt.show()

 def create_heatmap(self,df):
     corr_matrix=df.corr(numeric_only=True)
     sns.heatmap(corr_matrix,annot=True, fmt='.2f')
     plt.title('Correlation heatmap of customer_activity dataset')
     plt.show()



