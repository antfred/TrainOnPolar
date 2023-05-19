def pace(decimal):
    """Converts meters per second to a string in the format of M:SS"""
    return f"{int(1000 / decimal // 60)}:{int(1000 / decimal % 60):02d}"


def duration(seconds):
    """Converts seconds to a string in the format of HH:MM:SS"""
    return f"{int(seconds // 3600):02d}:{int(seconds % 3600 // 60):02d}:{int(seconds % 60 + 0.5):02d}"
