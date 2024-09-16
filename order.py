import os, sys, shutil, re, datetime, json                              

# The sets of extensions separeted by category
extensions_types : dict = json.loads(open(os.path.abspath(".        /types.json"), "r").read())

class Sorter():
    def __init__(self, path:str="./"):
        self.working_path = os.path.abspath(path)
        self.__excluded_paths = ['.git', '.godot', '.venv', '.vscode', 'node_modules']              

    def remove_if_empty(self, path):
        dir_list : list = [dir.path for dir in list(filter(lambda entry: entry.is_dir(), os.scandir(path)))]
        for (entry) in dir_list:    
            if os.listdir(entry) == []:
                os.rmdir(entry)

    def move(self, path: str):
        for entry in os.scandir(path):
            if entry.is_dir() and entry.path not in self.__excluded_paths:
                self.move(entry.path)
            elif entry.is_file() and path != self.working_path:
                
                destination = os.path.join(self.working_path, entry.name)

                if os.path.exists(destination):
                    base, extension = os.path.splitext(entry.name)
                    counter = 1
                    new_name = f"{base}_{counter}{extension}"
                    new_destination = os.path.join(self.working_path, new_name)

                    while os.path.exists(new_destination):
                        counter += 1
                        new_name = f"{base}_{counter}{extension}"
                        new_destination = os.path.join(self.working_path, new_name)

                    shutil.move(entry.path, new_destination)
                else:
                    shutil.move(entry.path, self.working_path)
            else:
                continue
        self.remove_if_empty(path)

    def sort_by_date(self):
        
        self.move(self.working_path)
        
        files_list: list = list(filter(lambda entry: entry.is_file(), os.scandir(self.working_path)))
        files_path_list: list = [file.path for file in files_list]
        year_list: list = []

        for (file) in files_path_list:
            file_mdate: str = str(datetime.datetime.fromtimestamp(os.stat(file).st_mtime))

            # mdate_list format [YYYY, MM, DD, "HH:MM:SS"]            
            mdate_list: list = re.split(r"[-\s]", file_mdate)

            if (mdate_list[0] not in year_list):
                year_list.append(mdate_list[0])
                os.mkdir(f"{self.working_path}/{mdate_list[0]}/")
                
            month_path: str = f"{self.working_path}/{mdate_list[0]}/{mdate_list[1]}"
            if not(os.path.exists(month_path)):
                os.mkdir(month_path)
            shutil.move(file, month_path)

    def sort_by_type(self):
        
        self.move(self.working_path)

        files_list: list = list(filter(lambda entry: entry.is_file(), os.scandir(self.working_path)))
        files_path_list: list = [file.path for file in files_list]
        types_list: list = []

        for (file) in files_path_list:

            file_name : str = os.path.basename(file)
            file_extension : str = file_name.split(".")[-1].lower()

            for (index, type) in enumerate(extensions_types.keys()):
                if (file_extension in extensions_types[type] and index < 8):
                    if ((type not in types_list)):
                        types_list.append(type)
                        os.mkdir(f"{self.working_path}/{type}/")
                    shutil.move(file, f"{self.working_path}/{type}/")
                    break
                elif (index == 8):
                    if ((type not in types_list)):    
                        types_list.append(type) 
                        os.mkdir(f"{self.working_path}/{type}/")
                    shutil.move(file, f"{self.working_path}/{type}/")

if __name__ == "__main__":
        if (len(sys.argv) in [2,3]):
            if (sys.argv[1].lower() in ["-d", "-t"] and os.path.exists(os.path.abspath(sys.argv[2]))):
                    v = Sorter(sys.argv[2])
                    if (sys.argv[1].lower() == "-d"):
                        v.sort_by_date()
                    elif (sys.argv[1].lower() == "-t"):
                        v.sort_by_type()
