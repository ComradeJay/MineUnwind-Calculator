import streamlit as st


st.set_page_config(page_title="Mineunwind Calculator")
st.subheader("Which Realm:")
dim = st.radio("",('Kingdom', 'Magekeep', 'Bonebay','Submera','Aquaris'))
st.subheader("Which Mix")
if dim=="Kingdom": # 𝟭𝘀𝘁 𝗥𝗲𝗮𝗹𝗺
     block = st.radio(
          "",
        ('Stone - Iron Mix', 'Iron - Diamond Mix', 'Diamond - Emerald Mix','Kingdom Mix', 'Kingdom Mix (Mix only)'))
     val=int(st.text_input('How Many Blocks?', 0))
     if block=='Stone - Iron Mix':
          a = int(val / 64)
          b = val % 64
          if ((b % 64)==0):
               st.header(f"You need {a:,d} Stacks of T3 Stone and Iron")
          else:
               st.header(f"You need {a:,d} stacks and {b} blocks of T3 Stone and Iron")
     elif block=="Iron - Diamond Mix":
          a = val*4
          b = int(a/64)
          c = a%64
          if ((c % 64)==0):
               st.header(f"You need {b:,d} Stacks of T3 Iron and Diamond")
          else:
               st.header(f"You need {b:,d} stacks and {c} blocks of T3 Iron and Diamond")
     elif block=="Diamond - Emerald Mix":
          a=val*8
          b=int(a/64)
          c=a%64
          if ((c % 64)==0):
               st.header(f"You need {b:,d} Stacks of T3 Diamond and Emerald")
          else:
               st.header(f"You need {b:,d} stacks and {c} blocks of T3 Diamond and Emerald ")
     elif block=='Kingdom Mix (Mix only)':
          ID = val*3
          DE = val*3
          if ((ID % 64)==0):
               st.header(f"{int(ID / 64):,d} Stacks of Iron - Diamond Mix")
          else:
               st.header(f"{int(ID / 64):,d} Stacks and {ID%64} Blocks of Iron - Diamond Mix")
          
          
          if ((DE % 64)==0):
               st.header(f"{int(DE / 64):,d} Stacks of Diamond - Emerald Mix")
          else:
               st.header(f"{int(DE/64):,d} Stacks and {DE%64} Blocks of Diamond - Emerald Mix")  
     else:
          Diamond = val*36
          Emerald = val*24
          Iron = val*12
          if ((Iron % 64)==0):
               st.header(f"You need {int(Iron / 64):,d} Stacks of T3 Iron")
          else:
               st.header(f"You need {int(Iron / 64):,d} Stacks and {Iron % 64} T3 Iron")
          if ((Diamond % 64)==0):
               st.header(f"You need {int(Diamond / 64):,d} Stacks of T3 Diamond")
          else:
               st.header(f"You need {int(Diamond/64):,d} Stacks and {Diamond%64} T3 Diamond")
          if ((Emerald % 64)==0):
               st.header(f"You need {int(Emerald / 64):,d} Stacks of T3 Emerald")
          else:
               st.header(f"You need {int(Emerald / 64):,d} Stacks and {Emerald % 64} T3 Emerald")


