// Value point: All values with specific value
from(bucket: "irregularbucket")
    |> range(start: 0, stop: now())
    |> filter(fn: (r) => r._value == 40000 and r.hostname == "host_2" and r._measurement == "net" and r._field == "bytes_recv")
    |> drop(columns: ["_start", "_stop"])