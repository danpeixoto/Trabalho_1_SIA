import pandas as pd
import numpy as np
import math
import random



def export_data_txt(data):
	ids = pd.Series(id_save)
	data.insert(loc=0, column='id', value=ids)
	data.to_csv('./resultados/kmeans/resultados_k_means.txt',sep='\t',index=False)

def manhatam_distance(u,v):
	return np.sum(np.abs(u-v))

def euclidian_distance(u,v):
	return np.sqrt(np.sum(np.power(u-v,2)))

def supreme_distance(u,v):
	return np.amax(np.abs(u-v))

def calculate_group(data,means,distance_to_use):
	groups = {k:v for (k,v) in zip(range(len(means)),means)}
	i = 0 
	for mean in means:
		groups[i] = distance_to_use(data,mean)
		i += 1

	return min(groups, key=groups.get)

def calculate_new_mean(data):
	data_array = data.iloc[:,:-1].values
	new_mean = [0.0 for i in range(len(data_array[0]))]

	for dt in data_array:
		for i in range(len(dt)):
			new_mean[i] += dt[i]
	
	return [x/float(len(data_array)) for x in new_mean]




def k_nearest_neighbors(data, k,seed, distance_to_use, iterations=200):
	data = data.assign(group = -1)
	means = data.sample(k, random_state = seed).values[:,:-1]
	old_data = None
	
	j = 0
	while True:
		
		for i in range(len(data)):
			data.loc[i,'group'] = calculate_group(data.iloc[i].values[:-1],means,distance_to_use)

		
		if j == iterations:
			export_data_txt(data)
			return
		
		old_data = data.copy()
		
		for i in range(k):
			data_by_group = old_data['group'] == i
			means[i] = calculate_new_mean(old_data[data_by_group])
			
		j += 1
	


def execute(path, k = 7, d = 2, seed = 42):
	data = pd.read_csv(path, delimiter=r'\t+',engine='python')
	global id_save #gambiarra
	id_save = data['id'].values
	data = data.drop('id', 1)
	data = data.drop('class', 1)

	if(d==0):
		distance = supreme_distance
	elif(d==1):
		distance = manhatam_distance
	else:
		distance = euclidian_distance

	k_nearest_neighbors(data.loc[:],k,seed,distance)




