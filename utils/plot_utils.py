import matplotlib.pyplot as plt

def plot_segments(logV, logI, segments, labels=None):
    plt.figure(figsize=(12,7))
    plt.plot(logV, logI, 'ko', ms=3, alpha=0.4)
    colors = ['tab:green', 'tab:blue', 'tab:purple', 'tab:orange', 'tab:red', 'tab:cyan']
    for i in range(len(segments) - 1):
        seg_logV = logV[segments[i]:segments[i+1]+1]
        seg_logI = logI[segments[i]:segments[i+1]+1]
        plt.plot(seg_logV, seg_logI, '-', color=colors[i % len(colors)], lw=2)
        if labels:
            plt.text(seg_logV[len(seg_logV)//2], seg_logI[len(seg_logI)//2], labels[i], fontsize=10)
    plt.xlabel('log10(|V|)')
    plt.ylabel('log10(|I|)')
    plt.title('Log-Log I-V Segmentation')
    plt.tight_layout()
    plt.show()
