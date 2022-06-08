// 1-12-mean
from(bucket: "irregularbucket")
    |> range(start: 1303002992, stop: 1303046192)
    |> filter(fn: (r) => r.hostname == "host_2" and r._measurement == "diskio" and r._field == "writes")
    |> window(every: 5m)
    |> mean()

// 5-12-max
from(bucket: "irregularbucket")
    |> range(start: 1303002992, stop: 1303046192)
    |> filter(fn: (r) => r.hostname == "host_0" and r._measurement == "cpu" and r._field == "usage_idle"
                or r.hostname == "host_0" and r._measurement == "mem" and r._field == "used_percent"
                or r.hostname == "host_1" and r._measurement == "cpu" and r._field == "usage_idle"
                or r.hostname == "host_1" and r._measurement == "mem" and r._field == "used_percent"
                or r.hostname == "host_2" and r._measurement == "cpu" and r._field == "usage_idle")
    |> window(every: 5m)
    |> group(columns: ["_start"])
    |> max()

// Last
from(bucket: "irregularbucket")
    |> range(start: 0, stop: now())
    |> last()
    |> drop(columns: ["_start", "_stop"])

// High value: Get all values over x for timeseries ts
from(bucket: "irregularbucket")
    |> range(start: 0, stop: now())
    |> filter(fn: (r) => r._value > 90 and r.hostname == "host_0" and r._measurement == "cpu" and r._field == "usage_idle")
    |> drop(columns: ["_start", "_stop"])

// Timestamp point 
from(bucket: "irregularbucket")
    |> range(start: 0, stop: now())
    |> filter(fn: (r) => r._time == 1454075479700 and r.hostname == "host_1" and r._measurement == "postgresl" and r._field == "deadlocks")
    |> drop(columns: ["_start", "_stop"])

// Value point: All values with specific value
from(bucket: "irregularbucket")
    |> range(start: 0, stop: now())
    |> filter(fn: (r) => r._value == 40000 and r.hostname == "host_2" and r._measurement == "net" and r._field == "bytes_recv")
    |> drop(columns: ["_start", "_stop"])

// Entire ts
from(bucket: "irregularbucket")
    |> range(start: 0, stop: now())
    |> filter(fn: (r) => r.hostname == "host_0" and r._measurement == "redis" and r._field == "sync_full")
    |> drop(columns: ["_start", "_stop"])