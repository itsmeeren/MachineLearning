import tensorflow as tf
# from tensorflow import keras
# import matplotlib.pyplot as plt
# from matplotlib import style
import numpy as np
import os
# style.use('fivethirtyeight')

mnist = tf.keras.datasets.mnist# Thhis function creates 28*28 imagehandwritten digits 0-9
(x_train, y_train), (x_test, y_test) = mnist.load_data()#minimalistic datamode

x_train=tf.keras.utils.normalize(x_train,axis=1)

x_test=tf.keras.utils.normalize(x_test,axis=1)

print(x_train[0])
# # Plotting the first training sample
# plt.imshow(x_train[0], cmap='gray')
# plt.axis('off')  # Turn off axis
# plt.show()



#Building the model here
''' -> Its a sequential model layes can be added sequentially ie linear stack of layers
    ->The first layer is flatten layer which flattens the input usuallt when working with
    image data
    ->It transforms the multidimensional data into one dimensional array and fed it into 
    Dense layer,In dense layer each nueron is connected to preseding layer and activation 
    function 'relu'=rectified linear output which introduces non linearity to the network
    ->Finally, this line adds the output layer to the model. It's another Dense layer with 
    10 neurons, which corresponds to the number of classes in your classification task. The 
    activation function used here is softmax,
     which is often used in multi-class classification problems. Softmax function converts the 
     raw output scores into probabilities, ensuring that the sum of the probabilities across all 
     classes is equal to 1. Each neuron in this layer represents the probability of the input belonging to one of the 10 classes.
'''

# Define the model
model = tf.keras.models.Sequential([
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(128, activation=tf.nn.relu),
    tf.keras.layers.Dense(128, activation=tf.nn.relu),
    tf.keras.layers.Dense(10, activation=tf.nn.softmax)
])

# Compile the model
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# Train the model
model.fit(x_train, y_train, epochs=3)

# Ensure the directory exists or provide the full path

# Ensure the directory exists or provide the full path
save_path = "num_reader.keras"
save_dir = os.path.dirname(save_path)
if not os.path.exists(save_dir):
    try:
        os.makedirs(save_dir)
    except OSError as e:
        print("Error: %s - %s." % (e.filename, e.strerror))

# Save the model
try:
    model.save(save_path)
    print("Model saved successfully.")
except IOError as io_err:
    print("Error occurred while saving the model:", io_err)
# Save the model
# model.save(save_path)

# Loading the model
new_model = tf.keras.models.load_model("num_reader.keras")

# Making predictions
predictions = new_model.predict(x_test)
print(np.argmax(predictions[0]))  # Print the prediction for the first test sample




#pannaga
