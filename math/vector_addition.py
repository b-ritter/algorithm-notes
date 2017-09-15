import numpy as np

a = np.radians(20)
b = np.radians(240)

v = np.array([8*np.cos(a), 8*np.sin(a)])
w = np.array([5*np.cos(b), 5*np.sin(b)])

vw = np.add(v,w)

# print(np.linalg.norm(vw))
# print(360 + np.degrees(np.arctan(vw[1]/vw[0])))

c = np.radians(235)
print(12*np.cos(c), 12*np.sin(c))