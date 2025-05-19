import hashlib
import os
import platform
import stat
import zipfile
import datetime
import win32com.client

DEFAULT_METADATA = ['Name', 'Size', 'Item type', 'Date modified', 'Date created', 'Date accessed', 'Attributes', 'Offline status', 'Availability', 'Perceived type', 'Owner', 'Kind', 'Date taken', 'Contributing artists', 'Album', 'Year', 'Genre', 'Conductors', 'Tags', 'Rating', 'Authors', 'Title', 'Subject', 'Categories', 'Comments', 'Copyright', '#', 'Length', 'Bit rate', 'Protected', 'Camera model', 'Dimensions', 'Camera maker', 'Company', 'File description', 'Masters keywords', 'Masters keywords']

class File:
    def __init__(self, path):
        self._path = path # Full Path with File
        self._dirname, self._filename = os.path.split(self._path) # Parent Folder and File Only with Extention
        self._extension = os.path.splitext(self._filename)[1] # Only Extention
    
    ## File Values ##
    def get_file_metadata(self, metadata=DEFAULT_METADATA):
        ## Windows Metadata ##
        if win32com and platform.system() == "Windows":
            try:
                sh = win32com.client.gencache.EnsureDispatch('Shell.Application', 0)
                ns = sh.NameSpace(self._dirname)
                item = ns.ParseName(str(self._filename))

                file_metadata = dict()
                for ind, attribute in enumerate(metadata):
                    attr_value = ns.GetDetailsOf(item, ind)
                    if attr_value:
                        file_metadata[attribute] = attr_value

                return file_metadata    
            except Exception as e:
                print(f"Error using Windows Shell API: {e}")
        else:
            ## Fallback: Cross-platform basic metadata ##
            try:
                stats = self.path.stat()
                return {
                    "name": self.path.name,
                    "path": str(self.path.resolve()),
                    "size_bytes": stats.st_size,
                    "created": datetime.datetime.fromtimestamp(stats.st_ctime),
                    "modified": datetime.datetime.fromtimestamp(stats.st_mtime),
                    "accessed": datetime.datetime.fromtimestamp(stats.st_atime),
                    "is_file": self.path.is_file(),
                    "is_dir": self.path.is_dir(),
                    "permissions": stat.filemode(stats.st_mode),
                    "extension": self.path.suffix,
                }
                
            except Exception as e:
                print(f"Failed to get file metadata: {e}")
                return None

    def get_file_size(self):
        return os.path.getsize(self._path)

    def get_file_hash(self, algorithm='sha256'):
        """Compute the hash of a file using the specified algorithm."""
        hash_func = hashlib.new(algorithm)

        try:
            with open(self._path, 'rb') as file:
                while chunk := file.read(8192):
                    hash_func.update(chunk)
                file.close()
        except Exception as e:
            print(e)
        
        return hash_func.hexdigest()
    
    ## File Functions ##
    def zip(self, compress=zipfile.ZIP_DEFLATED):
        with zipfile.ZipFile(self._filename + '.zip', 'w', compress) as target:
            with open(self._path) as f:
                target.write(f)
    
    def rename(self, name):
        os.rename(self._path, os.path.join(self._dirname, name + self._extension))
    
    def move(self, destPath):
        os.rename(self._path, destPath)
    
    def delete(self):
        os.remove(self._path)    

    ## File Property's ##
    @property
    def extention(self):
        return self._extension
    
    @property
    def filename(self):
        return self._filename

    @property
    def path(self):
        return self._path

    @property
    def parent(self):
        return self._dirname
    
    ## Content Related ##
    def write_content(self, content):
        """Override the content of the file"""
        with open(self._path, encoding="utf-8") as file:
            try:
                file.write(content)
                file.close()
            except Exception as e:
                print(e)
    
    def get_content(self):
        """Read the file and get its content."""
        with open(self._path, encoding="utf-8") as file:
            try:
                content = file.read()
                file.close()
                return content
            except Exception as e:
                print(e)
                return None