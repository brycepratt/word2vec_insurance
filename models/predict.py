from keras.models import Sequential
from keras.layers import Dense
from keras.models import model_from_json
from helper import parse_query
from helper import decode_delivery
from helper import decode_message
import numpy as np
import sys

X = parse_query(sys.argv[0], sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5], sys.argv[6], sys.argv[7], sys.argv[8])

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

print(decode_delivery(delivery),decode_message(message))
