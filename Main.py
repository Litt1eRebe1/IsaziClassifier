# Load libraries
from Classifier import Classifier

print("====== CARS ======")
cars_classifier = Classifier(['price', 'maintenance', 'doors', 'occupants', 'boot size', 'safety', 'buy'], "Resources/cars.csv", ["acc", "unacc"])
cars_classifier.classify()
print("====== SPORTS ======")
sports_classifier = Classifier(['Wind', 'Temperature', 'Weather', 'Humidity', 'Outcome'], "Resources/cars.csv", ["Play", "Cancel"])
sports_classifier.classify()

