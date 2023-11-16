from bs4 import BeautifulSoup
from owlready2 import *
from tqdm import tqdm
from unidecode import unidecode

# Criação/Carregamento da ontologia
onto = get_ontology("file://cbo.owl").load()
    
def createPanel(page_instance, pageN, panelN, characters=[]):
    panel_instance = Panel("Batman_Page_{:02d}_Panel_{:02d}".format(pageN, panelN))
    page_instance.hasPanel.append(panel_instance) 
    for character in characters:
        panel_instance.hasCharacter.append(character)
    return panel_instance

def createBalloon(panel_instance, pageN, panelN, balloonN, character, text):
    balloon_instance = Balloon("Batman_Page_{:02d}_Panel_{:02d}_Balloon_{:02d}".format(pageN, panelN, balloonN))
    balloon_instance.hasText = text
    if character != None:
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
    issue_instance = Issue("Batman_Renascimento_001_Panini")

    # Stories
    story_1 = Story("Eu_Sou_Gotham_Parte_1")
    issue_instance.story.append(story_1)
    story_1.right2left = True

    story_2 = Story("Eu_Sou_Gotham_Parte_2")
    issue_instance.story.append(story_2)
    story_2.right2left = True

    # Characters
    batman = Character("Batman")
    gordon = Character("Gordon")
    duke = Character("Duke")
    man_1 = Character("man_1")
    alfred = Character("Alfred")
    hugoStrange = Character("Hugo_Strange")
    gotham = Character("Gotham")
    gothamGirl = Character("Gotham_Girl")
    solomonGrundy = Character("Solomon_Grundy")
    bobCastro = Character("Bob_Castro")
    woman_1 = Character("woman_1")
    pirataPsiquico = Character("Pirata_Psiquico")
    general = Character("general")
    amandaWaller = Character("Amanda_Waller")

    # Topics
    superHeroi = Topic("Super_Heroi")
    conspiracao = Topic("Conspiracao")

    # Create instances in a loop
    for i in range(1, 50 + 1):
        page_instance = Page("Batman_Page_{:02d}".format(i))
        page_instance.pageNumber = i  
        issue_instance.hasPage.append(page_instance)

        if (i >= 5 and i <= 24):
            story_1.hasPage.append(page_instance)
        elif (i >= 27 and i <= 48):
            story_2.hasPage.append(page_instance)
        else:
            continue

        if (i == 5):
            panel = createPanel(page_instance, i, 1, [])
            text = "Senhoras e senhores, estamos iniciando nossa aterrissagem em Gotham."
            createBalloon(panel, i, 1, 1, None, text)

            panel = createPanel(page_instance, i, 2, [])
            text = "Por favor, certifique-se de que seu cinto de segurança está bem afivelado, o encosto de sua poltrona na posição vertical e sua mesa fechada e travada."
            createBalloon(panel, i, 2, 1, None, text)
            
            panel = createPanel(page_instance, i, 3, [])
            text = "Suas bagagens de mão devem permanecer guardadas abaixo da sua poltrona à sua frente ou no compartimento acima de sua cabeça."
            createBalloon(panel, i, 3, 1, None, text)
            text = "Obrigado."
            createBalloon(panel, i, 3, 2, None, text)
        elif (i == 6):
            panel = createPanel(page_instance, i, 1, [])
            text = "Recebi o memo ainda a pouco, o pessoal de uniforme não gosta de compartilhar nada."
            createBalloon(panel, i, 1, 1, None, text)

            panel = createPanel(page_instance, i, 2, [batman, gordon])
            text = "O ataque ao forte Marshall."
            createBalloon(panel, i, 2, 1, batman, text)
            text = "Não, o ataque insanamente confidencial ao forte Marshall, do qual ninguém nesta maldita terra sabe a respeito, exceto o secretário de defesa e eu."
            balloon = createBalloon(panel, i, 2, 2, gordon, text)
            balloon.addressesTopic.append(conspiracao)

            panel = createPanel(page_instance, i, 3, [gordon])
            text = "E você."
            balloon = createBalloon(panel, i, 3, 1, gordon, text)
            text = "Aparentemente."
            balloon.hasNextBalloon = createBalloon(panel, i, 3, 2, gordon, text)
            text = "Aconteceu semana passada, ao que parece. Uma semana, que insano"
            balloon = createBalloon(panel, i, 3, 3, gordon, text)
            text = "Os culpados pegaram três mísseis terra-ar."
            balloon.hasNextBalloon = createBalloon(panel, i, 3, 4, gordon, text)

            panel = createPanel(page_instance, i, 4, [batman])
            text = "Meus rapazes tropeçaram há uma hora em dois deles, em um ataque a uma célula do Kobra."
            createBalloon(panel, i, 4, 1, gordon, text)

            panel = createPanel(page_instance, i, 5, [gordon])
            text = "Eles perseguiram um indivíduo que fugiu com o terceiro..."
            createBalloon(panel, i, 5, 1, gordon, text)
            text = "...mas o perderam em algum lugar do Narrows."
            balloon = createBalloon(panel, i, 5, 2, gordon, text)
            text = "O que deixa um homem desesperado com uma grande e velha arma em algum lugar na minha cidade."
            balloon.hasNextBalloon = createBalloon(panel, i, 5, 3, gordon, text)

            panel = createPanel(page_instance, i, 6, [])
            text = "Sabe, amigo, eu adoro essa coisa toda que temos no telhado."
            balloon = createBalloon(panel, i, 6, 1, gordon, text)
            text = "Mas em momentos como esse, eu queria que você apenas me passasse a droga do seu número de telefone."
            balloon.hasNextBalloon = createBalloon(panel, i, 6, 2, gordon, text)
        elif (i == 7):
            panel = createPanel(page_instance, i, 1, [])
            text = "KAKOOM"
            createBalloon(panel, i, 1, 1, None, text)

            panel = createPanel(page_instance, i, 2, [gordon])
            text = "Santo--"
            createBalloon(panel, i, 2, 1, gordon, text)

            panel = createPanel(page_instance, i, 3, [gordon])
            text = "Precisamos arranjar--"
            createBalloon(panel, i, 3, 1, gordon, text)

            panel = createPanel(page_instance, i, 4, [gordon])
            text = "Certo"
            balloon = createBalloon(panel, i, 4, 1, gordon, text)
            text = "Certo"
            balloon.hasNextBalloon = createBalloon(panel, i, 4, 2, gordon, text)
        elif (i == 8):
            panel = createPanel(page_instance, i, 1, [batman])
            text = "Alfred."
            balloon = createBalloon(panel, i, 1, 1, batman, text)
            balloon.mentionsCharacter.append(alfred)
            text = "Estou monitorando as comunicações dos pilotos agora, patrão Bruce, o avião teve dano crítico no estabilizador vertical e leme traseiro."
            createBalloon(panel, i, 1, 2, alfred, text)
            text = "O que é pior: parece que eles perderam o control do sistema hidráulico central."
            createBalloon(panel, i, 1, 3, alfred, text)
            text = "Eles estipulam que cairão próximo da base do Kane Plaza, na praça Gotham, em aproximadamente seis minutos."
            createBalloon(panel, i, 1, 4, alfred, text)
            text = "É uma noite de sábado, a praça está lotada."
            createBalloon(panel, i, 1, 5, alfred, text)
            text = "Receio que a perda de vidas será... Excepcional."
    
onto.save(file="cbo.owl", format="rdfxml")