from database import *
from matplotlib import pyplot
import numpy

# given an array data for a single stock from database, create a line graph
def createLineGraph(data):

    # put the info in each entry into respective array
    dates = []
    news_sent = []
    twitter_sent = []
    num_news = []
    num_tweets = []
    for entry in data:
        twitter_sent.append(entry[1])
        news_sent.append(entry[2])
        num_tweets.append(entry[3])
        num_news.append(entry[4])
        dates.append(entry[5])

    # create the X axis data
    dates = numpy.array(dates)

    # create y axis arrays
    y_stack = numpy.row_stack((news_sent, twitter_sent, num_news, num_tweets))

    # create the plot
    fig = pyplot.figure(figsize=(11,8))
    graph = fig.add_subplot(111)

    # plot each respecive category
    graph.plot(dates, y_stack[0,:], label='News Sentiment', color='r', marker='o')
    graph.plot(dates, y_stack[1,:], label='Twitter Sentiment', color='b', marker='o')
    graph.plot(dates, y_stack[2,:], label='Number of News Articles', color='g', marker='o')
    graph.plot(dates, y_stack[3,:], label='Number of Tweets', color='c', marker='o')

    # label x axis
    pyplot.xticks(dates)
    pyplot.xlabel('Date')

    # create legend and turn graph lines on
    handles, labels = graph.get_legend_handles_labels()
    legend = graph.legend(handles, labels, loc='upper center', bbox_to_anchor=(1.15,1))
    graph.grid('on')

    # set graph title
    fig.suptitle(entry[0])

    # set the picture save name
    file_name = "test.png"

    plt.savefig(file_name)

    # return the file_name
    return file_name
