
// 1-12-max
from(bucket: "bucketname")
    |> filter(fn: (r) => r._measurement == "MEASUREMENTID", onEmpty: "drop")
    |> range(start: "StartTime", stop: "StartTime + 12 hours")
    |> window(every: 5m)
    |> max()

// 1-12-avg
from(bucket: "bucketname")
    |> range(start: "StartTime", stop: "StartTime + 12 hours")
    |> filter(fn: (r) => r._measurement == "MEASUREMENTID", onEmpty: "drop")
    |> window(every: 5m)
    |> mean()

// 5-12-max
from(bucket: "bucketname")
    |> range(start: "StartTime", stop: "StartTime + 12 hours")
    |> filter(fn: (r) => r._measurement == "MEASUREMENTID1" 
                        or r._measurement == "MEASUREMENTID2"
                        or r._measurement == "MEASUREMENTID3"
                        or r._measurement == "MEASUREMENTID4"
                        or r._measurement == "MEASUREMENTID5"
                        , onEmpty: "drop")
    |> window(every: 5m)
    |> max()

// Last
from(bucket: "testbucket")
    |> range(start: 0, stop: now())
    |> last()

// Get all values over x for timeseries ts
from(bucket: "testbucket")
    |> range(start: 0, stop: now())
    |> filter(fn: (r) => r._measurement == "house_1-channel_1" and r._value > 69, onEmpty: "drop")

// All values with specific value
from(bucket: "testbucket")
    |> range(start: 0, stop: now())
    |> filter(fn: (r) => r._measurement == "house_1-channel_1" and r._value == 69, onEmpty: "drop")

// Timestamp point 
from(bucket: "testbucket")
    |> range(start: 0, stop: now())
    |> filter(fn: (r) => r._measurement == "house_1-channel_1" and r._time == 69, onEmpty: "drop")

// Entire ts
from(bucket: "testbucket")
    |> range(start: 0, stop: now())
    |> filter(fn: (r) => r._measurement == "tsid")