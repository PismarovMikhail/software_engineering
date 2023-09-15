# *PROJECT App ResNet50. Predict image*

## Table of contents

### 1. Description
### 2. What kind of case we're solving?
### 3 Implementation requirements
### 4. Data summary
### 5. Aim to learn how to...
### 6. Composition of the project
### 7. Results 



### 1 Description:

*Develop API machine learning application and deploy it in the cloud.*


### 2 What kind of case we're solving?

*Predict Predict the image of a rhinoceros beetle, dung beetle, whisker* *beetle or tiger beetle using the ResNet50 neural network.*
*ResNet50 is a CNN that has 50 core layers (convolutional + fully* *connected). ResNet50 was developed at Microsoft in 2015 to solve the* *image recognition problem. This Machine Learning model is also trained* *on more than 1 million images from the ImageNet database.*

[About ResNet 50](https://keras.io/api/applications/resnet/)


### 3. Implementation requirements

#### 3.1 Source code must reside in a GitHub repository.
#### 3.2 CI processes must be configured in the GitHub repository.
#### 3.3 CI processes must necessarily include:
#### Running unit tests.
#### Checking code style for PEP8 compliance.
#### 3.4 Application feature development should be done in separate branches.
#### 3.5 Code Review should be performed when merging a branch into the main repository.
#### 3.6 The application code must conform to PEP8 style and clean code rules. 
#### 3.7 The project may use a pre-trained model. It is not required to train your own model.
#### 3.8 Deployment of the application to a cloud platform must be configured. 


### 4. Data summary

The ImageNet dataset contains 14,197,122 annotated images according to the WordNet hierarchy. Since 2010 the dataset is used in the ImageNet Large Scale Visual Recognition Challenge (ILSVRC), a benchmark in image classification and object detection. The publicly released dataset contains a set of manually annotated training images. 

[More about Imagenet](https://www.image-net.org/)

[More about Imagenet 2](https://ru.wikipedia.org/wiki/ImageNet)


### 5 Aim to learn how to...

#### 5.1 Use flake8 linter for automatic code quality checking in the process of Continuous Integration.
#### 5.2 Create pull request
#### 5.3 Analyse the code and perform refactoring
#### 5.4 Make changes to the repository on GitHub and code-review the changes.


### 6 Composition of the project

*Files: app.py, test_app.py, requirements.txt, README.md*

### 7 Results 

*The prediction results are the names of the three*
*best-fit classes with an indicdtion of the prediction*
*probability.*

*Created an API application using the modern,* 
*fast (high-performance) FastAPI web framework*

[About FastAPI](https://fastapi.tiangolo.com/ru/)



