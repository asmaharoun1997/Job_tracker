from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Job Tracker API fonctionne"}

@app.get("/candidatures")
def candidatures():
    return [
        {"entreprise": "Capgemini", "statut": "Envoyée"},
        {"entreprise": "OVH", "statut": "Entretien"}
    ]