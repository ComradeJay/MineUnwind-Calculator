import streamlit as st

st.set_page_config(page_title="Mineunwind Calculator")
st.subheader("Which Realm:")
dim = st.radio("",('River', 'Outpost', 'Kaeva','Inferno','Elysium'))
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
          a = val*2
          b = int(a/64)
          c = a%64
          if ((c % 64)==0):
               st.header(f"You need {b:,d} Stacks of T3 Iron and Diamond")
          else:
               st.header(f"You need {b:,d} stacks and {c} blocks of T3 Iron and Diamond")
     elif block=="Diamond - Emerald Mix":
          a=val*5
          b=int(a/64)
          c=a%64
          if ((c % 64)==0):
               st.header(f"You need {b:,d} Stacks of T3 Diamond and Emerald")
          else:
               st.header(f"You need {b:,d} stacks and {c} blocks of T3 Diamond and Emerald ")
     else:
          gra=val*21
          Emerald=val*15
          nano=val*6
          if ((nano % 64)==0):
               st.header(f"You need {int(nano / 64):,d} Stacks of T3 Iron")
          else:
               st.header(f"You need {int(nano / 64):,d} Stacks and {nano % 64} T3 Iron")
          if ((gra % 64)==0):
               st.header(f"You need {int(gra / 64):,d} Stacks of T3 Diamond")
          else:
               st.header(f"You need {int(gra/64):,d} Stacks and {gra%64} T3 Diamond")
          if ((Emerald % 64)==0):
               st.header(f"You need {int(Emerald / 64):,d} Stacks of T3 Emerald")
          else:
               st.header(f"You need {int(Emerald / 64):,d} Stacks and {Emerald % 64} T3 Emerald")
elif dim=="Outpost":
     block = st.radio(
          "",
          ('Brick - Tuff Mix','Tuff - Brain Coral Mix','Brain Coral - Basalt Mix','Outpost Mix'))
     val = int(st.text_input('How Many Blocks?', 0))
     if block == 'Brick - Tuff Mix':
          a=val*4
          b = int(a / 64)
          c = a % 64
          if ((c % 64)==0):
               st.header(f"You need {b:,d} Stacks of T3 Brick and Tuff")
          else:
               st.header(f"You need {b:,d} stacks and {c} blocks of T3 Brick and Tuff ")
     elif block == "Tuff - Brain Coral Mix":
          bass = val * 7
          db=val*7
          if ((bass % 64)==0):
               st.header(f"You need {int(bass/64):,d} Stacks of T3 Tuff")
          else:
               st.header(f"You need {int(bass/64):,d} stacks and {bass%64} blocks of T3 Tuff")
          if ((db % 64)==0):
               st.header(f"You need {int(db/64):,d} Stacks of T3 Emerald")
          else:
               st.header(f"You need {int(db/64):,d} stacks and {db%64} blocks of T3 Brain Coral")
     elif block == "Brain Coral - Basalt Mix":
          a = val * 12
          b = int(a / 64)
          c = a % 64
          if ((c % 64)==0):
               st.header(f"You need {b:,d} Stacks of T3 Brain Coral and Basalt")
          else:
               st.header(f"You need {b:,d} stacks and {c} blocks of T3 Brain Coral and Basalt ")
     else:
          tuff = val * 42
          db = val * 120
          bass = val * 84
          if ((tuff % 64)==0):
               st.header(f"You need {int(tuff / 64):,d} Stacks of T3 Tuff")
          else:
               st.header(f"You need {int(tuff / 64):,d} Stacks and {tuff % 64} T3 Tuff")
          if ((db % 64)==0):
               st.header(f"You need {int(db / 64):,d} Stacks of T3 Brain Coral")
          else:
               st.header(f"You need {int(db/64):,d} Stacks and {db%64} T3 Brain Coral")
          if ((bass % 64)==0):
               st.header(f"You need {int(bass / 64):,d} Stacks of T3 Basalt")
          else:
               st.header(f"You need {int(bass / 64):,d} Stacks and {bass % 64} T3 Basalt")
