import dask.array as da
import ray

def test_dask_ray():
    ray.init()
    arr = da.ones((1000,), chunks=100)
    result = arr.sum().compute()
    assert result == 1000
    ray.shutdown()
