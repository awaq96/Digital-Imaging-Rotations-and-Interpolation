class interpolation:

    def linear_interpolation(self, pt1, pt2, unknown):


        # Write your code for linear interpolation here
        unknown_intensity = (pt1[1] * (pt2[0] - unknown)) / (pt2[0] - pt1[0])
        unknown_intensity += (pt2[1] * (unknown - pt1[0])) / (pt2[0] - pt1[0])

        return unknown_intensity

    def bilinear_interpolation(self, pt1, pt2, pt3, pt4, unknown):

        # Write your code for bilinear interpolation here
        lin = interpolation()

        r1_pt1 = [pt1[1], pt1[2]]
        r1_pt2 = [pt2[1], pt2[2]]
        r1 = lin.linear_interpolation(r1_pt1,r1_pt2,unknown[1])

        r2_pt1 = [pt3[1], pt3[2]]
        r2_pt2 = [pt4[1], pt4[2]]
        r2 = lin.linear_interpolation(r2_pt1,r2_pt2,unknown[1])

        r3_pt1 = [pt3[0], r2]
        r3_pt2 = [pt1[0], r1]
        r3 = lin.linear_interpolation(r3_pt1, r3_pt2,unknown[0])

        # May be you can reuse or call linear interpolation method to compute this task
        return r3
