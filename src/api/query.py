import cmd
import dao
from core import *
import core.Commands as commands
import core.Filters as filters

from typing import List
from fastapi import APIRouter
import json

router = APIRouter()

@router.post("/data")
def getData(cmds: List[str]):
    ce: commands.CommandExecuter = commands.CommandExecuter()
    l: List[WorkTime] = dao.DAO.getWorkTimes()

    if len(cmds) == 0:
        ce.addCommand(commands.GroupByProject())
        ce.addCommand(commands.GroupByEmployee())
        ce.addCommand(commands.GroupByDate())
    else:
        for c in cmds:
            if (c == "project"):
                ce.addCommand(commands.GroupByProject())
            elif (c == "employee"):
                ce.addCommand(commands.GroupByEmployee())

    res: List[commands.Group] = ce.executeCommands(l)
    data: list = []
    if len(res) > 0:
        header = [k.capitalize() for k in res[0].getGroups().keys()]
        header.append("Count")
        data.append(header)
        for r in res:
            app: list = []
            app = [r.getGroups()[k] for k in r.getGroups().keys()]
            app.append(WorkTime.sumWorkTimes(r.getData()))
            data.append(app)
    return json.dumps(data)
