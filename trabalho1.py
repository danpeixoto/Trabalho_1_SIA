import sys
import argparse
sys.path.append('./modules/')

from knn import execute as execute_knn
from kmeans import execute as execute_k_means




if __name__ == '__main__':
	parser = argparse.ArgumentParser(description='Trabalho 1 da classe Sistema Inteligentes Aplicados')
	parser.add_argument('--knn',action='store_true',required=False)
	parser.add_argument('--kmeans',action='store_true',required=False)
	parser.add_argument('-k',action='store',type=int,required=True)
	parser.add_argument('-d',action='store',type=int,required=True)
	parser.add_argument('-s',action='store',default=1,type=int,required=False)
	parser.add_argument('file')
	args = parser.parse_args()
	
	if(args.knn):
		if('.txt' in args.file):
			execute_knn(args.file,args.k,args.d)
		else:
			print('ERRO, caminho de arquivo invalido')
	elif(args.kmeans):
		if('.txt' in args.file):
			execute_k_means(args.file,args.k,args.d,args.s)
		else:
			print('ERRO, caminho de arquivo invalido')
