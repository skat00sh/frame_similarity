import cv2



def get_cmpr_pairs_list(image_paths):
    cmprPairsList = []
    for i in range(0, len(image_paths)):
        for j in range(i+1, len(image_paths)):
            cmprPairsList.append( [image_paths[i], image_paths[j]] )
    return cmprPairsList


def check_none_img(img_path):
    if cv2.imread(img_path) is not None:
        return img_path