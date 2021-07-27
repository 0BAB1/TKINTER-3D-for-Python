#later on, this class will be controlled by a camera, and not the app
from math import sin, cos
from mesh import Mesh

class Scene:
    '''this class represent the 3d scene (euclidian norms) that will be projected on the canvas'''
    def __init__(self):
        self.meshes={} #array of Mesh objet
        self.rotations = {"x":0,"y":0,"z":0}
    
    def del_shape(self, name):
        # spare code, please keep it there
        # if name in self.meshes:
        #     for mesh,value in self.meshes:
        #         #for each mesh
        #         for i in range(len(name)):#we look for a match with name on the fists chars
        #             if name[i] == mesh[i]:
        #                 found = True
        #             else:
        #                 found = False
        #         if found:#if it matched , we look for a "-" in the name, if so, the two meshes were associated to the same shape, so we delet it
        #             if "-" in mesh:
        #    
        #             self.meshes.pop(mesh)
        if name in self.meshes:
            self.meshes.pop(name)
        if name in self.dots:
            self.dots.pop(name)

    def rotation(self, x, y, z, Rx, Ry, Rz):
        '''mainly used by rotation method, give it a dot and an angle, returns a tuple with new coords, used to siplify code'''

        rotation_matrix =[
            [cos(Ry)*cos(Rz), sin(Rx)*sin(Ry)*cos(Rz)+cos(Rx)*sin(Rz), -cos(Rx)*sin(Ry)*cos(Rz)+sin(Rx)*sin(Rz)],
            [-cos(Ry)*sin(Rz), -sin(Rx)*sin(Ry)*sin(Rz)+cos(Rx)*cos(Rz), cos(Rx)*sin(Ry)*sin(Rz)+sin(Rx)*cos(Rz)],
            [sin(Ry), -sin(Rx)*cos(Ry), cos(Rx)*cos(Ry)]
        ]

        new_x = x*rotation_matrix[0][0] + y*rotation_matrix[0][1] + z*rotation_matrix[0][2]
        new_y = x*rotation_matrix[1][0] + y*rotation_matrix[1][1] + z*rotation_matrix[1][2]
        new_z = x*rotation_matrix[2][0] + y*rotation_matrix[2][1] + z*rotation_matrix[2][2]

        return (new_x, new_y, new_z)
        
    def rotate(self,x,y,z) -> tuple:
        '''to rotate every shape around x y or / and z'''
        self.rotations["x"] += x 
        self.rotations["y"] += y
        self.rotations["z"] += z

        for name, mesh in self.meshes.items():
            for i in range(len(mesh)): #i is a triangle, following this structure : [color,outline,(x,y,z),(x,y,z),(x,y,z)]
                #a triangle as 3 dots (here j is a dot) :
                for j in range(2,len(self.meshes[name][i])):
                    new_dot = self.rotation(self.meshes[name][i][j][0],self.meshes[name][i][j][1],self.meshes[name][i][j][2],x,y,z)
                    self.meshes[name][i][j] = (new_dot[0],new_dot[1],new_dot[2])

    def add_line(self,x1,y1,z1, x2,y2,z2,name,color="black"):
        '''to add a simple line and create custom shapes'''
        #we just add a triangle with 3 dots aligned
        if not name in self.meshes:
            self.meshes[name] = []
        self.meshes[name].append(["black",color,(x1,y1,z1),(x2,y2,z2),(x1,y1,z1)])

    def add_surf(self, x1,y1,z1 ,x2,y2,z2 ,x3,y3,z3, name, color="black", outline="grey"):
        '''create a surface with 2 triangles , the first dot is the ORIGIN of your surface, the main diagonal wiil start from here'''
        if not name in self.meshes:
            self.meshes[name] = [] #memo : structure : {"name" : [[color, (x,y,z),(x,y,z),(x,z,y) ],[clolor, (xyz),(xyz),(xyz) ] etc]} or, an array of triangle, which is an array of dots + a color
        #a surface is two triangles
        self.meshes[name].append([color,outline,(x1,y1,z1),(x2,y2,z2),(x3,y3,z3)])#first triangle
        #we need to determine our dot2-dot3 middle, this will later be shrter but for comprehension issues ... well its like that
        middlex = min(x2,x3) + (max(x2,x3)-min(x2,x3))/2
        middley = min(y2,y3) + (max(y2,y3)-min(y2,y3))/2
        middlez = min(z2,z3) + (max(z2,z3)-min(z2,z3))/2
        if x1 < middlex:
            x4 = x1 + 2*(middlex-x1)
        elif x1 > middlex:
            x4 = x1 - 2*(middlex-x1)
        else : #if we want to create a line
            x4 = x1
        
        if y1 < middley:
            y4 = y1 + 2*(middley-y1)
        elif y1 > middlex:
            y4 = y1 - 2*(middley-y1)
        else : #if we want to create a line
            y4 = y1

        if z1 < middlez:
            z4 = z1 + 2*(middlez-z1)
        elif y1 > middlex:
            z4 = z1 - 2*(middlez-z1)
        else : #if we want to create a line
            z4 = z1
        
        self.meshes[name].append([color,outline,(x4,y4,z4),(x2,y2,z2),(x3,y3,z3)])#second triangle