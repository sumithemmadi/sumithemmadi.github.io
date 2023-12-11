# -*- coding: utf-8 -*-
"""UI20CS21_NLP_LAB5

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1SHTPPK7WWoCFpernwOUAgNDKKyeWRIUJ
"""

!pip install pandas scikit-learn matplotlib nltk tensorflow numpy

import numpy as np
import pandas as pd
import tensorflow as tf
import matplotlib.pyplot as plt
import re
import nltk
from nltk.util import ngrams
from nltk.probability import FreqDist
from nltk.corpus import stopwords
# from nltk.tokenize import word_token
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix, roc_auc_score, roc_curve
from keras.models import Sequential
from keras.layers import Dense
from sklearn.preprocessing import LabelEncoder
import matplotlib.pyplot as plt
from collections import Counter



nltk.download('stopwords')
nltk.download('punkt')
plt.style.use(style='seaborn')

df=pd.read_csv('/content/sample_data/financial_data.csv')
df

def remove_punctuation(text):
    return re.sub(r'[^\w\s]', '', str(text))

df["Sentence"] = df["Sentence"].apply(remove_punctuation)
df

def generate_N_grams(text:str,ngram:int)->str:
  """N-Gram Generating function."""

  words=[word.lower() for word in text.split(" ") if word not in set(stopwords.words('english'))]
  words=[word for word in words if word not in ['',' ']]
  temp=zip(*[words[i:] for i in range(0,ngram)])
  ans=[' '.join(ngram) for ngram in temp]

  return ans

generate_N_grams("The sun rises in the east",2)

df['unigram'] = df["Sentence"].apply(lambda x: generate_N_grams(x, 1))
df['bigram'] = df["Sentence"].apply(lambda x: generate_N_grams(x, 2))
df['trigram'] = df["Sentence"].apply(lambda x: generate_N_grams(x, 3))
df

def ngram_frequency(df, ngram_col='unigram', sentiment='positive'):
    filtered_df = df[df['Sentiment'] == sentiment]

    all_ngrams = [ngram for ngrams_list in filtered_df[ngram_col] for ngram in ngrams_list]
    ngram_counts = Counter(all_ngrams)
    ngram_df = pd.DataFrame(list(ngram_counts.items()), columns=['ngram', 'count'])
    ngram_df = ngram_df.sort_values(by='count', ascending=False).reset_index(drop=True)

    return ngram_df

def plot_top_ngrams(ngram_df, top_n=10, color='green'):
    top_ngrams = ngram_df.head(top_n)

    plt.figure(figsize=(10, 3))
    plt.bar(top_ngrams['ngram'], top_ngrams['count'], color=color)
    plt.xlabel('Ngram')
    plt.ylabel('Count')
    plt.title(f'Top {top_n} Ngrams')
    plt.xticks(rotation=45, ha='right')
    plt.show()

def sentiment_analysis(df, ngram_col, sentiment_col):

    df['text'] = df[ngram_col]
    df['text'] = df['text'].apply(lambda x: ' '.join(x))

    train_df, test_df = train_test_split(df, test_size=0.2, random_state=42)

    vectorizer = TfidfVectorizer()
    X_train = vectorizer.fit_transform(train_df['text'])
    X_test = vectorizer.transform(test_df['text'])

    le = LabelEncoder()
    y_train = le.fit_transform(train_df[sentiment_col])
    y_test = le.transform(test_df[sentiment_col])

    nb_model = MultinomialNB()
    nb_model.fit(X_train, y_train)
    nb_pred = nb_model.predict(X_test)

    svm_model = SVC(probability=True)
    svm_model.fit(X_train, y_train)
    svm_pred = svm_model.predict(X_test)

    rf_model = RandomForestClassifier()
    rf_model.fit(X_train, y_train)
    rf_pred = rf_model.predict(X_test)

    dnn_model = Sequential([
        Dense(64, activation='relu', input_shape=(X_train.shape[1],)),
        Dense(1, activation='sigmoid')
    ])
    dnn_model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    dnn_model.fit(X_train, y_train, epochs=5, batch_size=32, verbose=0)
    dnn_pred = (dnn_model.predict(X_test) > 0.5).astype(int)

    models = ['Naive Bayes', 'SVM', 'Random Forest', 'Deep Neural Network']
    predictions = [nb_pred, svm_pred, rf_pred, dnn_pred]

    for model, pred in zip(models, predictions):
        accuracy = accuracy_score(y_test, pred)
        classification_report_str = classification_report(y_test, pred)
        conf_matrix = confusion_matrix(y_test, pred)
        roc_auc = roc_auc_score(y_test, pred)

        print(f"\033[1m{ngram_col} {model}:\033[0m")
        print(f"\n{ngram_col} {model} Accuracy: {accuracy}")
        print(f"{ngram_col} {model} Classification Report:")
        print(classification_report_str)
        print(f"{ngram_col} {model} Confusion Matrix:")
        print(conf_matrix)
        print(f"{ngram_col} {model} AUC-ROC Score: {roc_auc}")

        fpr, tpr, _ = roc_curve(y_test, pred)
        plt.figure(figsize=(4, 4))
        plt.plot(fpr, tpr, color='darkorange', lw=2, label=f'{model} ROC curve (area = {roc_auc:.2f})')
        plt.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--')
        plt.xlabel('False Positive Rate')
        plt.ylabel('True Positive Rate')
        plt.title(f'{ngram_col} {model} ROC Curve')
        plt.legend(loc="lower right")
        plt.show()

unigram_positive_df = ngram_frequency(df, ngram_col='unigram', sentiment='positive')
unigram_negative_df = ngram_frequency(df, ngram_col='unigram', sentiment='negative')

print("Unigram Sentiment: positive\n",unigram_positive_df)
plot_top_ngrams(unigram_positive_df, top_n=10, color='green')

print("Unigram Sentiment: negative\n",unigram_negative_df)
plot_top_ngrams(unigram_negative_df, top_n=10, color='red')

sentiment_analysis(df, 'unigram', 'Sentiment')

bigram_positive_df = ngram_frequency(df, ngram_col='bigram', sentiment='positive')
bigram_negative_df = ngram_frequency(df, ngram_col='bigram', sentiment='negative')

print("Bigram Sentiment: positive\n",bigram_positive_df)
plot_top_ngrams(bigram_positive_df, top_n=10, color='green')

print("Bigram Sentiment: negative\n",bigram_negative_df)
plot_top_ngrams(bigram_negative_df, top_n=10, color='red')

sentiment_analysis(df, 'bigram', 'Sentiment')

trigram_positive_df = ngram_frequency(df, ngram_col='trigram', sentiment='positive')
trigram_negative_df = ngram_frequency(df, ngram_col='trigram', sentiment='negative')

print("Trigram Sentiment: positive\n",trigram_positive_df)
plot_top_ngrams(trigram_positive_df, top_n=10, color='green')

print("Trigram Sentiment: negative\n",trigram_negative_df)
plot_top_ngrams(trigram_negative_df, top_n=10, color='red')

sentiment_analysis(df, 'trigram', 'Sentiment')