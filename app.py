import streamlit as st
from streamlit_lottie import st_lottie
import json
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter
import io
from stmol import showmol
import py3Dmol
import biotite.structure.io as bsio
import requests


page="""
<style>
[data-testid="stAppViewContainer"]{
background-image: url("");

background-size: cover;
}

[data-testid="stHeader"]{
background-color: rgba(0,0,0,0);
}

[data-testid="stToolbar"]{
right: 2rem;
background-image: url("");

background-size: cover;
}

[data-testid="stMarkdown"]{
color: rgba(255,255,255,0);
}


[data-testid="stSidebar"]{
background-image: url("https://wallpapercave.com/wp/wp2646214.jpg");

background-size: cover;
     

}

</style>
"""
size=20
st.markdown(page, unsafe_allow_html=True)
st.markdown("<h1 style='text-align: center; '>ExPro - Explore Protein 3D 👨‍🔬</h1>", unsafe_allow_html=True)
st.markdown("---")


with st.sidebar:
    
    st.image("expro.png")
    st.title("ExPro - Explore Protein 3D")
    
    st.write("ExPro aims to provide the platform were the student can learn, explore and test out by interacting related to bio informatics sequencing (Protein)🔬")

    st.header("Features:")
    st.write('''
    🧬 Platform helps to advocate proetin and the sequence in 3D.

🔬 ChemQuiz - To help student to remember the concepts and learn something new about molecules. It also helps to enhance the knowledge to learn something new.

⭐ Providing 3D way to enhance the user experience.
    ''')
    st.header("Check out this and do give a ⭐ star on github to [ExPro](https://github.com/Hrishikesh332/ExPro-Explore-Protein-3D)")

DEFAULT_SEQ = "MGSSHHHHHHSSGLVPRGSHMRGPNPTAASLEASAGPFTVRSFTVSRPSGYGAGTVYYPTNAGGTVGAIAIVPGYTARQSSIKWWGPRLASHGFVVITIDTNSTLDQPSSRSSQQMAALRQVASLNGTSSSPIYGKVDTARMGVMGWSMGGGGSLISAANNPSLKAAAPQAPWDSSTNFSSVTVPTLIFACENDSIAPVNSSALPIYDSMSRNAKQFLEINGGSHSCANSGNSNQALIGKKGVAWMKRFMDNDTRYSTFACENPNSTRVSDFRTANCSLEDPAANKARKEAELAAATAEQ"
seq = st.text_area('Enter the protein sequence to predict: ', DEFAULT_SEQ, height=275)

def render(pdb):
    pview = py3Dmol.view()
    pview.addModel(pdb,'pdb')
    pview.setStyle({'cartoon':{'color':'spectrum'}})
    pview.setBackgroundColor('white')
    pview.zoomTo()
    pview.zoom(3, 700)
    pview.spin(True)
    showmol(pview, height = 600,width=1000)


def generate(sequence=seq):
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
    }
    res = requests.post('https://api.esmatlas.com/foldSequence/v1/pdb/', headers=headers, data=sequence)
    pdb_data = res.content.decode('utf-8')
    with open('predicted.pdb', 'w') as f:
        f.write(pdb_data)
    b = bsio.load_structure('predicted.pdb', extra_fields=["b_factor"])
    b_value = round(b.b_factor.mean(), 2)
    st.markdown("<h1 style='text-align: center; '>3D Visual of Protein: 🔬 </h1>", unsafe_allow_html=True)
    st.markdown("---")
    render(pdb_data)
    st.download_button(label="Download PDB File", data=pdb_data, file_name='predicted.pdb')
    st.subheader('plDDT')
    st.caption('plDDT is a per-residue estimate of the confidence in prediction on a scale from 0-100. plDDT showcase the confidence level of model predicted score on lDDT-Ca metric. High plDDT confidence score indicates that the molecule obtained is accurate.Regions with pLDDT between 70 and 90 are expected to be modelled well. ')
    st.code(f'plDDT: {b_value}')

predict = st.button('Predict', on_click=generate)

if predict:
    st.balloons()


