cube_verticies_vector3 = (
    (1.0000, 1.0000, 1.0000),
    (1.0000, 1.0000, -1.0000),
    (1.0000, -1.0000, 1.0000),
    (1.0000, -1.0000, -1.0000),
    (-1.0000, 1.0000, 1.0000),
    (-1.0000, 1.0000, -1.0000),
    (-1.0000, -1.0000, 1.0000),
    (-1.0000, -1.0000, -1.0000),
)
colors = (
    (1, 1, 1),
    (1, 0, 0),
    (1, 0, 1),
    (0, 1, 1),
    (1, 1, 1),
    (1, 1, 0),
    (1, 1, 1),
    (1, 0, 0),
    (1, 0, 1),
    (0, 1, 1),
    (1, 1, 1),
    (1, 1, 0),
)
cube_edges_vector2 = (
    (5, 7),
    (1, 5),
    (0, 1),
    (7, 6),
    (2, 3),
    (4, 5),
    (2, 6),
    (0, 2),
    (7, 3),
    (6, 4),
    (4, 0),
    (3, 1),
)

cube_faces_vector4 = (
    (0, 4, 6, 2),
    (3, 2, 6, 7),
    (7, 6, 4, 5),
    (5, 1, 3, 7),
    (1, 0, 2, 3),
    (5, 4, 0, 1),
)


MIN_COLOR_VALUE = 0
MAX_COLOR_VALUE = 255
FRAMES_PER_SECOND = 40
ANGLE_INCREMENTOR = 3