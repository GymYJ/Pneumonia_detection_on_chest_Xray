import glob
from PIL import Image

folder = ["train","test","val"]
cate = ["NORMAL","PNEUMONIA"]
for f in folder:

    img_dir = "C:\\Users\\YJ\\Desktop\\project\\chest_xray\\"
    img_dir = img_dir+f+"\\"
    temp = img_dir
    for c in cate:
        img_dir = temp + c + "\\*.jpeg"
        imglist = glob.glob(img_dir)
        for img_path in imglist:
            img = Image.open(img_path)
            img.resize((224,224)).save(img_path)

