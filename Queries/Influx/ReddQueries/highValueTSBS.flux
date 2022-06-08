// High value: Get all values over x for timeseries ts
from(bucket: "irregularbucket")
    |> range(start: 0, stop: now())
    |> filter(fn: (r) => r._measurement == "456" and r._value > 13318.5, onEmpty: "drop")
    |> drop(columns: ["_start", "_stop"])