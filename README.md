# KNBS-NCD-Symptoms-based-Disease
Zulfiqar Ali
Course: knowledge Based symptoms- Masters in Global Public Health
Enrollment No#  22402092
Ontology-Driven Symptom-to- NCD Disease Inference Web Tool to support symptom-based disease prediction for Non-Communicable Diseases (NCDs).# Symptom-to-Disease Ontology Web System

This project utilizes an OWL ontology to support Non-Communicable Disease (NCD) detection based on user-input symptoms. The ontology models relationships between diseases and their symptoms, enabling semantic reasoning through a web interface.

# 🔍 Features

- 🧠 Ontology-based inference engine for NCD diagnosis
- 🔗 Semantic relationships between `Disease` and `Symptom` via `hasSymptom` object property
- 📦 Reusable OWL file compatible with Protégé and OWL reasoners
- 💡 Web interface for user-friendly symptom entry and result display
- 🔁 Easily extensible with more diseases and symptoms
- 🌐 Designed for global health applications.

  #Running the app-
  -streamlit run ncd_symptoms.py
  -links
     + Local URL: http://localhost:8501
     + Network URL: http://192.168.178.48:8501
  ## 🛠️ Requirements

- Python 3.8+
- Protégé (for editing the `.owl` file)
-VS COde editor
- Web server (e.g., Flask)  for frontend/backend interaction
- OWL reasoner (e.g., HermiT, Pellet) or SPARQL endpoint (optional)

## 📦 Install Dependencies (Python Example)

If you're using a Python Flask backend with RDFLib:


-pip3 install streamlit
-pip3 install owlready2

## 🚀 How to Use

1. Open `ncd_symptoms.owl` in Protégé to review or expand the ontology.
2. Set up your backend to load and parse the OWL file using `owlready2`.
3. Create a simple form to take symptom input from the user.
4. Display results back to the user via the frontend.

## 📁 File Structure

```
project-root/
├── ncd_symptoms.owl         # OWL ontology file
├── ncd_symptoms.py          # streamlit
                              #owlready2

└── README.md
```

## 🧪 Example

If a user enters `Fatigue` and `Frequent Unrination`, the system might infer `Type 2 Diabetes, Cardiovascular diseases, Cancer` if defined in the ontology as having those symptoms.

## 📄 License

MIT License. Free to use and extend for academic or health research purposes.
