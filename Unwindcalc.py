import streamlit as st

st.set_page_config(page_title="Mineunwind Calculator")
st.subheader("Which Realm:")
dim = st.radio("",('Glacial', 'Market', 'Rift','Coast','Wreck'))
st.subheader("Which Block")
if dim=="Glacial":
     block = st.radio(
          "",
        ('Blue Ice - Prismarine Mix', 'Prismarine - Frozen Diamond Mix', 'Frozen Diamond - Frozen Emerald Mix','Glacial Mix'))
     val=int(st.text_input('How Many Blocks?', 0))
     if block=='Blue Ice - Prismarine Mix':
          a = int(val / 64)
          b = val % 64
          if ((b % 64)==0):
               st.header(f"You need {a:,d} Stacks of T3 Blue Ice and Prismarine")
          else:
               st.header(f"You need {a:,d} stacks and {b} blocks of T3 Blue Ice and Iron")
     elif block=="Prismarine - Frozen Diamond Mix":
          a = val*4
          b = int(a/64)
          c = a%64
          if ((c % 64)==0):
               st.header(f"You need {b:,d} Stacks of T3 Prismarine and Frozen Diamond")
          else:
               st.header(f"You need {b:,d} stacks and {c} blocks of T3 Prismarine and Frozen Diamond")
     elif block=="Frozen Diamond - Frozen Emerald Mix":
          a=val*8
          b=int(a/64)
          c=a%64
          if ((c % 64)==0):
               st.header(f"You need {b:,d} Stacks of T3 Frozen Diamond and Frozen Emerald")
          else:
               st.header(f"You need {b:,d} stacks and {c} blocks of T3 Frozen Diamond and Frozen Emerald ")
     else:
          FDiamond=val*36
          FEmerald=val*24
          Prismarine=val*12
          if ((Prismarine % 64)==0):
               st.header(f"You need {int(Prismarine / 64):,d} Stacks of T3 Prismarine")
          else:
               st.header(f"You need {int(Prismarine / 64):,d} Stacks and {Prismarine % 64} T3 Prismarine")
          if ((FrozenDiamond % 64)==0):
               st.header(f"You need {int(Frozen Diamond / 64):,d} Stacks of T3 Frozen Diamond")
          else:
               st.header(f"You need {int(Frozen Diamond/64):,d} Stacks and {Frozen Diamond%64} T3 Frozen Diamond")
          if ((Frozen Emerald % 64)==0):
               st.header(f"You need {int(Frozen Emerald / 64):,d} Stacks of T3 Frozen Emerald")
          else:
               st.header(f"You need {int(Frozen Emerald / 64):,d} Stacks and {Frozen Emerald % 64} T3 Frozen Emerald")
elif dim=="Market":
     block = st.radio(
          "",
          ('Basalt - Red Sandstone Mix','Red Sandstone - Artifact Mix','Artifact - Old Gold Mix','Market Mix'))
     val = int(st.text_input('How Many Blocks?', 0))
     if block == 'Basalt - Red Sandstone Mix':
          a=val*4
          b = int(a / 64)
          c = a % 64
          if ((c % 64)==0):
               st.header(f"You need {b:,d} Stacks of T3 Basalt and Red Sandstone")
          else:
               st.header(f"You need {b:,d} stacks and {c} blocks of T3 Basalt and Red Sandstone ")
     elif block == "Red Sandstone - Artifact Mix":
          Old Gold = val * 7
          Artifact=val*6
          if ((Old Gold % 64)==0):
               st.header(f"You need {int(Old Gold/64):,d} Stacks of T3 Red Sandstone")
          else:
               st.header(f"You need {int(Old Gold/64):,d} stacks and {Old Gold%64} blocks of T3 Red Sandstone")
          if ((Artifact % 64)==0):
               st.header(f"You need {int(Artifact/64):,d} Stacks of T3 Emerald")
          else:
               st.header(f"You need {int(Artifact/64):,d} stacks and {Artifact%64} blocks of T3 Artifact")
     elif block == "Artifact - Old Gold Mix":
          a = val * 12
          b = int(a / 64)
          c = a % 64
          if ((c % 64)==0):
               st.header(f"You need {b:,d} Stacks of T3 Artifact and Old Gold")
          else:
               st.header(f"You need {b:,d} stacks and {c} blocks of T3 Artifact and Old Gold ")
     else:
          RedSandstone = val * 42
          Artifact = val * 120
          OldGold = val * 84
          if ((Red Sandstone % 64)==0):
               st.header(f"You need {int(Red Sandstone / 64):,d} Stacks of T3 Red Sandstone")
          else:
               st.header(f"You need {int(Red Sandstone / 64):,d} Stacks and {Red Sandstone % 64} T3 Red Sandstone")
          if ((Artifact % 64)==0):
               st.header(f"You need {int(Artifact / 64):,d} Stacks of T3 Artifact")
          else:
               st.header(f"You need {int(Artifact/64):,d} Stacks and {Artifact%64} T3 Artifact")
          if ((Old Gold % 64)==0):
               st.header(f"You need {int(Old Gold / 64):,d} Stacks of T3 Old Gold")
          else:
               st.header(f"You need {int(Old Gold / 64):,d} Stacks and {Old Gold % 64} T3 Old Gold")
elif dim=="Rift":
     block = st.radio(
          "",
          ('Diorite - Coal Mix','Coal - Copper Mix','Copper - Blue Gem Mix','Rift Mix'))
     val = int(st.text_input('How Many Blocks?', 0))
     if block == 'Diorite - Coal Mix':
          a=val*8
          b = int(a / 64)
          c = a % 64
          if ((c % 64)==0):
               st.header(f"You need {b:,d} Stacks of T3 Diorite and Coal")
          else:
               st.header(f"You need {b:,d} stacks and {c} blocks of T3 Diorite and Coal ")
     elif block == "Coal - Copper Mix":
          Coal=val*10
          Copper=val*9
          if ((Coal % 64)==0):
               st.header(f"You need {int(Coal/64):,d} Stacks of T3 Coal")
          else:
               st.header(f"You need {int(Coal / 64):,d} Stacks and {Coal % 64} T3 Prismarine ")
          if ((Copper % 64)==0):
               st.header(f"You need {int(Copper/64):,d} Stacks of T3 Copper")
          else:
               st.header(f"You need {int(Copper / 64):,d} Stacks and {Copper % 64} T3 Copper")           
     elif block == "Copper - Blue Gem Mix":
          Copper=val*13
          Blue Gem=val*13
          if ((Copper % 64)==0):
               st.header(f"You need {int(Copper/64):,d} Stacks of T3 Copper")
          else:
               st.header(f"You need {int(Copper / 64):,d} Stacks and {Copper % 64} T3 Oceanstone ")
          if ((Blue Gem % 64)==0):
               st.header(f"You need {int(Blue Gem/64):,d} Stacks of T3 Blue Gem")
          else:
               st.header(f"You need {int(Blue Gem / 64):,d} Stacks and {Blue Gem % 64} T3 Blue Gem")        
     else:
          Prismarine = val * 70 
          Copper = val * 154 
          Blue Gem = val * 91 
          if ((Prismarine % 64)==0):
               st.header(f"You need {int(Prismarine/64):,d} Stacks of T3 Prismarine")
          else:
               st.header(f"You need {int(Prismarine / 64):,d} Stacks and {Prismarine % 64} T3 Prismarine")
          if ((Copper % 64)==0):
               st.header(f"You need {int(Copper/64):,d} Stacks of T3 Copper")
          else:
               st.header(f"You need {int(Copper / 64):,d} Stacks and {Copper % 64} T3 Copper ")
          if ((Blue Gem % 64)==0):
               st.header(f"You need {int(Blue Gem/64):,d} Stacks of T3 Blue Gem")
          else:
               st.header(f"You need {int(Blue Gem / 64):,d} Stacks and {Blue Gem % 64} T3 Blue Gem ")
elif dim=="Coast":
     block = st.radio(
          "",
          ('Yellow Coral - Pink Coral Mix','Pink Coral - Fire Coral Mix','Fire Coral - Blue Coral Mix','Coast Mix'))
     val = int(st.text_input('How Many Blocks?', 0))
     if block == 'Yellow Coral - Pink Coral Mix':
          a=val*9
          b = int(a / 64)
          c = a % 64
          if ((c % 64)==0):
               st.header(f"You need {b:,d} Stacks of T3 Yellow Coral and Pink Coral")
          else:
               st.header(f"You need {b:,d} stacks and {c} blocks of T3 Yellow Coral and Pink Coral ")
     elif block == "Pink Coral - Fire Coral Mix":
          a = val * 11
          b = int(a / 64)
          c = a % 64
          if ((c % 64)==0):
               st.header(f"You need {b:,d} Stacks of T3 Pink Coral and Fire Coral")
          else:
               st.header(f"You need {b:,d} stacks and {c} blocks of T3 Pink Coral and Fire Coral ")
     elif block == "Fire Coral - Blue Coral Mix":
          Aztec=val*15
          Blue Coral=val*15
          if ((Aztec % 64)==0):
               st.header(f"You need {int(Aztec/64):,d} Stacks of T3 Fire Coral ")
          else:
               st.header(f"You need {int(Aztec / 64):,d} Stacks and {Aztec % 64} T3 Fire Coral  ")
          if ((Blue Coral % 64)==0):
               st.header(f"You need {int(Blue Coral/64):,d} Stacks of T3  Blue Coral")
          else:
               st.header(f"You need {int(Blue Coral / 64):,d} Stacks and {Blue Coral % 64} T3  Blue Coral")
     else:
          Star = val * 77 
          Aztec = val * 168 
          Blue Coral = val * 105 
          if ((Star % 64)==0):
               st.header(f"You need {int(Star/64):,d} Stacks of T3 Pink Coral ")
          else:
               st.header(f"You need {int(Star / 64):,d} Stacks and {Star % 64} T3 Pink Coral ")
          if ((Aztec % 64)==0):
               st.header(f"You need {int(Aztec/64):,d} Stacks of T3  Fire Coral")
          else:
               st.header(f"You need {int(Aztec / 64):,d} Stacks and {Aztec % 64} T3  Fire Coral ")
          if ((Blue Coral % 64)==0):
               st.header(f"You need {int(Blue Coral/64):,d} Stacks of T3 Blue Coral")
          else:
               st.header(f"You need {int(Blue Coral / 64):,d} Stacks and {Blue Coral % 64} T3 Blue Coral ")
elif dim=="Wreck":
     block = st.radio(
          "",
          ('Cobblestone - Iron Mix','Iron - Magma Mix','Magma - Amethyst Mix','Wreck Mix'))
     val = int(st.text_input('How Many Blocks?', 0))
     if block == 'Cobblestone - Iron Mix':
          a=val*10
          b = int(a / 64)
          c = a % 64
          if ((c % 64)==0):
               st.header(f"You need {b:,d} Stacks of T3 Cobblestone and Iron")
          else:
               st.header(f"You need {b:,d} stacks and {c} blocks of T3 Cobblestone and Iron ")
     elif block == "Iron - Magma Mix":
          Iron=val*11
          Magma=val*11
          if ((Iron % 64)==0):
               st.header(f"You need {int(Iron/64):,d} Stacks of T3 Iron")
          else:
               st.header(f"You need {int(Iron / 64):,d} Stacks and {Iron % 64} T3 Iron ")
          if ((Magma % 64)==0):
               st.header(f"You need {int(Magma/64):,d} Stacks of T3 Magma")
          else:
               st.header(f"You need {int(Magma / 64):,d} Stacks and {Magma % 64} T3 Magma")
     elif block == "Magma - Amethyst Mix":
          Iron=val*16
          Magma=val*16
          if ((Iron % 64)==0):
               st.header(f"You need {int(Iron/64):,d} Stacks of T3 Magma")
          else:
               st.header(f"You need {int(Iron / 64):,d} Stacks and {Iron % 64} T3 Magma ")
          if ((Magma % 64)==0):
               st.header(f"You need {int(Magma/64):,d} Stacks of T3 Amethyst")
          else:
               st.header(f"You need {int(Magma / 64):,d} Stacks and {Magma % 64} T3 Amethyst")
     else:
          Amethyst = val * 160 
          Iron = val * 110  
          Magma = val * 270
          if ((Iron % 64)==0):
               st.header(f"You need {int(Iron/64):,d} Stacks of Iron")
          else:
               st.header(f"You need {int(Iron / 64):,d} Stacks and {Iron % 64} T3 Iron")
          if ((Magma % 64)==0):
               st.header(f"You need {int(Magma/64):,d} Stacks of T3 Magma")
          else:
               st.header(f"You need {int(Magma / 64):,d} Stacks and {Magma % 64} T3 Magma ")
          if ((Amethyst % 64)==0):
               st.header(f"You need {int(Amethyst/64):,d} Stacks of T3 Amethyst")
          else:
               st.header(f"You need {int(Amethyst / 64):,d} Stacks and {Amethyst % 64} T3 Amethyst ")
st.caption(f"Any issues message .comradejay on Discord")
st.caption(f"Original creators stresso and illusioner_ on Discord ")
st.caption(f"Special thanks to banishedghost and NyaaaaVie for the math <3.")
st.write(f"Github [link](https://github.com/ComradeJay/s5calc)")
