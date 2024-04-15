from django.shortcuts import render
from .price_processor import PriceProcessor
from .static_data import manufacturers,\
	models,\
	categories,\
	fuel,\
	gearbox,\
	driver_wheels,\
	doors,\
	wheels,\
	colors


def landingView(request):

	result = None
	# error = None

	if request.method == 'POST':
		form = request.POST
		keys = [
			'age',
			'engine_volume',
			'mileage',
			'airbags',
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

		numkeys = [
			'age',
			'engine_volume',
			'mileage',
			'airbags',
		]

		userCar = {}

		for key in keys:
			userCar[key] = form[key]
		
		for key in numkeys:
			userCar[key] = float(userCar[key])




		# for key in numkeys:
		# 	try:
		# 		userCar[key] = float(form[key])
		# 	except ValueError:
		# 		if form[key] == '':
		# 			error = f"{key} is required."
		# 			break
		# 		else:
		# 			error = f"{key} must be a number."


					
            
		
		priceProcessor = PriceProcessor(userCar)
		result = priceProcessor.process()

	context = {
		'manufacturers': manufacturers,
		'models': models,
		'categories': categories,
		'fuel': fuel,
		'gearbox': gearbox,
		'driver_wheels': driver_wheels,
		'doors': doors,
		'wheels': wheels,
		'colors': colors,
		'result': result,
		# 'error': error
	}
	return render(request, 'index.html', context)