import numpy as np

def segment_loglog(logV, logI, window=4, tolerance=0.18, min_points=6):
    local_slopes = []
    for i in range(len(logV) - 1):
        slope = (logI[i + 1] - logI[i]) / (logV[i + 1] - logV[i])
        local_slopes.append(slope)
    local_slopes = np.array(local_slopes)
    smooth_slopes = np.convolve(local_slopes, np.ones(window) / window, mode='valid')

    segments = [0]
    for i in range(1, len(smooth_slopes)):
        if abs(smooth_slopes[i] - smooth_slopes[i - 1]) > tolerance:
            if i + window - 1 - segments[-1] >= min_points:
                segments.append(i + window - 1)
    segments.append(len(logV) - 1)
    # Remove very short segments
    filtered = [segments[0]]
    for idx in range(1, len(segments)):
        if segments[idx] - filtered[-1] >= min_points:
            filtered.append(segments[idx])
    return filtered