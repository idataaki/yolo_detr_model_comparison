def make_confiusion_matrix():
    # make confusion matrix
    pass
def calc_acuracy_score():
    # get acuracy score
    pass
def calc_log_loss():
    # get log loss
    pass

# real files/labels.txt and store it
y_true = dict()
with open(r'files\labels.txt', 'r') as f:
    lines = f.readlines()
    p = 0
    for l in lines:
        i = l.index(')')
        y_true[p] = list(map(int, l[i+2:-1].split(' ')))
        p += 1
print(y_true)

# call detections/detr_det.py


# call detections/yolov5_det.py


# call detections/yolov8_det.py
