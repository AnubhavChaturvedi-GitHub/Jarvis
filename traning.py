import tensorflow as tf
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
import numpy as np

# Load your question and answer data from the text file
with open('C:/Users/vlogp/Desktop/J.A.R.V.I.S/Database/qna_logbook.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()

questions = []
answers = []

for line in lines:
    # Use maxsplit=1 to split only at the first occurrence of ':'
    q, a = line.strip().split(':', 1)
    questions.append(q.strip())
    answers.append(a.strip())

# Tokenize the text data
tokenizer = Tokenizer()
tokenizer.fit_on_texts(questions + answers)

vocab_size = len(tokenizer.word_index) + 1

# Create input sequences using the tokenized data
input_sequences = tokenizer.texts_to_sequences(questions)
input_sequences = pad_sequences(input_sequences)

# Create output sequences using the tokenized data
output_sequences = tokenizer.texts_to_sequences(answers)
output_sequences = pad_sequences(output_sequences)

# Create training data
X_train = input_sequences
y_train = np.zeros_like(output_sequences)
y_train[:, :-1] = output_sequences[:, 1:]

# Define the model
model = tf.keras.Sequential([
    tf.keras.layers.Embedding(input_dim=vocab_size, output_dim=50, input_length=X_train.shape[1]),
    tf.keras.layers.LSTM(100),
    # Update the number of neurons in the Dense layer to match the vocabulary size
    tf.keras.layers.Dense(vocab_size, activation='softmax')
])

# Update the loss function based on the nature of your labels
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# Train the model
model.fit(X_train, y_train, epochs=10, verbose=1)

# Save the model
model.save('jarvis_model.h5')

# Save the tokenizer
import pickle
with open('tokenizer.pickle', 'wb') as handle:
    pickle.dump(tokenizer, handle, protocol=pickle.HIGHEST_PROTOCOL)
