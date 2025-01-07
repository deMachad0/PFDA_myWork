

# Importing TensorFlow, a machine learning library
import tensorflow as tf

# Importing Keras from TensorFlow, which is used for building neural networks
from tensorflow import keras

# Importing NumPy, a library for numerical computations
import numpy as np

# Importing Matplotlib, a library for creating plots and visualizations
import matplotlib.pyplot as plt


# Function to display an image along with its label and predicted guess
def show_image(data, label, guess):
    # Converting the input image data into a TensorFlow variable for processing
    tensor = tf.Variable(data, dtype=tf.float32)

    # Reshaping the tensor into a 28x28 grid to match the original image dimensions
    img = tf.reshape(tensor, [28, -1])  # '-1' means automatically calculate the other dimension

    # Creating a new figure for the image plot
    plt.figure()

    # Displaying the image in grayscale using Matplotlib
    plt.imshow(img, cmap=plt.cm.binary)  # 'binary' creates a black-and-white colormap

    # Adding a title to the plot to show the expected (true) label
    plt.title(f"Expected: {label}")

    # Adding a label below the image to show the predicted guess
    plt.xlabel(f"Guess: {guess}")

    # Adding a color bar to the side of the image (optional)
    plt.colorbar()

    # Disabling the gridlines for a cleaner display
    plt.grid(False)

    # Displaying the image plot
    plt.show()


# Function to get a number input from the user, with validation
def get_number(max):
    # Start an infinite loop to repeatedly ask for input until valid or quit
    while True:
        # Asking the user to input a number
        num = input("Pick a number (non a digit to quit): ")

        # Checking if the input is a valid digit
        if num.isdigit():
            # Converting the input string into an integer
            num = int(num)

            # If the number is within the allowed range, return it
            if num <= max:
                return int(num)

            # If the number is too large, ask the user to try again
            else:
                print(f"Try again...less than {max}")
        else:
            # If the input is not a digit, return -1 to indicate quitting
            return -1
