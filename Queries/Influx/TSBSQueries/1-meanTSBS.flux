// 1-12-mean
from(bucket: "irregularbucket")
    |> range(start: 1451606400, stop: 1451649600)
    |> filter(fn: (r) => r.hostname == "host_2" and r._measurement == "diskio" and r._field == "writes")
    |> window(every: 5m)
    |> mean()