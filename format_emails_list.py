input_data = """
28877	obtomb@gmail.com
79	info@adigoldstein.com
8	asher@asherbitansky.com
39553	alejandro@cdirecords.com
92490	adamofficialmusic@outlook.dk
66031	yehezkel.raz@gmail.com
126905	wesleycarter86@gmail.com.sd
126877	label-pub-ops@artlist.io
127198	gt@greggterrence.com
141686	yuel@ellatv.co.uk
141017	info@luzonic.net
134365	julian@immrecords.com
144639	contact@dibsteur.com
142804	keakong1225@gmail.com
142507	alex.kumar@familyinmusic.com
142395	info@nxzsound.com 
145439	burak@coverz.com
222115	shantelbankonit@gmail.com
283693	payments@luzonic.net
283159	carlos@unitesync.com
282821	claudiopairot@puntilla.us
285597	finance@session-42.com
284397	payam.shams@tunepays.com
288647	brunkowrecordingfactory@bluewin.ch
289229	service@tdmusic.cn
290004	allenwang@sparklingrecreation.com
289337	copyright@kamirecords.co
299070	network@alkabits.com.br
297796	yen@indiehay.com
297148	mathias@highvibesdistribution.com
302247	julius.grimm@yourv.id
301300	marcodreamz@gmail.com
300410	todor@unleashlab.com
305759	sid@dropzik.com
304822	yonnyf@mentamusic.com
303709	alicia@acemusica.com
311690	support@redstar.media
310198	music.admin@soundstripe.com
309079	manager@vexdistroportal.com
313641	admin@daomusic.vn
321531	nickpacay@gmail.com
320759	levani.javakhadze@kingsmen.group
320034	support@majesticdistributions.com
323214	dw.lamusic@gmail.com
322719	info@g30music.com
322260	contact@fivesound.es
327572	info@tupartner.co
324855	info@brilliantmusic.net
324562	adam@carpentercreate.com
329158	mersel@nextfly.me
329156	info@musicbusinessartists.com
328657	audiotunemediagroup@gmail.com
330804	karan@bull18.com
330498	skmusic@aol.com
329161	accadm@strm.com.br 
332591	go@0to8.us
331942	flavaceo@gmail.com
331675	m4apublishing@gmail.com
333084	admin@bitaran.digital 
332935	christaylorbrown@icloud.com
339227	soura.bd@gmail.com
338653	omer@indieflow.me
336086	content@vibeable.io
339231	noud-roemer@wearemarqeters.com
344773	info@sharplinemusicgroup.com
341580	Philipp Börsig
339631	analytics@calientalomedia.com
345817	avish@avidz.co
345588	distros.music@gmail.com
345031	arman2musicgroup@gmail.com
347444	smaung@contentgateway.org
346841	info@apprisemusic.com
346588	info@1337battle.com
348746	dan@putumayodigital.com
348249	CEO@TLMUSICENT.COM
359638	wldyck01@163.com
350172	criativaproducoesartisticas@gmail.com
349146	cosminanton@manelementolate.com
366869	contact@oceandistribution.tech
366141	kobzx2z.perso@gmail.com
365918	rory@hitpiece.com
370633	integralsilence.pvt.ltd@gmail.com
369884	guillaume@parabelrecords.com
369718	diz.mgmt@hotmail.com
373759	starmakersdistribution@gmail.com
"""

formatted_output = "{\n"
lines = input_data.strip().split("\n")

for line in lines:
    parts = line.split("\t")
    if len(parts) == 2:
        identifier, email = parts
        formatted_output += f'    "{identifier}": "{email}",\n'

formatted_output += "}"

print(formatted_output)
