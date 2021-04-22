from .interpolation import interpolation
import math
import numpy as np

class Geometric:
    def __init__(self):
        pass

    def forward_rotate(self, image, theta):

        # Define corner points
        x1 = 0
        y1 = 0

        x2 = len(image)
        y2 = 0

        x3 = 0
        y3 = len(image[0])

        x4 = len(image)
        y4 = len(image[0])

        # Calculate rotated positions for corners
        x1_new = x1 * math.cos(theta) - y1 * math.sin(theta)
        y1_new = x1 * math.sin(theta) + y1 * math.cos(theta)

        x2_new = x2 * math.cos(theta) - y2 * math.sin(theta)
        y2_new = x2 * math.sin(theta) + y2 * math.cos(theta)

        x3_new = x3 * math.cos(theta) - y3 * math.sin(theta)
        y3_new = x3 * math.sin(theta) + y3 * math.cos(theta)

        x4_new = x4 * math.cos(theta) - y4 * math.sin(theta)
        y4_new = x4 * math.sin(theta) + y4 * math.cos(theta)

        # Find min and max x coordinate position
        min_x = min(x1_new, x2_new, x3_new, x4_new)
        max_x = max(x1_new, x2_new, x3_new, x4_new)

        # Find min and max y coordinate position
        min_y = min(y1_new, y2_new, y3_new, y4_new)
        max_y = max(y1_new, y2_new, y3_new, y4_new)

        # # Calculate new image dimensions and create blank grid for new image
        rows = int(max_x - min_x)
        cols = int(max_y - min_y)
        rotated_image = np.zeros([rows,cols])


        # Calculate rotation for each pixel and insert into new imag

        for x in range(0,len(image)):
            for y in range(0,len(image[0])):
                x_rotated = int(x * math.cos(theta) - y * math.sin(theta))
                y_rotated = int(x * math.sin(theta) + y * math.cos(theta))
                x_rotated = x_rotated - int(min_x)-1 # Offset to get position with respect to new grid origin
                y_rotated = y_rotated - int(min_y) # Offset to get position with respect to new grid origin
                if x < rows and y < cols:
                    rotated_image[x_rotated][y_rotated] = image[x][y]
                #
        img = np.array(rotated_image)
        return img


    def reverse_rotation(self, rotated_image, theta, origin, original_shape):
        # Original image shape
        corrected_image = np.zeros(original_shape)
        # Iterate through rotated image
        for i_n in range(0, len(rotated_image)):
            for j_n in range(0, len(rotated_image[0])):
                # Compute i' and j'
                i_prime = i_n - origin[0]
                j_prime = j_n - origin[1]

                # Apply inverse rotation matrix to compute i and j, truncate to whole index number
                i = int( i_prime * math.cos(theta) + j_prime * math.sin(theta))
                j = int( i_prime * -1* math.sin(theta) + j_prime * math.cos(theta))
                # If i and j within original image index, place into image
                if i <original_shape[0] and j < original_shape[1] and i> 0 and j>0:
                    corrected_image[i][j] = rotated_image[i_n][j_n]

        img = np.array(corrected_image)
        return img



    def rotate(self, image, theta, interpolation_type):
        if interpolation_type == "nearest_neighbor":
            x1 = 0
            y1 = 0

            x2 = len(image)
            y2 = 0

            x3 = 0
            y3 = len(image[0])

            x4 = len(image)
            y4 = len(image[0])

            # Calculate rotated positions for corners
            x1_new = x1 * math.cos(theta) - y1 * math.sin(theta)
            y1_new = x1 * math.sin(theta) + y1 * math.cos(theta)

            x2_new = x2 * math.cos(theta) - y2 * math.sin(theta)
            y2_new = x2 * math.sin(theta) + y2 * math.cos(theta)

            x3_new = x3 * math.cos(theta) - y3 * math.sin(theta)
            y3_new = x3 * math.sin(theta) + y3 * math.cos(theta)

            x4_new = x4 * math.cos(theta) - y4 * math.sin(theta)
            y4_new = x4 * math.sin(theta) + y4 * math.cos(theta)

            # Find min and max x coordinate position
            min_x = min(x1_new, x2_new, x3_new, x4_new)
            max_x = max(x1_new, x2_new, x3_new, x4_new)

            # Find min and max y coordinate position
            min_y = min(y1_new, y2_new, y3_new, y4_new)
            max_y = max(y1_new, y2_new, y3_new, y4_new)

            # Calculate new image dimensions and create blank grid for new image
            rows = int(max_x - min_x)
            cols = int(max_y - min_y)
            rotated_image = np.zeros([rows, cols])

            # Calculate rotation for each pixel and insert into new image
            for x in range(0, len(image)):
                for y in range(0, len(image[0])):
                    x_rotated = int(x * math.cos(theta) - y * math.sin(theta))
                    y_rotated = int(x * math.sin(theta) + y * math.cos(theta))
                    x_rotated -= int(min_x)  # Offset to get position with respect to new grid origin
                    y_rotated -= int(min_y)  # Offset to get position with respect to new grid origin
                    rotated_image[x_rotated][y_rotated] = image[x][y]
                    if x_rotated + 1 < len(rotated_image) and y_rotated + 1 < len(rotated_image[0]):
                        rotated_image[x_rotated][y_rotated + 1] = image[x][y]
                        rotated_image[x_rotated + 1][y_rotated] = image[x][y]
                        rotated_image[x_rotated + 1][y_rotated + 1] = image[x][y]


            img = np.array(rotated_image)
            return img

        if interpolation_type == "bilinear":
            # Define corner points
            x1 = 0
            y1 = 0

            x2 = len(image)
            y2 = 0

            x3 = 0
            y3 = len(image[0])

            x4 = len(image)
            y4 = len(image[0])

            # Calculate rotated positions for corners
            x1_new = x1 * math.cos(theta) - y1 * math.sin(theta)
            y1_new = x1 * math.sin(theta) + y1 * math.cos(theta)

            x2_new = x2 * math.cos(theta) - y2 * math.sin(theta)
            y2_new = x2 * math.sin(theta) + y2 * math.cos(theta)

            x3_new = x3 * math.cos(theta) - y3 * math.sin(theta)
            y3_new = x3 * math.sin(theta) + y3 * math.cos(theta)

            x4_new = x4 * math.cos(theta) - y4 * math.sin(theta)
            y4_new = x4 * math.sin(theta) + y4 * math.cos(theta)

            # Find min and max x coordinate position
            min_x = min(x1_new, x2_new, x3_new, x4_new)
            max_x = max(x1_new, x2_new, x3_new, x4_new)

            # Find min and max y coordinate position
            min_y = min(y1_new, y2_new, y3_new, y4_new)
            max_y = max(y1_new, y2_new, y3_new, y4_new)

            # Calculate new image dimensions and create blank grid for new image
            rows = int(max_x - min_x)
            cols = int(max_y - min_y)
            rotated_image = np.zeros([rows, cols])
            origin = [-1 * min_x, -1 * min_y]
            for i_n in range(0,len(rotated_image)):
                for j_n in range(0, len(rotated_image[0])):
                    i_prime = i_n - origin[0]
                    j_prime = j_n - origin[1]
                    # Apply inverse rotation matrix to compute i and j, truncate to whole index number
                    i = int(i_prime * math.cos(theta) + j_prime * math.sin(theta))
                    j = int(i_prime * -1 * math.sin(theta) + j_prime * math.cos(theta))
                    if i < 255 and j < 255 and i > 1 and j > 1:
                        # Find 4 nearest neighbors
                        pt1 = [i+1,j-1,image[i+1][j-1]]
                        pt2 = [i+1,j+1, image[i+1][j+1]]
                        pt3 = [i-1,j-1, image[i-1][j-1]]
                        pt4 = [i-1,j+1,image[i-1][j+1]]
                        # Call bi-linear function
                        bi_interpolation = interpolation()
                        intensity = bi_interpolation.bilinear_interpolation(pt1,pt2,pt3,pt4,[i,j])
                        rotated_image[i_n][j_n] = intensity
            img = np.array(rotated_image)
            return img

        #
        #
        #     # bilinear_interpolation = interpolation()
        #     # pt1 = [21,14,162]
        #     # pt2 = [21,15,95]
        #     # pt3 = [20,14,91]
        #     # pt4 = [20,15,210]
        #     # unkown = [20.2,14.5]
        #     # bilinear_interpolation.bilinear_interpolation(pt1,pt2,pt3,pt4,unkown)
        #     # return rotated_image
        #
        #
