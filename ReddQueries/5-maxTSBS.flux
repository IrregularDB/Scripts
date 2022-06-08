// 5-12-max
from(bucket: "irregularbucket")
    |> range(start: 1303002992, stop: 1303046192)
    |> filter(fn: (r) => r._measurement == "14" 
                        or r._measurement == "17"
                        or r._measurement == "15"
                        or r._measurement == "1"
                        or r._measurement == "9")
    |> window(every: 5m)
    |> group(columns: ["_start"])
    |> max()