#s09ThreeDimTest.py
import pj
import pjTkInter as tk
import pjThreeDim as pj3d
import math
import pjSound as sound
from logStdErr import logStdErrClass
lse=logStdErrClass()
lse.errToFile()
####
tk.updateMainLabel("s09ThreeDimTest")
tk.title("This shows some of Touched, Touch Moved, Button Pressed and KeyPressed.")
tk.removeAllFromCanvas()
####
##mateFileName="max_diffuse.png"
mateFileName="Material.001 Base Color_YassunThreeDim2025-0427-1717PM.png"
srcAbsPath1=lse.bundleAppPath + \
    "/PeterJohn.scnassets/"+mateFileName
destAbsPath1=lse.sandBoxProjDirPath + \
"/images/"+mateFileName
import os
import shutil
if os.path.isfile( srcAbsPath1 ) and not os.path.isfile( destAbsPath1 ):
  shutil.copy2( srcAbsPath1, destAbsPath1 )
####
##daeFileName="max.dae"
daeFileName="2025-0427-2022PM(Sun)YassunThreeDim_CenterLineSelectNKeyItemMedianXzero_ObjectModeMirrorApply_ObjectModeNKeyItemTransformDimensions_TransformPivotPointBBcenter_CollectionCameraAndLightRemovedByX_BBsizeByEditModeScale_SetOriginOriginTo3dCursori.dae"
####
srcAbsPath2=lse.bundleAppPath + \
    "/PeterJohn.scnassets/"+daeFileName
destAbsPath2=lse.sandBoxProjDirPath + \
"/images/"+daeFileName
if os.path.isfile( srcAbsPath2 ) and not os.path.isfile( destAbsPath2 ):
  shutil.copy2( srcAbsPath2, destAbsPath2 )
if os.path.isfile( destAbsPath1 ) and os.path.isfile( destAbsPath2 ) :
  pj3d.createSCNSceneWithFilePath(
    destAbsPath2,
    "Cube",
    "fox",0,0,0 )
  #####pj3d.setPosition("Max_rootNode",0.5,0,8)
  ####pj3d.removeFromParent("Max_rootNode")
pj3d.setPosition("fox",1,0,5)
####
mi1,mi2,mi3,ma1,ma2,ma3 = pj3d.getBoundingBoxMinMax("fox")
lse.print(f"min;{mi1,mi2,mi3},\nmax;{ma1,ma2,ma3}")
width = ma1 - mi1
height = ma2 - mi2
depth = ma3 - mi3
lse.print(f"height;{height}")
if height == 0 : ##Avoid DivisionByZero;Line65;
  height = 1
####
pj3d.setScale("fox",1/height,1/height,1/height)
####pj3d.setScale("fox",1,1,1)
##pj3d.setBoundingBoxMinMax("fox",-width/(2*height),0,-depth/(2*height),width/(2*height),height/height,depth/(2*height))
pj3d.setBoundingBoxMinMax("fox",-width/2,0,-depth/2,width/2,height,depth/2)
####pj3d.setBoundingBoxMinMax("fox",-0.5,0,-0.5,0.5,1,0.5)
mi1,mi2,mi3,ma1,ma2,ma3 = pj3d.getBoundingBoxMinMax("fox")
lse.print(f"min;{mi1,mi2,mi3},\nmax;{ma1,ma2,ma3}")
####
d = (90/180) * math.pi
#####pj3d.rotation("fox",1,0,0,d)
##pj3d.eulerAngles("fox",0*d,1*d,0) ##Front
####pj3d.createCamera("camera",1,0.53,5) ##
####pj3d.setNameToDefaultCamera("camera")
pj3d.setCameraConstraintLookAt("camera", "fox")
pj3d.setPosition("camera",1,0.53,5) ##
####
pj3d.createFloor("floor",
   0,-0.01,0, ## 'y' Needs Minus Value;
   0,255,0,123) ##Green;Alpha255;
