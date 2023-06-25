import tensorflow as tf
from tensorflow import keras
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix
import itertools
import cv2
from skimage import transform
from keras.applications.vgg16 import preprocess_input

def normalize(x):
    return (x.astype(float)/256)


model = keras.models.load_model('models/zetta.h5')

# img_array = cv2.imread('sample.png')
# img_array=np.flip(img_array, axis=-1)
# img_array = cv2.resize(img_array,(40,60),interpolation=cv2.INTER_AREA)
# plt.imshow(img_array)
# plt.show()
# img_array = np.expand_dims(img_array, axis=0)

# sample = keras.preprocessing.image.ImageDataGenerator(preprocessing_function=tf.keras.applications.vgg16.preprocess_input) \
#     .flow(img_array,batch_size=1)
# print(np.shape(img_array))
# print(img_array[10,2,1])
# print(img_array)
# sample=np.squeeze(sample)
#
# print(model.predict(img_array))
# print(np.round(model.predict(img_array)))
#

test_path = 'datasets/Images/small'
test_batches = keras.preprocessing.image.ImageDataGenerator(preprocessing_function=tf.keras.applications.vgg16.preprocess_input) \
.flow_from_directory(directory=test_path, target_size=(20, 30), classes=['1','2','3','4','5'], batch_size=10,shuffle=False)

# test_batches = keras.preprocessing.image.ImageDataGenerator(preprocessing_function=tf.keras.applications.vgg16.preprocess_input) \
#     .flow(img_array)

predictions = model.predict(x=test_batches, steps=len(test_batches), verbose=0)

# print(np.max(predictions))
# print(np.argmax(predictions))
print(np.round(predictions))


def plot_confusion_matrix(cm, classes,
                          normalize=False,
                          title='Confusion matrix',
                          cmap=plt.cm.Blues):
    """
    This function prints and plots the confusion matrix.
    Normalization can be applied by setting `normalize=True`.
    """
    plt.imshow(cm, interpolation='nearest', cmap=cmap)
    plt.title(title)
    plt.colorbar()
    tick_marks = np.arange(len(classes))
    plt.xticks(tick_marks, classes, rotation=45)
    plt.yticks(tick_marks, classes)

    if normalize:
        cm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]
        print("Normalized confusion matrix")
    else:
        print('Confusion matrix, without normalization')

    print(cm)

    thresh = cm.max() / 2.
    for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
        plt.text(j, i, cm[i, j],
            horizontalalignment="center",
            color="white" if cm[i, j] > thresh else "black")

    plt.tight_layout()
    plt.ylabel('True label')
    plt.xlabel('Predicted label')

cm = confusion_matrix(y_true=test_batches.classes, y_pred=np.argmax(predictions, axis=-1))
cm_plot_labels = ['1','2','3','4','5']
plot_confusion_matrix(cm=cm, classes=cm_plot_labels, title='Confusion Matrix')
plt.show()
# # test_batches.class_indices

imgs,labels = next(test_batches)
# imgs=np.squeeze(imgs)
# plt.imshow(imgs)
# plt.show()
def plotImages(images_arr):
    fig, axes = plt.subplots(1, 5, figsize=(20,30))
    axes = axes.flatten()
    for img, ax in zip( images_arr, axes):
        ax.imshow(img)
        ax.axis('off')
    plt.tight_layout()
    plt.show()
#
plotImages(imgs)

# print(labels)


