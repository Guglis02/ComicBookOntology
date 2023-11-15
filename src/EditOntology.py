from bs4 import BeautifulSoup
from owlready2 import *
from tqdm import tqdm
import openpyxl
from unidecode import unidecode

# Criação/Carregamento da ontologia
onto = get_ontology("file://cbo.owl").load()
    
with onto:
    # Classes

    # Assuming Page class is defined in your ontology
    class Page(onto.Thing):
        pass

    class Panel(onto.Thing):
        pass

    # Create instances in a loop
    for i in range(1, 68):  # Change the range as per your requirement
        page_instance = Page(f"TM_Page_{i}")
        page_instance.pageNumber = i  # Assuming you have a data property hasNumber in your ontology
        # Add more properties as needed]

        for j in range(1,8):
            panel_instance = Panel(f"TM_Page_{i}_Panel_{j}")
            page_instance.hasPanel = panel_instance 
    
onto.save(file="cbo.owl", format="rdfxml")