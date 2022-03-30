from datetime import date
from typing import List
from . import WorkTime, Project, Employee

#region interface Criteria
class Criteria:
    #region meetCriteria()
    def meetCriteria(self, workTimes: List[WorkTime]) -> List[WorkTime]:
        pass
    #endregion meetCriteria()
#endregion interface Criteria

#region class AndCriteria
class AndCriteria(Criteria):
    #region __init__()
    def __init__(
        self,
        criteria1: Criteria,
        criteria2: Criteria
    ):
        self.__criteria1: Criteria = criteria1
        self.__criteria2: Criteria = criteria2
    #endregion __init__()

    #region override meetCriteria()
    def meetCriteria(self, workTimes: List[WorkTime]) -> List[WorkTime]:
        app: List[WorkTime] = self.__criteria1.meetCriteria(workTimes)
        return self.__criteria2.meetCriteria(app)
    #endregion override meetCriteria()
#endregion class AndCriteria

#region class ProjectCriteria
class ProjectCriteria(Criteria):
    #region __init__()
    def __init__(
        self,
        project: Project
    ):
        self.__project: Project = project
    #endregion __init__()

    #region override meetCriteria()
    def meetCriteria(self, workTimes: List[WorkTime]) -> List[WorkTime]:
        app: List[WorkTime] = [w for w in workTimes if w.getProject() == self.__project]
        return app
    #endregion override meetCriteria()
#endregion class ProjectCriteria

#region class EmployeeCriteria
class EmployeeCriteria(Criteria):
    #region __init__()
    def __init__(
        self,
        employee: Employee
    ):
        self.__employee: Employee = employee
    #endregion __init__()

    #region meetCriteria()
    def meetCriteria(self, workTimes: List[WorkTime]) -> List[WorkTime]:
        app: List[WorkTime] = [w for w in workTimes if w.getEmployee() == self.__employee]
        return app
    #endregin meetCriteria()

#endregion class EmployeeCriteria

#region class DateCriteria
class DateCriteria(Criteria):
    #region __init__()
    def __init__(
        self,
        day: date
    ):
        self.__day: date = day
    #endregion __init__()

    def meetCriteria(self, workTimes: List[WorkTime]) -> List[WorkTime]:
        app: List[WorkTime] = [w for w in workTimes if w.getDay().date() == self.__day]
        return app
#endregion class DateCriteria