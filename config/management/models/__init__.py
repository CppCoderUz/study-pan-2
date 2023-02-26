''' Modellar '''

# Asosiy userlar modeli
from management.models.moderator import MainUser

# Dekanat modellari
from management.models.rectorate import LeadershipPosition, Leadership

# Fakultet modellari
from management.models.faculty import Faculty, FacultyMember, PositionEmployeeFaculty

# Kafedra modellari
from management.models.cafedra import Cafedra, CafedraEmployeePosition, CafedraMember
