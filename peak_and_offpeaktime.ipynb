from dask.distributed import Client, LocalCluster
import dask.dataframe as dd
cluster=LocalCluster(n_workers=10)
cc=Client(cluster)
df = dd.read_csv('taxi+_zone_lookup.csv')
df1=dd.read_parquet('gcs://anaconda-public-data/nyc-taxi/nyc.parquet/part.0.parquet')
df1 = df1.persist()
df1['time'] = df1['tpep_pickup_datetime'].dt.time
df2=df1['time'].value_counts().nlargest(2)
df3=df1['time'].value_counts().nsmallest(2)
df2.head()
df3.head()

