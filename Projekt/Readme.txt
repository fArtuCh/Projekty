Projekt nr 5 Readme.
Theme: K-means algorithm

			Composition	
-------------------------------------------------------------
-:Dataset 			:	data1.json
-:Chart presenting clusters 	:	----.
-:Python script			:	k_means_pyspark.py
-:----				:	-----
_____________________________________________________________

		K-means algorithm introduction
----------------------------------------------------------------------------------------
It's one of the simplest algorithm used in machine learning. 				|
It's used to classify a given data set through a certain number of clusters .	 	|
Each cluster is composed by it's own indywidual centroid.				|
Centroids should be placed away from each other for the best 				|
results. Of the posiotion of those depends the result of 				|
algorithm. Firts you have to take each data cell and associate it			|
with the given centroid, who is the closest one. It needs to be done for		|
all data. At this point we need to re-calculate k new centroids as barycenters of	|
the clusters resulting from the previous step. 						|
After we have these k new centroids, a new binding has to be done			|
between the same data set points and the nearest new centroid in a 			|
loop fashion. The centroids change their location step by step 				|
until no more changes are done, that means there are not longer moving. 		|
											|
The algorithm aims for minimalizing average quantization error.				|
											|
_________________________________________________________________________________________
 	

			Usage
-----------------------------------------------------------------------------------------
Open k_means_pyspark.py scipt and run it though console.

_____________________________________________________________