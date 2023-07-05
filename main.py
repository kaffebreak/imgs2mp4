import cv2
import os
import glob
import tqdm


# 画像が格納されているディレクトリ
path = "./images/"
image_files = glob.glob( path + "*.jpg" )


# 出力する動画のパスとファイル名
output_video = 'video.mp4'

# 動画のフレームレート（1秒あたりのフレーム数）
frame_rate = 1#12

# 画像のサイズ（横幅、高さ）
width = 1920
height = 1080


# 出力動画の設定
#fourcc = cv2.VideoWriter_fourcc("H", "2", "6", "4") #SNS用
fourcc = cv2.VideoWriter_fourcc("m", "p", "4", "v") #普通のmp4

video_out = cv2.VideoWriter(output_video, fourcc, frame_rate, (width, height))

for image_file in tqdm.tqdm(image_files):
    image = cv2.imread(image_file)
    
    # 画像のアスペクト比を計算
    img_height, img_width, _ = image.shape
    aspect_ratio = img_width / img_height
    
    # 縦長の画像の場合、横幅を短辺と揃えるようにリサイズ
    if aspect_ratio < 1:
        new_width = int(height * aspect_ratio)
        image = cv2.resize(image, (new_width, height))
        
        # 画像を中央に配置し、余白を黒で埋める
        left_padding = (width - new_width) // 2
        right_padding = width - new_width - left_padding
        padding_color = [0, 0, 0]  # 黒色
        image = cv2.copyMakeBorder(image, 0, 0, left_padding, right_padding, cv2.BORDER_CONSTANT, value=padding_color)
    else:
        image = cv2.resize(image, (width, height))
    
    # 動画にフレームを追加
    video_out.write(image)

# 出力動画を保存し、リソースを解放
video_out.release()