#### Explorative Data Analysis

Get data into a usable format!  
Find out if the following predictive modeling phase will be successful!

- Combine everything into a single big table
  - Convert files to .csv
  - Merge files
  - Fix encoding issues
  - Clean column names (english, no whitespace, no special chars)
  - Are there duplicate columns?
  - Fix datatypes (datetime, int, float, string)
- Look at the raw data
  - Sort data
  - Filter data by various criteria
- Investigation
  - Non-sensical observations/artifacts?
  - Coding of categorical features?
  - Missing values?
  - Outliers?
  - Constant values (=Zero Importance)?
  - Low importance features?
  - Collinear, correlated or otherwise dependent features?
  - Highly skewed features?
  - Irrelevant features?
- Univariate Analysis
  - Look at mean, median, min, max, std, iqr, quantiles (1%, 5%, 25%, 50%, 75%, 95%, 99%)
  - Draw boxplots, histograms
- Multivariate Analysis
  - Draw scatter plots
  - Create correlation matrix
- Time Series? -> Plot variables over time
- Fixing issues
  - Impute missing values (mode, median, mean)
  - Remove variables that have too many missings
  - Remove observations that have too many missings
  - Select appropriate time slice
- Preparation
  - Clip values that are too small/too large
  - Scale to [0,1] or normalize (mean=0, std=1)
  - One-hot encoding(1 for yes 0 for no), Label Encoding (0,1,2,3)
  - Create log-transformed versions for highly skewed variables
  - Create binned versions for variables (example is to bin values for Age into     categories such as 20-39, 40-59, and 60-79)
  - Combine categories for highly skewed categorical variables
  - Create sum/difference/product/quotient of variables
  - Create polynomial features
