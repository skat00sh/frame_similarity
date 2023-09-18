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




def calculate_similarity_scores(cmpr_pairs):
    counter = 0
    # score = []
    duplicate_frame = []
    prev_frame = preprocess_image_change_detection(cv2.imread(cmpr_pairs[0]))
    next_frame = preprocess_image_change_detection(cv2.imread(cmpr_pairs[1]))
    if prev_frame.shape == next_frame.shape:
        results = compare_frames_change_detection(prev_frame, next_frame, min_contour_area=10)
        # save_frames([prev_frame, next_frame], cmpr_pairs) if results[0] > 0.0 else save_frames(prev_frame, cmpr_pairs[0])
        if results[0] < 10000: 
            duplicate_frame = cmpr_pairs[0]
            # results[3] = cmpr_pairs[0] 
        return (results[0],duplicate_frame)
  

      

def find_similars_all(data_dir):
    print("Finding similar images...\n")
    results = []
    scores = []
    
    duplicate_frames = []
    similarImg = []         # a list that stores similar images
    image_paths = glob.glob(f"{data_dir}/*")
    with multiprocessing.Pool(8) as p:
        image_paths = p.map(check_none_img, image_paths)
    image_paths = [i for i in image_paths if i is not None]
    cmprPairsList = get_cmpr_pairs_list(image_paths)       
    cmprPairsCount = len(cmprPairsList)

    start = time.process_time()
    with multiprocessing.Pool(8) as p :
        print("Total images to compare : {} images\n".format(cmprPairsCount))
        results = p.map(calculate_similarity_scores, cmprPairsList)
    end = time.process_time()
    print(f"Score generation :{end-start}")
    scores = [i[0] for i in results if i is not None]
    duplicate_frame  = [i[1] for i in results if i != None and i[1] != []]
    duplicate_frame = list(set(duplicate_frame))
    for i in duplicate_frame:
        os.remove(i)
    # plt.plot(scores)
    # plt.show
    print(len(scores))

    print("\nDone searching for similar images!")


if __name__ == '__main__':
    find_similars_all(conf.default_config)

