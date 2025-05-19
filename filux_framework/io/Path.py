from vaultio.io.File import File
from urllib.request import urlopen

class Path:
    def __init__(self):
        pass
    
    ## Basic Operations ##
    def compare_files(self, PathOne, PathTwo):
        File_1 = File(PathOne)
        File_2 = File(PathTwo)
        
        if File_1.get_content == File_2.get_content() and File_1.get_file_hash() == File_2.get_file_hash() and File_1.get_file_size() == File_2.get_file_size():
            return True
        else:
            return False

    def download_file(self, destPath, URL):
        try:
            with urlopen(URL) as response, open(destPath, 'wb') as out_file:
                out_file.write(response.read())
        except Exception as e:
            print(f"Error downloading file: {e}")