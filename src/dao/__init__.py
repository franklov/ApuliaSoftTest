import json
from core import *
from typing import List

#region class DAO
class DAO:
    #region static getWorkTimes()
    def getWorkTimes() -> List[WorkTime]:
        db: list = None
        res: list = []
        with open("dao/db.json", "r") as f:
            db = json.load(f)
        for wt in db:
            app: dict = None
            app = wt["project"]
            project = Project(app["id"], app["name"])
            app = wt["employee"]
            employee = Employee(app["id"], app["name"])
            res.append(
                WorkTime(
                    project,
                    employee,
                    wt["date"],
                    wt["hours"]
                )
            )
        return res
    #endregion static getWorkTimes()

#endregion class DAO