from keras.models import Sequential
from keras.layers import Dense
from sklearn.utils import shuffle
from helper import read_data

X, y = read_data('data/data.csv')

X, y = shuffle(X, y, random_state=42)

# create model
model = Sequential()
model.add(Dense(100, input_dim=39, activation='relu'))
model.add(Dense(75, activation='relu'))
model.add(Dense(55, activation='softmax'))
# Compile model
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
model.fit(X, y, epochs=2, batch_size=10, verbose=1)

# serialize model to JSON
model_json = model.to_json()
with open("weights/model.json", "w") as json_file:
    json_file.write(model_json)
# serialize weights to HDF5
model.save_weights("weights/model.h5")
print("Saved model to disk")
