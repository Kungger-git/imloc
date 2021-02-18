import os, colorama, time


class Positions():
    def target_dir(self):
        os.chdir('/home/kali/Desktop')
        return 'Transferred to target directory'


    def local_dir(self):
        os.chdir(origin)
        return 'Transferred to original directory'


class Disk():
    def mount(self, seconds):
        os.system('sudo mount /dev/sda3 ~/Desktop')
        print(colorama.Fore.YELLOW,
                '\nDisk Mounted\n', colorama.Style.RESET_ALL)
        time.sleep(seconds)
        return 'Disk Mounted'


    def unmount(self, seconds):
        time.sleep(seconds)
        os.system('sudo umount /dev/sda3 ~/Desktop')
        print(colorama.Fore.YELLOW,
                '\nDisk Unmounted\n', colorama.Style.RESET_ALL)
        return 'Disk Unmounted'


def find_videos():
    Positions().target_dir()
    Disk().mount(2)
    vid_formats = ('.mkv', '.mp4', '.mpeg', '.mov', '.wmv', '.flv',
            '.avi', '.avchd', '.webm', '.mpe', '.mpv', '.ogg',
            'm4v', '.m4v', '.avi', '.qt', '.swf')
    for root, dirs, files in os.walk(os.getcwd()):
        for video in files:
            if video.endswith(vid_formats):
                found.append(os.path.join(root, video))
                print(colorama.Fore.GREEN,
                        f'[*] {video}', colorama.Style.RESET_ALL)

                if not os.path.exists(os.path.join(root, video)):
                    non_existent.append(os.path.join(root, video))
                    continue

                sizes.append(os.path.getsize(os.path.join(root, video)))
            else:
                continue
        for dir in dirs:
            fol.append(os.path.join(root, dir))
    Disk().unmount(2)


if __name__ == '__main__':
    origin = os.getcwd()
    found, sizes, non_existent, fol = [], [], [], []
    colorama.init()
    find_videos()
    Positions().local_dir()

    if not os.path.exists('Records/'):
        os.mkdir('Records/')

    i = 0
    with open('Records/Videos_Found.txt', 'w') as f:
        for video in found:
            i += 1
            f.write(f'{video}\n')

    print('Total Videos: {:,}'.format(i))
    print('Size of Found Videos: {:,}'.format(sum(sizes)))

    i = 0
    with open('Records/Ex_Videos_not_porn.txt', 'w') as f:
        for ex_video in non_existent:
            i += 1
            f.write(f'{ex_video}\n')

    with open('Directories_vid.txt', 'w') as f:
        for dir in fol:
            f.write(f'{dir}\n')

    print(f'Total Non Existent Videos: {i}')
