#!/usr/bin/env python3
#
# Copyright(C) 2021 wuyaoping
#


import numpy as np
import os.path as osp
import sys
import cv2
import dlib

OUT_SIZE = (224, 224)
LEFT_EYE_RANGE = (36, 42)
RIGHT_EYE_RABGE = (42, 48)
LEFT_EYE_POS = (0.35, 0.3815)
DAT_PATH = "./dat/shape_predictor_68_face_landmarks.dat"


def main(files):
    detector = dlib.get_frontal_face_detector()
    sp = dlib.shape_predictor(DAT_PATH)

    for file in files:
        img = cv2.imread(file, cv2.IMREAD_ANYCOLOR)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        faces = detect_align_faces(detector, sp, img)
        for (idx, face) in enumerate(faces):
            face = cv2.cvtColor(face, cv2.COLOR_RGB2BGR)
            filename, ext = osp.splitext(file)
            filename += '_face_{:03}'.format(idx) + ext
            cv2.imwrite(filename, face)


def detect_align_faces(detector, sp, img):
    faces = detector(img, 1)
    res = []
    for face in faces:
        shape = sp(img, face)
        left, right = shape_to_pos(shape)
        left_center = np.mean(left, axis=0)
        right_center = np.mean(right, axis=0)

        dx = right_center[0] - left_center[0]
        dy = right_center[1] - left_center[1]
        angle = np.degrees(np.arctan2(dy, dx))
        dist = np.sqrt(dy ** 2 + dx ** 2)
        out_dist = OUT_SIZE[0] * (1 - 2 * LEFT_EYE_POS[0])
        scale = out_dist / dist
        center = ((left_center + right_center) // 2).tolist()

        mat = cv2.getRotationMatrix2D(center, angle, scale)
        mat[0, 2] += (0.5 * OUT_SIZE[0] - center[0])
        mat[1, 2] += (LEFT_EYE_POS[1] * OUT_SIZE[1] - center[1])
        res_face = cv2.warpAffine(img, mat, OUT_SIZE, flags=cv2.INTER_CUBIC)
        res.append(res_face)

    return res


def shape_to_pos(shape):
    parts = []
    for p in shape.parts():
        parts.append((p.x, p.y))

    left = parts[LEFT_EYE_RANGE[0]: LEFT_EYE_RANGE[-1]]
    right = parts[RIGHT_EYE_RABGE[0]: RIGHT_EYE_RABGE[-1]]

    return (np.array(left), np.array(right))


if __name__ == '__main__':
    main(sys.argv[1:])
