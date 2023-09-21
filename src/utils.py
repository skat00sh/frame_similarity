import cv2
from imaging_interview import preprocess_image_change_detection



def get_cmpr_pairs_list(image_paths: list):
    """Calculates image comparison pairs. Described in readme

    Args:
        image_paths (list): 

    Returns:
        _type_: comparison pairs
    """
    cmpr_tuple = list(tuple())
    for i in range(0, len(image_paths)):
        for j in range(i+1, len(image_paths)):
            cmpr_tuple.append((i,j))
    return cmpr_tuple


def check_none_img(img_path: str) -> str:
    """Checks if an image is corrupted or not

    Args:
        img_path (str): 

    Returns:
        str:
    """
    img = cv2.imread(img_path)
    if img is not None:
        img = cv2.resize(img, (400,400))
        img = preprocess_image_change_detection(img)
        return (img , img_path)
    else:
        return (None, None)