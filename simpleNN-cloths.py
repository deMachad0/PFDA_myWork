# simple neural network using tensor flow to interpret handwritten digits
# Author: Andre

# Importing a custom utilities module (assumes utils.py exists with helper functions)
import utils

# Importing the TensorFlow library and its Keras module for building neural networks
from tensorflow import keras
import tensorflow as tf

# Importing the NumPy library for numerical operations
import numpy as np

# List of class names for the Fashion MNIST dataset, used to map labels to clothing categories
class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
               'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']

# Defining the main function to run the neural network
def run_neural_net():
    # Loading the Fashion MNIST dataset (a set of grayscale images of clothing items)
    fashion_mnist = keras.datasets.fashion_mnist

    # Splitting the dataset into training data (for learning) and testing data (for evaluation)
    (train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()

    # Building the neural network
    model = keras.Sequential([  # Sequential model means layers are stacked one after another
            keras.layers.Flatten(input_shape=(784,1)),  # Input layer: flattens images into a 1D array
            keras.layers.Dense(128, activation='relu'),  # Hidden layer: 128 neurons with ReLU activation
            keras.layers.Dense(10, activation='softmax')  # Output layer: 10 neurons for 10 categories
    ])

    # Compiling the model: setting the optimizer, loss function, and evaluation metrics
    model.compile(optimizer='adam',  # Optimizer: Adam algorithm to adjust weights
                  loss='sparse_categorical_crossentropy',  # Loss function for classification
                  metrics=['accuracy'])  # Metric to track accuracy

    # Training the model with training data for 1 epoch (one complete pass through the data)
    model.fit(train_images, train_labels, epochs=1)

    # Evaluating the model's performance on the test data
    validation_loss, validation_acc = model.evaluate(test_images, test_labels, verbose=1)
    # Printing the validation accuracy and loss
    print(f'Validation accuracy: {validation_acc}\nloss: {validation_loss}')

    # Making predictions on the test dataset
    print('Running Predictions...\n')
    predictions = model.predict(test_images)  # Model outputs probabilities for each category

    # Getting the number of test images for interactive prediction display
    max = len(test_images)  # Total number of test images
    num = utils.get_number(max)  # Get a user-inputted image index from a helper function
    while num != -1:  # Keep running until the user enters -1
        image = test_images[num]  # Get the image at the specified index
        label = test_labels[num]  # Get the true label for the image
        guess = np.argmax(predictions[num])  # Find the category with the highest predicted probability
        # Display the image with its true label and the predicted label
        utils.show_image(image, f"{label} {class_names[label]}" , f"{guess} {class_names[guess]}")
        num = utils.get_number(max)  # Ask the user for another image index

# Run the main function if this script is executed directly
if __name__ == '__main__':
    run_neural_net()
