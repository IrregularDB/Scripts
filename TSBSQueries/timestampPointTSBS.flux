// Timestamp point 
from(bucket: "irregularbucket")
    |> range(start: 1454075478, stop: 1454075480)
    |> filter(fn: (r) => r.hostname == "host_1" and r._measurement == "postgresl" and r._field == "deadlocks" and r._time == time(v: 1454075479700000000))
    |> drop(columns: ["_start", "_stop"])