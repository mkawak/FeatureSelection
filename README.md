# Feature Selection with Nearest Neighbor / Machine Learning

### Overview
In this project, a part of the Introduction to Artificial Intelligence course at UCR (CS170), we explore the critical aspect of feature selection in datasets. The goal is to enhance classification accuracy by selecting the most relevant features. We implement three distinct algorithms: Forward Selection, Backward Elimination, and Custom Random Feature Combinations.

### Key Algorithms

#### Forward Selection
- Iteratively selects features, aiming to find the combination with the highest classification accuracy.

#### Backward Elimination
- Starts with all features, then systematically removes the least significant ones to improve model performance.

#### Custom Random Feature Combinations
- Introduces a novel approach by generating random feature sets and evaluating them using Leave One Out Cross Validation (LOOCV).

### Key Insights
- **Algorithm Comparison**: We observed varying degrees of success among the algorithms, providing valuable insights into the nuances of feature selection.
- **Normalization Impact**: The study includes an analysis of how data normalization influences algorithm performance, comparing results with normalized versus unnormalized data.
- **Challenges Encountered**: Our journey was marked by challenges in algorithm implementation, data preprocessing, and avoiding overfitting—key learning points in machine learning.

### Author's Reflection
This project not only highlights the importance of feature selection but also serves as a practical exploration of machine learning principles. It demonstrates how selecting the right features can significantly enhance model accuracy in high-dimensional data scenarios.

### Project Structure

- `main.py`: The primary entry point of the program. It contains the main logic for feature selection algorithms and data preprocessing.
  - **Data Input**: Reads and processes the input data file.
  - **Normalization**: Includes functionality for Z normalization of the data.
  - **Algorithm Selection**: Allows the user to choose between Forward Selection, Backward Elimination, and Random Combinations algorithms.
- `forward_feature_selection`: Implements the Forward Selection algorithm, iteratively selecting features to improve accuracy.
- `backward_feature_elimination`: Features the Backward Elimination method, systematically removing features to enhance model performance.
- `random_feature_combinations`: A custom method for generating random feature combinations and evaluating them using cross-validation.
- `leave_one_out_cross_validation`: A utility function used by all the algorithms to evaluate the efficacy of the feature sets.
- `z_normalization`: Function for normalizing data using Z-score normalization.

### Getting Started
For a hands-on experience:
- Clone the repository to your local machine.
- Run `main.py` and follow the prompts to test different feature selection algorithms on your dataset.
### Author
Majd Kawak
### Collaborators
Abhinav Allam\
Jacqueline Gardea\
Rovin Soriano
