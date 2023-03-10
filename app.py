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
            options=["Explore","ChemPlay", "Suggestion"],  
            icons=["badge-3d-fill", "joystick","reply-all-fill"],  
            menu_icon="cast",  
            default_index=0,  
            orientation="horizontal",
        )
size=20
def side():
    
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


if (selected=="Explore"):
    side()
    st.markdown(page, unsafe_allow_html=True)
    st.markdown("<h1 style='text-align: center; '>ExPro - Explore Protein 3D 👨‍🔬</h1>", unsafe_allow_html=True)
    st.markdown("---")


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
    side()
    st.markdown("<h1 style='text-align: center; '>ChemPlay - Let's Play Quiz 🎮</h1>", unsafe_allow_html=True)
    st.markdown("---")
    if 'num' not in st.session_state:
        st.session_state.num = 0


    choices1 = ['Hydrogen', 'Carbon', 'Oxygen', 'Amino']
    choices2 = ['Shape', 'Taste', 'Reactivity','None of these']
    choices3 = ['Defend Body from harmful microorganisms', 'Hair', 'Muscle','None of these']
    choices4 = ['True','False']

    q1 = [('What is the central atom in an Amino Acid?', choices1),
        ('What determines a Proteins function?', choices2)]
    q2 = [('hich of these is NOT a function of Protein?', choices3),
        ('Athletes need much more protein than other people?', choices4)]


    def quiz():
        for _, _ in zip(q1, q2): 
            placeholder = st.empty()
            num = st.session_state.num
            with placeholder.form(key=str(num)):
                st.radio(q1[num][0], key=num+1, options=q1[num][1])
                st.radio(q2[num][0], key=num+1, options=q2[num][1])          
                        
                if st.form_submit_button():
                    st.session_state.num += 1
                    if st.session_state.num >= 2:
                        st.session_state.num = 0
                    placeholder.empty()
                else:
                    st.stop()


    quiz()

if (selected=="Suggestion"):
    side()
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




            
    


    


    
        





