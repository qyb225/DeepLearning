import numpy as np
from PIL import Image
from core.learning_model import LR, NeuralNetwork
from core.image_model import image_processing

# 1. Data
def load_images_data():
    train_set_x = None
    test_set_x = None
    train_set_y = np.zeros((1, 95))
    test_set_y = np.zeros((1, 17))

    for i in range(55):
        print ('loading: cat_' + str(i) + '.jpg...')
        img = Image.open('./Images/cat/cat_' + str(i) + '.jpg')
        if i == 0:
            train_set_x = image_processing.image_to_vector(img, 75, 100)
        else:
            train_set_x = np.column_stack((train_set_x, image_processing.image_to_vector(img, 75, 100)))
        train_set_y[0][i] = 1

    for i in range(55, 63):
        print ('loading: cat_' + str(i) + '.jpg...')
        img = Image.open('./Images/cat/cat_' + str(i) + '.jpg')
        if i == 55:
            test_set_x = image_processing.image_to_vector(img, 75, 100)
        else:
            test_set_x = np.column_stack((test_set_x, image_processing.image_to_vector(img, 75, 100)))
        test_set_y[0][i - 55] = 1

    for i in range(40):
        print ('loading: other_' + str(i) + '.jpg...')
        img = Image.open('./Images/other/' + str(i) + '.jpg')
        train_set_x = np.column_stack((train_set_x, image_processing.image_to_vector(img, 75, 100)))

    for i in range(40, 49):
        print ('loading: other_' + str(i) + '.jpg...')
        img = Image.open('./Images/other/' + str(i) + '.jpg')
        test_set_x = np.column_stack((test_set_x, image_processing.image_to_vector(img, 75, 100)))

    return train_set_x, train_set_y, test_set_x, test_set_y

def run():
    train_set_x, train_set_y, test_set_x, test_set_y = load_images_data()

    print ("NN2 Run...")
    nn2 = NeuralNetwork.NN(train_set_x, train_set_y, [25, 10, 7], lambda x : x / 255)
    #API:
    #nn.train_model_run(num_iterations = 1001, learning_rate = 0.01, keep_prop = 0.8, lambd = 0.7)

    nn2.train_model_run(3001, 0.01, 0.85, 0.9)
    nn2.predict_model_run(train_set_x, train_set_y)
    nn2.predict_model_run(test_set_x, test_set_y)

run()