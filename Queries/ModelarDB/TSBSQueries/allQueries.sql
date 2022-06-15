
--REDD - DATASET
--@startTime:=1451606400000
--@endTime:=  1451649600000
--@highValue:=90
--@timePoint:=1454075479700
--@valuePoint:=40000
--@lowerBound:= (1 - @error_bound) * @valuePoint
--@upperBound:= (1 + @error_bound) * @valuePoint


-- NO1 1-12:
--Simple aggregrate (AVG) for 1 time series every 5 mins for 12 hours
select avg(value), bucketNumber * 300000 as startTime, bucketNumber * 300000 + 300000 as endTime from (
    select value, DATEDIFF(ms, '1970-01-01 00:00:00', timestamp)/300000 as bucketNumber from datapoint
        where tid = @id1 and timestamp >= DATEADD('MILLISECOND', @startTime, DATE '1970-01-01')
            and timestamp <= DATEADD('MILLISECOND', @endTime, DATE '1970-01-01')
) group by bucketNumber;

--NO2 5-12:
--Simple aggregrate (MAX) for 5 time series every 5 mins for 12 hour
select max(value), bucketNumber from
    (select value, DATEDIFF(ms, '1970-01-01 00:00:00', timestamp)/300000 as bucketNumber from datapoint
     where timestamp >=  DATEADD('MILLISECOND', @startTime, DATE '1970-01-01')
       and timestamp <= DATEADD('MILLISECOND',  @endTime, DATE '1970-01-01')
       and (tid = @id2_1 OR tid = @id2_2 OR tid = @id2_3 OR tid = @id2_4 OR tid = @id2_5)
    ) group by bucketNumber;

--NO3 Last Point
--Get the last data point of each time series
--NOT SUPPORTED
--select dp.* from datapoint dp join (select max(end_time) as time, tid from segment group by tid) maxTimeDp on dp.timestamp = maxTimeDp.time and dp.tid = maxTimeDp.tid;

--NO4 High Value
-- Get all data points with a value above a threshold for a time series
-- calculate lower value using 10% error bound
select * from datapoint where tid = @id4 and value >= @highValue;


-- NO5 Time-point
--All data points with a specified timestamp for a time series
select * from datapoint where tid = @id5 and timestamp = DATEADD('MILLISECOND', @timePoint, DATE '1970-01-01') ;


--NO6 Value-point
--All data points with a specified value for a time series
-- use errorbound to calculate upper and lower bound
select * from datapoint where tid = @id6 and @lowerBound <= value and value <= @upperBound;


--NO7 All
--All data points for 1 time series
select * from datapoint where tid = @id7