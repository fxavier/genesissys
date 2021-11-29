
import os
import uuid


class Utility:

    @staticmethod
    def image_file_path(instance, filename):
        ext = filename.split('.')[-1]
        filename = f'{uuid.uuid4()}.{ext}'

        return os.path.join('uploads/images/', filename)
