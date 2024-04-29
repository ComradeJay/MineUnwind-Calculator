import streamlit as st


st.set_page_config(page_title="Mineunwind Calculator")
st.subheader("Which Realm:")
dim = st.radio("",('City', 'Farm', 'Colosseum','Cavern','Graveyard'))
st.subheader("Which Block")
if dim=="City": # 𝟭𝘀𝘁 𝗥𝗲𝗮𝗹𝗺
     block = st.radio(
          "",
        ('Stone - Iron Mix', 'Iron - Diamond Mix', 'Diamond - Emerald Mix','City Mix'))
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
     else:
          Diamond = val*36
          Emerald = val*24
          Iron = val*12
          City = val * 3
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
          st.header(f"You need {int(City / 64):,d} Stacks of Iron and Diamond Mix and {int(City / 64):,d} Stacks of Diamond and Emerald Mix")


elif dim=="Farm": # 𝟮𝗻𝗱 𝗥𝗲𝗮𝗹𝗺
     block = st.radio(
          "",
          ('Dirt - Grass Mix','Grass - Orange Mix','Orange - Lemon Mix','Farm Mix'))
     val = int(st.text_input('How Many Blocks?', 0))
     if block == "Dirt - Grass Mix":
          Dirt = val * 3
          Grass= val * 4
          if ((Dirt % 64)==0):
               st.header(f"You need {int(Dirt/64):,d} Stacks of T3 Dirt")
          else:
               st.header(f"You need {int(Dirt/64):,d} stacks and {Dirt%64} blocks of T3 Dirt")
          if ((Grass % 64)==0):
               st.header(f"You need {int(Grass/64):,d} Stacks of T3 Grass")
          else:
               st.header(f"You need {int(Grass/64):,d} stacks and {Grass%64} blocks of T3 Grass")
     elif block == "Grass - Orange Mix":
          Grass = val * 7
          Orange = val * 6
          if ((Grass % 64)==0):
               st.header(f"You need {int(Grass/64):,d} Stacks of T3 Grass")
          else:
               st.header(f"You need {int(Grass/64):,d} stacks and {Grass%64} blocks of T3 Grass")
          if ((Orange % 64)==0):
               st.header(f"You need {int(Orange/64):,d} Stacks of T3 Orange")
          else:
               st.header(f"You need {int(Orange/64):,d} stacks and {Orange%64} blocks of T3 Orange")
     elif block == "Orange - Lemon Mix":
          a = val * 12
          b = int(a / 64)
          c = a % 64
          if ((c % 64)==0):
               st.header(f"You need {b:,d} Stacks of T3 Orange and Lemon")
          else:
               st.header(f"You need {b:,d} stacks and {c} blocks of T3 Orange and Lemon ")
     else:
          Grass = val * 42
          Orange = val * 120
          Lemon = val * 84
          GO = val*6
          OL = val*7
          if ((Grass % 64)==0):
               st.header(f"You need {int(Grass / 64):,d} Stacks of T3 Grass")
          else:
               st.header(f"You need {int(Grass / 64):,d} Stacks and {Grass % 64} T3 Grass")
          if ((Orange % 64)==0):
               st.header(f"You need {int(Orange / 64):,d} Stacks of T3 Orange")
          else:
               st.header(f"You need {int(Orange/64):,d} Stacks and {Orange%64} T3 Orange")
          if ((Lemon % 64)==0):
               st.header(f"You need {int(Lemon / 64):,d} Stacks of T3 Lemon")
          else:
               st.header(f"You need {int(Lemon / 64):,d} Stacks and {Lemon % 64} T3 Lemon")
          st.header(f"You need {int(GO / 64):,d} Stacks of Grass and Orange Mix and {int(OL / 64):,d} Stacks of Orange and Lemon Mix")


