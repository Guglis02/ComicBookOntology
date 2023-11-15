from bs4 import BeautifulSoup
from owlready2 import *
from tqdm import tqdm
from unidecode import unidecode

# Criação/Carregamento da ontologia
onto = get_ontology("file://cbo.owl").load()
    
def createPanel(page_instance, pageN, panelN, characters=[]):
    panel_instance = Panel("TM_Page_{:02d}_Panel_{:02d}".format(pageN, panelN))
    page_instance.hasPanel.append(panel_instance) 
    for character in characters:
        panel_instance.hasCharacter.append(character)
    return panel_instance

def createBalloon(panel_instance, pageN, panelN, balloonN, character, text):
    balloon_instance = Balloon("TM_Page_{:02d}_Panel_{:02d}_Balloon_{:02d}".format(pageN, panelN, balloonN))
    balloon_instance.hasText = text
    character.says.append(balloon_instance)
    panel_instance.hasBalloon.append(balloon_instance)
    return balloon_instance

with onto:
    # Classes
    class Page(onto.Thing):
        pass

    class Panel(onto.Thing):
        pass

    class Balloon(onto.Thing):
        pass

    class Issue(onto.Thing):
        pass

    class Story(onto.Thing):
        pass

    class Character(onto.Thing):
        pass

    class Topic(onto.Thing):
        pass

    # Issue
    issue_instance = Issue("Turma_da_Monica_52_Panini")

    # Stories
    story_1 = Story("Ja_Chegou_O_Disco_Voador")
    issue_instance.story.append(story_1)
    story_1.right2left = True

    story_2 = Story("Placas")
    issue_instance.story.append(story_2)
    story_2.right2left = True

    story_3 = Story("Tomando_Posse")
    issue_instance.story.append(story_3)
    story_3.right2left = True

    story_4 = Story("Qual_é_o_Peixe?")
    issue_instance.story.append(story_4)
    story_4.right2left = True

    story_5 = Story("Apresenta_pra_Mim?")
    issue_instance.story.append(story_5)
    story_5.right2left = True

    story_6 = Story("Vestido_Novo")
    issue_instance.story.append(story_6)
    story_6.right2left = True

    story_7 = Story("Peixe-Rei")
    issue_instance.story.append(story_7)
    story_7.right2left = True

    story_8 = Story("Não_me_Chamem_de...")
    issue_instance.story.append(story_8)
    story_8.right2left = True

    # Characters
    monica = Character("Monica")
    cebolinha = Character("Cebolinha")
    cascao = Character("Cascao")
    magali = Character("Magali")
    xaveco = Character("Xaveco")
    xabeu = Character("Xabeu")
    magali = Character("Magali")
    nimbus = Character("Nimbus")
    marina = Character("Marina")
    piteco = Character("Piteco")
    bolota = Character("Bolota")
    andressa = Character("Andressa")
    donaCebola = Character("Dona Cebola")
    garoto1 = Character("Garoto_1")
    garoto2 = Character("Garoto_2")
    frank = Character("Frank")
    penadinho = Character("Penadinho")
    zeVampir = Character("Ze_Vampir")
    muminho = Character("Muminho")
    zeCaveirinha = Character("Ze_Caveirinha")
    pescador1 = Character("Pescador_1")
    franjinha = Character("Franjinha")

    # Topics
    discoVoador = Topic("Disco_Voador")

    # Create instances in a loop
    for i in range(1, 74 + 1):
        page_instance = Page("TM_Page_{:02d}".format(i))
        page_instance.pageNumber = i  
        issue_instance.hasPage.append(page_instance)

        if (i == 3 <= 29):
            story_1.hasPage.append(page_instance)
        elif (i == 31):
            story_2.hasPage.append(page_instance)
        elif (i >= 36 and i <= 37):
            story_3.hasPage.append(page_instance)
        elif (i >= 38 and i <= 41):
            story_4.hasPage.append(page_instance)
        elif (i >= 43 and i <= 48):
            story_5.hasPage.append(page_instance)
        elif (i >= 50 and i <= 55):
            story_6.hasPage.append(page_instance)
        elif (i >= 57 and i <= 68):
            story_7.hasPage.append(page_instance)
        elif (i >= 70 and i <= 72):
            story_8.hasPage.append(page_instance)
        else:
            continue

        mcc = [monica, cebolinha, cascao]
        if (i == 3):
            panel = createPanel(page_instance, i, 1, mcc)
            
            panel = createPanel(page_instance, i, 2, mcc)
            text = "Vocês já pelcebelam como as nuvens são engraçadas?"
            createBalloon(panel, i, 2, 1, cebolinha, text)
            
            panel = createPanel(page_instance, i, 3, mcc)
            text = "Por que?"
            balloon = createBalloon(panel, i, 3, 1, monica, text)
            text = "Elas contaram alguma piada pra você?"
            balloon.hasNextBalloon = createBalloon(panel, i, 3, 2, monica, text)
            text = "Hunf!"
            createBalloon(panel, i, 3, 3, cebolinha, text)
            text = "Engraçadas como, Cebolinha?"
            balloon = createBalloon(panel, i, 3, 4, cascao, text)
            balloon.mentionsCharacter.append(cebolinha)
        elif (i == 4):
            panel = createPanel(page_instance, i, 1, cebolinha)
            text = "Eu tô falando do folmato delas!"
            createBalloon(panel, i, 1, 1, cebolinha, text)
            text = "Olha só!"
            balloon = createBalloon(panel, i, 1, 2, cebolinha, text)
            text = "Aquela palece uma baleia!"
            balloon.hasNextBalloon = createBalloon(panel, i, 1, 3, cebolinha, text)

            panel = createPanel(page_instance, i, 2, mcc)
            text = "Aquela lembla um elefante!"
            createBalloon(panel, i, 2, 1, cebolinha, text)
            text = "E aquela outra parece um hipopótamo deitado na grama fazendo bolhas de sabão!"
            createBalloon(panel, i, 2, 2, cascao, text)

            panel = createPanel(page_instance, i, 3, mcc)
            text = "Como é que é?"
            createBalloon(panel, i, 3, 1, monica, text)
            text = "É sélio, Mônica!"
            balloon = createBalloon(panel, i, 3, 2, cebolinha, text)
            balloon.mentionsCharacter.append(monica)
            text = "Olha bem! Ali tem um telefone..."
            balloon = createBalloon(panel, i, 3, 3, cebolinha, text)
            text = "...E ali um balco à vela!"
            balloon.hasNextBalloon = createBalloon(panel, i, 3, 4, cebolinha, text)

            panel = createPanel(page_instance, i, 4, mcc)
            text = "É mesmo!"
            balloon = createBalloon(panel, i, 4, 1, monica, text)
            text = "Hê, hê!"
            balloonAux = createBalloon(panel, i, 4, 2, monica, text)
            balloon.hasNextBalloon = balloonAux
            text = "Que engraçado!"
            balloonAux.hasNextBalloon = createBalloon(panel, i, 4, 3, monica, text)
            text = "Ah! E aquela parece um disco voador!"
            balloon = createBalloon(panel, i, 4, 4, cascao, text)
            balloon.addressesTopic.append(discoVoador)
            text = "Olha só!"
            balloon.hasNextBalloon = createBalloon(panel, i, 4, 5, cascao, text)
        elif (i == 5):
            panel = createPanel(page_instance, i, 1, mcc)
            text = "Qual?"
            createBalloon(panel, i, 1, 1, monica, text)
            text = "Aquela ali, com formato circular e luzes coloridas, indo na direção contrária das outras!"
            createBalloon(panel, i, 1, 2, cascao, text)

            panel = createPanel(page_instance, i, 2, mcc)
            text = "Ah..."
            balloon = createBalloon(panel, i, 2, 1, cascao, text)
            text = "...sumiu!"
            balloon.hasNextBalloon = createBalloon(panel, i, 2, 2, cascao, text)

            panel = createPanel(page_instance, i, 3, mcc)
            text = "Glup!"
            createBalloon(panel, i, 3, 1, cebolinha, text)
            createBalloon(panel, i, 3, 2, monica, text)
            text = "Oh!"
            balloon = createBalloon(panel, i, 3, 3, cascao, text)
            text = "Ali tem uma que parece uma ovelinha!"
            balloon.hasNextBalloon = createBalloon(panel, i, 3, 4, cascao, text)

            panel = createPanel(page_instance, i, 4, mcc)
            text = "Cascão!! Aquilo não era uma nuvem!!"
            balloon = createBalloon(panel, i, 4, 1, monica, text)
            balloon.mentionsCharacter.append(cascao)
            text = "Ela um disco voador de veldade!!"
            createBalloon(panel, i, 4, 2, cebolinha, text)
            text = "Qual?!"
            balloon = createBalloon(panel, i, 4, 3, cascao, text)
            text = "A ovelha?!"
            balloon.hasNextBalloon = createBalloon(panel, i, 4, 4, cascao, text)
        elif (i == 6):
            panel = createPanel(page_instance, i, 1, mcc)
            text = "Não, cabeção! A outra!"
            createBalloon(panel, i, 1, 1, monica, text)
            text = "Você viu dileito?"
            balloon = createBalloon(panel, i, 1, 2, cebolinha, text)
            text = "Eu só vi um bolão!"
            balloon.hasNextBalloon = createBalloon(panel, i, 1, 3, cebolinha, text)
            text = "Bolão?"
            balloon = createBalloon(panel, i, 1, 4, cascao, text)
            text = "Será que não era a Mônica?"
            balloon.hasNextBalloon = createBalloon(panel, i, 1, 5, cascao, text)

            panel = createPanel(page_instance, i, 2, [])

            panel = createPanel(page_instance, i, 3, [monica, cascao])
            text = "Ele quis dizer 'borrão', seu engraçadinho!"
            createBalloon(panel, i, 3, 1, monica, text)

            panel = createPanel(page_instance, i, 4, mcc)

            panel = createPanel(page_instance, i, 5, mcc)
        # elif:
        #     for j in range(1,8):
        #         panel_instance = Panel("TM_Page_{:02d}_Panel_{:02d}".format(i, j))
        #         page_instance.hasPanel.append(panel_instance) 

        #         for k in range(1,3):
        #             balloon_instance = Balloon("TM_Page_{:02d}_Panel_{:02d}_Balloon_{:02d}".format(i, j, k))
        #             panel_instance.hasBalloon.append(balloon_instance)
    
onto.save(file="cbo.owl", format="rdfxml")