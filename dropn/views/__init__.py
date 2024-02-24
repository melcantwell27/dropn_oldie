# Import view classes for easier access
from .dance_class_views import dance_class_detail, dance_class_list
from .student_views import student_detail, student_list
from .studio_views import studio_detail, studio_list
from .teacher_views import teacher_detail, teacher_list

# Define __all__ array to specify which symbols should be imported when using "from views import *"
__all__ = [
    'dance_class_list',
    'dance_class_detail',
    'student_list', 
    'student_detail',
    'studio_list', 
    'studio_detail',
    'teacher_list', 
    'teacher_detail',
]