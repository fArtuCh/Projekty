from pyspark.sql import SparkSession
import numpy as np
import matplotlib.pyplot as plt


def parse_data(points):
    return np.array([x for x in points])


def get_x(points):
    return points[0]


def get_y(points):
    return points[1]


def find_group(point, centroids):
    group = 0
    min_distance = 10000000000
    for counter, centroid in enumerate(centroids):
        distance = np.sqrt(np.sum((point - centroid) ** 2))
        if distance < min_distance:
            min_distance = distance
            group = counter
    return group


if __name__ == "__main__":

    spark = SparkSession \
        .builder \
        .appName("Spark KMeans Algorithm") \
        .config("spark.some.config.option", "some-value") \
        .getOrCreate()

    sc = spark.sparkContext
    data = spark.read.option("multiline", "true").json("data1.json")
    data_parsed = sc.parallelize(data.rdd.values().map(parse_data).cache().collect()[0])

    data_parsed_x = data_parsed.map(get_x).collect()
    data_parsed_y = data_parsed.map(get_y).collect()

    K = int(input("Enter number of clusters: "))
    Acc = float(input("Enter accurracy of searching for new centroids: "))

    seed = np.random.randint(2000000000)
    centroids = data_parsed.takeSample(False, K, seed)

    centroids_x = [x[0] for x in centroids]
    centroids_y = [x[1] for x in centroids]

    plt.ion()
    fig = plt.figure()
    ax = fig.add_subplot(111)
    plt.title("KMeans, starting position of centroids and unclassified data")

    ax.scatter(data_parsed_x, data_parsed_y)
    ax.scatter(centroids_x, centroids_y, marker='x')
    fig.canvas.draw()
    fig.canvas.flush_events()

    while True:

        found_better_centroids = False

        classified = data_parsed.map(lambda point: (find_group(point, centroids), (point, 1)))
        groups_statistics = classified.reduceByKey(lambda points1, points2: (points1[0] + points2[0], points1[1] + points2[1]))
        groups_divided = classified.groupByKey().map(lambda x: (x[0], list(x[1]))).collect()
        new_centroids = groups_statistics.map(lambda stat: (stat[0], stat[1][0] / stat[1][1])).collect()

        for counter, i in enumerate(centroids):
            if (np.abs(i[0] - new_centroids[counter][1][0]) > Acc) or (np.abs(i[1] - new_centroids[counter][1][1]) > Acc):
                found_better_centroids = True

        for i, k in new_centroids:
            centroids[i] = k

        centroids_x = [x[0] for x in centroids]
        centroids_y = [x[1] for x in centroids]

        ax.clear()
        for group in range(K):
            group_x = [x[0][0] for x in groups_divided[group][1]]
            group_y = [x[0][1] for x in groups_divided[group][1]]
            ax.scatter(group_x, group_y)
        ax.scatter(centroids_x, centroids_y, marker='x')
        plt.title("Data classified, new centroids position")
        fig.canvas.draw()
        fig.canvas.flush_events()

        if not found_better_centroids:
            plt.title("Final centroids position")
            plt.pause(10)
            break
