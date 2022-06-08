#!/bin/sh

for i in 1 2 3 4 5
do
	/srv/data6/IrregularDB/influxdb2-client-2.3.0-linux-amd64/influx query --file /srv/data3/IrregularDB/InfluxDB/tsbsQueriesInflux/1-meanTSBS.flux
	sleep 3
done


for i in 1 2 3 4 5
do
	/srv/data6/IrregularDB/influxdb2-client-2.3.0-linux-amd64/influx query --file /srv/data3/IrregularDB/InfluxDB/tsbsQueriesInflux/5-maxTSBS.flux
	sleep 3
done


for i in 1 2 3 4 5
do
	/srv/data6/IrregularDB/influxdb2-client-2.3.0-linux-amd64/influx query --file /srv/data3/IrregularDB/InfluxDB/tsbsQueriesInflux/lastTSBS.flux
	sleep 3
done


for i in 1 2 3 4 5
do
	/srv/data6/IrregularDB/influxdb2-client-2.3.0-linux-amd64/influx query --file /srv/data3/IrregularDB/InfluxDB/tsbsQueriesInflux/highValueTSBS.flux
	sleep 3
done


for i in 1 2 3 4 5
do
	/srv/data6/IrregularDB/influxdb2-client-2.3.0-linux-amd64/influx query --file /srv/data3/IrregularDB/InfluxDB/tsbsQueriesInflux/timestampPointTSBS.flux
	sleep 3
done


for i in 1 2 3 4 5
do
	/srv/data6/IrregularDB/influxdb2-client-2.3.0-linux-amd64/influx query --file /srv/data3/IrregularDB/InfluxDB/tsbsQueriesInflux/valuePointTSBS.flux
	sleep 3
done


for i in 1 2 3 4 5
do
	/srv/data6/IrregularDB/influxdb2-client-2.3.0-linux-amd64/influx query --file /srv/data3/IrregularDB/InfluxDB/tsbsQueriesInflux/entireTsTSBS.flux
	sleep 3
done
