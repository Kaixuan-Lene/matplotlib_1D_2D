import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import datetime

starttime=datetime.datetime.now()   #计时开始

SPC_THG_S=np.loadtxt("Datasave\SPC_THG_s.txt")
SPC_THG_P=np.loadtxt("Datasave\SPC_THG_p.txt")    #加载TXT数据

Size=20
nofont = {'fontname':'Times New Roman'}
chfont = {'fontname':'Arial'}

matplotlib.rc('xtick',labelsize=Size)
matplotlib.rc('ytick',labelsize=Size)
extent=[0,1.334,0,90]    #分别指定XY轴坐标区间上下限
plt.figure(figsize=(12,4.59))   #设置图片大小

plt.subplot(121)
plt.imshow(SPC_THG_S,extent=extent,cmap="jet", aspect='auto',origin='lower')

plt.clim(0,1)   #clobar 区间
cb=plt.colorbar()
cb.set_ticks(np.linspace(0,1,6))   #设置colorbar's ticks
for l in cb.ax.yaxis.get_ticklabels():
    l.set_family("Times New Roman")   #设置字体

ax = plt.gca()    #To get the current axes
Xscale = np.around(np.arange(0, 1.333, 0.32), decimals=2)
ax.set_xticks(Xscale)
ax.set_xticklabels(('0', '0.32', '0.64', '0.96', '1.28'), **nofont)
#设置X轴
Yscale = np.linspace(0, 90, 4)
ax.set_yticks(Yscale)
ax.set_yticklabels(('0$\degree$', '30$\degree$', '60$\degree$', '90$\degree$'), **nofont)
#设置Y轴
plt.xlabel(r"Time delay $\tau $ (fs)", size=Size, **chfont)
plt.ylabel(r'Polarization angle $\theta$', size=Size, **chfont)
plt.title(r'$s$-polarized THG intensity',size=Size,**chfont)
#设置label and title.
plt.subplot(122)
plt.imshow(SPC_THG_P,extent=extent,cmap="jet", aspect='auto',origin='lower')
plt.clim(0,1)
cb=plt.colorbar()
cb.set_ticks(np.linspace(0,1,6))
for l in cb.ax.yaxis.get_ticklabels():
    l.set_family("Times New Roman")

ax = plt.gca()
Xscale = np.around(np.arange(0, 1.333, 0.32), decimals=2)
ax.set_xticks(Xscale)
ax.set_xticklabels(('0', '0.32', '0.64', '0.96', '1.28'), **nofont)

Yscale = np.linspace(0, 90, 4)
ax.set_yticks(Yscale)
ax.set_yticklabels(('0$\degree$', '30$\degree$', '60$\degree$', '90$\degree$'), **nofont)

plt.xlabel(r"Time delay $\tau $ (fs)", size=Size, **chfont)
plt.ylabel(r'Polarization angle $\theta$', size=Size, **chfont)
plt.title(r'$p$-polarized THG intensity',size=Size,**chfont)

plt.tight_layout()
plt.subplots_adjust(wspace=0.23)
#plt.savefig("Figsave/fig_2D",dpi=512,bbox_inches='tight')   #保存图片
endtime=datetime.datetime.now()   #计时结束
usetime=(endtime-starttime).microseconds
print(usetime,"us")
plt.show()   #显示图片
