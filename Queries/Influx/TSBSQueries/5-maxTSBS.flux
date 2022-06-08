// 5-12-max
from(bucket: "irregularbucket")
    |> range(start: 1451606400, stop: 1451649600)
    |> filter(fn: (r) => r.hostname == "host_0" and r._measurement == "cpu" and r._field == "usage_idle"
                or r.hostname == "host_0" and r._measurement == "mem" and r._field == "used_percent"
                or r.hostname == "host_1" and r._measurement == "cpu" and r._field == "usage_idle"
                or r.hostname == "host_1" and r._measurement == "mem" and r._field == "used_percent"
                or r.hostname == "host_2" and r._measurement == "cpu" and r._field == "usage_idle")
    |> map(fn: (r) => ({r with _value: float(v: r._value)}))
    |> window(every: 5m)
    |> group(columns: ["_start"])
    |> max()