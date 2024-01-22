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
This class is used to change the data types of rows in a dataframe.  
Taking the dataframe on the calss allows you to use the methods to select the target column that you want to transform.
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

### DataFrameInfo class

```
class DataFrameInfo:
    
    def __init__(self, target_dataframe):
        self.target_dataframe = target_dataframe

    def get_info(self):
        #returns info of the class dataframe
        return self.target_dataframe.info()
    
    def get_column_mean(self, target_column):
        # returns the mean of a selected column
        mean = self.target_dataframe[target_column].mean()
        print(f'Mean of {target_column} is {mean}')
        return mean
    
    def get_column_median(self, target_column):
        # returns the median of a selected column
        median = self.target_dataframe[target_column].median()
        print(f'Median of {target_column} is {median}')
        return median
    
    def get_column_mode(self, target_column):
        # returns the mode of a selected column
        mode = self.target_dataframe[target_column].mode()
        print(f'Mode of {target_column} is {mode}')
        return mode
    
    def get_standard_deviation(self):
        # returns the standard deviation of a selected column
        standard_deviation = self.target_dataframe.std(numeric_only=True)
        return standard_deviation
    
    def get_variance(self):
        # returns the variance of a selected column
        variance = self.target_dataframe.var(numeric_only=True)
        return variance

    def count_distinct_categories(self, target_column):
        # returns the number of distinct categories in a category column
        distinct_categories = self.target_dataframe[target_column].nunique()
        print(f'{distinct_categories} distinct categories in {target_column}')
        return distinct_categories
    
    def get_shape(self):
        # returns the shape of the class dataframe
        df_shape = self.target_dataframe.shape
        return df_shape
    
    def count_null(self):
        # returns a dataframe of the sum of nulls in each column of the class dataframe
        null_count = self.target_dataframe.isnull().sum()
        return null_count

    def null_percentage(self):
        # returns a dataframe of the percentage of nulls in in column of the class dataframe
        percent_null = self.target_dataframe.isnull().sum()/len(self.target_dataframe)
        return percent_null
    
    # D'Agostino's K^2 Test
    def normal_test(self, target_column):
        # returns the normality of a column in the class dataframe
        stat, p = normaltest(self.target_dataframe[target_column], nan_policy='omit')
        print('Statistics=%.3f, p=%.3f' % (stat, p))
    
    def describe_column(self, target_column):
        description = self.target_dataframe[target_column].describe()
        return description
    
```

### Plotter class

```
class Plotter:

    def __init__(self, target_dataframe):
        self.target_dataframe = target_dataframe

    def create_hist(self, target_column):
        # plots a histogram of a selected column
        hist = self.target_dataframe[target_column].hist(bins=20)
        return hist
    
    def create_qqplot(self, target_column):
        # plots a qqplot of a selected column
        qq = plt.show( qqplot(self.target_dataframe[target_column], scale=1 , line='q'))
        return qq

    def show_skew(self, target_column):
        self.target_dataframe[target_column].hist(bins=20)
        skew_value = self.target_dataframe[target_column].skew()
        print(f'The skew of {target_column} is: {skew_value}')

    def scatter_plot(self, x_axis, y_axis):
        sns.scatterplot(x=self.target_dataframe[x_axis], y=self.target_dataframe[y_axis])

    def box_plot(self, target_column):
        column = self.target_dataframe[target_column]
        value_set = column.unique()
        plt.figure(figsize=(10, 5))
        sns.boxplot(y=column, color='lightgreen', showfliers=True)
        sns.swarmplot(y=value_set, color='black', size=5)
```

### DataFrameTransform class

```
class DataFrameTransform:

    def __init__(self, target_dataframe):
        self.target_dataframe = target_dataframe

    def drop_column(self, target_column):
        # removes a whole column
        self.target_dataframe = self.target_dataframe.drop(target_column, axis='columns')
        return self.target_dataframe
    
    def drop_missing_values_in_column(self, target_column):
        # used to remove all rows with missing values in a specific column
        # only used when the number of missing values in a column is low
        self.target_dataframe = self.target_dataframe.dropna(subset=[target_column])
        return self.target_dataframe
    
    def median_imputation(self, target_column):
        # changes all null values in a column to the column median
        # used when the data has a non guassian/normal distribution
        self.target_dataframe[target_column] = self.target_dataframe[target_column].fillna(self.target_dataframe[target_column].median())
        return self.target_dataframe
    
    def mean_imputation(self, target_column):
        # changes all null values in a column to the column mean
        # used when the data has a guassian/normal distribution
        self.target_dataframe[target_column] = self.target_dataframe[target_column].fillna(self.target_dataframe[target_column].mean())
        return self.target_dataframe
    
    def categorical_imputation_mode(self, target_column):
        # changes all null values in a column to the most common category
        most_freq_cat = self.target_dataframe[target_column].mode()[0]
        self.target_dataframe[target_column] = self.target_dataframe[target_column].fillna(most_freq_cat)
        return self.target_dataframe
    
    def log_transform(self, target_column):
        log_column = self.target_dataframe[target_column].map(lambda i: np.log(i) if i > 0 else 0)
        t=sns.histplot(log_column,label="Skewness: %.2f"%(log_column.skew()))
        t.legend()
        self.target_dataframe[target_column] = log_column
        return self.target_dataframe
    
    def add_z_score(self, target_column):
        mean = self.target_dataframe[target_column].mean()
        std = self.target_dataframe[target_column].std()
        z_score = (self.target_dataframe[target_column] - mean) / std
        self.target_dataframe[f'{target_column}_z_score'] = z_score
        return self.target_dataframe

    def remove_z_score_outliers(self, target_column):
        self.target_dataframe = self.target_dataframe.drop(self.target_dataframe[self.target_dataframe[f'{target_column}_z_score'] >= 3].index)
        self.target_dataframe = self.target_dataframe.drop(self.target_dataframe[self.target_dataframe[f'{target_column}_z_score'] <= -3].index)
        self.target_dataframe = self.target_dataframe.drop([f'{target_column}_z_score'], axis=1)
        return self.target_dataframe

```


















