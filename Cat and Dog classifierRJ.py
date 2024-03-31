#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
import pandas as pd
from tensorflow.keras.preprocessing.image import ImageDataGenerator, load_img
from tensorflow.keras import utils  # to_categorical
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import random
import os
from tensorflow.keras.callbacks import EarlyStopping, ReduceLROnPlateau
import cv2


# In[5]:


FAST_RUN = False
IMAGE_WIDTH=128
IMAGE_HEIGHT=128
IMAGE_SIZE=(IMAGE_WIDTH, IMAGE_HEIGHT)
IMAGE_CHANNELS=3


# In[12]:


filenames = os.listdir(r'C:\Users\91969\Desktop\16271092 (1)\Cat_Dog_Classifiyer\train')
categories = []
for filename in filenames:
    category = filename.split('.')[0]
    print(category)
    
    if category == 'dog':
        categories.append(1)
    else:
        categories.append(0)


# In[16]:


df = pd.DataFrame({
    'filename': filenames,
    'category': categories
})


# In[17]:


df.head()


# In[21]:


df.tail()


# In[11]:


df['category'].value_counts().plot.bar()


# In[24]:


sample = random.choice(filenames)
image = load_img(r'C:\Users\91969\Desktop\16271092 (1)\Cat_Dog_Classifiyer\train\\'+sample)
plt.imshow(image)


# In[25]:


from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Dropout, Flatten, Dense, Activation, BatchNormalization

model = Sequential()

model.add(Conv2D(32, (3, 3), activation='relu', input_shape=(IMAGE_WIDTH, IMAGE_HEIGHT, IMAGE_CHANNELS)))
model.add(BatchNormalization())
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.25))

model.add(Conv2D(64, (3, 3), activation='relu'))
model.add(BatchNormalization())
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.25))

model.add(Conv2D(128, (3, 3), activation='relu'))
model.add(BatchNormalization())
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.25))

model.add(Flatten())
model.add(Dense(512, activation='relu'))
model.add(BatchNormalization())
model.add(Dropout(0.5))
model.add(Dense(2, activation='softmax'))

model.compile(loss='categorical_crossentropy', optimizer='rmsprop', metrics=['accuracy'])

model.summary()


# In[37]:


earlystop = EarlyStopping(patience=10)

learning_rate_reduction = ReduceLROnPlateau(monitor='val_accuracy',
                                            patience=2,
                                            verbose=1,
                                            factor=0.5,
                                            min_lr=0.00001)

callbacks = [earlystop, learning_rate_reduction]


# In[39]:


df.head()


# In[40]:


df["category"] = df["category"].replace({0: 'cat', 1: 'dog'})


# In[43]:


train_df, validate_df = train_test_split(df, test_size=0.20, random_state=42)
print(train_df)


# In[44]:


train_df = train_df.reset_index(drop=True)
validate_df = validate_df.reset_index(drop=True)
print(train_df)


# In[45]:


train_df.shape


# In[46]:


validate_df.shape


# In[58]:


total_train = train_df.shape[0]
total_validate = validate_df.shape[0]
batch_size=15


# In[62]:


train_datagen = ImageDataGenerator(
    rotation_range=15,
    rescale=1./255,
    shear_range=0.1,
    zoom_range=0.2,
    horizontal_flip=True,
    width_shift_range=0.1,
    height_shift_range=0.1)


# In[64]:


train_generator = train_datagen.flow_from_dataframe(
    train_df,
    "C:\\Users\\91969\\Desktop\\16271092 (1)\\Cat_Dog_Classifiyer\\train\\",
    x_col='filename',
    y_col='category',
    target_size=IMAGE_SIZE,
    class_mode='categorical',
    batch_size=batch_size)


# In[65]:


validation_datagen = ImageDataGenerator(rescale=1./255)

validation_generator = validation_datagen.flow_from_dataframe(
    validate_df,
    "C:\\Users\\91969\\Desktop\\16271092 (1)\\Cat_Dog_Classifiyer\\train\\",
    x_col='filename',
    y_col='category',
    target_size=IMAGE_SIZE,
    class_mode='categorical',
    batch_size=batch_size
)


# In[66]:


example_df = train_df.sample(n=1).reset_index(drop=True)
example_generator = train_datagen.flow_from_dataframe(
    example_df,
    "C:\\Users\\91969\\Desktop\\16271092 (1)\\Cat_Dog_Classifiyer\\train\\",
    x_col='filename',
    y_col='category',
    target_size=IMAGE_SIZE,
    class_mode='categorical'
)


# In[67]:


plt.figure(figsize=(12, 12))
for i in range(0, 15):
    plt.subplot(5, 3, i+1)
    for X_batch, Y_batch in example_generator:
        image = X_batch[0]
        plt.imshow(image)
        break
plt.tight_layout()
plt.show()


# In[79]:


epochs=3 if FAST_RUN else 50

history = model.fit(train_generator,
                              epochs=epochs,
                              validation_data=validation_generator,
                              validation_steps=total_validate//batch_size,
                              steps_per_epoch=total_train//batch_size,
                              callbacks=callbacks)
model.save("model.h5")


# In[80]:


fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))
ax1.plot(history.history['loss'], color='b', label="Training loss")
ax1.plot(history.history['val_loss'], color='r', label="validation loss")
ax1.set_xticks(np.arange(1, epochs, 1))
ax1.set_yticks(np.arange(0, 1, 0.1))

ax2.plot(history.history['accuracy'], color='b', label="Training accuracy")
ax2.plot(history.history['val_accuracy'], color='r',label="Validation accuracy")
ax2.set_xticks(np.arange(1, epochs, 1))

legend = plt.legend(loc='best', shadow=True)
plt.tight_layout()
plt.show()


# In[ ]:


for i in range(10):
    all_test_images = os.listdir('C:\Users\91969\Desktop\16271092 (1)\Cat_Dog_Classifiyer\test')
    random_image = random.choice(all_test_images)
    img = cv2.imread(f'C:\Users\91969\Desktop\16271092 (1)\Cat_Dog_Classifiyer\test/{random_image}')
    img = cv2.resize(img,(IMAGE_HEIGHT,IMAGE_WIDTH))

    org = img.copy()
    img = img.reshape(1,128,128,3)

    pred = model.predict(img)
    print(['cat','dog'][int(pred[0][0])])
    cv2.imshow('Live predictions',org)
    cv2.waitKey(0)
cv2.destroyAllWindows()


# In[ ]:




