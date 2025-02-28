five_instruction_str = "Svara endast med bokstaven på det rätta alternativet: A,B,C,D,E."
instruction_str = "Svara endast med bokstaven på det rätta alternativet: A,B,C,D."

## The original exam instructions
full_prompts = {
    "ORD": (
        f"I delprovet ORD inleds varje uppgift med ett ord i fetstil. Under detta finns fem "
        f"svarsförslag. Välj det svarsförslag som bäst motsvarar innebörden av det fetstilta "
        f"ordet.\n"
        "Exempel:\n"
        "Fråga: koalition\n"
        "A: överlämning\n"
        "B: beslutsamhet\n"
        "C: förhandling\n"
        "D: sammanslutning\n"
        "E: överensstämmelse\n"
        "Rätt svar:D"
    ),

    "LAS": (
        f"Delprovet LÄS består av svenska texter från olika ämnesområden och av varierande längd. "
        f"Varje uppgift består av en fråga med fyra svarsförslag, varav ett är rätt. Ibland kan du "
        f"klart se att ett av svarsförslagen är rätt och att de andra är fel. Ibland verkar flera "
        f"svar mer eller mindre rimliga. Då måste du, genom att jämföra de olika svarsförslagen, "
        f"välja ut det som bäst besvarar frågan. Observera att du ska lösa uppgifterna med "
        f"ledning av den information som ges."
    ),

    "MEK": (
        f"Uppgifterna i delprovet MEK består av korta textstycken där ett eller flera ord ersatts av "
        f"en lucka markerad med _____. En uppgift kan innehålla en, två eller tre luckor. Efter varje "
        f"textstycke följer fyra svarsförslag. Välj det svarsförslag som innehållsligt och språkligt "
        f"passar bäst in i textstycket som helhet.\n"
        "Exempel:\n"
        "Den dåliga recension som hans sista skiva fick _____ av fansen, som anser att allt han gör visar "
        "prov på konstnärlig _____.\n"
        "A: accepterades – kreativitet\n"
        "B: ifrågasattes – kalamitet\n"
        "C: ignorerades – genialitet\n"
        "D: välkomnades – sublimitet\n"
        "Orden ”ignorerades – genialitet” är de ord som tillsammans passar bäst in i sammanhanget. "
        "Rätt svar:C."
    ),

    "XYZ": (
        f"Delprovet XYZ handlar om matematisk problemlösning. Varje uppgift består av en fråga som "
        f"följs av fyra svarsalternativ, varav endast ett är rätt."
    ),

    "KVA": (
        f"Delprovet KVA innehåller uppgifter med beskrivningar av två kvantiteter, I och II. "
        f"Din uppgift är att jämföra de två kvantiteterna. I vissa fall ges inledande information "
        f"som ska användas vid jämförelsen. Till varje uppgift finns fyra svarsalternativ, varav "
        f"endast ett är rätt. I KVA har alla uppgifter samma svarsalternativ.\n"
        "Exempel:\n"
        "\\( x \\) och \\( y \\) är positiva heltal.\n"
        "$xy = 42 \\quad och \\quad x^2 + y^2 = 85$\n\n"
        "Kvantitet I: \\( x \\)\n"
        "Kvantitet II: \\( y \\)\n\n"
        "Svarsalternativ:\n\n"
        "A. I är större än II\n"
        "B. II är större än I\n"
        "C. I är lika med II\n"
        "D. Informationen är otillräcklig\n\n"
        "Förklaring till svarsalternativen:\n\n"
        "A. Kvantitet I är större än kvantitet II.\n"
        "B. Kvantitet II är större än kvantitet I.\n"
        "C. De två kvantiteterna är lika stora.\n"
        "D. Förhållandet mellan de två kvantiteterna kan inte entydigt bestämmas utifrån den "
        "givna informationen.\n\n"
        "Lösning: Antingen är x = 6 och y = 7 eller så är x = 7 och y = 6. Det går alltså inte att "
        "entydigt bestämma om x eller y är störst. Rätt svar:D"
    ),

    "NOG": (
        f"Delprovet NOG består av uppgifter med en fråga följd av två påståenden, $ (1) $ och $ (2) $, "
        f"som innehåller information. Frågan kan ibland föregås av viss inledande information. Din "
        f"uppgift är att avgöra om frågan entydigt kan besvaras med hjälp av informationen i "
        f"påståendena, och i så fall hur mycket av denna information som är tillräcklig. Till varje "
        f"uppgift finns fem svarsalternativ, varav endast ett är rätt. I NOG har alla uppgifter "
        f"samma svarsalternativ.\n\n"
        "Exempel:\n\n"
        "Linn har 125 kr i tjugokronorssedlar och femkronor. **Hur många femkronor har Linn?**\n"
        "$ (1) $ Linn har färre än 5 femkronor.\n"
        "$ (2) $ Linn har fler än 4 tjugokronorssedlar.\n\n"
        "Tillräcklig information för lösningen erhålls:\n\n"
        "A. $ (1) $ men ej $ (2) $\n"
        "B. $ (2) $ men ej $ (1) $\n"
        "C. $ (1) $ tillsammans med $ (2) $\n"
        "D. $ (1) $ och $ (2) $ var för sig\n"
        "E. ej genom de båda påståendena\n\n"
        "Förklaring till svarsalternativen:\n\n"
        "A. Informationen i $ (1) $ är i sig tillräcklig. Informationen i $ (2) $ är i sig inte tillräcklig.\n"
        "B. Informationen i $ (2) $ är i sig tillräcklig. Informationen i $ (1) $ är i sig inte tillräcklig.\n"
        "C. För att få tillräcklig information krävs att $ (1) $ används tillsammans med $ (2) $. "
        "Enbart $ (1) $ eller enbart $ (2) $ ger inte tillräcklig information.\n"
        "D. $ (1) $ och $ (2) $ innehåller var för sig tillräckligt mycket information.\n"
        "E. Inte ens $ (1) $ tillsammans med $ (2) $ ger tillräcklig information.\n\n"
        "Lösning:\n\n"
        "Informationen i $ (1) $ är tillräcklig för att kunna räkna ut att Linn har 1 femkrona.\n"
        "Med enbart informationen i $ (2) $ kan vi räkna ut att Linn har antingen 1 eller 5 femkronor. "
        "Informationen i $ (2) $ räcker alltså inte för att entydigt kunna besvara frågan. Rätt svar:A."
    )
}


