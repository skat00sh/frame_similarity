import cv2



def get_cmpr_pairs_list(image_paths: list) -> list(tuple):
    """Calculates image comparison pairs. Described in readme

    Args:
        image_paths (list): 

    Returns:
        _type_: comparison pairs
    """

    cmpr_pairs_list = []
    for i in range(0, len(image_paths)):
        for j in range(i+1, len(image_paths)):
            cmpr_pairs_list.append( [image_paths[i], image_paths[j]] )
    return cmpr_pairs_list


def check_none_img(img_path: str) -> str:
    """Checks if an image is corrupted or not

    Args:
        img_path (str): 

    Returns:
        str:
    """
    if cv2.imread(img_path) is not None:
        return img_path