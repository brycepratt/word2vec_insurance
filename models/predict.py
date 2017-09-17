from keras.models import Sequential
from keras.layers import Dense
from keras.models import model_from_json
from helper import parse_query
import numpy as np

X = parse_query()

# load json and create model
json_file = open('model.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
loaded_model = model_from_json(loaded_model_json)
# load weights into new model
loaded_model.load_weights("model.h5")

loaded_model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
temp_one_hot = loaded_model.predict(X)
temp_index = np.argmax(temp_one_hot)

delivery = temp_index % 5
message = temp_index // 5
