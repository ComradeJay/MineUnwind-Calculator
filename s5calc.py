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
          Emerald=val*21
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
          bass = val * 7
          db=val*7
          if ((bass % 64)==0):
               st.header(f"You need {int(bass/64):,d} Stacks of T3 Coal")
          else:
               st.header(f"You need {int(bass/64):,d} stacks and {bass%64} blocks of T3 Coal")
          if ((db % 64)==0):
               st.header(f"You need {int(db/64):,d} Stacks of T3 Emerald")
          else:
               st.header(f"You need {int(db/64):,d} stacks and {db%64} blocks of T3 Copper")
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
          db = val * 120
          bass = val * 84
          if ((Coal % 64)==0):
               st.header(f"You need {int(Coal / 64):,d} Stacks of T3 Coal")
          else:
               st.header(f"You need {int(Coal / 64):,d} Stacks and {Coal % 64} T3 Coal")
          if ((db % 64)==0):
               st.header(f"You need {int(db / 64):,d} Stacks of T3 Copper")
          else:
               st.header(f"You need {int(db/64):,d} Stacks and {db%64} T3 Copper")
          if ((bass % 64)==0):
               st.header(f"You need {int(bass / 64):,d} Stacks of T3 Redstone")
          else:
               st.header(f"You need {int(bass / 64):,d} Stacks and {bass % 64} T3 Redstone")
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
          id=val*10
          gd=val*9
          if ((id % 64)==0):
               st.header(f"You need {int(id/64):,d} Stacks of T3 Prismarine")
          else:
               st.header(f"You need {int(id / 64):,d} Stacks and {id % 64} T3 Prismarine ")
          if ((gd % 64)==0):
               st.header(f"You need {int(gd/64):,d} Stacks of T3 Oceanstone")
          else:
               st.header(f"You need {int(gd / 64):,d} Stacks and {gd % 64} T3 Oceanstone")           
     elif block == "Oceanstone - Seashine Mix":
          gd=val*13
          dd=val*13
          if ((gd % 64)==0):
               st.header(f"You need {int(gd/64):,d} Stacks of T3 Oceanstone")
          else:
               st.header(f"You need {int(gd / 64):,d} Stacks and {gd % 64} T3 Oceanstone ")
          if ((dd % 64)==0):
               st.header(f"You need {int(dd/64):,d} Stacks of T3 Seashine")
          else:
               st.header(f"You need {int(dd / 64):,d} Stacks and {dd % 64} T3 Seashine")        
     else:
          id = val * 70 
          gd = val * 154 
          dd = val * 91 
          if ((id % 64)==0):
               st.header(f"You need {int(id/64):,d} Stacks of T3 Prismarine")
          else:
               st.header(f"You need {int(id / 64):,d} Stacks and {id % 64} T3 Prismarine")
          if ((gd % 64)==0):
               st.header(f"You need {int(gd/64):,d} Stacks of T3 Oceanstone")
          else:
               st.header(f"You need {int(gd / 64):,d} Stacks and {gd % 64} T3 Oceanstone ")
          if ((dd % 64)==0):
               st.header(f"You need {int(dd/64):,d} Stacks of T3 Seashine")
          else:
               st.header(f"You need {int(dd / 64):,d} Stacks and {dd % 64} T3 Seashine ")
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
          mr=val*15
          ma=val*15
          if ((mr % 64)==0):
               st.header(f"You need {int(mr/64):,d} Stacks of T3 Aztec Relic ")
          else:
               st.header(f"You need {int(mr / 64):,d} Stacks and {mr % 64} T3 Aztec Relic  ")
          if ((ma % 64)==0):
               st.header(f"You need {int(ma/64):,d} Stacks of T3  Amethyst")
          else:
               st.header(f"You need {int(ma / 64):,d} Stacks and {ma % 64} T3  Amethyst")
     else:
          se = val * 77 
          mr = val * 168 
          ma = val * 105 
          if ((se % 64)==0):
               st.header(f"You need {int(se/64):,d} Stacks of T3 Star Rock ")
          else:
               st.header(f"You need {int(se / 64):,d} Stacks and {se % 64} T3 Star Rock ")
          if ((mr % 64)==0):
               st.header(f"You need {int(mr/64):,d} Stacks of T3  Aztec Relic")
          else:
               st.header(f"You need {int(mr / 64):,d} Stacks and {mr % 64} T3  Aztec Relic ")
          if ((ma % 64)==0):
               st.header(f"You need {int(ma/64):,d} Stacks of T3 Amethyst")
          else:
               st.header(f"You need {int(ma / 64):,d} Stacks and {ma % 64} T3 Amethyst ")
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
          nec=val*11
          fr=val*11
          if ((nec % 64)==0):
               st.header(f"You need {int(nec/64):,d} Stacks of T3 Purpur")
          else:
               st.header(f"You need {int(nec / 64):,d} Stacks and {nec % 64} T3 Purpur ")
          if ((fr % 64)==0):
               st.header(f"You need {int(fr/64):,d} Stacks of T3 Magma")
          else:
               st.header(f"You need {int(fr / 64):,d} Stacks and {fr % 64} T3 Magma")
     elif block == "Magma - Obsidian Mix":
          nec=val*16
          fr=val*16
          if ((nec % 64)==0):
               st.header(f"You need {int(nec/64):,d} Stacks of T3 Magma")
          else:
               st.header(f"You need {int(nec / 64):,d} Stacks and {nec % 64} T3 Magma ")
          if ((fr % 64)==0):
               st.header(f"You need {int(fr/64):,d} Stacks of T3 Obsidian")
          else:
               st.header(f"You need {int(fr / 64):,d} Stacks and {fr % 64} T3 Obsidian")
     else:
          cr = val * 110 
          nec = val * 270  
          fr = val * 160
          if ((cr % 64)==0):
               st.header(f"You need {int(cr/64):,d} Stacks of Purpur")
          else:
               st.header(f"You need {int(cr / 64):,d} Stacks and {cr % 64} T3 Purpur")
          if ((nec % 64)==0):
               st.header(f"You need {int(nec/64):,d} Stacks of T3 Magma")
          else:
               st.header(f"You need {int(nec / 64):,d} Stacks and {nec % 64} T3 Magma ")
          if ((fr % 64)==0):
               st.header(f"You need {int(fr/64):,d} Stacks of T3 Obsidian")
          else:
               st.header(f"You need {int(fr / 64):,d} Stacks and {fr % 64} T3 Obsidian ")
st.caption(f"Any issues message .comradejay on Discord")
st.caption(f"Original creators stresso and illusioner_ on Discord ")
st.caption(f"Special thanks to banishedghost and NyaaaaVie for the math <3.")
