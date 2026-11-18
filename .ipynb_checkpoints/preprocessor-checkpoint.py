import nltk

nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('vader_lexicon')
nltk.download('punkt')
nltk.download('punkt_tab')

from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
import re

def process_review(review):
    # Covert review into lowercase form
    review_lower=review.lower()

    # Remove punctuations,numbers
    review_puncs_nums_removed = re.sub(r"[^a-z\s]","",review_lower)

    # Tokenize the review : covert the sentence into words
    review_tokens = word_tokenize(review_puncs_nums_removed)

    #Remove stop words
    stop_words = stopwords.words('English')
    review_tokens_stopwords_removed = [token for token in review_tokens if token not in stop_words]

    #Lemmatization
    lemmatizer = WordNetLemmatizer()
    lemmatized_tokens = [lemmatizer.lemmatize(token, pos='n') for token in review_tokens_stopwords_removed]

    # Put all the tokens in the single string object 
    return"  ".join(lemmatized_tokens)

if __name__ == "__main__":
    review = "The product was really nice!!!"
    print(process_review(review))

