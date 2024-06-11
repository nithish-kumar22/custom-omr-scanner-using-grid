import cv2
import numpy as np
from imutils.perspective import four_point_transform

from .constants import (
    ANSWER_SHEET_COORDINATES,
    MAX_FEATURES,
    GOOD_MATCH_PERCENT,
    PERSPECTIVE_TRANSFORM_POINTS,
    PERSPECTIVE_TRANSFORM_Y_TOP_PADDING_VAL,
)
from .image_utils import binarize_answer_sheet


def align_image_based_on_ref(image: np.ndarray) -> np.ndarray:
    """
    Aligns the image based on the reference image (bg.png)
    from the data folder.
    """

    ref_image = cv2.imread("data/bg.png")

    # Convert images to grayscale
    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    ref_image_gray = cv2.cvtColor(ref_image, cv2.COLOR_BGR2GRAY)

    # Detect ORB features and compute descriptors.
    orb = cv2.ORB_create(MAX_FEATURES)
    keypoints1, descriptors1 = orb.detectAndCompute(image_gray, None)
    keypoints2, descriptors2 = orb.detectAndCompute(ref_image_gray, None)

    # Match features.
    matcher = cv2.DescriptorMatcher_create(cv2.DESCRIPTOR_MATCHER_BRUTEFORCE_HAMMING)
    matches = list(matcher.match(descriptors1, descriptors2, None))

    # Sort matches by score
    matches.sort(key=lambda x: x.distance, reverse=False)

    # Remove not so good matches
    numGoodMatches = int(len(matches) * GOOD_MATCH_PERCENT)
    matches = matches[:numGoodMatches]

    points1 = np.zeros((len(matches), 2), dtype=np.float32)
    points2 = np.zeros((len(matches), 2), dtype=np.float32)

    for i, match in enumerate(matches):
        points1[i, :] = keypoints1[match.queryIdx].pt
        points2[i, :] = keypoints2[match.trainIdx].pt

    # Find homography
    h, mask = cv2.findHomography(points1, points2, cv2.RANSAC)

    # Use homography
    height, width, channels = ref_image.shape
    return cv2.warpPerspective(image, h, (width, height))


def extract_answer_sheet(img: np.ndarray, binarize: bool = True) -> np.ndarray:
    """
    Extracts the answer sheet from the image
    """
    image = align_image_based_on_ref(img)
    x1, y1, x2, y2 = ANSWER_SHEET_COORDINATES
    answer_sheet = image[y1:y2, x1:x2]

    warped_image = four_point_transform(answer_sheet, PERSPECTIVE_TRANSFORM_POINTS)
    warped_image = warped_image[PERSPECTIVE_TRANSFORM_Y_TOP_PADDING_VAL:, :]

    if binarize:
        return binarize_answer_sheet(warped_image).copy()

    return warped_image.copy()
