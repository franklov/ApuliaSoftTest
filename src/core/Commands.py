from datetime import date
from typing import Dict, List

from . import Employee, Project, WorkTime
from .Filters import DateCriteria, EmployeeCriteria, ProjectCriteria, Criteria

#region class Group
class Group:
    #region __init__()
    def __init__(
        self,
        groups: Dict[str, str] = {},
        data: List[WorkTime] = []
    ):
        self.__groups: dict = groups
        self.__data: List[WorkTime] = data
    #endregion __init__()

    #region addData()
    def addData(self, workTime: WorkTime) -> None:
        self.__data.append(workTime)
    #endregion addData()

    #region getGroups()
    def getGroups(self) -> Dict[str, str]:
        return self.__groups.copy()
    #endregion getGroups()

    #region getData()
    def getData(self) -> List[WorkTime]:
        return self.__data
    #endregion getData()

#endregion class Group

#region interface GroupCommand
class GroupCommand:
    #region execute()
    def execute(self, groups: List[Group]) -> List[Group]:
        pass
    #endregion execute()
#endregion interface GroupCommand

#region class CommandExecuter
class CommandExecuter:
    #region __init__()
    def __init__(self):
        self.__commands: List[GroupCommand] = []
    #endregino __init__()

    #region addCommand()
    def addCommand(self, command: GroupCommand) -> None:
        self.__commands.append(command)
    #endregion addCommand()

    #region executeCommands()
    def executeCommands(self, workTimes: List[WorkTime]) -> List[Group]:
        groups: List[Group] = [Group({}, workTimes)]
        for c in self.__commands:
            groups: List[Group] = c.execute(groups)
        return groups
    #endregion executeCommands()
#endregion class CommandExecuter

#region class GroupByProject
class GroupByProject(GroupCommand):
    #region execute()
    def execute(self, groups: List[Group]) -> List[Group]:
        res: List[Group] = []
        if len(groups) == 0:
            return []
        if ("project" in groups[0].getGroups()):
            return groups
        for g in groups:
            projects: List[Project] = WorkTime.getProjects(g.getData())
            for p in projects:
                d: Dict[str, str] = g.getGroups()
                d["project"] = p.getName()
                c: Criteria = ProjectCriteria(p)
                wt: List[WorkTime] = c.meetCriteria(g.getData())
                res.append(Group(d, wt))
        return res
    #endregion execute()
#endregion class GroupByProject

#region class GroupByEmployee
class GroupByEmployee(GroupCommand):
    #region execute()
    def execute(self, groups: List[Group]) -> List[Group]:
        res: List[Group] = []
        if len(groups) == 0:
            return []
        if ("employee" in groups[0].getGroups()):
            return groups
        for g in groups:
            employees: List[Employee] = WorkTime.getEmployees(g.getData())
            for e in employees:
                d: Dict[str, str] = g.getGroups()
                d["employee"] = e.getName()
                c: Criteria = EmployeeCriteria(e)
                wt: List[WorkTime] = c.meetCriteria(g.getData())
                res.append(Group(d, wt))
        return res
    #endregion execute()
#endregion class GroupByEmployee

#region class GroupByDate
class GroupByDate(GroupCommand):
    #region execute()
    def execute(self, groups: List[Group]) -> List[Group]:
        res: List[Group] = []
        if len(groups) == 0:
            return []
        if ("date" in groups[0].getGroups()):
            return groups
        for g in groups:
            dates: List[date] = WorkTime.getDates(g.getData())
            for dt in dates:
                d: Dict[str, str] = g.getGroups()
                d["date"] = dt.strftime("%d %b %Y")
                c: Criteria = DateCriteria(dt)
                wt: List[WorkTime] = c.meetCriteria(g.getData())
                res.append(Group(d, wt))
        return res
    #endregion execute()
#endregion class GroupByDate
