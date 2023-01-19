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
            icons=["badge-3d-fill", "joystick", "book","reply-all-fill"],  
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
        mview.zoom(1, 200)
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


    def iupac(smiles):
        rep = "iupac_name"
        url = nom.format(smiles, rep)
        response = requests.get(url)
        response.raise_for_status()
        return response.text

    col1, col2 = st.columns(2)
    with col1:
        st.write("Please do enter SMILES (Simplified Molecular-input Line Entry System) in the below Prompt 🧪")
        st.caption("Go on and put the SMILES in the prompt to learn about the compound in a fun way with a smile 😊")
        smiles=st.text_input("", 'CCO')
    
        nom= "https://cactus.nci.nih.gov/chemical/structure/{0}/{1}"
        predict = st.button('Draw')
        st.text("")
        st.text("")
        st.write("Nomenclature:")
        st.code(iupac(smiles))

    with col2:
            struct=mol(smiles)
            
            if predict:
                render(struct)

    st.markdown("---")
    st.subheader("Time to learn smiles and get into the world of Molecules 🌎")
    st.markdown("---")
    st.subheader("Rules 📄")
    st.caption("Game can't be played, without Rules:")
    st.text('')
    st.write('''
    1. Each non-hydrogen atom is specified independently by its atomic symbol enclosed in square brackets [ ].
    
    2. Square brackets may be omitted for elements in the “organic subset” (B, C, N, O, P, S, F, Cl, Br, and I) if the proper number of implicit hydrogen atoms ⚛.
    
    3. Explicitly attached hydrogens and formal charges are always specified inside brackets【 】.
    ''')
    col7, col8 = st.columns(2)
    with col7:


        st.subheader("🔹 Symbols used to represent the bonds:")
        st.text("")
        st.text("")
        st.text("")
        st.text("")
        st.write(
            '''
            Single Bond   ----->  -

            Double Bond   ----->  =

            Triple Bond   ----->  #

            Aromatic Bond -----> :

            '''
        )
    with col8:
        st.subheader("🔹 Examples")
        st.code(
            '''
SMILES       Name      Molecular

CC        Ethane          (CH3CH3)

C=C       Ethene          (CH2CH2)

C#C       Ethyne           (CHCH)

COC    Dimethyl ether     (CH3OCH3)

CC=O   Acetaldehyde       (CH3-CH=O)

C#N    Hydrogen Cyanide      (HCN)
            '''
        )
    st.markdown("---")
    st.subheader("I guess 🤔, you're ready now. To make your own smiles")

    level = st.selectbox('How much ready are you ? Choose the Diffculty Level 🎚️:',('Easy 😅', 'Intermediate 😃', 'Difficult 💪', 'Extreme Difficult🤓'))
    def score(marks):
            if marks>1:
                    st.warning(f'Congratulation 🎉, You scored {marks}/3')
            else:
                    st.warning(f'Do not worry, Go practice more!!! You scored {marks}/3')
    if (level=="Easy 😅"):
        st.subheader("Write the nomenclature of given SMILES:")
        
        col5, col6 = st.columns(2)
        with col5:
            st.text("")
            st.text("")
            st.text("")
            st.write("Q1) CC")
            st.text("")
            st.text("")
            st.text("")
            st.write("Q2) CC=C")
            st.text("")
            st.text("")
            st.text("")
            st.write("Q3) CC(=O)O")
        with col6:
            marks=0
    
            a=st.text_input("Answer Q1:")
            b=st.text_input("Answer Q2:")
            c=st.text_input("Answer Q3:")
            submit=st.button("Submit")
            
            if submit:
                st.balloons()
                if (a.lower()=="ethane"):
                    marks+=1
                    if (b.lower()=="prop-1-ene"):
                        marks+=1
                        if (c.lower()=="ethanoic acid"):
                            marks+=1
                score(marks)

    if (level=="Intermediate 😃"):
        st.subheader("Write the nomenclature of given structure:")
        
        col5, col6 = st.columns(2)
        with col5:

            st.write("Q1)")
            st.image('q3.jpg')

            st.write("Q2)")
            st.image('q1.jpg')

            st.write("Q3)")
            st.image('q2.jpg')


        with col6:
            marks=0
    
            a=st.text_input("Answer Q1:")
            st.text('')
            st.text('')
            st.text('')
            st.text('')
            st.text('')
            st.text('')
            b=st.text_input("Answer Q2:")
            st.text('')
            st.text('')
            st.text('')
            st.text('')
            st.text('')
            st.text('')
            b=st.text_input("Answer Q3:")
            submit=st.button("Submit")
            
            if submit:
                st.balloons()
                if (a=="pent-1-ene"):
                    marks+=1
                    if (b=="4-methlyhex-1-ene"):
                        marks+=1
                        if (c=="2-methylbut-2-ene"):
                            marks+=1
                score(marks)
    if (level=="Extreme Difficult🤓"):
        st.subheader("Write the nomenclature of given structure:")
        
        col5, col6 = st.columns(2)
        with col5:

            st.write("Q1)")
            st.image('q4.jpg')


        with col6:
            marks=0
    
            a=st.text_input("Answer Q1:")
            submit=st.button("Submit")
            
            if submit:
                st.balloons()
                if (a=="1-ethenyl-2-hexenylcyclopropane"):
                    marks+=1
                score(marks)

    st.markdown("---")
    st.subheader("Resources to follow up and learn more 📖")
    st.warning("Nomenclature Part 1: (Previous Year MHT-CET)")
    st.video('https://www.youtube.com/watch?v=mrHxq0jBRsw&t=1494s')
    st.warning("Nomenclature Part 2: (Previous Year MHT-CET)")
    st.video('https://www.youtube.com/watch?v=-P9JRYGSno8&t=1125s')

 
 



            
    


    


    
        





