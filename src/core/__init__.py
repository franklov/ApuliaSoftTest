from operator import contains
from typing import List
from datetime import datetime, date
import dateutil.parser


#region interface Serializable
class Serializable:
    #region abstract serialize()
    def serialize(self) -> dict:
        pass
    #endregion abstract serialize()

    #region abstract static deserialize()
    def deserialize(data: dict):
        pass
    #endregion abstract static deserialize()
#endregion interface Serializable

#region class Project
class Project(Serializable):

    #region __init__()
    def __init__(
        self,
        id: int,
        name: str
    ):
        self.__id: int = id
        self.__name: str = name
    #endregion __init__()

    #region getName()
    def getName(self) -> str:
        return self.__name
    #endregion getName()

    #region getId()
    def getId(self) -> int:
        return self.__id
    #endregion getId()

    #region override serialize()
    def serialize(self) -> dict:
        return {
            "id": self.__id,
            "name": self.__name
        }
    #endregion override serialize()

    #region override static deserialize()
    def deserialize(data: dict):
        return Project(
            data["id"],
            data["name"]
        )
    #endregion override static deserialize()

    #region override __eq__()
    def __eq__(self, __o: object) -> bool:
        app: Project = __o
        return self.__id == app.getId()
    #endregion override __eq__()

#endregion class Project

#region class Employee
class Employee(Serializable):
    #region __init__()
    def __init__(
        self,
        id: int,
        name: str
    ):
        self.__id: int = id
        self.__name: str = name
    #endregion __init__()

    #region getId()
    def getId(self) -> int:
        return self.__id
    #endregion getId()

    #region getName()
    def getName(self) -> str:
        return self.__name
    #endregion getName()

    #region override serialize()
    def serialize(self) -> dict:
        return {
            "id": self.__id,
            "name": self.__name
        }
    #endregion override serialize()

    #region override static deserialize()
    def deserialize(data: dict):
        return Employee(
            data["id"],
            data["name"]
        )
    #endregion override static deserialize()

    #region override __eq__()
    def __eq__(self, __o: object) -> bool:
        app: Employee = __o
        return self.__id == app.getId()
    #endregion override __eq__()

#endregion class Employee


#region class WorkTime
class WorkTime(Serializable):
    #region static sumWorkTimes()
    def sumWorkTimes(workTimes: list) -> int:
        wt: WorkTime = None
        sum: int = 0
        for wt in workTimes:
            sum += wt.getHours()
        return sum
    #endregion static sumWorkTimes()

    #region static getProjects()
    def getProjects(workTimes: list) -> List[Project]:
        wt: WorkTime = None
        res: list = []
        for wt in workTimes:
            if (wt.getProject() not in res):
                res.append(wt.getProject())
        return res
    #endregion static getProjects()

    #region static getEmployees()
    def getEmployees(workTimes: list) -> List[Employee]:
        wt: WorkTime = None
        res: list = []
        for wt in workTimes:
            if (wt.getEmployee() not in res):
                res.append(wt.getEmployee())
        return res
    #endregion static getEmployees()

    #region static getDates()
    def getDates(workTimes: list) -> List[date]:
        wt: WorkTime = None
        res: list = []
        for wt in workTimes:
            if (wt.getDay().date() not in res):
                res.append(wt.getDay().date())
        return res
    #endregion static getDates()

    #region __init__()
    def __init__(
        self,
        project: Project,
        employee: Employee,
        day: str,
        hours: int
    ):
        self.__project: Project = project
        self.__employee: Employee = employee
        self.__day: datetime = dateutil.parser.isoparse(day)
        self.__hours: int = hours
    #endregin __init__()

    #region getProject()
    def getProject(self) -> Project:
        return self.__project
    #endregion getProject()

    #region getEmployee()
    def getEmployee(self) -> Employee:
        return self.__employee
    #endregion getEmployee()

    #region getDay()
    def getDay(self) -> datetime:
        return self.__day
    #endregion getDay()

    #region getHours()
    def getHours(self) -> int:
        return self.__hours
    #endregion getHours()

    #region override serialize()
    def serialize(self) -> dict:
        return {
            "project": self.__project.serialize(),
            "employee": self.__employee.serialize(),
            "day": self.__day.strftime("%d %b %Y"),
            "hours": self.__hours
        }
    #endregion override serialize()

#endregion class WorkTime