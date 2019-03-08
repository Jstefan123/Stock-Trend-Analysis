CREATE TABLE DOW30 (
  ticker VARCHAR(5) NOT NULL,
  twitter_sentiment FLOAT(1,4) NOT NULL,
  news_sentiment FLOAT(1,4) NOT NULL,
  percent_change FLOAT(1,4) NOT NULL,
  insert_date DATE DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY(ticker, insert_date)
);

CREATE TABLE NASDAQ100 (
  ticker VARCHAR(5) NOT NULL,
  twitter_sentiment FLOAT(1,4) NOT NULL,
  news_sentiment FLOAT(1,4) NOT NULL,
  percent_change FLOAT(1,4) NOT NULL,
  insert_date DATE DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY(ticker, insert_date)
);
