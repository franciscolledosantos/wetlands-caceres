import os; import matplotlib; matplotlib.use('Agg')
FIG = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'figuras'); os.makedirs(FIG, exist_ok=True)
import matplotlib.pyplot as plt, numpy as np
plt.rcParams.update({'font.family':'DejaVu Serif','font.size':9})
params=['COD','TSS /\nturbidity','Total P','Nitrate','Nitrite','Ammonia','BOD$_5$']
s1=[71.7,94.0,88.8,82.9,76.7,87.2,29.1]
s2=[70,90,88,80,65,85,15]
s3=[np.nan,70.0,-34.6,np.nan,34.2,np.nan,np.nan]
nu={6}  # pilot BOD: measured but not used (analytical caveat)
x=np.arange(len(params)); w=0.26
fig,ax=plt.subplots(figsize=(6.3,3.9))
c=['#9ecae1','#3182bd','#e6550d']
lab=['Scale 1: bench, synthetic sewage, $C. alternifolius$','Scale 2: bench, raw sewage, $H. psittacorum$','Scale 3: pilot HSSF, raw sewage, $H. psittacorum$']
for i,(s,cc,l) in enumerate(zip([s1,s2,s3],c,lab)):
    v=np.array(s,float); bars=ax.bar(x+(i-1)*w,np.nan_to_num(v),w,color=cc,label=l,edgecolor='k',lw=0.4)
    if i==2:
        bars[4].set_hatch('////')
    for xi,vi in zip(x+(i-1)*w,v):
        if np.isnan(vi): ax.text(xi,2,'n.u.' if (i==2 and int(round(xi-(i-1)*w)) in nu) else 'n.m.',ha='center',va='bottom',rotation=90,fontsize=6.5)
        else: ax.text(xi,vi+(2 if vi>=0 else -2),f'{vi:.0f}',ha='center',va='bottom' if vi>=0 else 'top',fontsize=6.5)
ax.axhline(0,color='k',lw=0.6); ax.set_xticks(x); ax.set_xticklabels(params)
ax.set_ylabel('Removal efficiency (%)'); ax.set_ylim(-50,110)
ax.legend(fontsize=7,loc='lower center',bbox_to_anchor=(0.5,1.0),ncol=1,frameon=False)
ax.spines[['top','right']].set_visible(False)
fig.tight_layout()
for e in ['tif','png']: fig.savefig(os.path.join(FIG, f'Figure3.{e}'),dpi=300)
# Fig 4
P=[('pH','',7.08,7.12,0.46),('Dissolved oxygen','mg L$^{-1}$',2.98,3.09,0.19),('TDS','mg L$^{-1}$',332.5,283.0,0.15),('Turbidity','NTU',207.5,62.4,0.004),('Nitrite','mg NO$_2^-$ L$^{-1}$',51.2,33.7,0.19),('Total phosphorus','mg L$^{-1}$',1.79,2.41,0.33),('BOD$_5$','mg L$^{-1}$',3.73,4.91,0.46)]
fig,axs=plt.subplots(2,4,figsize=(6.3,4.6)); axs=axs.ravel(); axs[7].axis('off')
for ax,(n,u,a,b,p) in zip(axs,P):
    col='#31a354' if p<0.05 else '#888888'
    ax.bar([0,1],[a,b],color=['#bdbdbd',col],edgecolor='k',lw=0.4,width=0.7)
    ch=100*(b-a)/a
    ax.set_title(n,fontsize=7.5); ax.set_xticks([0,1]); ax.set_xticklabels(['In','Out'],fontsize=7)
    ax.set_ylabel(u,fontsize=7); ax.tick_params(axis='y',labelsize=6.5)
    top=max(a,b); ax.set_ylim(0,top*1.32)
    ax.text(0.5,top*1.08,f'{ch:+.0f}%\np$_{{Holm}}$={p:g}',ha='center',fontsize=6.3)
    ax.spines[['top','right']].set_visible(False)
axs[7].text(-0.05,0.5,'Green bar: outlet differs\nfrom inlet after Holm\nadjustment\n(p < 0.05).\nGrey: not significant.\nn = 12 pairs on 6 dates\n(TDS: 10 non-zero;\nBOD: 8).',fontsize=7,va='center'); fig.tight_layout(w_pad=1.0,h_pad=1.2)
for e in ['tif','png']: fig.savefig(os.path.join(FIG, f'Figure4.{e}'),dpi=300)
