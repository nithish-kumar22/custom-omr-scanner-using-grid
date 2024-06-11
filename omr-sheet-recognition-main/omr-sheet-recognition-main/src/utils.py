from itertools import product
import numpy as np
import pandas as pd

from src.constants import (
    ANSWER_KEY,
    ROWS,
    COLS,
    QUESTIONS_PER_GROUP,
    ANSWERS_PER_QUESTION,
)


def get_grid() -> pd.DataFrame:
    """
    Returns a Pandas Dataframe with the following columns:

    1. Index (n)
    2. Row (row)
    3. Column (col)
    4. Question group index (qn_group_index)
    5. Answer index within a question group (ans_index)
    6. Question number (as in the PDF) (qn_num)
    7. Answer A,B,C,D or E (as in the PDF) (ans)
    """
    TOTAL_ANSWERS = ROWS * COLS * QUESTIONS_PER_GROUP * ANSWERS_PER_QUESTION
    grid = np.zeros((TOTAL_ANSWERS, 7), dtype=object)
    for n, [i, j, k, l] in enumerate(
        product(
            range(ROWS),
            range(COLS),
            range(QUESTIONS_PER_GROUP),
            range(ANSWERS_PER_QUESTION),
        )
    ):
        qn_num = i * QUESTIONS_PER_GROUP + j * ROWS * QUESTIONS_PER_GROUP + 1 + k
        grid[n] = [n, i, j, k, l, qn_num, ANSWER_KEY[l]]

    return pd.DataFrame(
        grid,
        columns=[
            "n",
            "row",
            "col",
            "qn_group_index",
            "ans_index",
            "qn_num",
            "ans",
        ],
    ).set_index("n")
