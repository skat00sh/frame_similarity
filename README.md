# Frame Similarity
This repo was created as part of recruitment process for Kopernikus Automotive.
The program removes duplicate frames from video based on a score thresholding approach.


## How to Run
The code was tested on:
```
- python 3.10
- numpy == 1.26
- opencv-python==4.8
```
Please check `requirements.txt` for sub-versions of all the packages

### Conda installation
```bash
conda create -n frame_similarity_env python==3.10
pip install -r requirements.txt
```

### Docker Run
Build docker image using `build.sh` and then run the module using `run.sh`

## Project Structure
1. Set data directory and score thresholf in `conf.py`
```
❯ ROOT
.
├── data
│   └── test_set
│       ├── c10-1623873231583 copy 2.png
│       ├── c10-1623873231583 copy.png
│       └── c10-1623873231583.png
└── src
    ├── conf.py
    ├── imaging_interview.py
    ├── main.py
    └── utils.py
├── build.sh
├── challenge PER.pdf
├── Dockerfile
├── README.md
├── requirements.txt
├── run.sh
```

## Answers to Questions asked