elif dim=="Magekeep": # 𝟮𝗻𝗱 𝗥𝗲𝗮𝗹𝗺
     block = st.radio(
          "",
          ('Endstone - Milk Mix','Milk - Dripstone Mix','Dripstone - Gold Mix','Magekeep Mix', 'Magekeep Mix (Mix only)'))
     val = int(st.text_input('How Many Blocks?', 0))
     if block == "Endstone - Milk Mix":
          Endstone = val * 3
          Milk= val * 4
          if ((Endstone % 64)==0):
               st.header(f"You need {int(Endstone/64):,d} Stacks of T3 Endstone")
          else:
               st.header(f"You need {int(Endstone/64):,d} stacks and {Endstone%64} blocks of T3 Endstone")
          if ((Milk % 64)==0):
               st.header(f"You need {int(Milk/64):,d} Stacks of T3 Milk")
          else:
               st.header(f"You need {int(Milk/64):,d} stacks and {Milk%64} blocks of T3 Milk")
     elif block == "Milk - Dripstone Mix":
          Milk = val * 7
          Dripstone = val * 6
          if ((Milk % 64)==0):
               st.header(f"You need {int(Milk/64):,d} Stacks of T3 Milk")
          else:
               st.header(f"You need {int(Milk/64):,d} stacks and {Milk%64} blocks of T3 Milk")
          if ((Dripstone % 64)==0):
               st.header(f"You need {int(Dripstone/64):,d} Stacks of T3 Dripstone")
          else:
               st.header(f"You need {int(Dripstone/64):,d} stacks and {Dripstone%64} blocks of T3 Dripstone")
     elif block == "Dripstone - Gold Mix":
          a = val * 12
          b = int(a / 64)
          c = a % 64
          if ((c % 64)==0):
               st.header(f"You need {b:,d} Stacks of T3 Dripstone and Gold")
          else:
               st.header(f"You need {b:,d} stacks and {c} blocks of T3 Dripstone and Gold ")
     elif block=='Magekeep Mix (Mix only)':
          GO = val*6
          OL = val*7
          if ((GO % 64)==0):
               st.header(f"{int(GO / 64):,d} Stacks of Milk - Dripstone Mix")
          else:
               st.header(f"{int(GO / 64):,d} Stacks and {GO%64} Blocks of Milk - Dripstone Mix")
          if ((OL % 64)==0):
               st.header(f"{int(OL / 64):,d} Stacks of Dripstone - Gold Mix")
          else:
               st.header(f"{int(OL/64):,d} Stacks and {OL%64} Blocks of Dripstone - Gold Mix")
     else:
          Milk = val * 42
          Dripstone = val * 120
          Gold = val * 84
          if ((Milk % 64)==0):
               st.header(f"You need {int(Milk / 64):,d} Stacks of T3 Milk")
          else:
               st.header(f"You need {int(Milk / 64):,d} Stacks and {Milk % 64} T3 Milk")
          if ((Dripstone % 64)==0):
               st.header(f"You need {int(Dripstone / 64):,d} Stacks of T3 Dripstone")
          else:
               st.header(f"You need {int(Dripstone/64):,d} Stacks and {Dripstone%64} T3 Dripstone")
          if ((Gold % 64)==0):
               st.header(f"You need {int(Gold / 64):,d} Stacks of T3 Gold")
          else:
               st.header(f"You need {int(Gold / 64):,d} Stacks and {Gold % 64} T3 Gold")


elif dim=="Bonebay": # 𝟯𝗿𝗱 𝗥𝗲𝗮𝗹𝗺
     block = st.radio(
          "",
          ('Sandstone - Mysterious Prismarine Mix','Mysterious Prismarine - Nylium Mix','Nylium - Fossil Mix','Bonebay Mix', 'Bonebay Mix (Mix only)'))
     val = int(st.text_input('How Many Blocks?', 0))
     if block == 'Sandstone - Mysterious Prismarine Mix':
          a=val*8
          b = int(a / 64)
          c = a % 64
          if ((c % 64)==0):
               st.header(f"You need {b:,d} Stacks of T3 Sandstone and Mysterious Prismarine")
          else:
               st.header(f"You need {b:,d} stacks and {c} blocks of T3 Sandstone and Mysterious Prismarine ")
     elif block == "Mysterious Prismarine - Nylium Mix":
          Mysterious=val*10
          Nylium=val*9
          if ((Mysterious % 64)==0):
               st.header(f"You need {int(Mysterious/64):,d} Stacks of T3 Mysterious Prismarine")
          else:
               st.header(f"You need {int(Mysterious / 64):,d} Stacks and {Mysterious % 64} T3 Mysterious Prismarine ")
          if ((Nylium % 64)==0):
               st.header(f"You need {int(Nylium/64):,d} Stacks of T3 Nylium")
          else:
               st.header(f"You need {int(Nylium / 64):,d} Stacks and {Nylium % 64} T3 Nylium")           
     elif block == "Nylium - Fossil Mix":
          Nylium=val*13
          Fossil=val*13
          if ((Nylium % 64)==0):
               st.header(f"You need {int(Nylium/64):,d} Stacks of T3 Nylium")
          else:
               st.header(f"You need {int(Nylium / 64):,d} Stacks and {Nylium % 64} T3 Nylium ")
          if ((Fossil % 64)==0):
               st.header(f"You need {int(Fossil/64):,d} Stacks of T3 Fossil")
          else:
               st.header(f"You need {int(Fossil / 64):,d} Stacks and {Fossil % 64} T3 Fossil")        
     elif block=='Bonebay Mix (Mix only)':
          BS = val*7
          SG = val*7
          if ((BS % 64)==0):
               st.header(f"{int(BS / 64):,d} Stacks of Mysterious Prismarine - Silver Mix")
          else:
               st.header(f"{int(BS / 64):,d} Stacks and {BS%64} Blocks of Mysterious Prismarine - Silver Mix")
          if ((SG % 64)==0):
               st.header(f"{int(SG / 64):,d} Stacks of Silver - Fossil Mix")
          else:
               st.header(f"{int(SG/64):,d} Stacks and {SG%64} Blocks of Silver - Fossil Mix")
     else:
          Mysterious = val * 70 
          Nylium = val * 154 
          Fossil = val * 91 
          if ((Mysterious % 64)==0):
               st.header(f"You need {int(Mysterious/64):,d} Stacks of T3 Mysterious Prismarine")
          else:
               st.header(f"You need {int(Mysterious / 64):,d} Stacks and {Mysterious % 64} T3 Mysterious Prismarine")
          if ((Nylium % 64)==0):
               st.header(f"You need {int(Nylium/64):,d} Stacks of T3 Nylium")
          else:
               st.header(f"You need {int(Nylium / 64):,d} Stacks and {Nylium % 64} T3 Nylium ")
          if ((Fossil % 64)==0):
               st.header(f"You need {int(Fossil/64):,d} Stacks of T3 Fossil")
          else:
               st.header(f"You need {int(Fossil / 64):,d} Stacks and {Fossil % 64} T3 Fossil ")

