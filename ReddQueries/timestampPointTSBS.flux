// Timestamp point 
from(bucket: "irregularbucket")
    |> range(start: 1303134414000, stop: 1303134414000)
    |> filter(fn: (r) => r._measurement == "7768" and r._time == 1303134414000, onEmpty: "drop")
    |> drop(columns: ["_start", "_stop"])