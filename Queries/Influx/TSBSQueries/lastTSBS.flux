// Last
from(bucket: "irregularbucket")
    |> range(start: 0, stop: now())
    |> last()
    |> drop(columns: ["_start", "_stop"])