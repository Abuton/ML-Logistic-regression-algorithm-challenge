#!/usr/bin/env python
# coding: utf-8

# In[1]:


# the main library to build the algorithm
import numpy as np
# for visualization after fitting the algorithm
import matplotlib.pyplot as plt 
# a sample dataset to test the algorithm
import sklearn.datasets as ds


# In[2]:


# the dataset
iris = ds.load_iris()


# In[3]:


# features
X = iris.data[:, :2]
# target
y = (iris.target != 0) * 1


# In[4]:


class LogisticRegression:
    """
    implementation of Logistic Regression from scratch
    """
    def __init__(self, lr=0.01, num_iter=100000, fit_intercept=True, verbose=False):
        self.lr = lr
        self.num_iter = num_iter
        self.fit_intercept = fit_intercept
        self.verbose = verbose
        
    def __add_intercept(self, X):
        intercept = np.ones((X.shape[0], 1))
        return np.concatenate((intercept, X), axis=1)
    
    def __sigmoid(self, z):
        return 1 / (1 + np.exp(-z))
    
    def __loss(self, h, y):
        return (-y * np.log(h) - (1 - y) * np.log(1 - h)).mean()
    
    def fit(self, X, y):
        if self.fit_intercept:
            X = self.__add_intercept(X)
            # weight initialization
            self.theta = np.zeros(X.shape[1])
            for i in range(self.num_iter):
                z = np.dot(X, self.theta)
                h = self.__sigmoid(z)
                gradient = np.dot(X.T, (h - y)) / y.size
                self.theta -= self.lr * gradient
                z = np.dot(X, self.theta)
                h = self.__sigmoid(z)
                loss = self.__loss(h, y)
                if(self.verbose == True and i % 10000 == 0):
                    print(f'loss: {loss}\t')
    
    def predict_proba(self, X):
        if self.fit_intercept:
            X = self.__add_intercept(X)
        return self.__sigmoid(np.dot(X, self.theta))

    def predict(self, X):
        return self.predict_proba(X).round()


# In[5]:


model = LogisticRegression(lr = 0.1, num_iter=200)


# In[6]:


get_ipython().run_line_magic('time', 'model.fit(X, y)')


# In[7]:


pred = model.predict(X)
print(f'Accuracy Score: {(pred == y).mean()}')


# In[8]:


plt.figure(figsize=(10,6))

plt.scatter(X[y==0][:,0], X[y == 0][:,1], color='b', label='0')
plt.scatter(X[y==1][:,0], X[y == 1][:,1], color='r', label='0')
plt.legend()

x1_min, x1_max = X[:,0].min(), X[:, 0].max()
x2_min, x2_max = X[:,1].min(), X[:, 1].max()

xx1, xx2 = np.meshgrid(np.linspace(x1_min, x1_max), np.linspace(x2_min, x2_max))
grid = np.c_[xx1.ravel(), xx2.ravel()]
probs = model.predict_proba(grid).reshape(xx1.shape)
plt.contour(xx1, xx2, probs, [0.5], linewidths=1, colors='black')


# In[ ]:




