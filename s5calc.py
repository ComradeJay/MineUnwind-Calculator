import streamlit as st

st.set_page_config(page_title="Mineunwind Calculator")
st.subheader("Which Realm:")
dim = st.radio("",('River', 'Ranch', 'Port','Empire','Citadel'))
st.subheader("Which Block")
if dim=="River":
     block = st.radio(
          "",
          ('Stone - Iron Mix', 'Iron - Diamond Mix', 'Diamond - Emerald Mix','River Mix'))
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
          Diamond=val*36
          Emerald=val*24
          Iron=val*12
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
elif dim=="Ranch":
     block = st.radio(
          "",
          ('Granite - Coal Mix','Coal - Copper Mix','Copper - Redstone Mix','Ranch Mix'))
     val = int(st.text_input('How Many Blocks?', 0))
     if block == 'Granite - Coal Mix':
          a=val*4
          b = int(a / 64)
          c = a % 64
          if ((c % 64)==0):
               st.header(f"You need {b:,d} Stacks of T3 Granite and Coal")
          else:
               st.header(f"You need {b:,d} stacks and {c} blocks of T3 Granite and Coal ")
     elif block == "Coal - Copper Mix":
          Redstone = val * 7
          Copper=val*6
          if ((Redstone % 64)==0):
               st.header(f"You need {int(Redstone/64):,d} Stacks of T3 Coal")
          else:
               st.header(f"You need {int(Redstone/64):,d} stacks and {Redstone%64} blocks of T3 Coal")
          if ((Copper % 64)==0):
               st.header(f"You need {int(Copper/64):,d} Stacks of T3 Emerald")
          else:
               st.header(f"You need {int(Copper/64):,d} stacks and {Copper%64} blocks of T3 Copper")
     elif block == "Copper - Redstone Mix":
          a = val * 12
          b = int(a / 64)
          c = a % 64
          if ((c % 64)==0):
               st.header(f"You need {b:,d} Stacks of T3 Copper and Redstone")
          else:
               st.header(f"You need {b:,d} stacks and {c} blocks of T3 Copper and Redstone ")
     else:
          Coal = val * 42
          Copper = val * 120
          Redstone = val * 84
          if ((Coal % 64)==0):
               st.header(f"You need {int(Coal / 64):,d} Stacks of T3 Coal")
          else:
               st.header(f"You need {int(Coal / 64):,d} Stacks and {Coal % 64} T3 Coal")
          if ((Copper % 64)==0):
               st.header(f"You need {int(Copper / 64):,d} Stacks of T3 Copper")
          else:
               st.header(f"You need {int(Copper/64):,d} Stacks and {Copper%64} T3 Copper")
          if ((Redstone % 64)==0):
               st.header(f"You need {int(Redstone / 64):,d} Stacks of T3 Redstone")
          else:
               st.header(f"You need {int(Redstone / 64):,d} Stacks and {Redstone % 64} T3 Redstone")
elif dim=="Port":
     block = st.radio(
          "",
          ('Sandstone - Prismarine Mix','Prismarine - Oceanstone Mix','Oceanstone - Seashine Mix','Port Mix'))
     val = int(st.text_input('How Many Blocks?', 0))
     if block == 'Sandstone - Prismarine Mix':
          a=val*8
          b = int(a / 64)
          c = a % 64
          if ((c % 64)==0):
               st.header(f"You need {b:,d} Stacks of T3 Sandstone and Prismarine")
          else:
               st.header(f"You need {b:,d} stacks and {c} blocks of T3 Sandstone and Prismarine ")
     elif block == "Prismarine - Oceanstone Mix":
          Prismarine=val*10
          Oceanstone=val*9
          if ((Prismarine % 64)==0):
               st.header(f"You need {int(Prismarine/64):,d} Stacks of T3 Prismarine")
          else:
               st.header(f"You need {int(Prismarine / 64):,d} Stacks and {Prismarine % 64} T3 Prismarine ")
          if ((Oceanstone % 64)==0):
               st.header(f"You need {int(Oceanstone/64):,d} Stacks of T3 Oceanstone")
          else:
               st.header(f"You need {int(Oceanstone / 64):,d} Stacks and {Oceanstone % 64} T3 Oceanstone")           
     elif block == "Oceanstone - Seashine Mix":
          Oceanstone=val*13
          Seashine=val*13
          if ((Oceanstone % 64)==0):
               st.header(f"You need {int(Oceanstone/64):,d} Stacks of T3 Oceanstone")
          else:
               st.header(f"You need {int(Oceanstone / 64):,d} Stacks and {Oceanstone % 64} T3 Oceanstone ")
          if ((Seashine % 64)==0):
               st.header(f"You need {int(Seashine/64):,d} Stacks of T3 Seashine")
          else:
               st.header(f"You need {int(Seashine / 64):,d} Stacks and {Seashine % 64} T3 Seashine")        
     else:
          Prismarine = val * 70 
          Oceanstone = val * 154 
          Seashine = val * 91 
          if ((Prismarine % 64)==0):
               st.header(f"You need {int(Prismarine/64):,d} Stacks of T3 Prismarine")
          else:
               st.header(f"You need {int(Prismarine / 64):,d} Stacks and {Prismarine % 64} T3 Prismarine")
          if ((Oceanstone % 64)==0):
               st.header(f"You need {int(Oceanstone/64):,d} Stacks of T3 Oceanstone")
          else:
               st.header(f"You need {int(Oceanstone / 64):,d} Stacks and {Oceanstone % 64} T3 Oceanstone ")
          if ((Seashine % 64)==0):
               st.header(f"You need {int(Seashine/64):,d} Stacks of T3 Seashine")
          else:
               st.header(f"You need {int(Seashine / 64):,d} Stacks and {Seashine % 64} T3 Seashine ")
elif dim=="Empire":
     block = st.radio(
          "",
          ('Moss Stone - Star Rock Mix','Star Rock - Aztec Relic Mix','Aztec Relic - Amethyst Mix','Empire Mix'))
     val = int(st.text_input('How Many Blocks?', 0))
     if block == 'Moss Stone - Star Rock Mix':
          a=val*9
          b = int(a / 64)
          c = a % 64
          if ((c % 64)==0):
               st.header(f"You need {b:,d} Stacks of T3 Moss Stone and Star Rock")
          else:
               st.header(f"You need {b:,d} stacks and {c} blocks of T3 Moss Stone and Star Rock ")
     elif block == "Star Rock - Aztec Relic Mix":
          a = val * 11
          b = int(a / 64)
          c = a % 64
          if ((c % 64)==0):
               st.header(f"You need {b:,d} Stacks of T3 Star Rock and Aztec Relic")
          else:
               st.header(f"You need {b:,d} stacks and {c} blocks of T3 Star Rock and Aztec Relic ")
     elif block == "Aztec Relic - Amethyst Mix":
          Aztec=val*15
          Amethyst=val*15
          if ((Aztec % 64)==0):
               st.header(f"You need {int(Aztec/64):,d} Stacks of T3 Aztec Relic ")
          else:
               st.header(f"You need {int(Aztec / 64):,d} Stacks and {Aztec % 64} T3 Aztec Relic  ")
          if ((Amethyst % 64)==0):
               st.header(f"You need {int(Amethyst/64):,d} Stacks of T3  Amethyst")
          else:
               st.header(f"You need {int(Amethyst / 64):,d} Stacks and {Amethyst % 64} T3  Amethyst")
     else:
          Star = val * 77 
          Aztec = val * 168 
          Amethyst = val * 105 
          if ((Star % 64)==0):
               st.header(f"You need {int(Star/64):,d} Stacks of T3 Star Rock ")
          else:
               st.header(f"You need {int(Star / 64):,d} Stacks and {Star % 64} T3 Star Rock ")
          if ((Aztec % 64)==0):
               st.header(f"You need {int(Aztec/64):,d} Stacks of T3  Aztec Relic")
          else:
               st.header(f"You need {int(Aztec / 64):,d} Stacks and {Aztec % 64} T3  Aztec Relic ")
          if ((Amethyst % 64)==0):
               st.header(f"You need {int(Amethyst/64):,d} Stacks of T3 Amethyst")
          else:
               st.header(f"You need {int(Amethyst / 64):,d} Stacks and {Amethyst % 64} T3 Amethyst ")
elif dim=="Citadel":
     block = st.radio(
          "",
          ('Marble - Purpur Mix','Purpur - Magma Mix','Magma - Obsidian Mix','Citadel Mix'))
     val = int(st.text_input('How Many Blocks?', 0))
     if block == 'Marble - Purpur Mix':
          a=val*10
          b = int(a / 64)
          c = a % 64
          if ((c % 64)==0):
               st.header(f"You need {b:,d} Stacks of T3 Marble and Purpur")
          else:
               st.header(f"You need {b:,d} stacks and {c} blocks of T3 Marble and Purpur ")
     elif block == "Purpur - Magma Mix":
          Purpur=val*11
          Magma=val*11
          if ((Purpur % 64)==0):
               st.header(f"You need {int(Purpur/64):,d} Stacks of T3 Purpur")
          else:
               st.header(f"You need {int(Purpur / 64):,d} Stacks and {Purpur % 64} T3 Purpur ")
          if ((Magma % 64)==0):
               st.header(f"You need {int(Magma/64):,d} Stacks of T3 Magma")
          else:
               st.header(f"You need {int(Magma / 64):,d} Stacks and {Magma % 64} T3 Magma")
     elif block == "Magma - Obsidian Mix":
          Purpur=val*16
          Magma=val*16
          if ((Purpur % 64)==0):
               st.header(f"You need {int(Purpur/64):,d} Stacks of T3 Magma")
          else:
               st.header(f"You need {int(Purpur / 64):,d} Stacks and {Purpur % 64} T3 Magma ")
          if ((Magma % 64)==0):
               st.header(f"You need {int(Magma/64):,d} Stacks of T3 Obsidian")
          else:
               st.header(f"You need {int(Magma / 64):,d} Stacks and {Magma % 64} T3 Obsidian")
     else:
          Obsidian = val * 160 
          Purpur = val * 110  
          Magma = val * 270
          if ((Obsidian % 64)==0):
               st.header(f"You need {int(Obsidian/64):,d} Stacks of Purpur")
          else:
               st.header(f"You need {int(Obsidian / 64):,d} Stacks and {Obsidian % 64} T3 Purpur")
          if ((Purpur % 64)==0):
               st.header(f"You need {int(Purpur/64):,d} Stacks of T3 Magma")
          else:
               st.header(f"You need {int(Purpur / 64):,d} Stacks and {Purpur % 64} T3 Magma ")
          if ((Magma % 64)==0):
               st.header(f"You need {int(Magma/64):,d} Stacks of T3 Obsidian")
          else:
               st.header(f"You need {int(Magma / 64):,d} Stacks and {Magma % 64} T3 Obsidian ")
st.caption(f"Any issues message .comradejay on Discord")
st.caption(f"Original creators stresso and illusioner_ on Discord ")
st.caption(f"Special thanks to banishedghost and NyaaaaVie for the math <3.")