elif dim=="Colosseum": # 𝟯𝗿𝗱 𝗥𝗲𝗮𝗹𝗺
     block = st.radio(
          "",
          ('Copper - Blood Mix','Blood - Silver Coin Mix','Silver Coin - Gold Coin Mix','Colosseum Mix'))
     val = int(st.text_input('How Many Blocks?', 0))
     if block == 'Copper - Blood Mix':
          a=val*8
          b = int(a / 64)
          c = a % 64
          if ((c % 64)==0):
               st.header(f"You need {b:,d} Stacks of T3 Copper and Blood")
          else:
               st.header(f"You need {b:,d} stacks and {c} blocks of T3 Copper and Blood ")
     elif block == "Blood - Silver Coin Mix":
          Blood=val*10
          SilverCoin=val*9
          if ((Blood % 64)==0):
               st.header(f"You need {int(Blood/64):,d} Stacks of T3 Blood")
          else:
               st.header(f"You need {int(Blood / 64):,d} Stacks and {Blood % 64} T3 Blood ")
          if ((SilverCoin % 64)==0):
               st.header(f"You need {int(SilverCoin/64):,d} Stacks of T3 Silver Coin")
          else:
               st.header(f"You need {int(SilverCoin / 64):,d} Stacks and {SilverCoin % 64} T3 Silver Coin")           
     elif block == "Silver Coin - Gold Coin Mix":
          SilverCoin=val*13
          GoldCoin=val*13
          if ((SilverCoin % 64)==0):
               st.header(f"You need {int(SilverCoin/64):,d} Stacks of T3 Silver Coin")
          else:
               st.header(f"You need {int(SilverCoin / 64):,d} Stacks and {SilverCoin % 64} T3 Silver Coin ")
          if ((GoldCoin % 64)==0):
               st.header(f"You need {int(GoldCoin/64):,d} Stacks of T3 Gold Coin")
          else:
               st.header(f"You need {int(GoldCoin / 64):,d} Stacks and {GoldCoin % 64} T3 Gold Coin")        
     else:
          Blood = val * 70 
          SilverCoin = val * 154 
          GoldCoin = val * 91 
          Colo=val*7
          if ((Blood % 64)==0):
               st.header(f"You need {int(Blood/64):,d} Stacks of T3 Blood")
          else:
               st.header(f"You need {int(Blood / 64):,d} Stacks and {Blood % 64} T3 Blood")
          if ((SilverCoin % 64)==0):
               st.header(f"You need {int(SilverCoin/64):,d} Stacks of T3 Silver Coin")
          else:
               st.header(f"You need {int(SilverCoin / 64):,d} Stacks and {SilverCoin % 64} T3 Silver Coin ")
          if ((GoldCoin % 64)==0):
               st.header(f"You need {int(GoldCoin/64):,d} Stacks of T3 Gold Coin")
          else:
               st.header(f"You need {int(GoldCoin / 64):,d} Stacks and {GoldCoin % 64} T3 Gold Coin ")
          st.header(f"You need {int(Colo / 64):,d} Stacks of Blood and Silver Coin Mix and {int(Colo / 64):,d} Stacks of Silver and Gold Coin Mix")

elif dim=="Cavern": # 𝟰𝘁𝗵 𝗥𝗲𝗮𝗹𝗺
     block = st.radio(
          "",
          ('Calcite - Amethyst Mix','Amethyst - Gilded Gold Mix','Gilded Gold - Limonite Mix','Cavern Mix'))
     val = int(st.text_input('How Many Blocks?', 0))
     if block == 'Calcite - Amethyst Mix':
          a=val*9
          b = int(a / 64)
          c = a % 64
          if ((c % 64)==0):
               st.header(f"You need {b:,d} Stacks of T3 Calcite and Amethyst")
          else:
               st.header(f"You need {b:,d} stacks and {c} blocks of T3 Calcite and Amethyst ")
     elif block == "Amethyst - Gilded Gold Mix":
          Amethyst=val*11
          GildedGold=val*9
          if ((Amethyst % 64)==0):
               st.header(f"You need {int(Amethyst/64):,d} Stacks of T3 Amethyst ")
          else:
               st.header(f"You need {int(Amethyst / 64):,d} Stacks and {Amethyst % 64} T3 Amethyst")
          if ((GildedGold % 64)==0):
               st.header(f"You need {int(GildedGold/64):,d} Stacks of T3  Gilded Gold")
          else:
               st.header(f"You need {int(GildedGold / 64):,d} Stacks and {GildedGold % 64} T3  Gilded Gold")
     elif block == "Gilded Gold - Limonite Mix":
          GildedGold=val*15
          Limonite=val*15
          if ((GildedGold % 64)==0):
               st.header(f"You need {int(GildedGold/64):,d} Stacks of T3 Gilded Gold ")
          else:
               st.header(f"You need {int(GildedGold / 64):,d} Stacks and {GildedGold % 64} T3 Gilded Gold  ")
          if ((Limonite % 64)==0):
               st.header(f"You need {int(Limonite/64):,d} Stacks of T3  Limonite")
          else:
               st.header(f"You need {int(Limonite / 64):,d} Stacks and {Limonite % 64} T3  Limonite")
     else:
          Amethyst = val * 77 
          GildedGold = val * 168 
          Limonite = val * 105 
          Cavern=val*7
          if ((Amethyst % 64)==0):
               st.header(f"You need {int(Amethyst/64):,d} Stacks of T3 Amethyst ")
          else:
               st.header(f"You need {int(Amethyst / 64):,d} Stacks and {Amethyst % 64} T3 Amethyst ")
          if ((GildedGold % 64)==0):
               st.header(f"You need {int(GildedGold/64):,d} Stacks of T3  Gilded Gold")
          else:
               st.header(f"You need {int(GildedGold / 64):,d} Stacks and {GildedGold % 64} T3  Gilded Gold ")
          if ((Limonite % 64)==0):
               st.header(f"You need {int(Limonite/64):,d} Stacks of T3 Limonite")
          else:
               st.header(f"You need {int(Limonite / 64):,d} Stacks and {Limonite % 64} T3 Limonite ")
          st.header(f"You need {int(Cavern / 64):,d} Stacks of Amethyst and Gilded Gold Mix and {int(Cavern / 64):,d} Stacks of Gilded Gold and Limonite Mix")

