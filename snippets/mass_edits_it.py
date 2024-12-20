from snippets.mass_edits import mass_translate

REPLACE_MAP = {
    "Continue...": "Continua...",
    "Do nothing.": "Non fare niente.",
    "Do something onboard the ship.": "Fai qualcosa a bordo.",
    "...": "...",
    "Nevermind.": "Lascia perdere.",
    "An unvisited location.": "Posizione non visitata.",
    "Explored location. Nothing left of interest.": "Posizione visitata. Non c'è più niente d'interessante.",
    "YOU SHOULD NEVER SEE THIS": "NON DOVRESTI MAI VEDERE QUESTO MESSAGGIO",
    "Use your blessing to avoid combat.": "Usa la tua benedizione per evitare il combattimento.",
    "Decline.": "Rifiuta.",
    "Yes.": "Sì.",
    "Refuse.": "Rifiuta.",
    "No.": "No.",
    "You start calibrating the drone...": "Inizi a calibrare il drone...",
    "You finish calibrating the drone successfully.": "Finisci di calibrare il drone.",
    "Return to the toggle menu.": "Torna al menù impostazioni.",
    "Renegade Cruiser": "Incrociatore rinnegato",
    "Leave.": "Vattene.",
    "Detach both modules.": "Sgancia entrambi i moduli.",
    "Exit hyperspeed.": "Esci dall'ipervelocità.",
    "You install the upgrade.": "Installi il miglioramento.",
    "You start the process.": "Inizi il processo.",
    "You finish the process.": "Termini il processo.",
    "Your crew cannot be cloned on your ship as they are inside the cannon.": "Non puoi clonare il membro dell'equipaggio sulla tua nave perché è dentro al cannone.",
    "You install the modification.": "Installi la modifica.",
    "Are you sure? You will not be able to retrieve them without a Clone Bay, and all skills will be lost.": "Sicuro? Non potrai recuperarli senza una Vasca di Clonazione e tutte le abilità andranno perse.",
    "Reset the cannon.": "Resetta il cannone.",
    "You reset the weapon.": "Resetti l'arma.",
    "You finish resetting the weapon.": "Finisci di resettare l'arma.",
    "Your Morph transforms into a new shape.": "Il tuo Mutaforma assume un nuovo aspetto.",
    "Projectile": "Proiettile",
    "(Clone Bay) Revive your crew.": "(Sala clonazione) Resuscita il tuo equipaggio.",
    "Though your crew's memories have been almost completely erased, they remember enough to at least remain loyal to the Federation.": "Anche se i ricordi del membro dell'equipaggio sono stati cancellati quasi del tutto, almeno ricorda abbastanza da restare fedele alla Federazione.",
    "Ignore them.": "Ignorali.",
    "Are you sure you want to change the drone's settings?": "Vuoi cambiare le impostazioni del drone?",
    "Reroute.": "Ridireziona.",
    "Accept their surrender.": "Accetta la resa.",
    "Nevermind, do something else.": "Lascia stare, fai qualcos'altro.",
    "Continue to the fight!": "Continua a combattere!",
    "???": "???",
    "Sylvan": "Sylvan",
    "YOU SHOULD NEVER SEE THIS.": "NON DOVRESTI MAI VEDERE QUESTO MESSAGGIO.",
    "No weapon has ever sparked a larger ethical controversy, but if it works it works.": "Nessun'arma ha mai generato polemiche etiche così grandi, ma se funziona, funziona.",
    "Accept.": "Accetta.",
    "No thanks.": "No grazie.",
    "Contact Federation command.": "Contatta il comando della Federazione.",
    "Multiverse Renegade": "Rinnegato multiversale",
    "Attack!": "All'attacco!",
    ".": ".",
    "Continue with the jump.": "Continua con l'ipersalto.",
    "You prepare to jump to the new co-ordinates, and change your flight path accordingly.": "Ti prepari all'ipersalto verso le nuove coordinate e cambi rotta.",
    "You prepare to secure their cargo by force.": "Ti prepari a prendere il carico con la forza.",
    "Agree.": "Accetta.",
    "Hail them.": "Contattali.",
    "Avoid the ship.": "Evita la nave.",
    "Your Morph transforms back to its original shape.": "Il tuo Mutaforma torna ad assumere le sue vere sembianze.",
    "Go back.": "Torna indietro.",
    "ESSENTIAL SYSTEMS": "SISTEMI ESSENZIALI",
    "AUXILIARY SYSTEMS": "SISTEMI AUSILIARI",
    "(Cloaking) Cloak and try to escape.": "(Occultamento) Occultati e prova a fuggire.",
    "(Adv. Engines) Try to escape the guard.": "(Motori avanzati) Prova a seminare la guardia.",
    "Character Recruited": "Personaggio reclutato",
    "Explore.": "Esplora.",
    "(Adv. Piloting) Activate the auto-pilot to try and escape.": "(Pilotaggio avanzato)",
    "Detach the modules.": "Sgancia i moduli.",
    "DECKHANDS": "EQUIPAGGIO",
    "Before you shop, you still have some time to do something else aboard the ship.": "Prima di fare acquisti, hai ancora del tempo per fare qualcosa a bordo della tua nave.",
    "Success!": "Successo!",
    "Loot Acquired": "Bottino ottenuto",
    "Modular Laser": "Laser modulare",
    "Mod. Laser": "Laser mod.",
    "Modular Ion": "Ione modulare",
    "Mod. Ion": "Ione mod.",
    "They stay outside your weapons range, and eventually jump away.": "Si tengono fuori dalla portata delle tue armi e alla fine eseguono l'ipersalto.",
    "DRONE": "DRONE",
    "*%$##@*%!": "*%$##@*%!",
    "Servant": "Servitore",
    "Demand the surrender of their goods.": "Ordina che consegnino la loro merce.",
    "WEAPONS OF THE DAY [33% OFF]": "ARMI DEL GIORNO [SALDI 33%]",
    "They look like they don't want to fight. They are trying to escape.": "Non sembra che siano intenzionati a combattere. Stanno cercando di fuggire.",
    "AUGMENTS OF THE DAY [33% OFF]": "ACCESSORI DEL GIORNO [SALDI 33%]",
    "Chaotic Renegade Cruiser": "Incrociatore Rinnegato Caotico",
    "Special loot weapon. See tooltip in the inventory to check the improvements over the base version.": "Arma speciale. Vedi la descrizione in inventario per controllare i miglioramenti rispetto alla versione base.",
    "Your new crew materializes in the room.": "Il tuo nuovo membro dell'equipaggio si materializza nella stanza.",
    "You power up the machine to max and watch as a rift opens, shaking the ship until suddenly it powers off, and a flashing green light followed by a string of coordinates signifies that it has worked.": "Alimenti al massimo il macchinario e guardi mentre si apre uno squarcio che fa tremare la nave, fino a quanto non si disattiva all'improvviso. Una luce verde seguita da una serie di coordinate indica che ha funzionato.",
    "Do something else instead.": "Fai qualcos'altro.",
    "Renegade Defeated": "Rinnegato sconfitto",
    "Boon Received": "Dono ricevuto",
    "Attack the guard.": "Attacca la guardia.",
    "Return.": "Torna indietro.",
    "DRONES OF THE DAY [33% OFF]": "DRONI DEL GIORNO [SALDI 33%]",
    "Modular Missile": "Missile modulare",
    "Mod. Missile": "Missile mod.",
    "We can't help.": "Non possiamo aiutare.",
    "Install the External Augment internally.": "Converti l'Accessorio esterno in uno interno.",
    "You activate the combat augment.": "Attivi l'accessorio da combattimento.",
    "The crew is dead, leaving you with the ship. Its cargo is yours for the taking. Aboard is the special tech you expected, which you bring back to your ship.": "L'equipaggio è morto, lasciandosi dietro la nave. La sua stiva è tua. A bordo c'è la tecnologia che ti aspettavi, e la riporti sulla tua nave.",
    "Ignore the station.": "Ignora la stazione.",
    "(Jerry) \"Hello!\"": "(Jerry) \"Ciao!\"",
    "Listen.": "Ascolta.",
    "Accept their offer.": "Accetta l'offerta.",
    "Ignore the ship.": "Ignora la nave.",
    "Attack them.": "Attacca.",
    "Close your eyes and relax...": "Chiudi gli occhi e rilassati...",
    "Install the Firestarter Module.": "Installa il modulo Innesco.",
    "Install the Hullbuster Module.": "Installa il modulo Tagliascafo.",
    "Install the Power Module.": "Istalla il modulo Potenza.",
    "Get to Sector 5 with the Type A to unlock this ship.": "Raggiungi il Settore 5 col tipo A per sbloccare questa nave.",
    "(Adv. Engines) Try to escape the Elite.": "(Motori avanzati) Prova a seminare l'élite.",
    "Obyn": "Obyn",
    "You decide not to do anything and prepare to fight.": "Decidi di non fare niente e ti prepari a combattere.",
    "Get to Sector 5 with the Type B or beat the game with the Type A to unlock this ship.": "Raggiungi il Settore 5 col tipo B o finisci il gioco col tipo A per sbloccare questa nave.",
    "Modular Beam": "Raggio modulare",
    "Mod. Beam": "Raggio mod.",
    "Leave them be.": "Lasciali stare.",
    "Attack them!": "All'attacco!",
    "(Mind Control) Convince the guard to leave you alone.": "(Controllo mentale) Convinci la guardia a lasciarti in pace.",
    "Nevermind, let's fight!": "Non importa, combattiamo!",
    "Approach.": "Avvicinati.",
    "Accept the job.": "Accetta l'incarico.",
    "The alarms buzz and an extra layer of security slams shut on the vault door. You quickly flee but the Zoltan reinforcements arrive just in time to fire a barrage of missiles straight through your defences before you can escape.": "Scatta l'allarme e un ulteriore livello di sicurezza chiude la porta del caveau. Fuggi in tutta fretta, ma i rinforzi Zoltan arrivano appena in tempo per scaricare uno sbarramento di missili oltre le tue difese prima che riesca a darti alla fuga.",
    "L-9678": "L-9678",
    "Contact the civilian ship.": "Contatta la nave civile.",
    "Install the Anti-Bio Module.": "Installa il modulo Necrogeno.",
    "Install the Cooldown Module.": "Installa il modulo Ricarica.",
    "Install the Neural Module.": "Installa il modulo Neurale.",
    "Prepare to fight!": "Preparati a combattere!",
    "Attack the outpost!": "Attacca l'avamposto!",
    "(Magnet Arm) Salvage the wreck further.": "(Braccio magnetico) Recupera altro materiale dal relitto.",
    "You now have some time to do something on the ship.": "Hai del tempo per fare qualcosa a bordo.",
    "\"Another day, another profit for both of ussss, eh ssstranger?\"": "\"Un altro giorno, un altro guadagno per entrambi, eh sssstraniero?\"",
    "You cannot install this lab modification, as you still have the external version.": "Non puoi installare questa modifica del laboratorio perché hai ancora la versione esterna.",
    "Artillery": "Artiglieria",
    "Anointed": "Eletto",
    "You prepare for combat.": "Ti prepari a combattere.",
    "Ignore the guard.": "Ignora la guardia.",
    "That's enough for now.": "Così basta per adesso.",
    "Install the Accuracy Module.": "Installa il modulo Precisione.",
    "Currently Installed: None": "Attualmente installati: Niente",
    "PHEROMONE": "FERORMONE",
    "Grant Received": "Dono ricevuto",
    "Blessing Received": "Benedizione ricevuta",
    "Pirate Fighter": "Caccia pirata",
    "Task Marker": "Icona incarico",
    "Obsidian Armor": "Corazza d'ossidiana",
    "Leave them alone.": "Lasciali in pace.",
    "Attack the ship.": "Attacca la nave.",
    "Dock.": "Attracca.",
    "\"Task accepted. Transferring coordinates to next sector. Do not disappoint me.\"": "\"Incarico accettato. Trasferimento coordinate per il prossimo settore. Non deludermi.\"",
    "From out of the tunnel comes a massive cruiser vessel, of unknown alien design! At once, a strange pattern appears on your computer... its frequency matches the signal from that beacon you had activated earlier!": "Dal tunnel esce un incrociatore colossale dall'aspetto sconosciuto e alieno! Allo stesso tempo, appare uno strano schema sul tuo computer... la frequenza combacia col segnale dell'astrofaro che hai attivato prima!",
    "You arm the weapons and engage the station!": "Prepari le armi e affronti la stazione!",
    "You activate the payload and launch it from the vessel.": "Attivi gli esplosivi e li lanci dalla nave.",
    "Set the drone to Boarding Mode.": "Imposta il drone in Modalità Abbordaggio.",
    "Pirate Scout": "Scout pirata",
    "Traveling Merchant": "Mercante itinerante",
    "Multiverse Flagship": "Ammiraglia multiversale",
    "Pay.": "Paga.",
    "You give the weapon to the engineer, allowing him to work on it.": "Dai l'arma all'ingegnere, permettendogli così di lavorarci sopra.",
    "After a short time, your weapon is returned to you, clad with an optimization.": "Poco dopo, l'arma ti viene restituita, completa di ottimizzazione.",
    "Contact the guard.": "Contatta la guardia.",
    "Install the Lockdown Module.": "Installa il modulo Isolamento.",
    "You must have the lab upgrade for this modification.": "Devi avere il laboratorio migliorato per questa modifica.",
    "You begin the upgrade...": "Inizi l'upgrade...",
    "Power rerouted to surge control. Proceeding to combat.": "Potere reindirizzato al controllo picchi di potenza. Inizio combattimento.",
    "Your Power Surge will occur after this countdown.": "Il tuo Picco di Potenza avverrà dopo questo conto alla rovescia.",
    "BOMB": "BOMBA",
    "Pirate Outrider": "Outrider pirata",
    "Investigate.": "Indaga.",
    "Request supplies.": "Richiedi scorte.",
    "Contact the refugee ship.": "Contatta la nave dei rifugiati.",
    "See what they're selling.": "Controlla cosa c'è in vendita.",
    "Install the Pierce Module.": "Installa il modulo Penetrazione.",
    "What upgrade do you want to install?": "Quale miglioramento vuoi installare?",
    "Your Malform transforms back to its original shape.": "Il tuo Malformato torna ad assumere il suo vero aspetto.",
    "Attack, we can steal their Mine Launcher tech!": "All'attacco, possiamo rubargli la tecnologia del Lanciamine!",
    "You've taken the risky choice of fighting the ship. Hopefully, you can protect yourself from their salvo long enough.": "Hai scelto di correre il rischio di affrontare la nave. Spera di riuscire a difenderti dai suoi attacchi abbastanza a lungo.",
    "Avoid the Trapper.": "Evita il disturbatore.",
    "Messing with a Trapper is a bad idea.": "Punzecchiare un disturbatore è una pessima idea.",
    "Human": "Umano",
    "Thing": "Essere",
    "Contact the Engi.": "Contatta gli engi.",
    "Sure.": "Certo.",
    "The ship breaks apart and you quickly salvage what you can.": "La nave va in pezzi e recuperi rapidamente quello che puoi.",
    "Salvage the ruins.": "Saccheggia le rovine.",
    "You rig the ammunition and set a trap for the Rebels. It's definitely illegal to do, but you'll be gone before it matters.": "Saboti le munizioni e tendi una trappola ai ribelli. È sicuramente illegale, ma non sarai più qui quando ci sarà da renderne conto.",
    "Pirate Transport": "Mercantile pirata",
    "Mascot": "Mascotte",
    "Merchant": "Mercante",
    "Awesome Laser": "Laser fighissimo",
    "Respond.": "Rispondi.",
    "Attack the station!": "Attacca la stazione!",
    "Surrender is not an option.": "La resa non è contemplata.",
    "\"A good choice. May it serve you well in your travels!\"": "\"Ottima scelta. Che ti sia utile nei tuoi viaggi!\"",
    "Jerry": "Jerry",
    "We have to go.": "Dobbiamo andare.",
    "I should go.": "Devo andare.",
    "Charlie": "Charlie",
    "The haunted vessel has been eliminated. Another to check off the list this time. That is, assuming they don't pop up again from across the Multiverse looking for revenge.": "La nave infestata è stata eliminata. Un'altra da depennare stavolta. Sempre che non rispuntino fuori dal multiverso in cerca di vendetta.",
    "You mute the ship and prepare for combat.": "Zittisci la nave e ti prepari a combattere.",
    "You await your reward, but the machine buzzes and an X flashes on the screen. Better luck next time...": "Aspetti la ricompensa, ma l'apparecchio fa un suono di errore e una X appare sullo schermo. Andrà meglio la prossima volta...",
    "Gamble again.": "Scommetti ancora.",
    "System disabled successfully.": "Sistema disattivato.",
    "Pirate Bomber": "Bombardiere pirata",
    "Tiiikaka Transport": "Mercantile Tiikaka",
    "Max Health is increased to 110": "Salute massima aumentata a 110",
    "Ignore the planet.": "Ignora il pianeta.",
    "Finish them off.": "Finiscili.",
    "Scrap the ship.": "Saccheggia la nave.",
    "Continue.": "Continua.",
    "We aren't interested.": "Non ci interessa.",
    "Okay.": "Ok.",
    "It seems your track record has caught up to you. The guard's crew have heard enough of the crimes you've been committing, and they don't intend to let you into the sector!": "Il tuo passato torna a galla. L'equipaggio della guardia sa dei crimini che hai commesso, e non ha intenzione di farti accedere al settore!",
    "You rush to defensive positions as the guard approaches menacingly.": "Corri alle postazioni di difesa mentre la guardia si avvicina minacciosa.",
    "Here we go again.": "Si riparte.",
    "(Powerful Beam) Show the Beam to Leah.": "(Raggio potente) Mostra il raggio a Leah.",
    "Whatever the ruins have to offer isn't worth the effort.": "Qualunque cosa ci sia in quelle rovine, non ne vale la pena.",
    "Ignore the merchant.": "Ignora il mercante.",
    "Yes": "Sì.",
    "Set the drone to Defensive Mode.": "Imposta il drone in Modalità Difensiva.",
    "Free Mantis Elder": "Anziano mantis liberi",
    "Morph": "Mutaforma",
    "Active Ability: Deploys a Breach, Lockdown, and Ion Bomb at the same time": "Abilità attiva: lancia una bomba perforante, isolante e ionica allo stesso tempo",
    "Recon Drone": "Drone ricognitore",
    "Battle Drone": "Drone bellico",
    "Ignore the ships.": "Ignora le navi.",
    "You were asked to escort an unprepared vessel to these coordinates.": "Ti è stato chiesto di scortare una nave impreparata a queste coordinate.",
    "Wait.": "Aspetta.",
    "More boarding pods are approaching!": "Si avvicinano altre capsule d'abbordaggio!",
    "What?": "Cosa?",
    "Your crew cannot be cloned, as you just sold them.": "Non puoi clonare il tuo membro dell'equipaggio, dato che l'hai solo venduto.",
    "With the crew dead you quickly salvage what you can.": "Con l'equipaggio morto, recuperi tutto quello che puoi.",
    "Contact the Monks.": "Contatta i Monaci",
    "The slave ship is destroyed. They won't continue their evil trade, but many lives were probably lost on that ship.": "La nave degli schiavisti è distrutta. Non continueranno il loro commercio malvagio, ma forse molte vite sono andate perse.",
    "Demand supplies.": "Esigi scorte.",
    "Change your mind and leave the guard alone.": "Cambia idea e lascia stare la guardia.",
    "You apologize and end comms. The guard makes no attempts to communicate further.": "Chiedi scusa e interrompi le comunicazioni. La guardia non tenta di comunicare oltre.",
    "This is the location of the Traveling Merchant.": "Questa è la posizione del Mercante itinerante.",
    "Er... sorry?": "Ehm... scusa?",
    "Buy the pen.": "Compra la penna.",
    "Rescue the store.": "Salva il negozio.",
    "Shop.": "Fai spese.",
    "Success, time for battle!": "Successo, è ora di combattere!",
    "Buy the cargo.": "Compra il carico.",
    "The transaction is done. With the looks of it, this piece of equipment might prove useful.": "La transazione è completata. A guardarlo, sembra che quest'oggetto potrà rivelarsi utile.",
    "Refuse and attack the transport.": "Rifiuta e attacca il mercantile",
    "The transport captain shrugs and continues on their way.": "Il capitano del mercantile fa spallucce e continua per la sua strada.",
    "Leah": "Leah"
}

mass_translate('locale/**/it.po', REPLACE_MAP, overwrite=True)
