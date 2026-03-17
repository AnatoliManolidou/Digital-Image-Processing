import numpy as np

def circ_hough(
        in_img_array: np.ndarray,   #Our binary image 
        R_min: float,               #Minimum radius of the circles we want to detect
        R_max: float,               #Maximum radius of the circles we want to detect
        dim: np.ndarray,            #Has lenght = 3 and contains the number of intervals that the horizontal and vertical axes of the image are divided into and the number of intervals that the [Rmin,Rmax] interval is divided into
        V_min: int                  #Minimum value of votes so a cell of the hough matrix can be considered a circle
) -> tuple[np.ndarray, np.ndarray, np.ndarray]: #Returns the centers of the circles, their radius and the number of votes they received

        #Defining the Hough voting space
        hough_space = np.zeros((dim[0], dim[1], dim[2])) #The first two dimensions are the horizontal and vertical intervals and the third dimension is the number of itervals of the radius interval

        a_inter = int(in_img_array.shape[0] / dim[0])    #Get the interval of the horizontal axis
        b_inter = int(in_img_array.shape[1] / dim[1])    #Get the interval of the vertical axis
        r_inter = int((R_max - R_min) / dim[2])          #Get the interval of the radius

        ys, xs = np.nonzero(in_img_array)                #Get the coordinates of the pixels that are part of an edge

        r_vals = np.linspace(R_min, R_max, dim[2])       #Get values for radii to iterate through

        for y, x in zip(ys, xs):   #Iterate through the coordinates of the pixels that are part of an edge
                for r in (r_vals): #Iterate through the radii
                        for theta in range(0, 360, 2):                       #Iterating for each angle from 0 to 360 degrees with a step of 2 degrees 
                                a = int(x - r * np.cos(theta * np.pi / 180)) #Get the x coordinate of the center of the circle
                                b = int(y - r * np.sin(theta * np.pi / 180)) #Get the y coordinate of the center of the circle

                                #Find the bin that the a, b and r belong to
                                a_bin = int(a / a_inter)
                                b_bin = int(b / b_inter)
                                r_bin = int((r - R_min) / r_inter)

                                #Check if the bin is within the bounds of the hough space
                                if 0 <= a_bin < dim[0] and 0 <= b_bin < dim[1] and 0 <= r_bin < dim[2]:
                                        hough_space[a_bin, b_bin, r_bin] += 1

        centers = []
        radii = []
        votes = []

        #Iterate through the hough space to get the centers, radii and votes of the circles
        for i in range(hough_space.shape[0]):
                for j in range(hough_space.shape[1]):
                        for k in range(hough_space.shape[2]):
                                if hough_space[i, j, k] > V_min:  #If the number of votes is greater than the minimum value

                                        #Get the coordinates of the center of the circle and its radius for the current cell
                                        ai = i * a_inter 
                                        bi = j * b_inter
                                        ri = R_min + (k * r_inter)

                                        #Get the coordinates of the center of the circle and its radius for the next cell
                                        aii = (i + 1) * a_inter
                                        bii = (j + 1) * b_inter
                                        rii = R_min + ((k + 1) * r_inter)

                                        #Calculate the center and radius of the circle
                                        cx = (ai + aii) / 2
                                        cy = (bi + bii) / 2
                                        r = (ri + rii) / 2

                                        centers.append([cx, cy])
                                        radii.append(r)
                                        votes.append(hough_space[i, j, k])

        centers = np.array(centers)
        radii = np.array(radii)
        votes = np.array(votes)

        return centers, radii, votes
