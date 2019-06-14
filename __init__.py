import cv2
import tf
import evaluation as ev


tf.getInputPhoto('input.png')
tf.processImg('input.png', 'output')

inp = cv2.imread('static/uploads/input.png', 1)
outp = cv2.imread('static/result/output.png', 1)

cv2.imshow('Input', inp)
cv2.imshow('Output', outp)
cv2.waitKey()

'''
inp = cv2.imread('static/result-db/1a.png', 1)
outp = cv2.imread('static/result-db/1b.png', 1)

psnr = ev.psnr(inp, outp, 1)
print(psnr)
'''
