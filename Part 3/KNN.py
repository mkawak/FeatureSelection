import math

def leave_one_out_cross_validation(data_passed, current_set, feature_to_add_or_remove, flag, k):
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
    if (len(data) > 1):
        # Iterate through columns features
        for object_to_classify, object_class_label in enumerate(data[0]):
            # Object Index      Object Label 1 or 2

            # Initialize a list to store k nearest neighbor distances and locations
            k_nearest_neighbor_distances = [float('inf')] * k
            k_nearest_neighbor_locations = [None] * k

            # Iterating through all features columns except first label column
            for k_value in range(len(data[0])):
                if k_value != object_to_classify:
                    distance = 0
                    # print("Ask if ", object_to_classify, " is nearest neighbor with ", k)
                    for feature_column in data[1:]:
                        distance += math.pow(feature_column[object_to_classify] - feature_column[k_value], 2)
                    distance = math.sqrt(distance)

                    # Update the k nearest neighbor list
                    max_distance_index = k_nearest_neighbor_distances.index(max(k_nearest_neighbor_distances))
                    if distance < k_nearest_neighbor_distances[max_distance_index]:
                        k_nearest_neighbor_distances[max_distance_index] = distance
                        k_nearest_neighbor_locations[max_distance_index] = k_value

            # Create a dictionary to count the frequency of each class among the nearest neighbors
            class_frequency = {}
            for location in k_nearest_neighbor_locations:
                label = data[0][location]
                if label in class_frequency:
                    class_frequency[label] += 1
                else:
                    class_frequency[label] = 1

            # Find the class with the highest frequency
            highest_frequency = max(class_frequency.values())
            highest_class = [label for label, freq in class_frequency.items() if freq == highest_frequency][0]

            # Check whether it classified it right
            if object_class_label == highest_class:
                number_correctly_classified += 1

        # Calculate Accuracy
        accuracy = number_correctly_classified / len(data[0])
        # Return Accuracy result
        return accuracy * 100
    else:
        return 0
