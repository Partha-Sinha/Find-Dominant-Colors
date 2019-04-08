# Find-Dominant-Colors
Finding dominant colors in an Image using K-Means Clustering Algorithm

### Environment:
  1. Python 3
  2. Libraries: scikit_learn, numpy, openCV, collections
  3. OS: Linux ( Ubuntu 18 )

### Approach:
  1. At first, I converted the RGB image to HSV image
  2. Then I tried to eliminate the Neutral Colors by adjusting the lower and upper bounds to filter color using trail and error method
  3. Used K-Means clustering to get 5 dominating colors from the image
  4. Used Centroid Pie chart to represent the dominant colors and their respective HEX codes
