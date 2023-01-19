import streamlit as st
from streamlit_lottie import st_lottie
import json
from streamlit_option_menu import option_menu
import io
from stmol import showmol
import py3Dmol
import biotite.structure.io as bsio
import requests
from streamlit_lottie import st_lottie
from stmol import showmol
from rdkit import Chem
from rdkit.Chem import AllChem

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
def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)

lottie_s=load_lottiefile("suggestion.json")

selected = option_menu(
            menu_title=None,  
            options=["Explore","ChemPlay","X-Mol", "Suggestion"],  
            icons=["badge-3d-fill", "joystick", "reply-all-fill"],  
            menu_icon="cast",  
            default_index=0,  
            orientation="horizontal",
        )
size=20

if (selected=="Explore"):
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



    sequence = "MGSSHHHHHHSQDLMVTSTYIPMSQRRSWADVKPIMQDDGPNPVVPIMYSEEYKDAMDYFRAIAAKEEKSERALELTEIIVRMNPAHYTVWQYRFSLLTSLNKSLEDELRLMNEFAVQNLKSYQVWHHRLLLLDRISPQDPVSEIEYIHGSLLPDPKNYHTWAYLHWLYSHFSTLGRISEAQWGSELDWCNEMLRVDGRNNSAWGWRWYLRVSRPGAETSSRSLQDELIYILKSIHLIPHNVSAWNYLRGFLKHFSLPLVPILPAILPYTASKLNPDIETVEAFGFPMPSDPLPEDTPLPVPLALEYLADSFIEQNRVDDAAKVFEKLSSEYDQMRAGYWEFRRRECAE"
    seq = st.text_area('Enter the protein sequence to predict: ', sequence, height=275)
    st.caption("You can also from you're own sequence and explore the molecule:")

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
        st.header('plDDT Confidence Score')
        st.caption('plDDT is a per-residue estimate of the confidence in prediction on a scale from 0-100. plDDT showcase the confidence level of model predicted score on lDDT-Ca metric. High plDDT confidence score indicates that the molecule obtained is accurate.Regions with pLDDT between 70 and 90 are expected to be modelled well. ')
        st.code(f'plDDT: {b_value}')

    predict = st.button('Predict', on_click=generate)

    st.header("Time to Explore more 🔬:")
    st.markdown("---")
    st.subheader("🟥 Example 1:")
 
  
    st.write("""Gene: 'thrL'""")
    st.write("""Product: 'thr operon leader peptide'""")
    st.write("""Protein id: 'BAO32072.1'""")
    st.write("Sequence:")
    st.code('MRNISLKTTIITTTDTTGNGAG')

    st.markdown("---")
    st.subheader("🟥 Example 2:")
    st.write("""Gene: 'thrA'""")
    st.write("""Product: 'fused aspartokinase I and homoserine'""")
    st.write("""Protein id: 'BAO32073.1'""")
    st.write("Sequence:")
    st.code('''      MRVLKFGGTSVANAERFLRVADIMESNARQGQVATVLSAPAKIT
                     NHLVAMIDKTVAGQDILPNISDAERIFADLLSGLAQALPGFEYDRLKSVVDQEFAQLK
                     QVLHGVSLLGQCPDSVNAAIICRGEKLSIAIMEGVFRAKGYPVTVINPVEKLLAQGHY
                     LESTVDIAESTLRIAAAAIPADHIVLMAGFTAGNDKGELVVLGRNGSDYSAAVLAACL
                     RADCCEIWTDVDGVYTCDPRTVPDARLLKSMSYQEAMELSYFGAKVLHPRTITPIAQF
                     QIPCLIKNTSNPQAPGTLIGKDSTDDAMPVKGITNLNNMAMINVSGPGMKGMVGMAAR
                     VFAVMSRAGISVVLITQSSSEYSISFCVPQGELLRARRALEEEFYLELKDGVLDPLDV
                     MERLAIISVVGDGMRTLRGISARFFSALARANINIVAIAQGSSERSISVVVSNESATT
                     GVRVSHQMLFNTDQVIEVFVIGVGGVGGALIEQIYRQQPWLKQKHIDLRVCGIANSRV
                     MLTNVHGIALDSWRDELAGAQEPFNLGRLIRLVKEYHLLNPVIVDCTSSQAVADQYVD
                     FLADGFHVVTPNKKANTSSMNYYQQLRAAAAGSHRKFLYDTNVGAGLPVIENLQNLLN
                     AGDELVRFSGILSGSLSFIFGKLDEGLSLSAATLQARANGYTEPDPRDDLSGMDVARK
                     LLILAREAGYKLELSDIEVESVLPPSFDASGDVDQFLARLPELDKEFARNVANAAEQG
                     KVLRYVGLIDEGRCKVRIEAVDGNDPLYKVKNGENALAFYSRYYQPLPLVLRGYGAGN
                     DVTAAGVFADLLRTLSWKLGV''')

    st.markdown("---")
    st.header("Time to Experiment and Cure World 🌎:")
    st.write("Do visit [protein database](https://www.ncbi.nlm.nih.gov/protein) provided by National Library of Medicine, Protein database contains collection of sequences from various sources like translations from annotated coding regions in GenBank, RefSeq and TPA.")
    st.write("Protein Structure helps to understand the functionality which is the major concern while deriving drugs.")
    st.caption("Building world more better Discovering Drugs 💊")

    if predict:
        st.balloons()

