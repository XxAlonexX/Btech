# Introduction to Machine Learning
Machine Learning (ML) is a field of AI that enables computers to learn patterns from data without being explicitly programmed. ML models improve their performance on tasks over time as they process more data.
#### **How It Works (Logic)**:

1. **Data**: Input data is used for learning.
2. **Model**: An algorithm (e.g., linear regression) processes the data.
3. **Training**: The model adjusts parameters to minimize error.
4. **Prediction**: The trained model predicts outcomes for new data.
### **Types of Machine Learning**

1. **Supervised Learning**:
    
    - Learn from labeled data.
    - Example: Predicting house prices.
    - Algorithms: Linear Regression, Decision Trees.
2. **Unsupervised Learning**:
    
    - Find hidden patterns in unlabeled data.
    - Example: Customer segmentation.
    - Algorithms: K-Means Clustering, PCA.
3. **Reinforcement Learning**:
    
    - Learn from interaction with the environment.
    - Example: Teaching a robot to walk.
    - Algorithms: Q-Learning, Deep Q-Networks.

## Types of Machine Learning 
1. **Supervised Learning**:
    
    - Learn from labelled data.
    - Example: Predicting house prices.
    - Algorithms: Linear Regression, Decision Trees.
2. **Unsupervised Learning**:
    
    - Find hidden patterns in unlabelled data.
    - Example: Customer segmentation.
    - Algorithms: K-Means Clustering, PCA.
3. **Reinforcement Learning**:
    
    - Learn from interaction with the environment.
    - Example: Teaching a robot to walk.
    - Algorithms: Q-Learning, Deep Q-Networks.

________________________________________________________________________

# Feature Engineering 
Feature engineering involves transforming raw data into meaningful inputs for machine learning models. It improves model accuracy and performance.
## Features
- Individual measurable properties of data.
- Example: Height, weight, or age in a dataset.
## Types of Feature

- **Numerical Features**: Continuous or discrete numbers.
- **Categorical Features**: Represent categories or groups (e.g., gender).
- **Ordinal Features**: Categories with a meaningful order (e.g., education level).


## Handling Missing Data
Replace or remove missing values to maintain dataset integrity.
1. **Methods**:

- Replace with the mean, median, or mode.
- Remove rows/columns with missing values.
- Predict missing values using other features.
```python
from sklearn.impute import SimpleImputer

imputer = SimpleImputer(strategy='mean')  # Replace missing values with mean
data = imputer.fit_transform(data)
```

## Dealing with Categorical Feature 
Transform categorical variables into numerical formats for ML models.
1.  **Label Encoding**: Assigns a unique number to each category.
2. **One-Hot Encoding**: Creates binary columns for each category.

```python
from sklearn.preprocessing import OneHotEncoder

encoder = OneHotEncoder()
encoded_data = encoder.fit_transform(data)
```
________________________________________________________________________

# Working with Features
Features are the core inputs to machine learning models. The process of working with features—preparing, transforming, or selecting them—ensures that models can learn effectively and make accurate predictions.
### **Why Do We Need to Work with Features?**

Features are the core inputs to machine learning models. The process of working with features—preparing, transforming, or selecting them—ensures that models can learn effectively and make accurate predictions. Here’s why it's crucial:
### **Core Use of Working with Features**

1. **Improves Model Accuracy**
    
    - Quality and relevance of features directly impact a model’s predictive power.
    - Well-processed features reduce noise and allow the model to focus on meaningful patterns.
2. **Handles Data Diversity**
    
    - Raw data often contains inconsistencies, missing values, or outliers.
    - Transformations like scaling, encoding, and imputing missing data standardise the dataset for better learning.
3. **Reduces Model Complexity**
    
    - Eliminating irrelevant or redundant features minimises over-fitting.
    - Feature selection/extraction helps reduce dimensionality, improving computational efficiency.
4. **Enhances Interpretability**
    
    - Proper feature engineering reveals relationships and patterns in data.
    - Simplifies understanding of the decision-making process.
## Feature Scaling 
- Normalise or standardise data to ensure features are on a comparable scale.
- Example: MinMaxScaler, StandardScaler.

```python
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
scaled_data = scaler.fit_transform(data)
```
## Feature Selection
Select the most important features to reduce dimensionality.
1. **Filter Methods**: Statistical tests (e.g., chi-square).
2. **Wrapper Methods**: Recursive feature elimination.
3.  **Embedded Methods**: Regularization (e.g., Lasso Regression).

```python
from sklearn.feature_selection import SelectKBest, chi2

selected_features = SelectKBest(chi2, k=5).fit_transform(X, y)
```

---

# Feature Extraction
Derive new features from existing ones (e.g., PCA).
Feature extraction is about transforming raw data into a smaller set of meaningful features. Let's use **Principal Component Analysis (PCA)** as an example.

## Principal Component Analysis (PCA)
PCA reduces the number of features while preserving maximum variance.\

**How It Works (Logic)**:
- Calculates principal components (new features) by transforming data.
- Components are linear combinations of original features.

```python 
from sklearn.decomposition import PCA

pca = PCA(n_components=2)
reduced_data = pca.fit_transform(data)
```

