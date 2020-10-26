import os

class PathInfo:
    def __init__(self, path):
        self.path = path
        self._files = []
        self._folders =[]
        self._get_list_dir()

    def _get_list_dir(self):
        path_list_dir = os.listdir(self.path)
        for item in path_list_dir:
            path_item = os.path.join(self.path, item)
            if os.path.isfile(path_item):
                self._files.append(path_item)
            else:
                self._folders.append(path_item)

    def __repr__(self):
        return f"Files: {self._files}\nFolders: {self._folders}"

    def show_files(self):
        return self._files

    def show_folders(self):
        return self._folders


path_info = PathInfo("OLD_HOME_WORK")
print(path_info)
print(path_info.show_files())
print(path_info.show_folders())