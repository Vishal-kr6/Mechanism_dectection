from utils.io_utils import load_iv_data
from segmentation.slope_segmentation import segment_loglog
from utils.plot_utils import plot_segments
from classify import classify_mechanism
import numpy as np

def main():
    V, I = load_iv_data("data/RRAMdevice1.csv")
    mask = (np.abs(V) > 1e-12) & (np.abs(I) > 1e-15) & (V >= 0.01) & (V <= 2.5)
    Vf = V[mask]
    If = I[mask]
    logV = np.log10(np.abs(Vf))
    logI = np.log10(np.abs(If))
    segments = segment_loglog(logV, logI, window=4, tolerance=0.18, min_points=6)
    labels = []
    for i in range(len(segments) - 1):
        seg_logV = logV[segments[i]:segments[i+1]+1]
        seg_logI = logI[segments[i]:segments[i+1]+1]
        seg_V = Vf[segments[i]:segments[i+1]+1]
        seg_I = If[segments[i]:segments[i+1]+1]
        mech, slope, r2 = classify_mechanism(seg_logV, seg_logI, seg_V, seg_I)
        print(f"Segment {i+1}: Mechanism={mech}, Slope={slope}, R2={r2}")
        labels.append(f"{mech}\nSlope={slope:.2f}" if slope else mech)
    plot_segments(logV, logI, segments, labels)

if __name__ == "__main__":
    main()