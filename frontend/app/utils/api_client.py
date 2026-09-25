import httpx
import asyncio


class Client:
    """
    Client envoie les differentes requetes a l'API FastApi afin de de CRUD les donnees 
    Utilisateurs: Administrateur, enseignant, etudiant, parent, comptable.
    """

    def __init__(self):
        self.client = httpx.AsyncClient(
            base_url="http://127.0.0.1:8000",
            timeout=10.0
        )
        self.token = None

    def set_token(self, token):
        self.token = token

    def headers(self):
        if self.token:
            return {
                "Authorization": f"Bearer {self.token}"
            }
        return {}

    async def get(self, url):
        return await self.client.get(
            url,
            headers=self.headers()
        )

    async def post(self, url, data=None):
        return await self.client.post(
            url,
            json=data,
            headers=self.headers()
        )

    async def update(self, url, data=None):
        return await self.client.put(
            url,
            json=data,
            headers=self.headers()
        )

    async def delete(self, url, data=None):
        return await self.client.delete(
            url,
            json=data,
            headers=self.headers()
        )

    async def close(self):
        await self.client.aclose()


client = Client()
