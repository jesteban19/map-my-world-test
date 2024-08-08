-- Script para crear las tablas en SQLite


CREATE TABLE IF NOT EXISTS categories (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE
);


CREATE TABLE IF NOT EXISTS locations (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    latitude REAL NOT NULL,
    longitude REAL NOT NULL,
    UNIQUE(latitude, longitude)
);

CREATE TABLE IF NOT EXISTS location_category_reviewed (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    location_id INTEGER NULL,
    category_id INTEGER NULL,
    last_reviewed_at TIMESTAMP NULL,
    FOREIGN KEY(location_id) REFERENCES locations(id) ON DELETE CASCADE,
    FOREIGN KEY(category_id) REFERENCES categories(id) ON DELETE CASCADE,
    UNIQUE(location_id, category_id)
);


-- datos de pruebas
-- Insertar registros en 'locations'
INSERT INTO locations (latitude, longitude)
VALUES
    (40.712776, -74.005974),   -- Nueva York
    (34.052235, -118.243683),  -- Los Ángeles
    (41.878113, -87.629799),   -- Chicago
    (29.760427, -95.369804),   -- Houston
    (39.099727, -94.578568),   -- Kansas City
    (37.774929, -122.419418),  -- San Francisco
    (47.606209, -122.332069),  -- Seattle
    (25.761680, -80.191820),   -- Miami
    (32.715736, -117.161087),  -- San Diego
    (33.448376, -112.074036),  -- Phoenix
    (40.730610, -73.935242),   -- Nueva York 2
    (34.052235, -118.243684),  -- Los Ángeles 2
    (41.878114, -87.629800),   -- Chicago 2
    (29.760428, -95.369805),   -- Houston 2
    (39.099728, -94.578569),   -- Kansas City 2
    (37.774930, -122.419419),  -- San Francisco 2
    (47.606210, -122.332070),  -- Seattle 2
    (25.761681, -80.191821),   -- Miami 2
    (32.715737, -117.161088),  -- San Diego 2
    (33.448377, -112.074037),  -- Phoenix 2
    (40.712777, -74.005975),   -- Nueva York 3
    (34.052236, -118.243685),  -- Los Ángeles 3
    (41.878115, -87.629801),   -- Chicago 3
    (29.760429, -95.369806),   -- Houston 3
    (39.099729, -94.578570),   -- Kansas City 3
    (37.774931, -122.419420),  -- San Francisco 3
    (47.606211, -122.332071),  -- Seattle 3
    (25.761682, -80.191822),   -- Miami 3
    (32.715738, -117.161089),  -- San Diego 3
    (33.448378, -112.074038),  -- Phoenix 3
    (40.712778, -74.005976),   -- Nueva York 4
    (34.052237, -118.243686),  -- Los Ángeles 4
    (41.878116, -87.629802),   -- Chicago 4
    (29.760430, -95.369807),   -- Houston 4
    (39.099730, -94.578571),   -- Kansas City 4
    (37.774932, -122.419421),  -- San Francisco 4
    (47.606212, -122.332072),  -- Seattle 4
    (25.761683, -80.191823),   -- Miami 4
    (32.715739, -117.161090),  -- San Diego 4
    (33.448379, -112.074039),  -- Phoenix 4
    (40.712779, -74.005977),   -- Nueva York 5
    (34.052238, -118.243687),  -- Los Ángeles 5
    (41.878117, -87.629803),   -- Chicago 5
    (29.760431, -95.369808),   -- Houston 5
    (39.099731, -94.578572),   -- Kansas City 5
    (37.774933, -122.419422),  -- San Francisco 5
    (47.606213, -122.332073),  -- Seattle 5
    (25.761684, -80.191824),   -- Miami 5
    (32.715740, -117.161091),  -- San Diego 5
    (33.448380, -112.074040);  -- Phoenix 5

-- Insertar registros en 'location_category_reviewed' con fechas variadas
INSERT INTO location_category_reviewed (location_id, category_id, last_reviewed_at)
VALUES
    (1, 1, '2024-08-01 12:00:00'),
    (2, 2, '2024-08-05 12:00:00'),
    (3, 3, '2024-07-25 12:00:00'),
    (4, 4, '2024-07-20 12:00:00'),
    (5, 5, '2024-06-30 12:00:00'),
    (6, 6, '2024-05-15 12:00:00'),
    (7, 7, '2024-04-10 12:00:00'),
    (8, 8, '2024-03-20 12:00:00'),
    (9, 9, '2024-02-14 12:00:00'),
    (10, 10, '2024-01-01 12:00:00'),
    (11, 1, '2024-08-02 12:00:00'),
    (12, 2, '2024-08-06 12:00:00'),
    (13, 3, '2024-07-26 12:00:00'),
    (14, 4, '2024-07-21 12:00:00'),
    (15, 5, '2024-07-01 12:00:00'),
    (16, 6, '2024-05-16 12:00:00'),
    (17, 7, '2024-04-11 12:00:00'),
    (18, 8, '2024-03-21 12:00:00'),
    (19, 9, '2024-02-15 12:00:00'),
    (20, 10, '2024-01-02 12:00:00'),
    (21, 1, '2024-08-03 12:00:00'),
    (22, 2, '2024-08-07 12:00:00'),
    (23, 3, '2024-07-27 12:00:00'),
    (24, 4, '2024-07-22 12:00:00'),
    (25, 5, '2024-07-02 12:00:00'),
    (26, 6, '2024-05-17 12:00:00'),
    (27, 7, '2024-04-12 12:00:00'),
    (28, 8, '2024-03-22 12:00:00'),
    (29, 9, '2024-02-16 12:00:00'),
    (30, 10, '2024-01-03 12:00:00'),
    (31, 1, '2024-08-04 12:00:00'),
    (32, 2, '2024-08-08 12:00:00'),
    (33, 3, '2024-07-28 12:00:00'),
    (34, 4, '2024-07-23 12:00:00'),
    (35, 5, '2024-07-03 12:00:00'),
    (36, 6, '2024-05-18 12:00:00'),
    (37, 7, '2024-04-13 12:00:00'),
    (38, 8, '2024-03-23 12:00:00'),
    (39, 9, '2024-02-17 12:00:00'),
    (40, 10, '2024-01-04 12:00:00'),
    (41, 1, '2024-08-09 12:00:00'),
    (42, 2, '2024-08-10 12:00:00'),
    (43, 3, '2024-07-29 12:00:00'),
    (44, 4, '2024-07-24 12:00:00'),
    (45, 5, '2024-07-04 12:00:00'),
    (46, 6, '2024-05-19 12:00:00'),
    (47, 7, '2024-04-14 12:00:00'),
    (48, 8, '2024-03-24 12:00:00'),
    (49, 9, '2024-02-18 12:00:00'),
    (50, 10, '2024-01-05 12:00:00');