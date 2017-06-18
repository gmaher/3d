import vtk

def colorPD(pd,lc,c):
    colors = vtk.vtkUnsignedCharArray()
    colors.SetNumberOfComponents(3)
    for i in range(pd.GetNumberOfLines()):
        colors.InsertNextTuple3(lc[0],lc[1],lc[2])

    for i in range(pd.GetNumberOfPolys()):
        colors.InsertNextTuple3(c[0],c[1],c[2])

    pd.GetCellData().SetScalars(colors)

    return pd

class Scene:
    def __init__(self, size=1000, background=(1,1,1), camPosition=(20,10,20), camFocal=(0,0,0)):

        self.renderer = vtk.vtkRenderer()
        self.renderWindow = vtk.vtkRenderWindow()
        self.renderWindow.AddRenderer(self.renderer)
        self.renderWindow.SetSize(size, size)
        self.interactor = vtk.vtkRenderWindowInteractor()
        self.interactor.SetRenderWindow(self.renderWindow)
        self.renderer.SetBackground(background[0],background[1],background[2])

        self.camera = vtk.vtkCamera()
        self.camera.SetPosition(camPosition)
        self.camera.SetFocalPoint(camFocal)

        self.renderer.SetActiveCamera(self.camera)

        axes = vtk.vtkAxesActor()

        self.renderer.AddActor(axes)
    def addObject(self,pd, linecolor=(0.0,0.0,0.0), linewidth=1.0,
        color=(255,255,255), wireframe=False, noLight=True):
        pd = colorPD(pd,linecolor,color)

        m = vtk.vtkPolyDataMapper()
        m.SetInputData(pd)
        a = vtk.vtkActor()
        a.SetMapper(m)

        self.renderer.AddActor(a)

        a.GetProperty().SetLineWidth(linewidth)
        if wireframe:
            a.GetProperty().SetRepresentationToWireframe()

        if noLight:
            a.GetProperty().LightingOff()

    def render(self):
        self.renderWindow.Render()
        self.interactor.Start()

    def save(self):
        pass
