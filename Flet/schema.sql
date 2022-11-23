DROP TABLE IF EXISTS profiles;



CREATE TABLE profiles
(
    profile_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    mode TEXT NOT NULL,
    speed TEXT NOT NULL,
    laps TEXT NOT NULL
);
DROP TABLE IF EXISTS defaultprofile;
CREATE TABLE defaultprofile
(
    configured INT,
    mode TEXT,
    speed TEXT,
    laps TEXT
);
INSERT INTO defaultprofile (configured, mode, speed, laps)
VALUES
  (1, 'Automatic', 'Default', 'One Lap' );

DROP TABLE IF EXISTS schedules;

CREATE TABLE schedules
(
    schedule_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    day TEXT,
    time TEXT,
    repetition TEXT,
    profile TEXT,
    mode TEXT,
    speed TEXT,
    laps TEXT
);