elif dim=="Submera": # 𝟰𝘁𝗵 𝗥𝗲𝗮𝗹𝗺
     block = st.radio(
          "",
          ('Gem - Pearl Mix','Pearl - Volcanic Silt Mix','Volcanic Silt - Fluorite Mix','Submera Mix', 'Submera Mix (Mix only)'))
     val = int(st.text_input('How Many Blocks?', 0))
     if block == 'Gem - Pearl Mix':
          a=val*9
          b = int(a / 64)
          c = a % 64
          if ((c % 64)==0):
               st.header(f"You need {b:,d} Stacks of T3 Gem and Pearl")
          else:
               st.header(f"You need {b:,d} stacks and {c} blocks of T3 Gem and Pearl ")
     elif block == "Pearl - Volcanic Silt Mix":
          Pearl=val*11
          VolcanicSilt=val*9
          if ((Pearl % 64)==0):
               st.header(f"You need {int(Pearl/64):,d} Stacks of T3 Pearl ")
          else:
               st.header(f"You need {int(Pearl / 64):,d} Stacks and {Pearl % 64} T3 Pearl")
          if ((VolcanicSilt % 64)==0):
               st.header(f"You need {int(VolcanicSilt/64):,d} Stacks of T3  Volcanic Silt")
          else:
               st.header(f"You need {int(VolcanicSilt / 64):,d} Stacks and {VolcanicSilt % 64} T3  Volcanic Silt")
     elif block == "Volcanic Silt - Fluorite Mix":
          VolcanicSilt=val*15
          Fluorite=val*15
          if ((VolcanicSilt % 64)==0):
               st.header(f"You need {int(VolcanicSilt/64):,d} Stacks of T3 Volcanic Silt ")
          else:
               st.header(f"You need {int(VolcanicSilt / 64):,d} Stacks and {VolcanicSilt % 64} T3 Volcanic Silt  ")
          if ((Fluorite % 64)==0):
               st.header(f"You need {int(Fluorite/64):,d} Stacks of T3  Fluorite")
          else:
               st.header(f"You need {int(Fluorite / 64):,d} Stacks and {Fluorite % 64} T3  Fluorite")
     elif block=='Submera Mix (Mix only)':
          AG = val*7
          GL = val*7
          if ((AG % 64)==0):
               st.header(f"{int(AG / 64):,d} Stacks of Pearl - Volcanic Silt Mix")
          else:
               st.header(f"{int(AG / 64):,d} Stacks and {AG%64} Blocks of Pearl - Volcanic Silt Mix")
          if ((GL % 64)==0):
               st.header(f"{int(GL / 64):,d} Stacks of Volcanic Silt - Fluorite Mix")
          else:
               st.header(f"{int(GL/64):,d} Stacks and {GL%64} Blocks of Volcanic Silt - Fluorite Mix")
     else:
          Pearl = val * 77 
          VolcanicSilt = val * 168 
          Fluorite = val * 105 
          if ((Pearl % 64)==0):
               st.header(f"You need {int(Pearl/64):,d} Stacks of T3 Pearl ")
          else:
               st.header(f"You need {int(Pearl / 64):,d} Stacks and {Pearl % 64} T3 Pearl ")
          if ((VolcanicSilt % 64)==0):
               st.header(f"You need {int(VolcanicSilt/64):,d} Stacks of T3  Volcanic Silt")
          else:
               st.header(f"You need {int(VolcanicSilt / 64):,d} Stacks and {VolcanicSilt % 64} T3  Volcanic Silt ")
          if ((Fluorite % 64)==0):
               st.header(f"You need {int(Fluorite/64):,d} Stacks of T3 Fluorite")
          else:
               st.header(f"You need {int(Fluorite / 64):,d} Stacks and {Fluorite % 64} T3 Fluorite ")


