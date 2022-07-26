import win32api
from mss import mss
from gluoncv import model_zoo, data, utils

net = model_zoo.get_model("yolo3_darknet53_coco",pretrained=True)

def aim(x,y):
    win32api.SetCursorPos((x,y))

def shot():
    with mss() as sct:
        sct.shot()

while True:
    shot()
    x,img = data.transforms.presets.yolo.load_test("monitor-1.png",short=512)
    class_IDs,scores,bounding_boxs = net(x)
    if class_IDs[0][0] == 0:
        x = ((bounding_boxs[0][0][0]+bounding_boxs[0][0][2])/2)*(win32api.GetSystemMetrics(0)/910)
        y = ((bounding_boxs[0][0][1]+bounding_boxs[0][0][3])/2)*(win32api.GetSystemMetrics(1)/512)
        x = "".join(map(str,x))
        y = "".join(map(str,y))
        x = round(float(x.split()[0][1:-1]))
        y = round(float(y.split()[0][1:-1]))
        aim(x,y)
