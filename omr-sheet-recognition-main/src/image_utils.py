import cv2
import numpy as np

from src.constants import (
    X_START,
    Y_START,
    QN_GROUP_X_OFFSET,
    QN_GROUP_Y_OFFSET,
    ANS_W,
    ANS_H,
)


def binarize_answer_sheet(img: np.ndarray) -> np.ndarray:
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (5, 5), 0)
    _, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
    return thresh


def get_answer_box(row: int, col: int, qn_group_index: int, ans_index: int):
    """
    Get the coordinates of the answer box from the row, column,
     question group index, and answer index
    """
    x = X_START + (col * QN_GROUP_X_OFFSET)
    y = Y_START + (row * QN_GROUP_Y_OFFSET)

    ans_x1 = x + (ans_index * ANS_W)
    ans_y1 = y + (qn_group_index * ANS_H)
    ans_x2 = ans_x1 + ANS_W
    ans_y2 = ans_y1 + ANS_H

    return ans_x1, ans_y1, ans_x2, ans_y2


def is_answer_box_marked(
    img: np.ndarray,
    row: int,
    col: int,
    qn_group_index: int,
    ans_index: int,
    threshold: int = 50,
) -> bool:
    """
    Checks if the answer box is marked by checking the number of black pixels
    """

    x1, y1, x2, y2 = get_answer_box(row, col, qn_group_index, ans_index)

    answer_box = img[y1:y2, x1:x2]

    gray = cv2.dilate(answer_box, (1, 1), iterations=1)
    _, gray_thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    return np.count_nonzero(gray_thresh == 0) > threshold
