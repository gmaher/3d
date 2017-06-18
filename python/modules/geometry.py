import vtk

def translate(pd,x,y,z):
        transform = vtk.vtkTransformPolyDataFilter()
        t = vtk.vtkTransform()
        t.Translate(x,y,z)

        transform.SetTransform(t)
        transform.SetInputData(pd)
        transform.Update()
        return transform.GetOutput()

def rotate(pd,angle,x=0,y=0,z=0):
        transform = vtk.vtkTransformPolyDataFilter()
        t = vtk.vtkTransform()
        t.RotateWXYZ(angle,x,y,z)

        transform.SetTransform(t)
        transform.SetInputData(pd)
        transform.Update()
        return transform.GetOutput()

def rotateXYZ(pd,rotation_axis=0):
    if rotation_axis==0:
        o = rotate(pd,90,1,0,0)
    elif rotation_axis==1:
        o = rotate(pd,90,0,1,0)
    elif rotation_axis==2:
        o = rotate(pd,90,0,0,1)

    return o

def mergePDs(pds):
    app = vtk.vtkAppendPolyData()
    for pd in pds:
        app.AddInputData(pd)
    app.Update()

    cleaner = vtk.vtkCleanPolyData()
    cleaner.SetInputConnection(app.GetOutputPort())
    cleaner.Update()
    return cleaner.GetOutput()


def square(center=[0.0,0.0,0.0],orientation=0):
    lines = vtk.vtkCellArray()
    points = vtk.vtkPoints()
    polys = vtk.vtkCellArray()

    p0 = (center[0]-0.5,center[1]-0.5,center[2])
    p1 = (center[0]+0.5,center[1]-0.5,center[2])
    p2 = (center[0]+0.5,center[1]+0.5,center[2])
    p3 = (center[0]-0.5,center[1]+0.5,center[2])

    points.InsertNextPoint(p0)
    points.InsertNextPoint(p1)
    points.InsertNextPoint(p2)
    points.InsertNextPoint(p3)

    for i in range(3):
        l = vtk.vtkLine()
        l.GetPointIds().SetId(0,i)
        l.GetPointIds().SetId(1,i+1)
        lines.InsertNextCell(l)

    l = vtk.vtkLine()
    l.GetPointIds().SetId(0,3)
    l.GetPointIds().SetId(1,0)
    lines.InsertNextCell(l)

    polys.InsertNextCell(4,[0,1,2,3])

    pd = vtk.vtkPolyData()
    pd.SetPoints(points)
    pd.SetLines(lines)
    pd.SetPolys(polys)

    pd = rotateXYZ(pd,orientation)

    return pd

def cube(center=[0.0,0.0,0.0]):
    points = vtk.vtkPoints()
    lines = vtk.vtkCellArray()
    faces = vtk.vtkCellArray()
    pd = vtk.vtkPolyData()

    pts = [[0,0,1],[1,0,1],[1,1,1],[0,1,1],[0,0,0],[1,0,0],[1,1,0],[0,1,0]]
    lns = [[0,1],[1,2],[2,3],[3,0],[0,4],[1,5],[2,6],[3,7],[4,5],[5,6],[6,7],[7,4]]
    fcs = [[0,1,2,3],[4,5,6,7],[1,5,6,2],[0,4,7,3],[0,4,5,1],[3,2,6,7]]

    [points.InsertNextPoint(p) for p in pts]
    [lines.InsertNextCell(2,lns[i]) for i in range(len(lns))]
    [faces.InsertNextCell(4,fcs[i]) for i in range(len(fcs))]
    pd.SetPoints(points)
    pd.SetLines(lines)
    pd.SetPolys(faces)

    pd = translate(pd,-0.5,-0.5,-0.5)
    pd = translate(pd,center[0],center[1],center[2])
    return pd

def grid(n1,n2,center=[0.0,0.0,0.0],orientation=0):
    squares = []
    start = center[:]
    start[0] -= (float(n1)/2 - 0.5)
    start[1] -= (float(n2)/2 - 0.5)
    for i in range(n1):
        for j in range(n2):
            p = start[:]
            p[0] += i
            p[1] += j
            s = square(p)
            squares.append(s)

    grid = mergePDs(squares)
    grid = rotateXYZ(grid,orientation)
    return grid
