// 1-12-mean
from(bucket: "irregularbucket")
    |> range(start: 1303002992, stop: 1303046192)
    |> filter(fn: (r) => r._measurement == "9")
    |> window(every: 5m)
    |> mean()