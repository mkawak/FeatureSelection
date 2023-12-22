# Abhinav Allam (aalla009) 862200322
# Jacqueline Gardea (jgard046) 862305608
# Majd Kawak (mkawa025) 862273310
# Rovin Soriano (rsori013) 862149089

import random
def leave_one_out_cross_validation(data, currSet, featureToAdd):
    return random.randint(0, 100)

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

                # Stub function
                accuracy = leave_one_out_cross_validation(data, total_features_set, feature_index)
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

                # Stub function
                accuracy = leave_one_out_cross_validation(data, total_features_set, feature_index)
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
    if(index == 0):
        for index, row_value in enumerate(row_values):
            # Append or extend value
            col = [row_value]
            rows_columns.append(col)
    else:
        for index, row_value in enumerate(row_values):
            rows_columns[index].append(row_value)

# Test functions
feature_search_forward(rows_columns)
feature_search_backward(rows_columns)

file.close()