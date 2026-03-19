import streamlit as st
st.title("Calcul de la (VO)")
vo=st.selectbox("Sélectionnez le type de VO (HT/TCC): ", ["Choisir...", "HT", "TCC"])
if vo.upper() == "HT":
    montant=st.number_input("enter le montant HT: ")
    st.write(f"la valeur d'origine est {montant} HT")

elif vo.upper() == "TCC":
    montant_tcc=st.number_input("enter le montant TTC: ")
    VO_HT = montant_tcc/1.2
    st.success(f"la valeur d'origine est {VO_HT:.2f} HT")

else:
    st.error(f"Sorry, {vo} n'est pas un type de VO valable")


    