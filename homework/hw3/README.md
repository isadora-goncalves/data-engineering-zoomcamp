CREATE OR REPLACE VIEW `data-zoomcamp-isadora.nytaxi.yellow_tripdata_2024_vw` AS
SELECT * FROM `data-zoomcamp-isadora.nytaxi.yellow_tripdata_2024-01_raw`
UNION ALL
SELECT * FROM `data-zoomcamp-isadora.nytaxi.yellow_tripdata_2024-02_raw`
UNION ALL
SELECT * FROM `data-zoomcamp-isadora.nytaxi.yellow_tripdata_2024-03_raw`
UNION ALL
SELECT * FROM `data-zoomcamp-isadora.nytaxi.yellow_tripdata_2024-04_raw`
UNION ALL
SELECT * FROM `data-zoomcamp-isadora.nytaxi.yellow_tripdata_2024-05_raw`
UNION ALL
SELECT * FROM `data-zoomcamp-isadora.nytaxi.yellow_tripdata_2024-06_raw`
UNION ALL
SELECT * FROM `data-zoomcamp-isadora.nytaxi.yellow_tripdata_2024-07_raw`
UNION ALL
SELECT * FROM `data-zoomcamp-isadora.nytaxi.yellow_tripdata_2024-08_raw`
UNION ALL
SELECT * FROM `data-zoomcamp-isadora.nytaxi.yellow_tripdata_2024-09_raw`
UNION ALL
SELECT * FROM `data-zoomcamp-isadora.nytaxi.yellow_tripdata_2024-10_raw`
UNION ALL
SELECT * FROM `data-zoomcamp-isadora.nytaxi.yellow_tripdata_2024-11_raw`
UNION ALL
SELECT * FROM `data-zoomcamp-isadora.nytaxi.yellow_tripdata_2024-12_raw`;


Q1
SELECT count(tpep_pickup_datetime) FROM `data-zoomcamp-isadora.nytaxi.yellow_tripdata_2024_vw`

41169720


Q4
SELECT count(tpep_pickup_datetime) FROM `data-zoomcamp-isadora.nytaxi.yellow_tripdata_2024_vw` where fare_amount = 0

17260
