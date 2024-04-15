import joblib
import numpy as np

class PriceProcessor():
	def __init__(self, userCar):
		self.userCar = userCar

	def process(self):
		loaded_rf = joblib.load("landing/models/my_random_forest_2.joblib")
		loaded_cats_encoding = joblib.load("landing/models/cats_encoding_2.bin")
		loaded_scaler = joblib.load("landing/models/std_scaler_2.bin")

		categry_columns = [
			'manufacturer',
			'model',
			'category',
			'fuel',
			'gearbox',
			'driver_wheels',
			'doors',
			'wheels',
			'colors',
		]

		user_car_filterout_cats = {key: self.userCar[key] for key in categry_columns}
		encoded_user_car_filterout_cats = loaded_cats_encoding.transform(np.array([list(user_car_filterout_cats.values())], dtype=object))

		for i, feature in enumerate(user_car_filterout_cats):
			user_car_filterout_cats[feature] = encoded_user_car_filterout_cats[0][i]
			  
		self.userCar.update(user_car_filterout_cats)
		user_car_values_scaled = loaded_scaler.transform(np.array(list(self.userCar.values())).reshape(1, -1))

		prediction = int(np.exp(loaded_rf.predict(user_car_values_scaled))[0])
		return prediction