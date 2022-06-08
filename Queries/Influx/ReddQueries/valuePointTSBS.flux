// Value point: All values with specific value
from(bucket: "irregularbucket")
    |> range(start: 0, stop: now())
    |> filter(fn: (r) => r._measurement == "996" and r._value == 318.5475612997497, onEmpty: "drop")
    |> drop(columns: ["_start", "_stop"])