if (selected=="ChemPlay"):
    if 'num' not in st.session_state:
        st.session_state.num = 0


    choices1 = ['no answer', 'manila', 'tokyo', 'bangkok']
    choices2 = ['no answer', 'thailand', 'japan', 'philippines']

    qs1 = [('What is the capital of Japan', choices1),
        ('What is the capital of Philippines', choices1),
        ('What is the capital of Thailand', choices1)]
    qs2 = [('What country has the highest life expectancy?', choices2),
        ('What country has the highest population?', choices2),
        ('What country has the highest oil deposits?', choices2)]


    def main():
        for _, _ in zip(qs1, qs2): 
            placeholder = st.empty()
            num = st.session_state.num
            with placeholder.form(key=str(num)):
                st.radio(qs1[num][0], key=num+1, options=qs1[num][1])
                st.radio(qs2[num][0], key=num+1, options=qs2[num][1])          
                        
                if st.form_submit_button():
                    st.session_state.num += 1
                    if st.session_state.num >= 3:
                        st.session_state.num = 0
                    placeholder.empty()
                else:
                    st.stop()


    main()

if (selected=="Suggestion"):
    st.title("Suggestions:")
    st_lottie(
    lottie_s,
    speed=1.5,
    reverse=False,
    loop=True,
    quality="low", 
    height=250,
    width=None,
    key=None,
)
    st.write("We are here to help you out, if you have any query/issues or wanted to add on any new features which would help others too. Do raise the issue here: [ExPro Issues](https://github.com/Hrishikesh332/ExPro-Explore-Protein-3D/issues)")

if (selected=="X-Mol"):
    
    def mol(smi):
        mol = Chem.MolFromSmiles(smi)
        mol = Chem.AddHs(mol)
        AllChem.EmbedMolecule(mol)
        molecule = Chem.MolToMolBlock(mol)
        return molecule

    def render(m):
        mview = py3Dmol.view()
        mview.addModel(m,'mol')
        mview.setStyle({'stick':{}})
        mview.setBackgroundColor('white')
        mview.zoomTo()
        showmol(mview,height=400,width=500)
    st.markdown("<h1 style='text-align: center; '>X-Mol - Explore Molecular Structure </h1>", unsafe_allow_html=True)
    col3, col4 = st.columns(2)
    with col3:
        st.text("")
        st.text("")
        st.markdown("![Alt Text](https://media.tenor.com/ZZl5JnTJo9oAAAAM/polar-molecules-partial-charges.gif)")
    with col4:
        st.subheader("Are you worried about remembering the Nomenclature, SMILES and Structure of Compounds ?")
        st.write("Don't worry, Making logic clear will help you out to understand the structure in a more better way, Practicing ✍️ everyday can make you better drawing structure from SMILES")
    st.markdown("---")
    col1, col2 = st.columns(2)
    with col1:
        st.write("Please do enter SMILES (Simplified Molecular-input Line Entry System) in the below Prompt 🧪")
        st.caption("Go on and put the SMILES in the prompt to learn about the compound in a fun way with a smile 😊")
        smiles=st.text_input("", 'CCO')

    with col2:
            struct=mol(smiles)
            render(struct)
        





