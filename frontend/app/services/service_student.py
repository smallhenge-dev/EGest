from frontend.app.utils.api_client import Client

class ServiceStudent:

    def __init__(self, api:Client):
        self.api = api

    async def affiche_(self):
        liste_student = await self.api.get("/students/info")
        return liste_student.json()

    async def info_(self, student:int):
        info_student = await self.api.get("/students/info/{student}")
        return info_student.json()

    async def inscription_(self, data=None):
        inscrit_student = await self.api.post("/students/inscription", data=data)
        return inscrit_student.json()

    async def modification_(self, student:int, data=None):
        modification_student = await self.api.update("/students/info/modification/{student}")
        return modification_student.json()

    async def cancel_(self, student:int):
        cancel_student = await self.api.delete("/students/info/delete.{student}")
        return cancel_student.json()