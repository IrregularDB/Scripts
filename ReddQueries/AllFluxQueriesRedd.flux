// 1-12-mean
from(bucket: "irregularbucket")
    |> range(start: 1303002992, stop: 1303046192)
    |> filter(fn: (r) => r._measurement == "9")
    |> window(every: 5m)
    |> mean()

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

// Last
from(bucket: "irregularbucket")
    |> range(start: 0, stop: now())
    |> last()
    |> drop(columns: ["_start", "_stop"])

// High value: Get all values over x for timeseries ts
from(bucket: "irregularbucket")
    |> range(start: 0, stop: now())
    |> filter(fn: (r) => r._measurement == "456" and r._value > 13318.5, onEmpty: "drop")
    |> drop(columns: ["_start", "_stop"])

// Timestamp point 
from(bucket: "irregularbucket")
    |> range(start: 1303134414000, stop: 1303134414000)
    |> filter(fn: (r) => r._measurement == "7768" and r._time == 1303134414000, onEmpty: "drop")
    |> drop(columns: ["_start", "_stop"])

// Value point: All values with specific value
from(bucket: "irregularbucket")
    |> range(start: 0, stop: now())
    |> filter(fn: (r) => r._measurement == "996" and r._value == 318.5475612997497, onEmpty: "drop")
    |> drop(columns: ["_start", "_stop"])

// Entire ts
from(bucket: "irregularbucket")
    |> range(start: 0, stop: now())
    |> filter(fn: (r) => r._measurement == "10004")
    |> drop(columns: ["_start", "_stop"])