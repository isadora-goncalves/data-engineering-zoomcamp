# Module 2 Homework — Kestra / NYC Taxi

This repo contains reproducible commands to compute the answers without downloading files to disk (streaming with `wget | gunzip`).

## Helper functions (bash)
> How to run: copy/paste the functions below into your terminal (same shell session), then run the commands shown in each question.

```bash
# Uncompressed size (MiB, 1 decimal)
uncompressed_mib() {
  local taxi="$1" year="$2" month="$3"
  wget -qO- "https://github.com/DataTalksClub/nyc-tlc-data/releases/download/${taxi}/${taxi}_tripdata_${year}-${month}.csv.gz" \
    | gunzip -c \
    | wc -c \
    | awk '{printf "%.1f MiB\n", $1/1024/1024}'
}

# Count data rows (excluding header) for a single month
count_rows_month() {
  local taxi="$1" year="$2" month="$3"
  wget -qO- "https://github.com/DataTalksClub/nyc-tlc-data/releases/download/${taxi}/${taxi}_tripdata_${year}-${month}.csv.gz" \
    | gunzip -c \
    | tail -n +2 \
    | wc -l
}

# Sum rows across all months for a given year
count_rows_year() {
  local taxi="$1" year="$2"
  local total=0 m n
  for m in {01..12}; do
    n="$(count_rows_month "$taxi" "$year" "$m")"
    total=$((total + n))
  done
  echo "$total"
}


# Q1. Within the execution for Yellow Taxi data for the year 2020 and month 12: what is the uncompressed file size (i.e. the output file yellow_tripdata_2020-12.csv of the extract task)?
# uncompressed_mib yellow 2020 12
# 128.3 MiB

# Q3. How many rows are there for the Yellow Taxi data for all CSV files in the year 2020?
# count_rows_year yellow 2020
# 24648499

# Q4. How many rows are there for the Green Taxi data for all CSV files in the year 2020?
# count_rows_year green 2020
# 1734051

# Q5. How many rows are there for the Yellow Taxi data for the March 2021 CSV file?
# count_rows_month yellow 2021 03
# 1925152