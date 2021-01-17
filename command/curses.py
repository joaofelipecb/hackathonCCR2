from sqlalchemy import create_engine
import pymysql
import re
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import nltk
nltk.download('stopwords')
nltk.download('wordnet')
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

database = {}
database['user'] = 'root'
database['password'] = ''
database['host'] = 'localhost'
database['database'] = 'eivizinho'

#database = data.config.get_config('database')
db_connection_str = 'mysql+pymysql://'+database['user']+':'+database['password']+'@'+database['host']+'/'+database['database']
db_connection = create_engine(db_connection_str)

df = pd.read_sql('SELECT * FROM negocio', con=db_connection)

X, y = list(df[['negocio_descricao']]['negocio_descricao']), list(df[['negocio_nome']]['negocio_nome'])

documents = []

stemmer = WordNetLemmatizer()

for sen in range(0, len(X)):
    # Remove all the special characters
    document = re.sub(r'\W', ' ', str(X[sen]))
    
    # remove all single characters
    document = re.sub(r'\s+[a-zA-Z]\s+', ' ', document)
    
    # Remove single characters from the start
    document = re.sub(r'\^[a-zA-Z]\s+', ' ', document) 
    
    # Substituting multiple spaces with single space
    document = re.sub(r'\s+', ' ', document, flags=re.I)
    
    # Removing prefixed 'b'
    document = re.sub(r'^b\s+', '', document)
    
    # Converting to Lowercase
    document = document.lower()
    
    # Lemmatization
    document = document.split()

    document = [stemmer.lemmatize(word) for word in document]
    document = ' '.join(document)
    
    documents.append(document)

vectorizer = CountVectorizer(max_features=100, min_df=2, max_df=0.2, stop_words=stopwords.words('portuguese'))

X = vectorizer.fit_transform(documents).toarray()

tfidfconverter = TfidfTransformer()
X = tfidfconverter.fit_transform(X).toarray()

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

classifier = RandomForestClassifier(n_estimators=100, random_state=0)
classifier.fit(X_train, y_train)

y_pred = classifier.predict(X_test)

print(y_pred)
print(y_test
)