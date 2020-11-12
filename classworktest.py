from genes import *

"""
This code performs tests defining requirements that each method must achieve, 
"""

def assertEqual(entity, target):
    try:
        assert entity == target
    except:
        print(f'{entity} is different from{target}')
        raise AssertionError

def VerticesSpaceTest():
    ## Space construction test
    space = VerticesSpace((5, 3))
    assertEqual(space.getnVertices(), sum((5, 3)))
    assertEqual(space.getspace(), [[1, 2, 3, 4, 5], [6, 7, 8]])
    space = VerticesSpace((5, 3, 2))
    assertEqual(space.getnVertices(), sum((5, 3, 2)))
    assertEqual(space.getspace(), [[1, 2, 3, 4, 5], [6, 7, 8], [9, 10]])
    space = VerticesSpace((5, 3, 2), 'Eve')
    assertEqual(space.getspace(), [list(reversed([1, 2, 3, 4, 5])), list(reversed([6, 7, 8])), list(reversed([9, 10]))])
    print('Space has been successfully constructed.')

    ## Set element test
    space = VerticesSpace((1, 2, 2), [[2], [1, 3], [4, 5]])
    space.setElement((1, 1), 2)
    space.setElement((0, 0), 1)
    assertEqual(space.getspace(), [[1], [1, 2], [4, 5]])
    print('Element of a space can be set.')
    
    ## Set space test
    space = VerticesSpace((3, 2))
    space.setSpace([[2, 3, 4], [1, 5]])
    assertEqual(space.getspace(), [[2, 3, 4], [1, 5]])
    print('A space can be set by also a list.')
    

    ## Swap test
    space.swapElement((0,1), (0, 2))
    assertEqual(space.getspace(), [[2, 4, 3], [1, 5]])
    print('A space can be swapped.')

def HexagonTest():
    space = VerticesSpace((8, 2))
    pos = [(0, 0), (1, 0), (1, 1), (0, 6), (0, 4), (0, 2)]
    hex = Hexagon(pos)
    assertEqual(hex.getVerticesValues(space), [1, 9, 10, 7, 5, 3])
    print('Hexagon class has been successfully created.')
    # hex.setPos([()])
    # hex.rotate(space)
    pass

def TortoiseTest():
    t = Tortoise(length=2)
    # t.getHexagons()
    # t.getAdjHexagons(0)

# p = Problem(n_hex=4)
# sol_space = p.solve()


VerticesSpaceTest()
HexagonTest()
TortoiseTest()
print('All Tests Done!')