import shutil
import random
import glob

total = list(range(61944)) # NORMAL 파일의 총 개수 61944

random.shuffle(total)

selected = total[0:5704] # PNEUMONIA 파일의 총 개수인 5704와 갯수를 맞춤
selected.sort()
selected_index = 0

cur_dir = "C:/Users/Yujin/Desktop/NORMAL/"
mov_dir = "../shuffled_chest_xray2/train/NORMAL/"

files = glob.glob(cur_dir+"*.jpeg")
for i, f in enumerate(files): # 모든 NORMAL 파일 중에서 selected에 선택된 인덱스에 해당한 파일만 옮김
    if i == selected[selected_index]:
        file = f[30:]
        shutil.move(f, mov_dir+file)
        print(str(selected_index+1)+"번째 파일 이동 완료")
        selected_index += 1
        if selected_index == 5704:
            break

# 위와 같은 진행
total = list(range(5704)) # 선택된 NORMAL 파일의 개수 5704

random.shuffle(total)

selected = total[0:1141] # 5704의 20%인 1141개 선별
selected.sort()
selected_index = 0

cur_dir = "../shuffled_chest_xray2/train/NORMAL/"
mov_dir = "../shuffled_chest_xray2/test/NORMAL/"

files = glob.glob(cur_dir+"*.jpeg")
for i, f in enumerate(files):
    if i == selected[selected_index]:
        file = f[37:]
        shutil.move(f, mov_dir+file)
        print(str(selected_index+1)+"번째 파일 이동 완료")
        selected_index += 1
        if selected_index == 1141:
            break

# 위와 같은 진행
total = list(range(5704)) # PNEUMONIA 파일의 개수 5704

random.shuffle(total)

selected = total[0:1141] # 5704의 20%인 1141개 선별
selected.sort()
selected_index = 0

cur_dir = "../shuffled_chest_xray2/train/PNEUMONIA/"
mov_dir = "../shuffled_chest_xray2/test/PNEUMONIA/"

files = glob.glob(cur_dir+"*.jpeg")
for i, f in enumerate(files):
    if i == selected[selected_index]:
        file = f[40:]
        shutil.move(f, mov_dir+file)
        print(str(selected_index+1)+"번째 파일 이동 완료")
        selected_index += 1
        if selected_index == 1141:
            break
