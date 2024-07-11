
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Creating a custom dataset
sentiment = [
    "I feel really good about this company and its future",
    "I feel good about the company and its future",
    "I don't feel good nor bad about the company and its future",
    "I feel slightly worried about the company and its future",
    "I feel very bad about the company and its future",
]

# Creating our labels
labels = ["Very Positive", "Positive", "Neutral", "Negative", "Very Negative"]

# Creating our TF-IDF vectorizer
tfidf_vectorizer = TfidfVectorizer()

# Transforming the text data into TF-IDF features
tfidf_features = tfidf_vectorizer.fit_transform(sentiment)

# Splitting the data into training and testing sets
x_train, x_test, y_train, y_test = train_test_split(tfidf_features, labels, test_size=0.2, random_state=42)

# Build a logistic regression classifier
classifier = LogisticRegression()

# Train the classifier on the training data
classifier.fit(x_train, y_train)

# Making Predictions on the test data
y_prediction = classifier.predict(x_test)

# Calculate accuracy
accuracy = accuracy_score(y_test, y_prediction)
print("Accuracy:", accuracy)

# predicting a new document
new_document = ["I feel good about working at this company"]
new_tfidf = tfidf_vectorizer.transform(new_document)
predicted_class = classifier.predict(new_tfidf)
print("Predicted class for new document: ", predicted_class[0])
