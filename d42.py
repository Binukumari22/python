web_dev = ["Ami","Balu","Sree"]
Data_science = ["Rani","Manu","Anjana"]
UI_design = ["Keerthi","rakhi","roshan"]
all_participants = [web_dev,Data_science,UI_design]
print(all_participants)
web_dev.append("Mithra")
print(web_dev)
Data_science.insert(1,"Devika")
print(Data_science)
UI_design.pop()
print(UI_design)
new_DS = Data_science.copy()
Data_science.clear()
print(new_DS)
x = web_dev[:2]
print(x)
name_len = [len(x) for x in new_DS]
print(name_len)
print(("Asha" in web_dev) or("Asha" in new_DS) or("Asha" in UI_design))
first_participants = (web_dev[0],new_DS[0],UI_design[0])
print(first_participants)