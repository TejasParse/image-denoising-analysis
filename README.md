# BRISQUE Based Image Denoising  
## Abstract  
Our Main Goal is to denoise the images. We used BRISQUE score to categorize images and we pick a denoising algorithm based on the score obtained.  
## Datasets Used  
 - SIDD
 - LIVE
 - CSIQ
 - TID13  

*Only Noisy images were used for this experiment  
## Denoising Algorithms  
 - Weiner Filtering (Kernel size = 5)
 - Gaussian Filtering (sigma=0.6)
 - Median Filtering (Kernel size = 5)
 - Wavelet Transform
 - [NAFNet](https://github.com/megvii-research/NAFNet)
 - [MIRNet](https://github.com/swz30/MIRNetv2)

## Our Methodology  
![Image](/Methodology%20Overview.png)  

## Research  
1. Applied the denoising algorithms on the images to all the images. All the results are in [Analysis Folder](/analysis/) 
2. Grouped the data based on theri BRISQUE Score and found the average and median for each methodology for each range for each dataset. All the results are in [Conclusion Folder](/conclusion/).
3. Took the weighted average for each method among all datasets in that particular range. For that range, pick the method with lowest negative weight average. Negative average signifies improved image quality. All results are in [Final Analysis.xlsx](/Final%20Analysis.xlsx)  

## Results  
For BRISQUE Score in range [Low, High) the particular method size is applied
|   Low(>=) |   High(<) | Best Method   |
|------:|-------:|:--------------|
|     1 |      6 | Weiner        |
|     6 |     11 | Wavelet       |
|    11 |     16 | Weiner        |
|    16 |     21 | Weiner        |
|    21 |     26 | Weiner        |
|    26 |     31 | Weiner        |
|    31 |     36 | Weiner        |
|    36 |     41 | Gaussian      |
|    41 |     46 | Gaussian      |
|    46 |     51 | Gaussian      |
|    51 |     56 | Gaussian      |
|    56 |     61 | Gaussian      |
|    61 |     66 | Gaussian      |
|    66 |     71 | Gaussian      |
|    71 |     76 | Gaussian      |
|    76 |     81 | Gaussian      |
|    81 |     86 | Gaussian      |
|    86 |     91 | Gaussian      |
|    91 |     96 | Gaussian      |
|    96 |    101 | Gaussian      |
|   101 |    106 | Gaussian      |
|   106 |    111 | NAFNet        |
|   111 |    116 | MIRNet        |
|   116 |    121 | MIRNet        |
|   121 |    126 | Gaussian      |
|   126 |    131 | Gaussian      |
|   131 |    136 | Gaussian      |
|   136 |    141 | MIRNet        |
|   141 |    146 | MIRNet        |
|   146 |    151 | MIRNet        |
|   151 |    156 | MIRNet        |
|   156 |    161 | MIRNet        |