from math import cos, sin
#
#  This file will contain all algebra (for later) (dot product, vectorial product, matrix product etc...)
#

def rotation(x, y, z, Rx, Ry, Rz) -> tuple:
    '''mainly used by rotation method, give it a dot and an angle, returns a tuple with new coords, used to siplify code'''

    #main rotation matrix : Rx . Ry .Rz => Matrix3x3 . Matrix3x3 . Matrix3x3
    rotation_matrix =[
        [cos(Ry)*cos(Rz), sin(Rx)*sin(Ry)*cos(Rz)+cos(Rx)*sin(Rz), -cos(Rx)*sin(Ry)*cos(Rz)+sin(Rx)*sin(Rz)],
        [-cos(Ry)*sin(Rz), -sin(Rx)*sin(Ry)*sin(Rz)+cos(Rx)*cos(Rz), cos(Rx)*sin(Ry)*sin(Rz)+sin(Rx)*cos(Rz)],
        [sin(Ry), -sin(Rx)*cos(Ry), cos(Rx)*cos(Ry)]
    ]

    #vect3 . Matrix3x3
    new_x = x*rotation_matrix[0][0] + y*rotation_matrix[0][1] + z*rotation_matrix[0][2]
    new_y = x*rotation_matrix[1][0] + y*rotation_matrix[1][1] + z*rotation_matrix[1][2]
    new_z = x*rotation_matrix[2][0] + y*rotation_matrix[2][1] + z*rotation_matrix[2][2]

    return (new_x,new_y,new_z)