elif dim=="Kaeva":
     block = st.radio(
          "",
          ('Mossy Cobblestone - Iron Deposit Mix','Iron Deposit - Emerald Deposit Mix','Emerald Deposit - Diamond Deposit Mix','Kaeva Mix'))
     val = int(st.text_input('How Many Blocks?', 0))
     if block == 'Mossy Cobblestone - Iron Deposit Mix':
          a=val*8
          b = int(a / 64)
          c = a % 64
          if ((c % 64)==0):
               st.header(f"You need {b:,d} Stacks of T3 Mossy Cobblestone and Iron Deposit")
          else:
               st.header(f"You need {b:,d} stacks and {c} blocks of T3 Mossy Cobblestone and Iron Deposit ")
     elif block == "Iron Deposit - Emerald Deposit Mix":
          id=val*10
          gd=val*9
          if ((id % 64)==0):
               st.header(f"You need {int(id/64):,d} Stacks of T3 Iron Deposit")
          else:
               st.header(f"You need {int(id / 64):,d} Stacks and {id % 64} T3 Iron Deposit ")
          if ((gd % 64)==0):
               st.header(f"You need {int(gd/64):,d} Stacks of T3 Emerald Deposit")
          else:
               st.header(f"You need {int(gd / 64):,d} Stacks and {gd % 64} T3 Emerald Deposit")           
     elif block == "Emerald Deposit - Diamond Deposit Mix":
          gd=val*13
          dd=val*13
          if ((gd % 64)==0):
               st.header(f"You need {int(gd/64):,d} Stacks of T3 Emerald Deposit")
          else:
               st.header(f"You need {int(gd / 64):,d} Stacks and {gd % 64} T3 Emerald Deposit ")
          if ((dd % 64)==0):
               st.header(f"You need {int(dd/64):,d} Stacks of T3 Diamond Deposit")
          else:
               st.header(f"You need {int(dd / 64):,d} Stacks and {dd % 64} T3 Diamond Deposit")        
     else:
          id = val * 70 
          gd = val * 154 
          dd = val * 91 
          if ((id % 64)==0):
               st.header(f"You need {int(id/64):,d} Stacks of T3 Iron Deposit")
          else:
               st.header(f"You need {int(id / 64):,d} Stacks and {id % 64} T3 Iron Deposit")
          if ((gd % 64)==0):
               st.header(f"You need {int(gd/64):,d} Stacks of T3 Emerald Deposit")
          else:
               st.header(f"You need {int(gd / 64):,d} Stacks and {gd % 64} T3 Emerald Deposit ")
          if ((dd % 64)==0):
               st.header(f"You need {int(dd/64):,d} Stacks of T3 Diamond Deposit")
          else:
               st.header(f"You need {int(dd / 64):,d} Stacks and {dd % 64} T3 Diamond Deposit ")
