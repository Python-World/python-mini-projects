from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import matplotlib.pyplot as plt
import wikipedia
import sys
import warnings
warnings.filterwarnings("ignore")

def gen_cloud(topic):
    try:
        content = str(wikipedia.page(topic).content[:5000])
    except:
        print("Error, try searching something else...")
        sys.exit()
    STOPWORDS.add('==')
    stopwords = set(STOPWORDS)
    wordcloud = WordCloud(stopwords=stopwords, max_words=200, background_color="black", width=600, height=350).generate(content)
    return wordcloud

def save_cloud(wordcloud):
    wordcloud.to_file("./wc.png")

def show_cloud(wordcloud):
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    plt.show()

if __name__ == '__main__':
    topic = input("What do you want to search: ").strip()
    wordcloud = gen_cloud(topic)
    save_cloud(wordcloud)
    desc = input("Do you wish to see the output(y/n): ")
    if desc == 'y':
        show_cloud(wordcloud)
