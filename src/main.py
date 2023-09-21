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
from tqdm import tqdm




def calculate_similarity_scores(prev_img, next_img) -> tuple:
    """Calculates similarity scores and path of duplicate frame to be deleted

    Args:
        cmpr_pairs (list): (prev and next frame parh)

    Returns:
        tuple: score from frame comparison and path of duplicate frame to be removed
    """
    
    method_start_time = time.perf_counter()
    SCORE_THRESHOLD = conf.default_config['score_threshold']
    duplicate_frame = []
    
    
    
    if prev_img.shape == next_img.shape:
        bottleneck_start_time = time.perf_counter()

        results = compare_frames_change_detection(prev_img, next_img, min_contour_area=10)
        bottleneck_end_time = time.perf_counter()
        if results[0] < SCORE_THRESHOLD: 
            duplicate_frame = True
    
        method_end_time = time.perf_counter()
        total_method_time =  method_end_time - method_start_time
        total_bottleneck_time =  bottleneck_end_time - bottleneck_start_time
        
        return (results[0],duplicate_frame)
  

      

def find_similars_all(data_dir: str) -> None:
    """Finds similar frames and removes from the dir

    Args:
        data_dir (str): 
    """
    
    print("Finding similar images...\n")
    results = []
    scores = []
    duplicate_frames = []
    
    image_paths = glob.glob(f"{data_dir}/*")
    with multiprocessing.Pool(8) as p:
        images_and_paths = p.map(check_none_img, image_paths)
    image_paths = [i[1] for i in images_and_paths if i[1] is not None]
    images = [i[0] for i in images_and_paths if i[0] is not None]

    cmpr_pairs_tuples = get_cmpr_pairs_list(image_paths)       
    
    for i in tqdm(cmpr_pairs_tuples):
        results = calculate_similarity_scores(images[i[0]], images[i[1]])
        if results[1] == True:
            duplicate_frames.append(image_paths[i[0]])
        

    
    print(f"\nRemoving duplicate frames from: {data_dir}")
    # Uncomment only when you want to delete images from the directory
    # for i in duplicate_frames:
    #     os.remove(i)


    print("\nDone searching for similar images!")


if __name__ == '__main__':
    CONFIG = conf.default_config
    find_similars_all(conf.default_config['dataset'])

