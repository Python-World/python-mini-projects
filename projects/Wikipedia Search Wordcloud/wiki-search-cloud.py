from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import matplotlib.pyplot as plt
import wikipedia
import sys
import warnings
# supressing unnecessary warnings
warnings.filterwarnings("ignore")


# function to search the wikipedia article and generate the wordcloud
def gen_cloud(topic):
    try:
        content = str(wikipedia.page(topic).content)
    except:
        print("Error, try searching something else...")
        sys.exit()
    STOPWORDS.add('==')
    stopwords = set(STOPWORDS)
    wordcloud = WordCloud(stopwords=stopwords, max_words=200, background_color="black", width=600, height=350).generate(content)
    return wordcloud


# function to save the wordcloud to current directory
def save_cloud(wordcloud):
    wordcloud.to_file("./wordcloud.png")


# function to display the wordcloud with matplotlib
def show_cloud(wordcloud):
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    plt.show()


# driver code
if __name__ == '__main__':
    topic = input("What do you want to search: ").strip()
    wordcloud = gen_cloud(topic)
    save_cloud(wordcloud)
    print("Wordcloud saved to current directory as wordcloud.png")
    desc = input("Do you wish to see the output(y/n): ")
    if desc == 'y':
        show_cloud(wordcloud)
    sys.exit()
