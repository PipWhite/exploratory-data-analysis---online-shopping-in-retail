# Exploratory Data Analysis - Online Shopping in Retail

## Project Brief  
This is a industry project simulating the role of a data analyst for a large retail company. The task is to conduct data analysis on a dataset of online shopping website activity. With the increasing popularity of online shopping, this dataset provides valuable insights into consumer behaviour.  
Using various statistical and visualisation techniques we will explore data and draw meaningful insights. The analysis will not only provide a better understanding of customer behaviour but also help the business optimise marketing strategies and improve their customer experience.  
The data contains information about the website activity of users over one year. Each sample represents the user interacting with the website during a shopping session.  
Overall, this project will showcase the power of exploratory data analysis in uncovering valuable insights from large datasets and how to leveraged these insights to drive business success.  

## Project Dependencies  
To run this project the following modules need to be installed:  
- `pandas`
- `numpy`
- `matplotlib`
- `seaborn`
- `plotly`
- `scipy`

## The dataset
The following is a decription of the dataset that we will be using in this project.  
- **administrative**: Columns which indicates which administrative activity the user was performing on their account.
- **administrative_duration**: How long a user performed administrative tasks in that session.
- **informational**: Indicates which informational activity the user was performing on the website.
- **informational_duration**: How long a users performed informational tasks in seconds during that session.
- **product_related**: Indicates which product the user was viewing on the website.
- **product_related_duration**: How long a user browsed products during that session. 
- **bounce_rates**: Historical bounce rate of that particular page for all users. They visited the directly and immediately exited.
- **exit_rates**: Historical exit rate of the users from that particular page. 
- **page_values**: The average value contribution of a page to a customer sale
- **month**: Month the users activity took place
- **operating_systems**: Operating system the user was using
- **browser**: The browser used by the user
- **region**: The region the user originated from
- **traffic_type**: How the user was redirected to the site
- **visitor_type**: Whether a customer was is new/returning or other
- **weekend**: Whether the activity only took place during the weekend
- **revenue**: Whether the customer purchased anything that session

## Class creation
The following classes are created for this project however they can be applied to other datasets when needed. They involve data transformations, information gathering, and data plots.  
### DataTransform class

```
class DataTransform:

    def __init__(self, target_dataframe):
        self.target_dataframe = target_dataframe
    
    def column_to_int(self, target_column):
        #converts a column datatype to init64. Returns dataframe
        self.target_dataframe[target_column] = self.target_dataframe[target_column].astype('int64', errors='ignore')
        return self.target_dataframe
    
    def column_to_category(self, target_column):
        #converts column datatype to category. returns dataframe
        self.target_dataframe[target_column] = self.target_dataframe[target_column].astype('category')
        return self.target_dataframe
```
