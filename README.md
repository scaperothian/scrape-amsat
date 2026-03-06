# Scrape AMSAT webpage for satellite status

Pull from the status table on AMSAT and get a top ten most active satellites just for funsies.

## Installation

Install Deps with Poetry (need to have that installed first
```
poetry install
```

## Runtime

Run scrape_amsat.py
```
poetry run python src/scrape_amsat.py
```

Output should look something like this...
```
         Satellite  Activity
0         ISS_[FM]        11
1      AO-123_[FM]         8
2      RS-44_[V/u]         8
3       AO-7_[U/v]         7
4      SO-125_[FM]         7
5       SO-50_[FM]         7
6      JO-97_[U/v]         4
7      AO-73_[U/v]         3
8  SONATE-2_[APRS]         3
9       AO-7_[V/a]         1
```
