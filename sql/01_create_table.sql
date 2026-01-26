CREATE SCHEMA IF NOT EXISTS usgs;

DROP TABLE IF EXISTS usgs.earthquakes;

CREATE TABLE usgs.earthquakes (
  event_id    TEXT PRIMARY KEY,
  time        TIMESTAMPTZ,
  updated     TIMESTAMPTZ,
  magnitude   DOUBLE PRECISION,
  magtype     TEXT,
  location    TEXT,
  event_type  TEXT,
  latitude    DOUBLE PRECISION,
  longitude   DOUBLE PRECISION,
  depth_km    DOUBLE PRECISION,
  status      TEXT,
  year        INTEGER,
  month       TEXT,
  day         DATE
);
