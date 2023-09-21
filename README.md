# Frame Similarity
This repo was created as part of recruitment process.
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
#### Building from local Dockerfile
1. Build docker image using `build.sh`  
2. Run the module using `run.sh`
3. Optionally you can also run unit tests using `test.sh`

#### Using Docker pull

1. `docker pull skat00sh/kopernikus_image_similarity:v0.0.1`

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
├── test.sh
```

## Answers to Questions asked
Please answer following questions:
- What did you learn after looking on our dataset?

    Things I learned:
        
        1. There are a lot of similar images and comaparing each-pair is very time consuming. I decided to use two methods to reduce the time:

                a. Using Multi-processing
                b. Calculating image comparison pairs without counting inverses. For eg. to compare [1,2,3,4]
                ```
                1 -> 1   2 -> 1   3 -> 1   4 -> 1 
                1 -> 2   2 -> 2   3 -> 2   4 -> 2
                1 -> 3   2 -> 3   3 -> 3   4 -> 3
                1 -> 4   2 -> 4   3 -> 4   4 -> 4
                ```
                I created a comparison list as:
                ```
                1 -> 2  
                1 -> 3   2 -> 3  
                1 -> 4   2 -> 4   3 -> 4 
                ```
                This reduced the number of comparison from 1080x1080 = 1166400 to 581581 comparisons
        2. Some images are corrupted. So they needed to filtered out as well
        3. Lightning conditions have an impact on comparison score

- How does you program work?

    Described above and both `main.py` and `utils.py` have docstrings to explain. Briefly, it's a 2 step process:

        1. Check for invalid image (parallelized) for all paths
        2. Generate comparison pairs list
        3. Generate scores and duplicate frame path list (parallelized)

- What values did you decide to use for input parameters and how did you ﬁnd these values?

    I wasn't able to test my process on the entire dataset because my laptop consistently ran out of memory when I was using multi-processing and without using multi-processing, it was estimating a time of 5+ hours. So, I tested on a subset and chose a value close to the median score for identifying duplicate frames

- What you would suggest to implement to improve data collection of unique cases in future?
    
    Introducing a conditional data capture when a new object is detected in frame will be helpful. A combination of Object detection and tracking could help achieve that.

- Any other comments about your solution

    1. I could've improved the way I compare further by removing duplicates after every few comparisons, regenrating comparison list instead of deleting all duplicates at the end.

    2. I wanted to implement exception handling at a few places but couldn't do it in time

