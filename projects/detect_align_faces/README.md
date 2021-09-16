# Detect and align faces

This algorithm can detect the faces from picture and then align them.

## Requirement

**Dowload model parameters:**

You should dowload the [model parameters](http://dlib.net/files/shape_predictor_68_face_landmarks.dat.bz2) 
from dlib, decompress and move to `./dat`

**Installation:**

```shell
$ pip install -r requirements.txt
```

## Usage

```shell
$ python3 main.py [pic1, pic2...]
```

After the script finished, you will get some faces picture in the same
directory.