elif dim=="Inferno":
     block = st.radio(
          "",
          ('Scorched Earth - Vaporized Fauna Mix','Vaporized Fauna - Magma Mix','Magma - Molten Rock Mix','Inferno Mix'))
     val = int(st.text_input('How Many Blocks?', 0))
     if block == 'Scorched Earth - Vaporized Fauna Mix':
          a=val*9
          b = int(a / 64)
          c = a % 64
          if ((c % 64)==0):
               st.header(f"You need {b:,d} Stacks of T3 Scorched Earth and Vaporized Fauna")
          else:
               st.header(f"You need {b:,d} stacks and {c} blocks of T3 Scorched Earth and Vaporized Fauna ")
     elif block == "Vaporized Fauna - Magma Mix":
          a = val * 11
          b = int(a / 64)
          c = a % 64
          if ((c % 64)==0):
               st.header(f"You need {b:,d} Stacks of T3 Vaporized Fauna and Magma")
          else:
               st.header(f"You need {b:,d} stacks and {c} blocks of T3 Vaporized Fauna and Magma ")
     elif block == "Magma - Molten Rock Mix":
          mr=val*15
          ma=val*15
          if ((mr % 64)==0):
               st.header(f"You need {int(mr/64):,d} Stacks of T3 Magma ")
          else:
               st.header(f"You need {int(mr / 64):,d} Stacks and {mr % 64} T3 Magma  ")
          if ((ma % 64)==0):
               st.header(f"You need {int(ma/64):,d} Stacks of T3  Molten Rock")
          else:
               st.header(f"You need {int(ma / 64):,d} Stacks and {ma % 64} T3  Molten Rock")
     else:
          se = val * 77 
          mr = val * 168 
          ma = val * 105 
          if ((se % 64)==0):
               st.header(f"You need {int(se/64):,d} Stacks of T3 Vaporized Fauna ")
          else:
               st.header(f"You need {int(se / 64):,d} Stacks and {se % 64} T3 Vaporized Fauna ")
          if ((mr % 64)==0):
               st.header(f"You need {int(mr/64):,d} Stacks of T3  Magma")
          else:
               st.header(f"You need {int(mr / 64):,d} Stacks and {mr % 64} T3  Magma ")
          if ((ma % 64)==0):
               st.header(f"You need {int(ma/64):,d} Stacks of T3 Molten Rock")
          else:
               st.header(f"You need {int(ma / 64):,d} Stacks and {ma % 64} T3 Molten Rock ")
elif dim=="Elysium":
     block = st.radio(
          "",
          ('Terrain - Crust Mix','Crust - Nectar Mix','Nectar - Fruit Mix','Elysium Mix'))
     val = int(st.text_input('How Many Blocks?', 0))
     if block == 'Terrain - Crust Mix':
          a=val*10
          b = int(a / 64)
          c = a % 64
          if ((c % 64)==0):
               st.header(f"You need {b:,d} Stacks of T3 Terrain and Crust")
          else:
               st.header(f"You need {b:,d} stacks and {c} blocks of T3 Terrain and Crust ")
     elif block == "Crust - Nectar Mix":
          nec=val*11
          fr=val*11
          if ((nec % 64)==0):
               st.header(f"You need {int(nec/64):,d} Stacks of T3 Crust")
          else:
               st.header(f"You need {int(nec / 64):,d} Stacks and {nec % 64} T3 Crust ")
          if ((fr % 64)==0):
               st.header(f"You need {int(fr/64):,d} Stacks of T3 Nectar")
          else:
               st.header(f"You need {int(fr / 64):,d} Stacks and {fr % 64} T3 Nectar")
     elif block == "Nectar - Fruit Mix":
          nec=val*16
          fr=val*16
          if ((nec % 64)==0):
               st.header(f"You need {int(nec/64):,d} Stacks of T3 Nectar")
          else:
               st.header(f"You need {int(nec / 64):,d} Stacks and {nec % 64} T3 Nectar ")
          if ((fr % 64)==0):
               st.header(f"You need {int(fr/64):,d} Stacks of T3 Fruit")
          else:
               st.header(f"You need {int(fr / 64):,d} Stacks and {fr % 64} T3 Fruit")
     else:
          cr = val * 110 
          nec = val * 270  
          fr = val * 160
          if ((cr % 64)==0):
               st.header(f"You need {int(cr/64):,d} Stacks of Crust")
          else:
               st.header(f"You need {int(cr / 64):,d} Stacks and {cr % 64} T3 Crust")
          if ((nec % 64)==0):
               st.header(f"You need {int(nec/64):,d} Stacks of T3 Nectar")
          else:
               st.header(f"You need {int(nec / 64):,d} Stacks and {nec % 64} T3 Nectar ")
          if ((fr % 64)==0):
               st.header(f"You need {int(fr/64):,d} Stacks of T3 Fruit")
          else:
               st.header(f"You need {int(fr / 64):,d} Stacks and {fr % 64} T3 Fruit ")
st.caption(f"Any issues message .comradejay on Discord")
st.caption(f"Original creators stresso and illusioner_ on Discord ")
st.caption(f"Special thanks to banishedghost and NyaaaaVie for the math <3.")
