// Entire ts
from(bucket: "irregularbucket")
    |> range(start: 0, stop: now())
    |> filter(fn: (r) => r.hostname == "host_0" and r._measurement == "redis" and r._field == "sync_full")
    |> drop(columns: ["_start", "_stop"])