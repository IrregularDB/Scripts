select avg(value), bucketNumber * 300000 as startTime, bucketNumber * 300000 + 300000 as endTime from (select value, DATEDIFF(ms, '1970-01-01 00:00:00', timestamp)/300000 as bucketNumber from datapoint where tid = 20 and timestamp >= DATEADD('MILLISECOND', 1451606400000, DATE '1970-01-01') and timestamp <= DATEADD('MILLISECOND', 1451649600000, DATE '1970-01-01') ) group by bucketNumber;
select avg(value), bucketNumber * 300000 as startTime, bucketNumber * 300000 + 300000 as endTime from (select value, DATEDIFF(ms, '1970-01-01 00:00:00', timestamp)/300000 as bucketNumber from datapoint where tid = 20 and timestamp >= DATEADD('MILLISECOND', 1451606400000, DATE '1970-01-01') and timestamp <= DATEADD('MILLISECOND', 1451649600000, DATE '1970-01-01') ) group by bucketNumber;
select avg(value), bucketNumber * 300000 as startTime, bucketNumber * 300000 + 300000 as endTime from (select value, DATEDIFF(ms, '1970-01-01 00:00:00', timestamp)/300000 as bucketNumber from datapoint where tid = 20 and timestamp >= DATEADD('MILLISECOND', 1451606400000, DATE '1970-01-01') and timestamp <= DATEADD('MILLISECOND', 1451649600000, DATE '1970-01-01') ) group by bucketNumber;
select avg(value), bucketNumber * 300000 as startTime, bucketNumber * 300000 + 300000 as endTime from (select value, DATEDIFF(ms, '1970-01-01 00:00:00', timestamp)/300000 as bucketNumber from datapoint where tid = 20 and timestamp >= DATEADD('MILLISECOND', 1451606400000, DATE '1970-01-01') and timestamp <= DATEADD('MILLISECOND', 1451649600000, DATE '1970-01-01') ) group by bucketNumber;
select avg(value), bucketNumber * 300000 as startTime, bucketNumber * 300000 + 300000 as endTime from (select value, DATEDIFF(ms, '1970-01-01 00:00:00', timestamp)/300000 as bucketNumber from datapoint where tid = 20 and timestamp >= DATEADD('MILLISECOND', 1451606400000, DATE '1970-01-01') and timestamp <= DATEADD('MILLISECOND', 1451649600000, DATE '1970-01-01') ) group by bucketNumber;

