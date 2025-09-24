import kinematics as k
from math import degrees, radians, sin, cos
# velocity: m/s
# angle: degrees
def perform(velocity, angle):
  angle = radians(angle)
  vx = velocity * cos(angle)
  vy = velocity * sin(angle)
  a = -9.8
  print("Max height: %s" % k.kinematics2(vf=0, vi=vy, a=a, d="?"))
  print("Total air time: %s" % k.kinematics3(vf=0, vi=vy, a=a, t="?"))
  
