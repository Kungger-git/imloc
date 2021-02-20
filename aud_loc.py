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


def find_audio():
    Positions().target_dir()
    Disk().mount(2)
    audio_formats = ('.3gp', '.aa', '.aac', '.aax', '.act', '.aiff',
                     '.alac', '.amr', '.ape', '.au', '.awb', '.dss',
                     '.dvf', '.flac', '.gsm', '.iklax', '.ivs', '.m4a',
                     '.m4b', '.mmf', '.mp3', '.mpc', '.msv', '.nmf', '.ogg',
                     '.oga', '.mogg', '.opus', '.org', '.ra', '.rm', '.raw',
                     '.rf64', '.sln', '.tta', '.voc', '.vox', '.wav', '.wma',
                     '.wv', '.webm', '.8svx', '.cda')
    for root, dirs, files in os.walk(os.getcwd()):
        for audio in files:
            if audio.endswith(audio_formats):
                found.append(os.path.join(root, audio))
                print(colorama.Fore.GREEN,
                        f'[*] {audio}', colorama.Style.RESET_ALL)

                if not os.path.exists(os.path.join(root, audio)):
                    non_existent.append(os.path.join(root, audio))
                    continue

                sizes.append(os.path.getsize(os.path.join(root, audio)))
            else:
                continue
        for dir in dirs:
            fol.append(os.path.join(root, dir))
    Disk().unmount(2)


if __name__ == '__main__':
    origin = os.getcwd()
    found, sizes, non_existent, fol = [], [], [], []
    colorama.init()
    find_audio()
    Positions().local_dir()

    if not os.path.exists('Records/'):
        os.mkdir('Records/')

    i = 0
    with open('Records/Audios_Found.txt', 'w') as f:
        for audio in found:
            i += 1
            f.write(f'{audio}\n')

    print('Total Audios: {:,}'.format(i))
    print('Size of Found Audios: {:,}'.format(sum(sizes)))

    i = 0
    with open('Records/Ex_Audio_not_porn.txt', 'w') as f:
        for ex_audio in non_existent:
            i += 1
            f.write(f'{ex_audio}\n')

    with open('Records/Directories_aud.txt', 'w') as f:
        for dir in fol:
            f.write(f'{dir}\n')

    print(f'Total Non Existent Audio: {i}')
