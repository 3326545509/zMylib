from matplotlib import pyplot as plt 
import numpy as np
from typing import List, Tuple

def hello():
	print('quiciDraw.py is imported successfully')

def quick2DMap(fname		:	str,
			   scatterSize	:	float=None,
			   legend		:	str=None,
			   xlabel		:	str=None,
			   ylabel		:	str=None,
			   title		:	str=None,
			   outPath		:	str="quick2DMap.png",
			   cmap			:	list[float,float]=None,
			   xlim			:	list[float,float]=None,
			   ylim			:	list[float,float]=None,
			   cmapStyle	:	str='seismic_r',
			   shrink		:	float=None,
			   figsize		:	Tuple[float,float]=None
			   )->None:
	'''
	Generate a *2D scatter plot* from the data file.

	Inpute:
	-------
		Data file:	is should contain 3 lines. (x,y,value)
	
	Output:
	-------
		A png file with the default name "./quick2DMap.png"

	Parameters with examples:
	-------
		fname	: 	data.txt #file name
		outPath	:	The name will be processed automatically
						laji.png
						../laji.png
						../	
	'''
	try:
		x,y,z 	=	np.loadtxt(fname=fname,unpack=True)
	except Exception as e:
		print(f"Error when loading {fname}")
		return 
	plt.figure(figsize=figsize)
	if cmap:
		plt.scatter(x,y,c=z,s=scatterSize,cmap=cmapStyle,vmin=cmap[0],vmax=cmap[1])
	else:
		plt.scatter(x,y,c=z,s=scatterSize,cmap=cmapStyle)

	
	plt.title(title)
	plt.xlabel(xlabel)
	plt.ylabel(ylabel)
	plt.axis('equal')

	if xlim:
		plt.xlim(xlim[0],xlim[1])
	if ylim:
		plt.ylim(ylim[0],ylim[1])

	if shrink:
		plt.colorbar(label=legend,shrink=shrink)
	else:
		plt.colorbar(label=legend)

	plt.savefig(outPath)

def quickScastter():
	return
