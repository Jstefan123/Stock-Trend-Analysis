CREATE TABLE history (
  ticker VARCHAR(5) NOT NULL,
  indx VARCHAR(6) NOT NULL,
  twitter_sentiment FLOAT(1,4) NOT NULL,
  news_sentiment FLOAT(1,4) NOT NULL,
  num_tweets TINYINT(3) NOT NULL,
  num_news TINYINT(3) NOT NULL,
  insert_date DATE DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY(ticker, indx)
);
