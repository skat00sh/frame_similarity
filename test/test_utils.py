import cv2

import glob

from src.conf import test_config
from src.utils import get_cmpr_pairs_list
from src.imaging_interview import preprocess_image_change_detection, compare_frames_change_detection



def test_get_cmpr_pairs_list():
    image_paths = glob.glob(f"{test_config['dataset']}/*")
    assert len(get_cmpr_pairs_list(image_paths)) == 1
    


def test_score_gen():
    image_paths = glob.glob(f"{test_config['dataset']}/*")
    img1 = cv2.imread(image_paths[0])
    img1 = preprocess_image_change_detection(img1)
    img2 = cv2.imread(image_paths[1])
    img2 = preprocess_image_change_detection(img2)

    results = compare_frames_change_detection(img1,img2,1.0)
    assert results[0] == 0
