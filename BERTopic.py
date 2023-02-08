import os
import pandas as pd 
import numpy as np
from bertopic import BERTopic
import re
import pyreadstat

os.chdir('C:\\Users\\Vahin\\Desktop')

df1 = pd.read_spss("Meloni - campioni (solo incivili).sav")

df1['text'] = df1['text'].apply(str.lower)
df1["text"][:5]

df1['text']=df1['text'].apply(str)

def remove_usernames_links(text):
    text = re.sub('@[^\s]+','', text)
    text = re.sub('http[^\s]+','', text)
    return text
df1['text'] = df1['text'].apply(remove_usernames_links)

df1['text'] = df1['text'].str.replace(r'''!()-;:'"\,<>./?$%^&*_~''', '')
df1['text'] = df1.text.str.replace('“','')
df1['text'] = df1.text.str.replace('”','')
df1['text'] = df1['text'].str.replace("#", "")
df1['text'] = df1['text'].str.replace(".", "")
df1['text'] = df1['text'].str.replace("?", " ")
df1['text'] = df1['text'].str.replace("!", " ")
df1['text'] = df1['text'].str.replace(",", " ")
df1['text'] = df1['text'].str.replace("-", " ")
df1['text'] = df1['text'].str.replace("_", " ")
df1['text'] = df1['text'].str.replace("(", " ") 
df1['text'] = df1['text'].str.replace(")", " ")
df1['text'] = df1['text'].str.replace("«", " ")
df1['text'] = df1['text'].str.replace("»", " ")
print(df1["text"][:5])

