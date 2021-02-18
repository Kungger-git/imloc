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


def find_photos():
    Positions().target_dir()
    Disk().mount(2)
    imgs = ('.jpg', '.jpeg', '.png')
    for root, dirs, files in os.walk(os.getcwd()):
        for photo in files:
            if photo.endswith(imgs):
                found.append(os.path.join(root, photo))
                print(colorama.Fore.GREEN,
                        f'[*] {photo}', colorama.Style.RESET_ALL)

                if not os.path.exists(os.path.join(root, photo)):
                    non_existent.append(os.path.join(root, photo))
                    continue

                sizes.append(os.path.getsize(os.path.join(root, photo)))
            else:
                continue
        for dir in dirs:
            fol.append(os.path.join(root, dir))
    Disk().unmount(2)


if __name__ == '__main__':
    origin = os.getcwd()
    found, sizes, non_existent, fol = [], [], [], []
    colorama.init()
    find_photos()
    Positions().local_dir()

    i = 0
    with open('Photos_Found.txt', 'w') as f:
        for photo in found:
            i += 1
            f.write(f'{photo}\n')

    print('Total photos: {:,}'.format(i))
    print('Size of Found Photos: {:,}'.format(sum(sizes)))

    if not os.path.exists('Records/'):
        os.mkdir('Records/')

    i = 0
    with open('Records/Ex_Photos_not_porn.txt', 'w') as f:
        for ex_photo in non_existent:
            i += 1
            f.write(f'{ex_photo}\n')

    with open('Records/Directories_img.txt', 'w') as f:
        for dir in fol:
            f.write(f'{dir}\n')

    print(f'Total Non Existent Photos: {i}')
