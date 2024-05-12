try:
    import cv2
    CAP_ANY = cv2.CAP_ANY
except ModuleNotFoundError:
    CAP_ANY = 0


class CameraInfo:
    def __init__(self, index, name, path, vid, pid, backend):
        self.index = index
        self.name = name
        self.path = path
        self.vid = vid
        self.pid = pid
        self.backend = backend

    def __str__(self):
        if self.vid is not None and self.pid is not None:
            return f'{self.index}: {self.name} ({self.vid:04X}:{self.pid:04X})'
        return f'{self.index}: {self.name}'

    def __repr__(self):
        return str(self)

    def to_any(self):
        return CameraInfo(self.index + self.backend, self.name, self.path, self.vid, self.pid, CAP_ANY)


__all__ = ['CameraInfo']
