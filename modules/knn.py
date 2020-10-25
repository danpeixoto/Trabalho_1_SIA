import pandas as pd
import numpy as np


def manhatam_distance(u,v):
	return np.sum(np.abs(u-v))

def euclidian_distance(u,v):
	return np.sqrt(np.sum(np.power(u-v,2)))

def supreme_distance(u,v):
	return np.amax(np.abs(u-v))



def calculate_class(data, classes):
	classes_dict = {classes[i]: i for i in range(len(classes))}
	classes_results = [0 for i in range(len(classes))]

	for i in range(len(data)):
		classes_results[classes_dict[data.iloc[i, -2]]] += 1

	arg_max = np.argmax(classes_results)
	class_value = list(classes_dict.keys())[arg_max]

	print('Classe prevista:{}'.format(class_value))
	print('vizinhos mais proximos: ', end='')
	print(','.join(str(x) for x in list(data.index)), '\n')


def k_nearest_neighbors(data, predict, k, distance_to_use):

	data_array = data.iloc[:].values
	predict_array = predict.iloc[:].values

	data_indexes = list(data.index)
	predict_indexes = list(predict.index)

	classes = data['class'].unique()

	for i_p in range(len(predict)):
		distances = []
		for i_d in range(len(data)):
			if(data_indexes[i_d] != predict_indexes[i_p]):
				distance = distance_to_use(data_array[i_d][:-1], predict_array[i_p][:-1])
				distances.append(distance)
			else:
				distances.append(9999999)
		data['distance'] = distances
		# print(predict_array[ip][-1])
		sorted_data = data.sort_values('distance')

		calculate_class(sorted_data.iloc[:k], classes)


def execute(path, k = 7, d = 2):

	data = pd.read_csv(path, delimiter=r'\s+')
	data = data.drop('id', 1)
	train, test = data, data

	if(d==0):
		distance = supreme_distance
	elif(d==1):
		distance = manhatam_distance
	elif(d == 2):
		distance = euclidian_distance

	k_nearest_neighbors(train.loc[:], test.loc[:], k, distance)



