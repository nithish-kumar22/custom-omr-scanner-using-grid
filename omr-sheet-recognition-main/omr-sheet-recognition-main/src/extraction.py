from pathlib import Path

import cv2

from src.image_utils import get_answer_box, is_answer_box_marked
from src.pdf_utils import get_page_from_pdf
from src.transformations import extract_answer_sheet
from src.utils import get_grid


def extract_answers_from_pdf_page(
    pdf_file_path: Path,
    page_number: int,
    threshold: int = 50,
    plot=False,
):
    """
    Extracts answers from a PDF page.
    """

    grid_df = get_grid()

    img = get_page_from_pdf(pdf_file_path, page_number)

    original_answer_sheet = None

    if plot:
        original_answer_sheet = extract_answer_sheet(img, binarize=False)

    answer_sheet = extract_answer_sheet(img, binarize=True)

    answers = {}

    for qn_num, qn_grid_df in grid_df.groupby("qn_num"):
        answers[qn_num] = None

        for i, grid_row in qn_grid_df.iterrows():
            if is_answer_box_marked(
                answer_sheet,
                grid_row["row"],
                grid_row["col"],
                grid_row["qn_group_index"],
                grid_row["ans_index"],
                threshold=threshold,
            ):
                if plot:
                    x1, y1, x2, y2 = get_answer_box(
                        grid_row["row"],
                        grid_row["col"],
                        grid_row["qn_group_index"],
                        grid_row["ans_index"],
                    )
                    cv2.rectangle(
                        original_answer_sheet,
                        (x1, y1),
                        (x2, y2),
                        (0, 255, 0),
                        thickness=2,
                    )

                answers[qn_num] = None if answers[qn_num] else grid_row["ans"]
    if plot:
        return answers, original_answer_sheet

    return answers, None
