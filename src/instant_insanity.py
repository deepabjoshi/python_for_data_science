"""
Solution for Instant Insanity puzzle - https://en.wikipedia.org/wiki/Instant_Insanity
"""

from enum import Enum, auto


class Faces(Enum):
    TOP = auto()
    LEFT = auto()
    BACK = auto()
    RIGHT = auto()
    FRONT = auto()
    BOTTOM = auto()

    def rotate_faces(self, face_list):
        rotated_faces = []
        rotated_faces.extend(face_list)
        return rotated_faces

    def face_permutations(self):
        fp = []
        orig = list(Faces)
        # Keep top and bottom same
        fp.extend(self.rotate_faces(orig))
        # Flip top and bottom
        # Move left to top
        # Move right to top
        # Move front to top
        # Move back to top
        return fp


Color = Enum('Color', ['RED', 'YELLOW', 'GREEN', 'BLUE'])


def find_orientations(cube):
    orientations = []
    fp = Faces.face_permutations()
    # for p in fp:
    #
    return orientations


print(dir(Color))
print(dir(Faces))

cubes = [dict(zip(list(Faces), [Color.RED, Color.BLUE, Color.YELLOW, Color.GREEN, Color.RED, Color.BLUE])),
         dict(zip(list(Faces), [Color.RED, Color.RED, Color.BLUE, Color.YELLOW, Color.GREEN, Color.GREEN])),
         dict(zip(list(Faces), [Color.RED, Color.BLUE, Color.YELLOW, Color.GREEN, Color.BLUE, Color.YELLOW])),
         dict(zip(list(Faces), [Color.RED, Color.BLUE, Color.YELLOW, Color.YELLOW, Color.GREEN, Color.GREEN]))]
print(cubes)

for d in cubes:
    cube_colors = [(f.name, c.name) for f, c in d.items()]
    print(cube_colors)

print(list(Faces))
print(Faces(1))