#-*-coding:utf-8-*-
import os ,sys
caffe_root='/home/yangwentao/caffe-master/'
os.chdir(caffe_root)
sys.path.insert(0,caffe_root+'python')
import caffe                        
import numpy as np
from PIL import Image

test_dir = '/home/yangwentao/caffe-master/data/myself/sunvisor/test33/'
dst_dir = '/home/yangwentao/caffe-master/data/myself/sunvisor/TResize/'
test_image = []
for file in os.listdir(test_dir):
    imgOpen = Image.open(test_dir+file)
    imgOpen = imgOpen.resize((60,60),Image.ANTIALIAS)
    imgOpen.save(dst_dir+file)
    
    test_image.append(test_dir + file)
test_image = list(test_image)

def test(my_project_root, deploy_proto):
     filename='/home/yangwentao/caffe-master/data/myself/sunvisor/result.txt'
     caffe_model = my_project_root + '/trainlm/solver_0419_iter_10000.caffemodel'
     with open(filename,'w') as f:      
     	for i in range(0,len(test_image)):
		#caffe_model = my_project_root + '/trainlenet/solver_iter_10000.caffemodel'
          img = test_image[i]
     		#print img                       
                #img='/home/yinlili/caffe/caffe-master/data/myself/test/T/P_20180302093615_784_0.jpeg'
          net = caffe.Net(deploy_proto, caffe_model, caffe.TEST)       
          transformer = caffe.io.Transformer({'data': net.blobs['data'].data.shape})
          transformer.set_transpose('data', (2,0,1))
          transformer.set_mean('data', np.array([104,117,123]))
          transformer.set_raw_scale('data', 255) 
          transformer.set_channel_swap('data', (2,1,0))

          im = caffe.io.load_image(img)
          net.blobs['data'].data[...] = transformer.preprocess('data',im)
          #out = net.forward()
      
          labels = np.loadtxt('/home/yangwentao/caffe-master/data/myself/sunvisor/synset_words.txt', str,delimiter='\n')
          prob = net.blobs['prob'].data[0].flatten()
          print(prob) 
          order = prob.argsort()[-1]
          print(img, labels[order])
          f.write("%s %s\n" %(img,labels[order]))
          f.close()
if __name__ == '__main__':
   
    my_project_root = "/home/yangwentao/caffe-master/data/myself/sunvisor"
    deploy_proto = my_project_root + "/deploy_0419.prototxt"
    test(my_project_root, deploy_proto)