pj3d.createSphere("sphere",1, ## Height(2);
  -2,1,0,
  255,255,0,255) ##Yellow;Alpha255;
pj3d.createBox("box",
  4,2,4,0.2, ## Height(2);
  4,1,0,
  0,0,255,255) ##Blue;Alpha255;
pj3d.createCapsule("capsule",
  0.25,2, ## Height(2);
  0,1,0,
  255,0,0,255) ##Red;Alpha255;
####
##(1;Hero,2;Floor,4;OtherObject);;
##(1;Hero,2;Friend,4;Enemy),(1;Collectable,2;Floor,4;OtherObject)*256;;
####Dynamic;
##pj3d.setPhysicsBodyDynamic("fox",1,2,0)##Dynamic(catergory,contactTest,collision);Fox;Colides(sphere,sideWall,ceiling)
##pj3d.setPhysicsBodyDynamic("fox",1,4,0)##Dynamic(catergory,contactTest,collision);
##pj3d.setPhysicsBodyDynamic("sphere",2,1,0)##Static(catergory,contactTest,collision);Sphere;Colides(sphere,sideWall,ceiling)
##pj3d.setPhysicsBodyDynamic("sphere",2,4,0)##Static(catergory,contactTest,collision);
####
pj3d.setPhysicsBodyStatic("fox",1,4,0)##Static(catergory,contactTest,collision);
####pj3d.changePivotPosition("fox", 0,0.5,20) ##Line64;;##NoNeed After EmptyTransformLocationYzero;
####pj3d.movePhysicsShape("fox",0,0.5,20);NoNeed After EmptyTransformLocationYzero;
####
pj3d.setPhysicsBodyStatic("floor",2,0,0)##Static(catergory,contactTest,collision);
pj3d.setPhysicsBodyStatic("sphere",4,1,0)##Static(catergory,contactTest,collision);
pj3d.setPhysicsBodyStatic("capsule",4,1,0)##Static(catergory,contactTest,collision);
pj3d.setPhysicsBodyStatic("box",4,1,0)##Static(catergory,contactTest,collision);
#### Light;;
####pj3d.setPosition("directionalLight",0,10,0)
pj3d.setPosition("omniLight",0,4,0)##MakeGreenFloor;
pj3d.setLightIntensity("omniLight",2000)##MakeGreenFloor;
####
pj3d.setPosition("ambientLight",0,-2,0)
pj3d.setLightIntensity("ambientLight",3000)##MakeGreenFloor;
##pj3d.setColor("ambientLight",165,165,0,10) ##Orange
pj3d.setColor("ambientLight",255,77,0,255) ##Yellow
####pj3d.setColor("ambientLight",252,64,0,255) ##Naked Color Matched;;
####pj3d.setColor("ambientLight",255,128,51,255) ##BulbLightColor;
####
pj.changeTitleLabelToReplMode()
sound.setTouchesEndedOn() ##
tk.setTitleLabelBgColor(1,2,3,0) ##
##tk.setCanvasColor(1,2,3,0) ##
####tk.setZPosition("Title",65535) ##
pj3d.changePortRaitGamePadToThreeDimMode() ##set PortRaitGamePad To ThreeDim;;
####pj3d.removeCameraConstraintLookAt("camera")
####
class CameraAngle :
  ####
  def __init__(self) :
    self.cameraRotAngle = 0
    self.blenderAdjust = 90
    self.cameraDistMax = 7.0
    self.cameraDistMin = 2.0
    self.diffBase = 0.1 ##To Avoid Passing Through;
    self.angleBase = 5 ##Each Five Degrees;;
    self.diffAngle = 0
    self.beforeFx = 0
    self.beforeFz = 0
    self.contactDx = 0
    self.contactDz = 0
    self.eventX = -1
    self.eventY = -1
    self.evRightX = -1
    self.evRightY = -1
    ####
    self.d = (90/180) * math.pi
    self.rotateCameraAroundFox( self.cameraRotAngle )
    ####
    self.shapEusdzFileName = [
      "aBirthDayCupCake-tmpfksaxw0u.usdz",
      "aPenguin-tmpe2q9477p.usdz",
      "aSpaceShip-tmpkxt8xclh.usdz",
     ]
    self.shapEglbFileName = [
      "aBirthDayCupCake-tmpfksaxw0u.glb",
      "aPenguin-tmpe2q9477p.glb",
      "aSpaceShip-tmpkxt8xclh.glb",
     ]
    self.shapEglbMeshName = [
        "tmpclsl_kqt_ply",
        "tmp3l_3e6fb_ply",
        "tmplzm23orf_ply",
     ]
    ####
    self.create3dModelGLB(self.shapEglbFileName[0],self.shapEglbMeshName[0],"aBirthDayCupCake")
    self.create3dModelGLB(self.shapEglbFileName[1],self.shapEglbMeshName[1],"aPenguin")
    self.create3dModelGLB(self.shapEglbFileName[2],self.shapEglbMeshName[2],"aSpaceShip")
    pj3d.setPosition("aBirthDayCupCake",0,0.5,5)
    pj3d.setPosition("aPenguin",2,0.5,5)
    pj3d.setPosition("aSpaceShip",1,1.5,3)
    pj3d.eulerAngles("aPenguin",0*self.d,90*self.d,0) 
    pj3d.eulerAngles("aSpaceShip",0*self.d,40*self.d,0) 
  ####
  def create3dModel(self,mateFileName,daeFileName,meshName,modelName) :
    srcAbsPath1=lse.bundleAppPath + \
    "/PeterJohn.scnassets/"+mateFileName
    srcAbsPath2=lse.bundleAppPath + \
    "/PeterJohn.scnassets/"+daeFileName
    if not os.path.isfile( srcAbsPath1 ) :
      lse.print(f"doesNot Exist;{srcAbsPath1}")
      return
    if not os.path.isfile( srcAbsPath2 ) :
      lse.print(f"doesNot Exist;{srcAbsPath2}")
      return
    if os.path.isfile( srcAbsPath1 ) and os.path.isfile( srcAbsPath2 ) :
      pj3d.createSCNSceneWithFilePath(
        srcAbsPath2,
        meshName,
        modelName,0,0,0 )
    ####
    mi1,mi2,mi3,ma1,ma2,ma3 = pj3d.getBoundingBoxMinMax(modelName)
    ##lse.print(f"min;{mi1,mi2,mi3},\nmax;{ma1,ma2,ma3}")
    width = ma1 - mi1
    height = ma2 - mi2
    depth = ma3 - mi3
    ##lse.print(f"height;{height}")
    if height == 0 : ##Avoid DivisionByZero;Line65;
      height = 1
    ####
    pj3d.setScale(modelName,1/height,1/height,1/height)
  ####
  def create3dModelUSDZ(self,usdzFileName,meshName,modelName) :
    srcAbsPath2=lse.bundleAppPath + \
    "/PeterJohn.scnassets/"+usdzFileName
    if not os.path.isfile( srcAbsPath2 ) :
      lse.print(f"doesNot Exist;{srcAbsPath2}")
      return
    if os.path.isfile( srcAbsPath2 ) :
      pj3d.createSCNSceneWithFilePath(
        srcAbsPath2,
        meshName,
        modelName,0,0,0 )
    ####
    mi1,mi2,mi3,ma1,ma2,ma3 = pj3d.getBoundingBoxMinMax(modelName)
    lse.print(f"modelName;{modelName};min;{mi1,mi2,mi3},\nmax;{ma1,ma2,ma3}")
    width = ma1 - mi1
    height = ma2 - mi2
    depth = ma3 - mi3
    lse.print(f"modelName;{modelName};height;{height}")
    if height == 0 : ##Avoid DivisionByZero;Line65;
      height = 1
    ####
    pj3d.setScale(modelName,1/height,1/height,1/height)
  ####
  def create3dModelGLB(self,glbFileName,meshName,modelName) :
    srcAbsPath2=lse.bundleAppPath + \
    "/PeterJohn.scnassets/"+glbFileName
    if not os.path.isfile( srcAbsPath2 ) :
      lse.print(f"doesNot Exist;{srcAbsPath2}")
      return
    ##
    meshNameList = pj3d.getMeshNameListFromGLBFile( srcAbsPath2 )
    lse.print(f"modelName;{modelName}, MeshNameList;{meshNameList}")
    if not meshName in meshNameList :
      lse.print(f"WARNING;{meshName} doesNot Exist in MeshNameList;{meshNameList}. Apple might have Replaced '.ply' to '_ply'.")
    if os.path.isfile( srcAbsPath2 ) :
      pj3d.createSCNSceneWithGLBFilePath(
        srcAbsPath2,
        meshName,
        modelName,0,0,0 )
    ####
    mi1,mi2,mi3,ma1,ma2,ma3 = pj3d.getBoundingBoxMinMax(modelName)
    lse.print(f"modelName;{modelName};min;{mi1,mi2,mi3},\nmax;{ma1,ma2,ma3}")
    width = ma1 - mi1
    height = ma2 - mi2
    depth = ma3 - mi3
    lse.print(f"modelName;{modelName};height;{height}")
    if height == 0 : ##Avoid DivisionByZero;Line65;
      height = 1
    ####
    pj3d.setScale(modelName,1/height,1/height,1/height)
  ####
  def dist(self, fx, fy, fz, cx, cy, cz ) :
    dist = math.sqrt(math.pow(fx - cx,2)+math.pow(fy-cy,2)+math.pow(fz-cz,2))
    if dist < 0.001 :
      dist = 0.001
    return dist
  ####
  def rotateAaroundB(self, nameA, nameB, angle) :
    angle = angle + self.blenderAdjust
    fx,fy,fz = pj3d.getPosition(nameB)
    cx,cy,cz = pj3d.getPosition(nameA)
    dist = self.dist(fx,fy,fz,cx,cy,cz)
    if dist > self.cameraDistMax :
      dist = self.cameraDistMax
    if dist < self.cameraDistMin :
      dist = self.cameraDistMin
    cx = fx + dist * math.cos((math.pi/180)*angle)
    cz = fz + dist * math.sin((math.pi/180)*angle)
    pj3d.setPosition(nameA,cx, cy, cz ) ##Line85;;
  ####
  def rotateCameraAroundFox(self, angle) :
    self.rotateAaroundB("camera","fox",angle)
  ####
  def showPos(self) :
    fx,fy,fz = pj3d.getPosition("fox")
    cx,cy,cz = pj3d.getPosition("camera")
    pj3d.setPosition("omniLight",cx,4,cz)##MakeGreenFloor;
    dist = self.dist(fx,fy,fz,cx,cy,cz)
    tk.title(f"(fx,fy,fz);({fx:.2f},{fy:.2f},{fz:.2f})\n")
    tk.appendTitleLabel(f"(cx,cy,cz);({cx:.2f},{cy:.2f},{cz:.2f})\n")
    tk.appendTitleLabel(f"cameraRotAngle;{self.cameraRotAngle},dist;{dist:.2f}")
  ####
  def keyPress(self, eventKeySym):
    tk.updateMainLabel("eventKeySym:" + eventKeySym)
  ####
  def button(self, eventNum):
    tk.updateMainLabel("eventNum:" + str(eventNum))
  ####
  def contact(self, contactNodeA, contactNodeB, contactNormalX, contactNormalY, contactNormalZ ):
    if str(contactNodeA) == "fox" or str(contactNodeB) == "fox" :
      self.eventX = -1 ##To Stop Motion;;
      self.eventY = -1 ##To Stop Motion;;
      fx,fy,fz = pj3d.getPosition("fox")
      ##
      diffFx = fx - self.beforeFx
      diffFz = fz - self.beforeFz
      ####
      if diffFx >= 0 :
        dx =  -math.fabs( contactNormalX )
      else :
        dx = math.fabs( contactNormalX )
      ####fy = fy + contactNormalY
      if diffFz >= 0 :
        dz = -math.fabs( contactNormalZ )
      else :
        dz = math.fabs( contactNormalZ )
      ####
      tk.updateMainLabel(f"nodeA;{str(contactNodeA)}, nodeB;{str(contactNodeB)}, normal;({contactNormalX:.2f},{contactNormalY:.2f},{contactNormalZ:.2f}),diffFx;{diffFx:.2f},diffFz;{diffFz:.2f}")
      if math.fabs(contactNormalY) > 0.35 :
        return
      self.moveFoxContact(fx,fy,fz,dx,dz)
  ####
  def moveFoxContact(self, fx,fy,fz,dx,dz) :
    self.contactDx = dx
    self.contactDz = dz
  ####
  def motion(self, eventX, eventY):
    if eventX != -1 and eventY != -1 :
      tk.updateMainLabel("(eventX,eventY):("+ str(eventX) + "," + str(eventY) + ")" )
    self.eventX = eventX
    self.eventY = eventY
  ####
  def motionRight(self, evRightX, evRightY):
    if evRightX != -1 and evRightY != -1 :
      tk.updateMainLabel("(evRightX,evRightY):("+ str(evRightX) + "," + str(evRightY) + ")" )
    self.evRightX = evRightX
    self.evRightY = evRightY
  ####
  def turnFront(self) :
    y = 0 - self.cameraRotAngle/90
    pj3d.eulerAngles("fox",0*self.d,y*self.d,0) ##Front
  def turnRight(self) :
    y = 1 - self.cameraRotAngle/90
    pj3d.eulerAngles("fox",0*self.d,y*self.d,0) ##Right
  def turnRear(self) :
    y = 2 - self.cameraRotAngle/90
    pj3d.eulerAngles("fox",0*self.d,y*self.d,0) ##Rear
  def turnLeft(self) :
    y = 3 - self.cameraRotAngle/90
    pj3d.eulerAngles("fox",0*self.d,y*self.d,0) ##Left
  ####
  def motionFromGameLoop(self) :
    if self.eventX == -1 and self.eventY == -1 :
      return
    ####
    fx,fy,fz = pj3d.getPosition("fox")
    cx,cy,cz = pj3d.getPosition("camera")
    dist = self.dist(fx,fy,fz,cx,cy,cz)
    ####m1 = (fz-cz)/(fx-cx)
    ####m2 = -(fx-cx)/(fz-cz)
    dx = 0
    dy = 0
    if self.eventX  >= 320 + 64 : ##Right
      self.turnRight()
      dx =  - (fz-cz)/dist
      dz = (fx-cx)/dist
      self.moveFox(fx,fy,fz,dx,dz)
    elif self.eventX < 320 - 64 : ##Left
      self.turnLeft()
      dx =  (fz-cz)/dist
      dz =  - (fx-cx)/dist
      self.moveFox(fx,fy,fz,dx,dz)
    ####
    if self.eventY >= 240 + 48 :##Rear
      self.turnRear()
      dx =  (fx-cx)/dist
      dz = (fz-cz)/dist
      self.moveFox(fx,fy,fz,dx,dz)
    elif self.eventY < 240 - 48 :##Front
      self.turnFront()
      dx = - (fx-cx)/dist
      dz = - (fz-cz)/dist
      self.moveFox(fx,fy,fz,dx,dz)
    ####
    self.rotateCameraAroundFox( self.cameraRotAngle )
  ####
  def moveFox(self, fx,fy,fz,dx,dz) :
    self.beforeFx = fx
    self.beforeFz = fz
    fx = fx + dx * self.diffBase
    fz = fz + dz * self.diffBase
    pj3d.setPosition("fox", fx, fy, fz)
  ####
  def motionRightFromGameLoop(self) :
    if self.evRightX == -1 and self.evRightY == -1 :
      return
    ####
    fx,fy,fz = pj3d.getPosition("fox")
    cx,cy,cz = pj3d.getPosition("camera")
    dist = self.dist(fx,fy,fz,cx,cy,cz)
    dx = 0
    dy = 0
    if self.evRightY >= 240 + 48 :##Rear
      dx = (fx-cx)/dist
      dz = (fz-cz)/dist
      cx = cx + dx * self.diffBase
      cz = cz + dz * self.diffBase
      dist = self.dist(fx,fy,fz,cx,cy,cz)
      if dist <= self.cameraDistMax and dist >= self.cameraDistMin :
        pj3d.setPosition("camera",cx, cy, cz)
    elif self.evRightY < 240 - 48 :##Front
      dx = - (fx-cx)/dist
      dz = - (fz-cz)/dist
      cx = cx + dx * self.diffBase
      cz = cz + dz * self.diffBase
      dist = self.dist(fx,fy,fz,cx,cy,cz)
      if dist <= self.cameraDistMax and dist >= self.cameraDistMin :
        pj3d.setPosition("camera",cx, cy, cz)
    ####
    if self.evRightX  >= 320 + 64 : ##Right;BackGround Goes Left;
      self.diffAngle = self.angleBase
      ####self.cameraRotAngle = ( self.cameraRotAngle - self.diffAngle ) % 360
      ####self.rotateCameraAroundFox( self.cameraRotAngle )
    elif self.evRightX  < 320 - 64 : ##Left;BackGround Goes Right;
      self.diffAngle = -self.angleBase
      ####self.cameraRotAngle = ( self.cameraRotAngle + self.diffAngle ) % 360 ## -90 = (-1)*360 + 270; (-90 % 360)->270, Needs to be Plus Number;
      ####self.rotateCameraAroundFox( self.cameraRotAngle )
  ####
  def motionCanvas(self, evCanvasX, evCanvasY):
    if evCanvasX != -1 and evCanvasY != -1 :
      tk.updateMainLabel("(evCanvasX,evCanvasY):(" + str(evCanvasX) + "," + str(evCanvasY) + ")" )
  ####
  def gameLoop(self) :
    self.motionFromGameLoop()
    self.motionRightFromGameLoop()
    if self.diffAngle != 0 :
      self.cameraRotAngle = ( self.cameraRotAngle + self.diffAngle ) % 360 ## -90 = (-1)*360 + 270; (-90 % 360)->270, Needs to be Plus Number;
      self.rotateCameraAroundFox( self.cameraRotAngle )
      self.diffAngle = 0
    ####
    fx,fy,fz = pj3d.getPosition("fox")
    if self.contactDx != 0 :
      fx += self.contactDx
      self.contactDx = 0
    if self.contactDz != 0 :
      fz += self.contactDz
      self.contactDz = 0
    pj3d.setPosition("fox",fx,fy,fz)
    self.showPos()
####
ca = CameraAngle()

tk.bindKeyPressFunction("s09ThreeDimTest:s09ThreeDimTest.ca.keyPress")

tk.bindButtonFunction("s09ThreeDimTest:s09ThreeDimTest.ca.button")

tk.bindMotionFunction("s09ThreeDimTest:s09ThreeDimTest.ca.motion")

tk.bindMotionRightFunction("s09ThreeDimTest:s09ThreeDimTest.ca.motionRight")

tk.bindMotionCanvasFunction("s09ThreeDimTest:s09ThreeDimTest.ca.motionCanvas")

tk.startTimerFunctionAfter("s09ThreeDimTest:s09ThreeDimTest.ca.gameLoop", 0.1)

pj3d.bindContactFunction("s09ThreeDimTest:s09ThreeDimTest.ca.contact")
