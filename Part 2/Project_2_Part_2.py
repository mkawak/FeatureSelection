# Abhinav Allam (aalla009) 862200322 
# Jacqueline Gardea (jgard046) 862305608 
# Majd Kawak (mkawa025) 862273310 
# Rovin Soriano (rsori013) 862149089

import random
import math
import numpy as np


def leave_one_out_cross_validation(data_passed, current_set, feature_to_add_or_remove, flag):
    # Add labels
    data = [data_passed[0]]
    # Add current all features except if flag is 1, then don't add feature_to_remove
    for feature in current_set:
        if flag == 1:
            if feature != feature_to_add_or_remove:
                data.append(data_passed[feature])
        else:
            data.append(data_passed[feature])
    # Add left over feature from flag 0  we're processing
    if flag == 0:
        data.append(data_passed[feature_to_add_or_remove])
    # Number of right classification
    number_correctly_classified = 0
    # Iterate through columns features
    for object_to_classify, object_class_label in enumerate(data[0]):
        # Object Index      Object Label 1 or 2

        # Calculates nearest neighbor distance
        nearest_neighbor_distance = float('inf')
        nearest_neighbor_location = None

        # Iterating through all features columns except first label column
        for k in range(len(data[0])):
            if k != object_to_classify:
                distance = 0
                # print("Ask if ", object_to_classify, " is nearest neigbour with ", k)
                for feature_column in data[1:]:
                    distance += math.pow(feature_column[object_to_classify] - feature_column[k], 2)
                distance = math.sqrt(distance)
                if distance < nearest_neighbor_distance:
                    nearest_neighbor_distance = distance
                    nearest_neighbor_location = k
        # Check whether it classified it right
        if object_class_label == data[0][nearest_neighbor_location]:
            number_correctly_classified += 1
        # print("Object ", object_to_classify, " is in class ", object_class_label)
        # print("Its nearest_neighbor is ", nearest_neighbor_location, " which is in class ", data[0][nearest_neighbor_location])
    # Calculate Accuracy
    accuracy = number_correctly_classified / len(data[0])
    # Return Accuracy result
    return accuracy


def feature_search_forward(data):
    # Holds our total features set
    total_features_set = []

    # Iterate through columns features except the first
    for col_index, column in enumerate(data[1:], start=1):

        print("On the ", col_index, " level of the search tree\n")

        # Holds our current features at each level
        features_for_Level = -1
        best_so_far_accuracy = 0

        # Access columns features except the first
        for feature_index, value in enumerate(data[1:], start=1):

            # If a feature is not in our total set, consider it
            if feature_index not in total_features_set:

                # Accuracy function with flag 0 to add
                accuracy = leave_one_out_cross_validation(data, total_features_set, feature_index, 0)
                print("--Considering adding the ", feature_index, " feature with accuracy of ", accuracy)

                if accuracy > best_so_far_accuracy:
                    best_so_far_accuracy = accuracy
                    features_for_Level = feature_index

        total_features_set.append(features_for_Level)
        print("\nOn level ", col_index, " I added feature ", features_for_Level, " to current set with accuracy of ",
              best_so_far_accuracy)
        print("Current Set of Features: ", total_features_set)
        print("---------------------------------------------")


def feature_search_backward(data):
    # Holds our total features set
    total_features_set = [i for i in range(1, len(data))]

    # Iterate through columns features except the first -- inverse
    for col_index in reversed(range(1, len(data))):

        print("On the ", col_index, " level of the search tree\n")

        # Holds our current features at each level
        features_for_Level = -1
        best_so_far_accuracy = 0

        # Access columns features except the first -- in reverse
        for feature_index in reversed(range(1, len(data))):

            # If a feature is in our total set, consider it
            if feature_index in total_features_set:

                # Accuracy function with flag 1 to remove
                accuracy = leave_one_out_cross_validation(data, total_features_set, feature_index, 1)
                print("--Considering adding the ", feature_index, " feature with accuracy of ", accuracy)

                if accuracy > best_so_far_accuracy:
                    best_so_far_accuracy = accuracy
                    features_for_Level = feature_index

        total_features_set.remove(features_for_Level)
        print("\nOn level ", col_index, " I removed feature ", features_for_Level, " to current set with accuracy of ",
              best_so_far_accuracy)
        print("Current Set of Features: ", total_features_set)
        print("---------------------------------------------")


# Specify the file path
file_path = "small-test-dataset.txt"

# Read the entire file as a single string
with open(file_path, "r") as file:
    content = file.read()

# Split the content by newlines to get rows
rows = content.split("\n")

# Initialize a list to store the column values for each row
rows_columns = []

for index, row in enumerate(rows):
    # Split each row by tabs to get columns
    row_values = row.split()
    if (index == 0):
        for index, row_value in enumerate(row_values):
            # Append or extend value
            col = [float(row_value)]
            rows_columns.append(col)
    else:
        for index, row_value in enumerate(row_values):
            rows_columns[index].append(float(row_value))


def min_max_scaling(arr):
    min_val = np.min(arr)
    max_val = np.max(arr)
    normalized_arr = (arr - min_val) / (max_val - min_val)
    return normalized_arr


normalized_rows_columns = []
normalized_rows_columns.append(rows_columns[0])

# Normalize each column
for column in rows_columns[1:]:
    normalized_subarray = min_max_scaling(column)
    normalized_rows_columns.append(normalized_subarray)

# Test functions
#feature_search_forward(normalized_rows_columns)
feature_search_backward(normalized_rows_columns)

# Close file
file.close()