my_stopwords = ["all", "l", "purché", "purchè", "purche", "là", "propri", "proprio", "t", "co", "https", "a", "non", "ma", "un", "uno", "una", "dell'", "abbastanza","abbia","abbiamo","abbiano","abbiate","accidenti","ad","adesso","affinché","agl","agli","ahime","ahimè","ai","al","alcuna","alcuni","alcuno","all","alla","alle","allo","allora","altre","altri","altrimenti","altro","altrove","altrui","anche","ancora","anni","anno","ansa","anticipo","assai","attesa","attraverso","avanti","avemmo","avendo","avente","aver","avere","averlo","avesse","avessero","avessi","avessimo","aveste","avesti","avete","aveva","avevamo","avevano","avevate","avevi","avevo","avrai","avranno","avrebbe","avrebbero","avrei","avremmo","avremo","avreste","avresti","avrete","avrà","avrò","avuta","avute","avuti","avuto","basta","ben","bene","benissimo","brava","bravo","buono","c","caso","cento","certa","certe","certi","certo","che","chi","chicchessia","chiunque","ci","ciascuna","ciascuno","cima","cinque","cio","cioe","cioè","circa","citta","città","ciò","co","codesta","codesti","codesto","cogli","coi","col","colei","coll","coloro","colui","come","cominci","comprare","comunque","con","concernente","conclusione","consecutivi","consecutivo","consiglio","contro","cortesia","cos","cosa","cosi","così","cui","d","da","dagl","dagli","dai","dal","dall","dalla","dalle","dallo","dappertutto","davanti","degl","degli","dei","del","dell","della","delle","dello","dentro","detto","deve","devo","di","dice","dietro","dire","dirimpetto","diventa","diventare","diventato","dopo","doppio","dov","dove","dovra","dovrà","dovunque","due","dunque","durante","e","ebbe","ebbero","ebbi","ecc","ecco","ed","effettivamente","egli","ella","entrambi","eppure","era","erano","eravamo","eravate","eri","ero","esempio","esse","essendo","esser","essere","essi","ex","fa","faccia","facciamo","facciano","facciate","faccio","facemmo","facendo","facesse","facessero","facessi","facessimo","faceste","facesti","faceva","facevamo","facevano","facevate","facevi","facevo","fai","fanno","farai","faranno","fare","farebbe","farebbero","farei","faremmo","faremo","fareste","faresti","farete","farà","farò","fatto","favore","fece","fecero","feci","fin","finalmente","finche","fine","fino","forse","forza","fosse","fossero","fossi","fossimo","foste","fosti","fra","frattempo","fu","fui","fummo","fuori","furono","futuro","generale","gente","gia","giacche","giorni","giorno","giu","già","gli","gliela","gliele","glieli","glielo","gliene","grande","grazie","gruppo","ha","haha","hai","hanno","ho","i","ie","ieri","il","improvviso","in","inc","indietro","infatti","inoltre","insieme","intanto","intorno","invece","io","l","la","lasciato","lato","le","lei","li","lo","lontano","loro","lui","lungo","luogo","là","ma","macche","magari","maggior","mai","male","malgrado","malissimo","me","medesimo","mediante","meglio","meno","mentre","mesi","mezzo","mi","mia","mie","miei","mila","miliardi","milioni","minimi","mio","modo","molta","molti","moltissimo","molto","momento","mondo","ne","negl","negli","nei","nel","nell","nella","nelle","nello","nemmeno","neppure","nessun","nessuna","nessuno","niente","no","noi","nome","non","nondimeno","nonostante","nonsia","nostra","nostre","nostri","nostro","novanta","nove","nulla","nuovi","nuovo","o","od","oggi","ogni","ognuna","ognuno","oltre","oppure","ora","ore","osi","ossia","ottanta","otto","paese","parecchi","parecchie","parecchio","parte","partendo","peccato","peggio","per","perche","perchè","perché","percio","perciò","perfino","pero","persino","persone","però","piedi","pieno","piglia","piu","piuttosto","più","po","pochissimo","poco","poi","poiche","possa","possedere","posteriore","posto","potrebbe","preferibilmente","presa","press","prima","primo","principalmente","probabilmente","promesso","proprio","puo","pure","purtroppo","può","qua","qualche","qualcosa","qualcuna","qualcuno","quale","quali","qualunque","quando","quanta","quante","quanti","quanto","quantunque","quarto","quasi","quattro","quel","quella","quelle","quelli","quello","quest","questa","queste","questi","questo","qui","quindi","quinto","realmente","recente","recentemente","registrazione","relativo","riecco","rispetto","salvo","sara","sarai","saranno","sarebbe","sarebbero","sarei","saremmo","saremo","sareste","saresti","sarete","sarà","sarò","scola","scopo","scorso","se","secondo","seguente","seguito","sei","sembra","sembrare","sembrato","sembrava","sembri","sempre","senza","sette","si","sia","siamo","siano","siate","siete","sig","solito","solo","soltanto","sono","sopra","soprattutto","sotto","spesso","sta","stai","stando","stanno","starai","staranno","starebbe","starebbero","starei","staremmo","staremo","stareste","staresti","starete","starà","starò","stata","state","stati","stato","stava","stavamo","stavano","stavate","stavi","stavo","stemmo","stessa","stesse","stessero","stessi","stessimo","stesso","steste","stesti","stette","stettero","stetti","stia","stiamo","stiano","stiate","sto","su","sua","subito","successivamente","successivo","sue","sugl","sugli","sui","sul","sull","sulla","sulle","sullo","suo","suoi","tale","tali","talvolta","tanto","te","tempo","terzo","th","ti","titolo","tra","tranne","tre","trenta","triplo","troppo","trovato","tu","tua","tue","tuo","tuoi","tutta","tuttavia","tutte","tutti","tutto","uguali","ulteriore","ultimo","un","una","uno","uomo","va","vai","vale","vari","varia","varie","vario","verso","vi","vicino","visto","vita","voi","volta","volte","vostra","vostre","vostri","vostro","è"]
my_names = ["giuseppe", "conte", "giuseppi", "giuseppeconte", "calenda", "dimaio", "luigi", "carlo", "carlocalenda", "luigidimaio", "gigi", "giggino", "mario", "draghi", "mariodraghi", "monti", "mariomonti", "trump", "giorgia", "meloni", "giorgiameloni", "silvio", "berlusconi", "silvioberlusconi", "matteo", "renzi", "salvini", "matteosalvini", "matteorenzi", "enrico", "letta", "enricoletta"]

df1['text'] = df1['text'].apply(lambda x: ' '.join([word for word in x.split() if word not in (my_stopwords)]))
df1['text'] = df1['text'].apply(lambda x: ' '.join([word for word in x.split() if word not in (my_names)]))

tweets_list = df1.text.tolist()
print(tweets_list)

model = BERTopic(language="multilingual", verbose=True)
# model = BERTopic(nr_topics=20) 

topics, probabilities = model.fit_transform(tweets_list)

model.get_topic_freq()
model.get_topic(0)
# new_topics, new_probs = model.reduce_topics(docs, topics, probabilities, nr_topics=15)

df2 = pd.read_spss("Meloni - campioni (solo incivili).sav")
df2 = df2.assign(topics=topics)
df2 = df2.assign(probabilities=probabilities)
col_list = df2.columns.tolist()
col_list.insert(3, col_list.pop(col_list.index('topics')))
col_list.insert(4, col_list.pop(col_list.index('probabilities')))
df2 = df2.reindex(columns=col_list)

complete_topics = model.get_topics()
topic_word_lists = pd.DataFrame.from_dict(complete_topics, orient='columns')

pyreadstat.write_sav(df2, "Meloni - campioni con topic.sav")
topic_word_lists.to_csv("topics campioni meloni.csv")
