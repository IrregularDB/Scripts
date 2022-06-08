// High value: Get all values over x for timeseries ts
from(bucket: "irregularbucket")
    |> range(start: 0, stop: now())
    |> filter(fn: (r) => r._value > 90 and r.hostname == "host_0" and r._measurement == "cpu" and r._field == "usage_idle")
    |> drop(columns: ["_start", "_stop"])