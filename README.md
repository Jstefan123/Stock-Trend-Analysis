# Stock Sentiment Analysis
### Supports socks listed in the DOW30 and NASDAQ100 indices

### Fetching Data (every 24 hours)
###### Uses Twitter Developer API to fetch up to 100 tweets that match a stock
###### Uses NewsAPI.org to fetch all articles published in the past 24 hours that match a stock


### Sentiment Analysis
###### Each body of text is analyzed independently using Natural Language Processing
###### Utilizing sentiment analyisis, a body of text is assigned a polarity rating [-1,1]
###### -1 = very negative, 0 = neutral, 1 = very positive
###### Each rating for a stock is summed and the total is divided by the number of results to calculate an average polarity rating for that day
###### The data for each stock is stored in an SQL database in the corresponding index's table with the respective date of insertion

### Plots (matplotlib.pyplot)
###### Each stock's historical data is represented by a graph in the respective index's folder
###### Each graph contains an average polarity rating vs data line graph and a number of results vs date line graph
###### Each plot is updated with the new data every time data is inserted into SQL database


