import cv2
from PIL import Image
from imaging_interview import preprocess_image_change_detection, compare_frames_change_detection
import glob
import time
import multiprocessing
from pathlib import Path
import os
import conf
from utils import check_none_img, get_cmpr_pairs_list




def calculate_similarity_scores(cmpr_pairs: list) -> tuple:
    """Calculates similarity scores and path of duplicate frame to be deleted

    Args:
        cmpr_pairs (list): (prev and next frame parh)

    Returns:
        tuple: score from frame comparison and path of duplicate frame to be removed
    """
    
    SCORE_THRESHOLD = conf.default_config['score_threshold']
    duplicate_frame = []
    
    prev_frame = preprocess_image_change_detection(cv2.imread(cmpr_pairs[0]))
    next_frame = preprocess_image_change_detection(cv2.imread(cmpr_pairs[1]))
    
    if prev_frame.shape == next_frame.shape:
        results = compare_frames_change_detection(prev_frame, next_frame, min_contour_area=10)
        if results[0] < SCORE_THRESHOLD: 
            duplicate_frame = cmpr_pairs[0]
            
        return (results[0],duplicate_frame)
  

      

def find_similars_all(data_dir: str) -> None:
    """Finds similar frames and removes from the dir

    Args:
        data_dir (str): 
    """
    
    print("Finding similar images...\n")
    results = []
    scores = []
    
    image_paths = glob.glob(f"{data_dir}/*")
    with multiprocessing.Pool(8) as p:
        image_paths = p.map(check_none_img, image_paths)
    image_paths = [i for i in image_paths if i is not None]
    cmpr_pairs_list = get_cmpr_pairs_list(image_paths)       
    cmpr_pairs_count = len(cmpr_pairs_list)

   
    with multiprocessing.Pool(8) as p :
        print("Total images to compare : {} images\n".format(cmpr_pairs_count))
        results = p.map(calculate_similarity_scores, cmpr_pairs_list)

    scores = [i[0] for i in results if i is not None]
    duplicate_frames  = [i[1] for i in results if i != None and i[1] != []]
    duplicate_frames = list(set(duplicate_frames))
    
    print(f"\nRemoving duplicate frames from: {data_dir}")
    for i in duplicate_frames:
        os.remove(i)


    print("\nDone searching for similar images!")


if __name__ == '__main__':
    CONFIG = conf.default_config
    find_similars_all(conf.default_config['dataset'])

