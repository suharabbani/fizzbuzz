
from ekphrasis.classes.segmenter import Segmenter
from wordcloud import WordCloud

#Reads label mapping into dictionary
def get_mapping(path):
    mapping = {}
    with open(path) as fh:
        for line in fh:
            key, label = line.strip().split(None, 1)
            mapping[key] = label.strip()
    return mapping

seg_tw = Segmenter(corpus='twitter')

def serialize(df):
    list_of_words=[]
    for line in df:
        if line != []:
            for word in line:
                list_of_words.append(word)
    return list_of_words

def grab_hashtags(df):
    hashtags=[]
    segmented_hashtags=[]
    for line in df:
        if line != []:
            for word in line:
                hashtags.append(word)
                segment_word = seg_tw.segment(word)
                segment_word = segment_word.split()
                for sw in segment_word:
                    segmented_hashtags.append(sw)
    return [hashtags, segmented_hashtags] 

def create_word_clouds(words):
    unique_string=(" ").join(words)
    wordcloud = WordCloud(width = 5000, height = 1000).generate(unique_string)
    return wordcloud