from browser import document

def podstrankadva(event):
    button = document['myButton']
    op1 = document["option1"]
    op2 = document["option2"]
    op3 = document["option3"]
    op4 = document["option4"]
    op5 = document["option5"]
    op6 = document["option6"]
    op7 = document["option7"]
    op8 = document["option8"]
    op9 = document["option9"]
    op10 = document["option10"]
    op11 = document["option11"]
    op12 = document["option12"]
    op13 = document["option13"]
    op14 = document["option14"]

    print = document["print"]
    
    if button.text == "Nauč sa":
        
        if op1.checked  and op11.checked:
            print.innerHTML = "Vietor spôsobuje prenáša prach a piesok - mení povrch (napr. púšte)." 
        if op1.checked and op9.checked:
            print.innerHTML = "Zrážky z atmosféry sú zdrojom vody vo vodných tokoch."
        if op1.checked and op13.checked:
            print.innerHTML = "Vietor prenáša peľ aj semená niektorých rastlín."
        if op1.checked and op14.checked:
            print.innerHTML = "Počasie ovplyvňuje aktivitu živočíchov. Vietor pomáha živočíchom pri lietaní a migráciách."
        if op1.checked and op10.checked:
            print.innerHTML = "Od podnebia závisí vznik a vlastnosti pôdy vrátane úrodnosti."
        if op1.checked and op12.checked:
            print.innerHTML = "Počasie ovplyvňuje aktivity človeka (poľnohospodárstvo, doprava, pohyb v prírode...) Podnebie je významný faktor pre osídlenie a využívanie územia človekom."

        if op4.checked and op8.checked:
            print.innerHTML = "Vysoké pohoria ovplyvňujú prúdenie vzduchu. Od nadmorskej výšky závisí podnebie (teplota, zrážky...)."
        if op4.checked and op9.checked:
            print.innerHTML = "Povrch a horniny v litosfére ovplyvňujú smer korýt vodných tokov. Minerály z hornín sa rozpúšťajú vo vode a ovplyvňujú chemické zloženie povrchových aj podzemných vôd."
        if op4.checked and op13.checked:
            print.innerHTML = "Od zloženia hornín závisí koľko a aké minerálne látky sú dostupné pre rastliny."
        if op4.checked and op14.checked:
            print.innerHTML = "V rôznych nadmorských výškach žijú rôzne druhy živočíchov. Na skalnatom dne žijú iné živočíchy ako na piesčitom dne."
        if op4.checked and op10.checked:
            print.innerHTML = "Z hornín litosféry vzniká pôda a to určuje jej vlastnosti, napr. pôdny druh (ľahké, stredne ťažké, ťažké pôdy)."
        if op4.checked and op12.checked:
            print.innerHTML = "Prítomnosť alebo neprítomnosť nerastných surovín rozhoduje o hospodárskom využití územia. Charakter terénu ovplyvňuje výstavbu budov, ciest..."
        
        if op2.checked and op8.checked:
            print.innerHTML = "Vodné plochy absorbujú a uvoľňujú teplo - zmierňujú teplotné extrémy podnebia. Vyparujúca sa voda zvlhčuje ovzdušie."
        if op2.checked and op11.checked:
            print.innerHTML = "Tečúca voda prenáša rôzne veľké úlomky hornín z vyšších polôh do nižších polôh (z pohorí do nížin alebo až do morí) a tak formuje vzhľad krajiny. Voda rozpúšťa vápence a vytvára v nich jaskyne."
        if op2.checked and op13.checked:
            print.innerHTML = "Rastliny potrebujú k životu kvapalnú vodu. Voda je životným prostredím vodných rastlín."
        if op2.checked and op14.checked:
            print.innerHTML = "Živočíchy potrebujú k životu kvapalnú vodu. Voda je životným prostredím vodných živočíchov. Prúdenie vody pomáha k migráciám živočíchov."
        if op2.checked and op10.checked:
            print.innerHTML = "Voda prispieva k tvorbe a vlastnostiam pôd - napr. transportom látok v pôde nahor alebo nadol mení pôdne typy."
        if op2.checked and op12.checked:
            print.innerHTML = "Človek potrebuje vodu na pitie, zavlažovanie, priemysel... Vodné plochy sú významné pre dopravu. Vodné plochy a ich pobrežia sa využívajú na rekreáciu a športové aktivity."
        
        if op6.checked and op8.checked:
            print.innerHTML = "Rastliny produkujú kyslík do atmosféry. Rastliny spotrebúvajú oxid uhličitý z atmosféry. Rastliny vyparovaním vody zvlhčujú atmosféru (menia mikroklímu)."
        if op6.checked and op11.checked:
            print.innerHTML = "Korene rastlín v puklinách skál počas rastu trhajú skaly."
        if op6.checked and op9.checked:
            print.innerHTML = "Rastliny vo a pri vodách ovplyvňujú kvalitu a čistotu vody."
        if op6.checked and op14.checked:
            print.innerHTML = "Rastliny poskytujú potravu a útočisko pre živočíchy."
        if op6.checked and op10.checked:
            print.innerHTML = "Odumierajúce časti rastlín sa rozkladajú a vzniká z nich pôdny humus."
        if op6.checked and op12.checked:
            print.innerHTML = "Rastliny poskytujú človeku kyslík. Rastliny sú základnou zložkou potravy ľudí. Ľudia používajú rastliny na kŕmenie hospodárskych zvierat. Rastliny poskytujú človeku materiály (bavlna, drevo, bioetanol, bionafta...)"
        
        if op7.checked and op8.checked:
            print.innerHTML = "Živočíchy spotrebúvajú kyslík z atmosféry. Živočíchy produkujú oxid uhličitý do atmosféry."
        if op7.checked and op11.checked:
            print.innerHTML = "Koraly, mäkkýše a iné živočíchy s vápenatými schránkami vytvárajú nové vrstvy hornín - vápencov."
        if op7.checked and op9.checked:
            print.innerHTML = "Živočíchy ovplyvňujú kolobeh látok vo vodách, najmä v mori."
        if op7.checked and op13.checked:
            print.innerHTML = "Živočíchy pomáhajú v opeľovaní rastlín a rozširovaní semien."
        if op7.checked and op10.checked:
            print.innerHTML = "Živočíchy prispievajú k rozkladu organických látok v pôde. Dážďovky prekyprujú pôdu."
        if op7.checked and op12.checked:
            print.innerHTML = "Živočíchy poskytujú človeku potravu (mäso, mlieko, vajcia, med...). Živočíchy sú zdrojom rôznych materiálov (vlna, koža, hodváb, vosk...). Živočíchy uľahčujú človeku prácu - nosenie bremien, cestovanie. Domestikované živočíchy sú spoločníkmi človeka (napr. pes, mačka...)."
        
        if op3.checked and op8.checked:
            print.innerHTML = "Charakter pôdy ovplyvňuje pohlcovanie svetla a tým teplotu vzduchu nad povrchom."
        if op3.checked and op11.checked:
            print.innerHTML = "Chemické procesy v pôde menia minerály v horninách."
        if op3.checked and op9.checked:
            print.innerHTML = "Pôda zadržiava vodu a ovplyvňuje tvorbu podzemných vôd."
        if op3.checked and op13.checked:
            print.innerHTML = "Pôda poskytuje vodu s minerálnymi látkami na rast rastlín. Pôda poskytuje oporu pre korene rastlín."
        if op3.checked and op14.checked:
            print.innerHTML = "Pôda je prostredím života pôdnych živočíchov (krt, larvy hmyzu, mravce...)."
        if op3.checked and op12.checked:
            print.innerHTML = "Pôda je základný výrobný prostriedok v poľnohospodárstve - od nej závisí výživa ľudstva."
        
        if op5.checked and op8.checked:
            print.innerHTML = "Človek spotrebúva kyslík z atmosféry. Človek produkuje oxid uhličitý do atmosféry. Človek znečisťuje atmosféru emisiami a prachom."
        if op5.checked and op11.checked:
            print.innerHTML = "Človek využíva horniny a minerály ako nerastné suroviny. Človek mení reliéf podľa svojich potrieb (zarovnanie pre výstavbu, buduje kanály, zárezy, násypy, haldy, tunely...)."
        if op5.checked and op9.checked:
            print.innerHTML = "Človek znečisťuje povrchové aj podzemné vody, moria a oceány. Človek mení kolobeh vody najmä na územiach s nedostatkom vody."
        if op5.checked and op13.checked:
            print.innerHTML = "Ľudské aktivity môžu ničiť prirodzené biotopy rastlín. Človek výrubom odstránil lesy. Človek na iných miestach vysádza a pestuje lesy."
        if op5.checked and op14.checked:
            print.innerHTML = "Ľudské aktivty menia životné prostredie a tým aj výskyt živočíchov v prírode. Človek priamo likviduje niektoré živočíšne druhy. Človek ochranou prispieva k udržaniu a rozšíreniu niektorých druhov živočíchov."
        if op5.checked and op10.checked:
            print.innerHTML = "Vhodné postupy obrábania zúrodňujú pôdu. Niektoré ľudské aktivity znečisťujú a znehodnocujú pôdu. Výstavbou ľudia zničia pôdu."
        

document['enter'].bind('click', podstrankadva)