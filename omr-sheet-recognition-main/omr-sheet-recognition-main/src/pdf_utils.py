from pathlib import Path

import cv2
import imutils
import numpy as np
from pdf2image import convert_from_path
from PIL import Image
import typing


def get_page_as_opencv_image(page: Image, width: int = 800) -> np.ndarray:
    """
    Get a page from a PDF as an OpenCV image
    """
    np_img = np.array(page)
    cv_img = cv2.cvtColor(np_img, cv2.COLOR_RGB2BGR)
    return imutils.resize(cv_img, width=width)


def get_page_from_pdf(pdf_path: Path, page_number: int, width: int = 800) -> np.ndarray:
    """
    Get a page from a PDF as an OpenCV image
    """
    pages = convert_from_path(pdf_path)
    page = pages[page_number]
    return get_page_as_opencv_image(page, width)


def get_images_from_pdf(pdf_path: Path, width: int = 800) -> typing.List[np.ndarray]:
    """
    Get all pages from a PDF as OpenCV images
    """
    pages = convert_from_path(pdf_path)
    return [get_page_as_opencv_image(page, width) for page in pages]
