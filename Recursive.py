import os
import shutil

def move_files_by_extension(target_folder, extension):
    desktop_path = os.path.expanduser(r'C:\Users\yakim\Desktop')
    target_folder_path = os.path.join(target_folder, extension)
    if not os.path.exists(target_folder_path):
        os.makedirs(target_folder_path)
    extension = '.' + extension

    try:
        # デスクトップ上のすべてのファイルとフォルダーを再帰的に探索
        for root, _, files in os.walk(desktop_path):
            for file in files:
                if file.endswith(extension):
                    file_path = os.path.join(root, file)
                    # ファイル名から空白を置換して '-' にする例
                    filename = file_path.replace(':', '-').replace('/', '-').replace('\\', '-')  # '\\' でバックスラッシュを正しく置換
                    print(f'{filename}')
                    target_file_path = os.path.join(target_folder_path, filename)
                    #print(f'Copying {file_path} to {target_file_path}')
                    shutil.copy2(file_path, target_file_path)

    except Exception as e:
        print(f'An error occurred: {str(e)}')

target_folder = r'C:\Users\yakim\Documents\sort'
extension = ''
move_files_by_extension(target_folder, extension)
