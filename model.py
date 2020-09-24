import tensorflow as tf
import numpy as np


class Model:
    def __init__(self, train_flag, settings):
        self.model_path = settings.model_path # Place to save/load model to/from

        if train_flag:
            self.load_train_data()
            self.prepare_train_data()
            self.train_model()
            self.test_model()
            self.save_model()
        else:
            self.load_model()

    def load_model(self):
        self.model = tf.keras.models.load_model(self.model_path)
        print('Model Loaded!')

    def save_model(self):
        self.model.save(self.model_path)
        print('Model Saved!')

    def load_train_data(self):
        mnist = tf.keras.datasets.mnist
        (self.x_train, self.y_train), (self.x_test, self.y_test) = mnist.load_data()
        print('Loaded Training Data')

    def prepare_train_data(self):
        self.x_train = self.x_train/255.0
        self.x_test = self.x_test/255.0
        self.x_train = np.rint(self.x_train).astype(int).reshape(self.x_train.shape[0], -1)
        self.x_test = np.rint(self.x_test).astype(int).reshape(self.x_test.shape[0], -1)
        print('Prepared Training Data')

    def train_model(self):
        self.model = tf.keras.models.Sequential()

        # self.model.add(tf.keras.layers.Flatten())
        self.model.add(tf.keras.layers.Dense(128, activation=tf.nn.relu, input_shape=self.x_train.shape[1:]))
        self.model.add(tf.keras.layers.Dense(128, activation=tf.nn.relu))
        self.model.add(tf.keras.layers.Dense(10, activation=tf.nn.softmax))

        self.model.compile(optimizer='adam',
                      loss='sparse_categorical_crossentropy',
                      metrics=['accuracy'])

        self.model.fit(self.x_train, self.y_train, epochs=3)
        print('Trained model!')

    def test_model(self):
        val_loss, val_acc = self.model.evaluate(self.x_test, self.y_test)
        print(val_loss)
        print(val_acc)

    def predict_class(self, in_data):
        in_data = in_data.reshape(1, 784)
        prediction = self.model.predict(in_data)
        class_pred = np.argmax(prediction)
        pred_score = np.max(prediction)*100

        return class_pred, pred_score
