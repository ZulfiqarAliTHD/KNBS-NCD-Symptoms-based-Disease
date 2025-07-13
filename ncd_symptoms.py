import streamlit as st
from owlready2 import get_ontology

ONTOLOGY_PATH = "ncd_symptoms.owl"

# --- Load ontology ---
@st.cache_resource
def load_ontology():
    try:
        onto = get_ontology(f"file://{ONTOLOGY_PATH}").load()
        return onto
    except Exception as e:
        st.error(f"❌ Failed to load ontology: {e}")
        return None

# --- Extract symptoms ---
def get_symptoms(onto):
    symptoms = set()
    for cls in onto.classes():
        if cls.name.lower() == "symptom":
            for inst in cls.instances():
                symptoms.add(inst.name)
    return sorted(symptoms)

# --- Infer diseases from selected symptoms ---
def infer_diseases_from_symptoms(selected_symptoms, onto):
    results = {}
    for disease in onto.classes():
        if "disease" in disease.name.lower():
            for inst in disease.instances():
                linked_symptoms = set()
                for prop in inst.get_properties():
                    for val in prop[inst]:
                        if hasattr(val, "name") and val.name in selected_symptoms:
                            linked_symptoms.add(val.name)
                if linked_symptoms:
                    results[inst.name] = linked_symptoms
    return results

# --- Streamlit UI ---
def main():
    st.title("🩺 NCD Symptoms Based Disease diagnosis")

    onto = load_ontology()
    if not onto:
        st.stop()

    st.subheader("Step 1: Select Symptoms")
    symptoms = get_symptoms(onto)

    if not symptoms:
        st.warning("⚠️ No symptoms found in ontology.")
        st.stop()

    selected_symptoms = st.multiselect("Choose symptoms:", symptoms)

    if st.button("Find Possible Diseases"):
        if not selected_symptoms:
            st.warning("Please select at least one symptom.")
        else:
            results = infer_diseases_from_symptoms(selected_symptoms, onto)
            if results:
                st.success("🩻 Possible Diseases Associated with Selected Symptoms:")
                for disease, matched in results.items():
                    st.write(f"🔹 **{disease}** (matched: {', '.join(matched)})")
            else:
                st.info("No diseases matched the selected symptoms.")

if __name__ == "__main__":
    main()
