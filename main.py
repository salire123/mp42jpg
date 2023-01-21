import ffmpeg
import imageio
import os
video = 0
directory = 'video'
for filename in os.listdir(directory):
    f = os.path.join(filename)
    print(f)
    if os.path.isfile(f'{directory}/{f}'):
        reader = imageio.get_reader(f'{directory}/{f}')

        for frame_number, im in enumerate(reader):
            imageio.imwrite(f'data/{f}_frame_{frame_number}.jpg', im)
        video = video + 1
        print(f'{f} video have {frame_number} convert to jpg')
print(f'{video} video convert to jpg')
