"""
Task 9: Disease Diagnosis Program
File: task9_disease_diagnosis.py

A simple symptom-based diagnostic tool for Jeshi Hospital.
Diagnoses: Typhoid, Malaria, Pneumonia, Diabetes.
"""


def diagnose(symptom1, symptom2):
    """Return a diagnosis based on two symptoms.

    Args:
        symptom1 (str): First symptom entered by the patient.
        symptom2 (str): Second symptom entered by the patient.

    Returns:
        str: Diagnosis name or an unrecognised-combination message.
    """
    # Normalise to lowercase so matching is case-insensitive
    s1 = symptom1.strip().lower()
    s2 = symptom2.strip().lower()

    # Build a set from both symptoms for order-independent matching
    symptoms = {s1, s2}

    # ── Typhoid ──────────────────────────────────────────────────────────
    if symptoms == {"fever", "headache"}:
        return "Typhoid"

    # ── Malaria ──────────────────────────────────────────────────────────
    if symptoms == {"fever", "chills"}:
        return "Malaria"

    # ── Pneumonia ────────────────────────────────────────────────────────
    if symptoms == {"cough", "difficulty breathing"}:
        return "Pneumonia"

    # ── Diabetes ─────────────────────────────────────────────────────────
    if symptoms == {"frequent urination", "excessive thirst"}:
        return "Diabetes"

    # ── Unrecognised combination ──────────────────────────────────────────
    return (
        "We are sorry to inform you, but your symptom combination is not recognised in our database. "
        "Please consult a doctor immediately,thank you for choosing Jeshi Hospital."
    )


def main():
    """Run the Jeshi Hospital Disease Diagnosis Program."""

    # ── Welcome message ───────────────────────────────────────────────────
    print("=" * 55)
    print("      WELCOME TO JESHI HOSPITAL")
    print("      Disease Diagnosis System")
    print("=" * 55)

    # ── Capture patient details ───────────────────────────────────────────
    print("\n-- Patient Registration --")
    patient_name = input("Patient Name       : ")
    gender       = input("Gender (Male/Female): ")
    age          = input("Age                : ")
    residence    = input("Place of Residence : ")

    # ── Capture symptoms ──────────────────────────────────────────────────
    print("\n-- Symptom Assessment --")
    print("Common symptoms : fever, headache, chills, cough,")
    print("  difficulty breathing, frequent urination, excessive thirst")
    symptom_1 = input("Symptom 1          : ")
    symptom_2 = input("Symptom 2          : ")

    # ── Get diagnosis ─────────────────────────────────────────────────────
    result = diagnose(symptom_1, symptom_2)

    # ── Formatted output ──────────────────────────────────────────────────
    print("\n" + "=" * 55)
    print("      DIAGNOSIS REPORT – JESHI HOSPITAL")
    print("=" * 55)
    print(f"  Patient Name    : {patient_name}")
    print(f"  Gender          : {gender}")
    print(f"  Age             : {age}")
    print(f"  Residence       : {residence}")
    print("-" * 55)
    print(f"  Symptom 1       : {symptom_1}")
    print(f"  Symptom 2       : {symptom_2}")
    print("-" * 55)
    print(f"  DIAGNOSIS       : {result}")
    print("=" * 55)
    print("  Note: This is a preliminary diagnosis only.")
    print("  Please just see a qualified physician for confirmation.")
    print("=" * 55)


if __name__ == "__main__":
    main()
