from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {
        "application": "Job Tracker",
        "status": "running"
    }

@app.get("/candidatures")
def candidatures():
    return [
        {
            "entreprise": "Capgemini",
            "poste": "Technicien Support",
            "statut": "Envoyee"
        },
        {
            "entreprise": "OVHcloud",
            "poste": "Technicien Systeme",
            "statut": "Entretien"
        }
    ]