elif dim=="Aquaris": # 𝟱𝘁𝗵 𝗥𝗲𝗮𝗹𝗺
     block = st.radio(
          "",
          ('Smurf - Bubblegum Mix','Bubblegum - Spicy Mix','Spicy - Grape Mix','Aquaris Mix', 'Aquaris Mix (Mix only)'))
     val = int(st.text_input('How Many Blocks?', 0))
     if block == 'Smurf - Bubblegum Mix':
          a=val*10
          b = int(a / 64)
          c = a % 64
          if ((c % 64)==0):
               st.header(f"You need {b:,d} Stacks of T3 Smurf and Bubblegum")
          else:
               st.header(f"You need {b:,d} stacks and {c} blocks of T3 Smurf and Bubblegum ")
     elif block == "Bubblegum - Spicy Mix":
          Bubblegum=val*11
          Spicy=val*11
          if ((Bubblegum % 64)==0):
               st.header(f"You need {int(Bubblegum/64):,d} Stacks of T3 Bubblegum")
          else:
               st.header(f"You need {int(Bubblegum / 64):,d} Stacks and {Bubblegum % 64} T3 Bubblegum ")
          if ((Spicy % 64)==0):
               st.header(f"You need {int(Spicy/64):,d} Stacks of T3 Spicy")
          else:
               st.header(f"You need {int(Spicy / 64):,d} Stacks and {Spicy % 64} T3 Spicy")
     elif block == "Spicy - Grape Mix":
          Bubblegum=val*16
          Spicy=val*16
          if ((Bubblegum % 64)==0):
               st.header(f"You need {int(Bubblegum/64):,d} Stacks of T3 Spicy")
          else:
               st.header(f"You need {int(Bubblegum / 64):,d} Stacks and {Bubblegum % 64} T3 Spicy ")
          if ((Spicy % 64)==0):
               st.header(f"You need {int(Spicy/64):,d} Stacks of T3 Grape")
          else:
               st.header(f"You need {int(Spicy / 64):,d} Stacks and {Spicy % 64} T3 Grape")
     elif block=='Aquaris Mix (Mix only)':
          TC = val*10
          CC = val*10
          if ((TC % 64)==0):
               st.header(f"{int(TC / 64):,d} Stacks of Bubblegum - Spicy Mix")
          else:
               st.header(f"{int(TC / 64):,d} Stacks and {TC%64} Blocks of Bubblegum - Spicy Mix")
          if ((CC % 64)==0):
               st.header(f"{int(CC / 64):,d} Stacks of Spicy - Grape Mix")
          else:
               st.header(f"{int(CC/64):,d} Stacks and {CC%64} Blocks of Spicy - Grape Mix")
     else:
          Grape = val * 160 
          Bubblegum = val * 110  
          Spicy = val * 270
          if ((Bubblegum % 64)==0):
               st.header(f"You need {int(Bubblegum/64):,d} Stacks of Bubblegum")
          else:
               st.header(f"You need {int(Bubblegum / 64):,d} Stacks and {Bubblegum % 64} T3 Bubblegum")
          if ((Spicy % 64)==0):
               st.header(f"You need {int(Spicy/64):,d} Stacks of T3 Spicy")
          else:
               st.header(f"You need {int(Spicy / 64):,d} Stacks and {Spicy % 64} T3 Spicy ")
          if ((Grape % 64)==0):
               st.header(f"You need {int(Grape/64):,d} Stacks of T3 Grape")
          else:
               st.header(f"You need {int(Grape / 64):,d} Stacks and {Grape % 64} T3 Grape ")


st.caption(f"Any issues ping .comradejay on Discord")
st.caption(f"Original creators stresso and illusioner_ on Discord ")
st.caption(f"Special thanks to banishedghost and NyaaaaVie for the math <3.")
st.write(f"Github [link](https://github.com/ComradeJay/s5calc)")
