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
                    target_file_path = os.path.join(target_folder_path, os.path.basename(file_path))

                    # 移動先に同じ名前のファイルが存在する場合はリネームして移動する
                    if os.path.exists(target_file_path):
                        base_name, ext = os.path.splitext(os.path.basename(file_path))
                        new_file_name = f'{base_name}_duplicate{ext}'
                        target_file_path = os.path.join(target_folder_path, new_file_name)
                        print(f'File {os.path.basename(file_path)} already exists in {target_folder_path}. Renaming to {new_file_name}')

                    print(f'Moving {os.path.basename(file_path)} to {target_file_path}')
                    shutil.copy2(file_path, target_file_path)
                    print(f'{os.path.basename(file_path)} moved successfully.')

    except Exception as e:
        print(f'An error occurred: {str(e)}')

# 使用例
target_folder = r'C:\Users\yakim\Documents\sort'
extension = 'dat'
move_files_by_extension(target_folder, extension)
