from dask.distributed import Client, LocalCluster
cluster=LocalCluster(n_workers=10)
cc=Client(cluster)
