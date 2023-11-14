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
|     1 |     21 | None          |
|    21 |     36 | Weiner        |
|    36 |    106 | Gaussian      |
|   106 |    111 | NAFNet        |
|   111 |    121 | MIRNet        |
|   121 |    136 | Gaussian      |
|   136 |    161 | MIRNet        |