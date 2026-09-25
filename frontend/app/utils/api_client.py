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

    async def get(self, url:str):
        return await self.client.get(
            url,
            headers=self.headers()
        )

    async def post(self, url:str, data=None):
        return await self.client.post(
            url,
            json=data,
            headers=self.headers()
        )

    async def update(self, url:str, data=None):
        return await self.client.put(
            url,
            json=data,
            headers=self.headers()
        )

    async def delete(self, url:str, data=None):
        return await self.client.delete(
            url,
            json=data,
            headers=self.headers()
        )

    async def close(self):
        await self.client.aclose()


async def main():
    client = Client()

    # Exemple d'utilisation du client pour envoyer une requête GET
    response = await client.get("/health")
    print(response.json())

    # Exemple d'utilisation du client pour envoyer une requête POST
    student_data = {
        "user_id": 1,
        "matricule": "ETUD2026001",
        "first_name": "Small",
        "last_name": "grace",
        "date_of_birth": "2004-04-03",
        "place_of_birth": "Enyelle",
        "gender": "Masculin",
        "phone_number": "057643606",
        "address": "52, NGAMABA",
        "photo_url": "string",
        "status": "eleve",
        "email": "smallhenge@gmail.com",
        "is_active": True,
        "id": 1,
        "created_at": "2026-09-22T13:03:34.570Z",
        "updated_at": "2026-09-22T13:03:34.570Z"
    }
    response = await client.post("/student", data=student_data)
    print(response.json())

    await client.close()

if __name__ == "__main__":
    asyncio.run(main())
