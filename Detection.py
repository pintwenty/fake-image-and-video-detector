from FakeImageDetection import predict, show_prediction_labels_on_image
import os
import sys
import os.path
from FakeImageDetection import *
from resize2 import resize


def fakedetection(image_file):
    try:
        result = ""
        full_file_path = os.path.join("../FakeImageDetection/test", image_file)

        print("Looking for faces in {}".format(image_file))

        # Find all people in the image using a trained classifier model
        # Note: You can pass in either a classifier file name or a classifier model instance
        resize(full_file_path)
        predictions = predict(
            full_file_path, model_path="trained_knn_model.clf")

        # Print results on the console
        for name, (top, right, bottom, left) in predictions:
            result=name
            print("- Found {} at ({}, {})".format(name, left, top))

            # Display results overlaid on an image
            show_prediction_labels_on_image(os.path.join(
                "../FakeImageDetection/test", image_file), predictions, image_file)

        return result



    except Exception as e:
            print(e.args[0])
            tb = sys.exc_info()[2]
            print(tb.tb_lineno)


#fakedetection("ran.jpg")
