import numpy as np

def Cal_IoU(GT_bbox, Pred_bbox):
    '''
    Args:
        GT_bbox:  the bounding box of the ground truth
        Pred_bbox: the bounding box of the predicted
    Returns:
        IoU: Intersection over Union
    '''
    #1. Calculate the area of the intersecting area
    ixmin = max(GT_bbox[0], Pred_bbox[0])
    iymin = max(GT_bbox[1], Pred_bbox[1])
    ixmax = min(GT_bbox[2], Pred_bbox[2])
    iymax = min(GT_bbox[3], Pred_bbox[3])
    iw = np.maximum(ixmax - ixmin + 1., 0.) # the weight of the area
    ih = np.maximum(iymax - iymin + 1., 0.) # the height of the area
    area = iw * ih

    #2. Calculate the area of all area
    #S = S1 + S2 - area
    S1 = (Pred_bbox[2] - GT_bbox[0] + 1) * (Pred_bbox[3] - GT_bbox[1] + 1)
    S2 = (GT_bbox[2] - GT_bbox[0] + 1) * (GT_bbox[3] - GT_bbox[1] + 1)
    S = S1 + S2 - area

    #3. Calculate the IoU
    iou = area / S
    return iou

if __name__ == "__main__":
    pred_bbox = np.array([40, 40, 100, 100])
    gt_bbox = np.array([70, 80, 110, 130])
    print(Cal_IoU(pred_bbox, gt_bbox))
