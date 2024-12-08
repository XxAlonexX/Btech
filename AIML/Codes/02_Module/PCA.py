from sklearn.decomposition import PCA
import numpy as np

# Sample Data: 4 features (columns) for 5 flowers (rows)
data = np.array([[5.1, 3.5, 1.4, 0.2],
                 [4.9, 3.0, 1.4, 0.2],
                 [4.7, 3.2, 1.3, 0.2],
                 [4.6, 3.1, 1.5, 0.2],
                 [5.0, 3.6, 1.4, 0.3]])

# Applying PCA to extract 2 new features
pca = PCA(n_components=2)
reduced_data = pca.fit_transform(data)

print("Reduced Features:")
print(reduced_data)
