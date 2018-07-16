import matplotlib.pyplot as plt
import numpy as np

plt.figure(figsize=(18,6))   #set the size of the figure.
Size=20
matplotlib.rc('xtick', labelsize=Size)   #去除当前tick,并定义字体大小
matplotlib.rc('ytick', labelsize=Size)

plt.subplot(121)
nofont = {'fontname':'Times New Roman'}
chfont = {'fontname':'Arial'}      # Set up the font
x=np.linspace(-10,10,100)
plt.plot(x,pylab.sin(x),color="red",linestyle="--",linewidth=2,label='Chris')
plt.legend(loc=2,prop={'size':Size},frameon=False)   #添加label后下面必须添加legend()
ax=plt.gca()      #To get the current polar axes
Xscale=np.around(np.linspace(-10,10,5),decimals=1)
ax.set_xticks(Xscale)
ax.set_xticklabels(('-10','5','0','5','10'),**nofont)   #Change the font of xticks and specify the xticks
for label in (ax.get_yticklabels()):
    label.set_fontname('Times New Roman')   #Change the font of yticks
plt.xlabel(r"Time $\tau$",size=Size,**chfont)   #Add X-label
plt.ylabel(r"Amplitude $\varphi$",size=Size,**nofont)   #Add Y-label
plt.title("Dependence relation",y=1.01,size=Size,**nofont)   #add title and set its space/ font
plt.axhline(y=0,color="g",linewidth=1,linestyle="-.")    #horizontal axial line
plt.axvline(x=0,color="b",linewidth=1,linestyle=':')     #vertical axial line

plt.subplot(122,polar=True)   #极坐标图
plt.plot(x,pylab.tan(x),color="red",linestyle="--",linewidth=2)
plt.title("Christing",size=Size,y=1.1,x=0,**chfont)
plt.tight_layout()    #是图片变得紧凑
plt.subplots_adjust(wspace=0.01)   #调节子图之间的宽度间隔
plt.savefig('Figsave/fig_1D',dpi=512,bbox_inches='tight')
plt.show()