## The original exam instructions without the example questions.
zero_shot_prompts = {
    "ORD": (
        f"I delprovet ORD inleds varje uppgift med ett ord i fetstil. Under detta finns fem "
        f"svarsförslag. Välj det svarsförslag som bäst motsvarar innebörden av det fetstilta ordet. "
        f"{five_instruction_str}"
    ),

    "LAS": (
        f"Delprovet LÄS består av svenska texter från olika ämnesområden och av varierande längd. "
        f"Varje uppgift består av en fråga med fyra svarsförslag, varav ett är rätt. Ibland kan du "
        f"klart se att ett av svarsförslagen är rätt och att de andra är fel. Ibland verkar flera "
        f"svar mer eller mindre rimliga. Då måste du, genom att jämföra de olika svarsförslagen, "
        f"välja ut det som bäst besvarar frågan. Observera att du ska lösa uppgifterna med ledning "
        f"av den information som ges."
    ),

    "MEK": (
        f"Uppgifterna i delprovet MEK består av korta textstycken där ett eller flera ord ersatts av en lucka markerad med _____. En uppgift kan innehålla en, två eller tre luckor. Efter varje textstycke följer fyra svarsförslag. Välj det svarsförslag som innehållsligt och språkligt passar bäst in i textstycket som helhet."
    ),

    "XYZ": (
        f"Delprovet XYZ handlar om matematisk problemlösning. Varje uppgift består av en fråga som "
        f"följs av fyra svarsalternativ, varav endast ett är rätt."
    ),

    "KVA": (
        f"Delprovet KVA innehåller uppgifter med beskrivningar av två kvantiteter, I och II. Din "
        f"uppgift är att jämföra de två kvantiteterna. I vissa fall ges inledande information som "
        f"ska användas vid jämförelsen. Till varje uppgift finns fyra svarsalternativ, varav endast "
        f"ett är rätt. I KVA har alla uppgifter samma svarsalternativ."
    ),

    "NOG": (
        f"Delprovet NOG består av uppgifter med en fråga följd av två påståenden, $ (1) $ och $ (2) $, som innehåller information. Frågan kan ibland föregås av viss inledande information. Din"
        f"uppgift är att avgöra om frågan entydigt kan besvaras med hjälp av informationen i "
        f"påståendena, och i så fall hur mycket av denna information som är tillräcklig. Till varje "
        f"uppgift finns fem svarsalternativ, varav endast ett är rätt. I NOG har alla uppgifter samma svarsalternativ."
    )
}
