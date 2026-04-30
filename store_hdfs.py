from pyspark import SparkConf, SparkContext

if __name__ == "__main__":
    conf = SparkConf() \
        .setAppName("NOAA Read") \
        .setMaster("local[*]") \
        .set("spark.hadoop.fs.defaultFS", "hdfs://127.0.0.1:9000")
    sc = SparkContext(conf=conf)
    rising = sc.textFile("file:///home/jp/Desktop/artist-rise&fall/rising.txt")
    falling = sc.textFile("file:///home/jp/Desktop/artist-rise&fall/falling.txt")
    rising.saveAsTextFile("hdfs://127.0.0.1:9000/artist/rise")
    falling.saveAsTextFile("hdfs://127.0.0.1:9000/artist/fall")
    sc.stop()