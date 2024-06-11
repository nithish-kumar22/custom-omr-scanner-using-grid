# Constants that are used throughout the project

import numpy as np

# -------------------------------- #
# Answer sheet extraction constants #

# The coordinates of the four corners of the answer sheet
ANSWER_SHEET_COORDINATES = np.array(
    [
        90,
        670,
        1560,
        2220,
    ]
)

# The corner points on the answer sheet that should be used
# for perspective transform
PERSPECTIVE_TRANSFORM_POINTS = np.array(
    [
        [10, 9],
        [6, 1538],
        [1456, 1540],
        [1463, 7],
    ]
)

# Padding value for the top of the answer sheet
# that should be removed after perspective transform
PERSPECTIVE_TRANSFORM_Y_TOP_PADDING_VAL = 38

# ------------------------ #
# ORB algorithm constants #

# Maximum number of features to detect in the ORB algorithm
MAX_FEATURES = 1000

# The percentage of good matches to keep in the ORB algorithm
GOOD_MATCH_PERCENT = 0.15


# ------------------------ #
# Grid constants #

# Number of groups of questions
ROWS = 6
COLS = 4

# Number of questions per group
QUESTIONS_PER_GROUP = 5
ANSWERS_PER_QUESTION = 5


# ------------------------ #
# Answer sheet constants #

# Top left corner of the answer sheet
X_START = 55
Y_START = 0

# Width and height of a question group
QN_GROUP_W = 200
QN_GROUP_H = 196

# Space between question groups
QN_GROUP_X_OFFSET = 199 + QN_GROUP_W
QN_GROUP_Y_OFFSET = 64 + QN_GROUP_H

# Width and height of an answer box
ANS_W = QN_GROUP_W // 5
ANS_H = QN_GROUP_H // 5


ANSWER_KEY = {i: chr(ord("A") + i) for i in range(ANSWERS_PER_QUESTION)}

REVERSE_ANSWER_KEY = {v: k for k, v in ANSWER_KEY.items()}
