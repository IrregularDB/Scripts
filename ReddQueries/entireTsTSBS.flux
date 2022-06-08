// Entire ts
from(bucket: "irregularbucket")
    |> range(start: 0, stop: now())
    |> filter(fn: (r) => r._measurement == "10004")
    |> drop(columns: ["_start", "_stop"])