elif dim=="Graveyard": # 𝟱𝘁𝗵 𝗥𝗲𝗮𝗹𝗺
     block = st.radio(
          "",
          ('Necrosol - Tombstone Mix','Tombstone - Coffin Mix','Coffin - Crying Soul Mix','Graveyard Mix'))
     val = int(st.text_input('How Many Blocks?', 0))
     if block == 'Necrosol - Tombstone Mix':
          a=val*10
          b = int(a / 64)
          c = a % 64
          if ((c % 64)==0):
               st.header(f"You need {b:,d} Stacks of T3 Necrosol and Tombstone")
          else:
               st.header(f"You need {b:,d} stacks and {c} blocks of T3 Necrosol and Tombstone ")
     elif block == "Tombstone - Coffin Mix":
          Tombstone=val*11
          Coffin=val*11
          if ((Tombstone % 64)==0):
               st.header(f"You need {int(Tombstone/64):,d} Stacks of T3 Tombstone")
          else:
               st.header(f"You need {int(Tombstone / 64):,d} Stacks and {Tombstone % 64} T3 Tombstone ")
          if ((Coffin % 64)==0):
               st.header(f"You need {int(Coffin/64):,d} Stacks of T3 Coffin")
          else:
               st.header(f"You need {int(Coffin / 64):,d} Stacks and {Coffin % 64} T3 Coffin")
     elif block == "Coffin - Crying Soul Mix":
          Tombstone=val*16
          Coffin=val*16
          if ((Tombstone % 64)==0):
               st.header(f"You need {int(Tombstone/64):,d} Stacks of T3 Coffin")
          else:
               st.header(f"You need {int(Tombstone / 64):,d} Stacks and {Tombstone % 64} T3 Coffin ")
          if ((Coffin % 64)==0):
               st.header(f"You need {int(Coffin/64):,d} Stacks of T3 Crying Soul")
          else:
               st.header(f"You need {int(Coffin / 64):,d} Stacks and {Coffin % 64} T3 Crying Soul")
     else:
          CryingSoul = val * 160 
          Tombstone = val * 110  
          Coffin = val * 270
          Grave=val*10
          if ((Tombstone % 64)==0):
               st.header(f"You need {int(Tombstone/64):,d} Stacks of Tombstone")
          else:
               st.header(f"You need {int(Tombstone / 64):,d} Stacks and {Tombstone % 64} T3 Tombstone")
          if ((Coffin % 64)==0):
               st.header(f"You need {int(Coffin/64):,d} Stacks of T3 Coffin")
          else:
               st.header(f"You need {int(Coffin / 64):,d} Stacks and {Coffin % 64} T3 Coffin ")
          if ((CryingSoul % 64)==0):
               st.header(f"You need {int(CryingSoul/64):,d} Stacks of T3 Crying Soul")
          else:
               st.header(f"You need {int(CryingSoul / 64):,d} Stacks and {CryingSoul % 64} T3 Crying Soul ")
          st.header(f"You need {int(Grave / 64):,d} Stacks of Tombstone and Coffin Mix and {int(Grave / 64):,d} Stacks of Coffin and Crying Soul Mix")


st.caption(f"Any issues ping .comradejay on Discord")
st.caption(f"Original creators stresso and illusioner_ on Discord ")
st.caption(f"Special thanks to banishedghost and NyaaaaVie for the math <3.")
st.write(f"Github [link](https://github.com/ComradeJay/s5calc)")
