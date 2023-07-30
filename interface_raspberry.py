#! /usr/bin env python3

from tkinter import *
from tkinter import ttk
from modules.database import *
import modules.firebase as firebase
import time
import re
# Funciones

window = Tk()
window.title("Gestión de nodos sensores")
window.geometry("1040x650")

frame=LabelFrame(window, text="Gestión de nodos sensores", padx=20, pady=20)
frame.place(x=10,y=10,width=1020,height=330)
frame_variables=LabelFrame(window, text="Gestión de umbrales y periodos de muestreo", padx=20, pady=20)
frame_variables.place(x=10,y=350,width=1020,height=290)

#Variables
id_node = IntVar()
mac_node = StringVar()
status_node = StringVar()
latitude_node = DoubleVar()
longitude_node = DoubleVar()
variable = StringVar()
threshold = DoubleVar()
interval = IntVar()
unity_interval = StringVar()

# Inputs
text_id_nodo = Label(frame, text="ID:").grid(row=0, column=0)
input_id_nodo = ttk.Combobox(frame, values=[0], textvariable=id_node, state="readonly", width=4)
input_id_nodo.grid(row=0, column=1)
input_id_nodo.current(0)

text_mac_nodo = Label(frame, text="Direción MAC:").grid(row=0, column=2, padx=1)
input_mac_nodo = Entry(frame, textvariable=mac_node)
input_mac_nodo.grid(row=0, column=3)

text_status_node = Label(frame, text="Estado:").grid(row=0, column=4)
input_status_node = ttk.Combobox(frame, values=["Activo", "Inactivo"], textvariable=status_node, state='readonly', width=8)
input_status_node.grid(row=0, column=5)
input_status_node.current(0)

text_latitude_node = Label(frame, text="Latitud:").grid(row=0, column=6)
input_latitude_node = Entry(frame, textvariable=latitude_node, width=16)
input_latitude_node.grid(row=0, column=7)

text_longitude_node = Label(frame, text="Longitud:").grid(row=0, column=8)
input_longitude_node = Entry(frame, textvariable=longitude_node, width=16)
input_longitude_node.grid(row=0, column=9)

text_threshold = Label(frame_variables, text="Umbral de alerta:").grid(row=0, column=0, padx=1)
input_threshold = Entry(frame_variables, textvariable=threshold)
input_threshold.grid(row=0, column=1)

text_interval = Label(frame_variables, text="Periodo de muestreo:").grid(row=0, column=2, padx=1)
input_interval = Entry(frame_variables, textvariable=interval)
input_interval.grid(row=0, column=3)

input_interval_unity = ttk.Combobox(frame_variables, values=["Minutos", "Horas"], textvariable=unity_interval, state='readonly', width=8)
input_interval_unity.grid(row=0, column=4, padx=1)
input_interval_unity.current(0)

mensage = Label(frame, text=" ", fg="green")
mensage.grid(row=1, column=0, columnspan=10, pady=5)

mensage_variables = Label(frame_variables, text=" ", fg="green")
mensage_variables.grid(row=1, column=0, columnspan=2, pady=5)

mensage_intervals = Label(frame_variables, text=" ", fg="green")
mensage_intervals.grid(row=1, column=2, columnspan=3, pady=5)

# Función del evento
def select_node(event):
    try:
        mensage["text"] = ''
        selected_item = main_table.focus()
        if selected_item:
            id = main_table.selection()[0]
            id_node.set(main_table.item(id, "values")[0])
            mac_node.set(main_table.item(id, "values")[1])
            status_node.set(main_table.item(id, "values")[2])
            latitude_node.set(main_table.item(id, "values")[3])
            longitude_node.set(main_table.item(id, "values")[4])
    except Exception as e:
        print(str(e))

def select_variable(event):
    try:
        mensage["text"] = ''
        selected_item = table_variables.focus()
        if selected_item:
            id = table_variables.selection()[0]
            threshold.set(table_variables.item(id, "values")[1])
    except Exception as e:
        print(str(e))

def select_interval(event):
    try:
        mensage["text"] = ''
        selected_item = table_intervals.focus()
        if selected_item:
            id = table_intervals.selection()[0]
            interval.set(table_intervals.item(id, "values")[0])
    except Exception as e:
        print(str(e))

# Table nodes
main_table = ttk.Treeview(frame,height=7)
main_table.grid(row=2, column=0, columnspan=10, pady=10)
main_table['columns'] = ("ID", "Dirección MAC", "Estado", "Latitud", "Longitud", "ID firebase")
main_table.column("#0", width=0, stretch=NO)
main_table.column("ID", anchor=CENTER, width=60)
main_table.column("Dirección MAC", anchor=CENTER, width=210)
main_table.column("Estado", anchor=CENTER, width=210)
main_table.column("Latitud", anchor=CENTER, width=210)
main_table.column("Longitud", anchor=CENTER, width=210)
main_table.column("ID firebase", width=0, stretch=NO)
#Encabezados nodes
main_table.heading("#0", text="", anchor=CENTER)
main_table.heading("ID", text="ID", anchor=CENTER)
main_table.heading("Dirección MAC", text="Dirección MAC", anchor=CENTER)
main_table.heading("Estado", text="Estado", anchor=CENTER)
main_table.heading("Latitud", text="Latitud", anchor=CENTER)
main_table.heading("Longitud", text="Longitud", anchor=CENTER)
main_table.heading("ID firebase", text="ID firebase", anchor=CENTER)
main_table.bind("<<TreeviewSelect>>", select_node)

# Table variables
table_variables = ttk.Treeview(frame_variables, height=5)
table_variables.grid(row=2, column=0, columnspan=2, pady=10)
table_variables['columns'] = ("Variable", "Umbral de alerta", "Unidad", "Name Firebase")
table_variables.column("#0", width=0, stretch=NO)
table_variables.column("Variable", anchor=CENTER, width=140)
table_variables.column("Umbral de alerta", anchor=CENTER, width=140)
table_variables.column("Unidad", anchor=CENTER, width=120)
table_variables.column("Name Firebase", width=0, stretch=NO)
#Encabezados variables
table_variables.heading("#0", text="", anchor=CENTER)
table_variables.heading("Variable", text="Variable", anchor=CENTER)
table_variables.heading("Umbral de alerta", text="Umbral de alerta", anchor=CENTER)
table_variables.heading("Unidad", text="Unidad", anchor=CENTER)
table_variables.heading("Name Firebase", text="Name Firebase", anchor=CENTER)
table_variables.bind("<<TreeviewSelect>>", select_variable)

# Table intervarls
table_intervals = ttk.Treeview(frame_variables, height=1)
table_intervals.grid(row=2, column=2, columnspan=3, pady=10)
table_intervals['columns'] = ("Periodo de muestreo", "Unidad")
table_intervals.column("#0", width=0, stretch=NO)
table_intervals.column("Periodo de muestreo", anchor=CENTER, width=170)
table_intervals.column("Unidad", anchor=CENTER, width=120)
#Encabezados intervals
table_intervals.heading("#0", text="", anchor=CENTER)
table_intervals.heading("Periodo de muestreo", text="Periodo de muestreo", anchor=CENTER)
table_intervals.heading("Unidad", text="Unidad", anchor=CENTER)
table_intervals.bind("<<TreeviewSelect>>", select_interval)

# Buttons
button_add = Button(frame, text="Añadir nodo", command=lambda: add_node())
button_add.grid(row=3, column=1, columnspan=1, pady=10)

button_delete = Button(frame, text="Eliminar nodo", command=lambda: delete_node())
button_delete.grid(row=3, column=3, columnspan=1, pady=10)

button_update = Button(frame, text="Actualizar nodo", command=lambda: update_node())
button_update.grid(row=3, column=5, columnspan=1, pady=10)

button_refresh = Button(frame, text="Refrescar", command=lambda: refresh_table())
button_refresh.grid(row=3, column=7, columnspan=1, pady=10)

button_update_variable = Button(frame_variables, text="Actualizar umbral", command=lambda: update_umbral())
button_update_variable.grid(row=3, column=0, pady=10)

button_refresh_variable = Button(frame_variables, text="Refrescar", command=lambda: refresh_umbral())
button_refresh_variable.grid(row=3, column=1, pady=10)

button_update_interval = Button(frame_variables, text="Actualizar periodo", command=lambda: update_interval())
button_update_interval.grid(row=3, column=2, pady=10)

button_refresh_interval = Button(frame_variables, text="Refrescar", command=lambda: refresh_interval())
button_refresh_interval.grid(row=3, column=4, pady=10)

# Functions
def clear_table():
    try:
        for row in main_table.get_children():
            main_table.delete(row)
    except Exception as e:
        print(str(e))

def clear_table_variables():
    try:
        for row in table_variables.get_children():
            table_variables.delete(row)
    except Exception as e:
        print(str(e))

def clear_table_intervals():
    try:
        for row in table_intervals.get_children():
            table_intervals.delete(row)
    except Exception as e:
        print(str(e))

def clear_inputs():
    id_node.set(0)
    mac_node.set("")
    status_node.set("Activo")
    latitude_node.set(0)
    longitude_node.set(0)
    threshold.set(0)
    interval.set(0)
    unity_interval.set("Minutos")

def validation_inputs(state_inputs):
    message_errors = {
        "id": "El id del nodo debe ser diferente de 0 o ya está en uso",
        "mac": "La dirección MAC no es válida o ya está en uso",
        "latitude": "La latitud debe ser diferente de 0",
        "longitude": "La longitud debe ser diferente de 0"
    }
    for key, value in state_inputs.items():
        if not value:
            return [False, message_errors[key]]
    return [True, ""]

def get_node():
    clear_table()
    database  = Database()
    nodes = database.get_local_nodes()
    ids = database.get_all_id()
    database.close()
    used_ids=[]
    rest_ids=[]
    for id in ids:
        used_ids.append(id[0])
    for i in range(1, 101):
        if i not in used_ids:
            rest_ids.append(i)
    input_id_nodo['values'] = rest_ids
    for node in nodes:
        if node[2] == 1:
            status = "Activo"
        else:
            status = "Inactivo"
        main_table.insert("", END, values=(node[1], node[0], status, node[3], node[4], node[5]))
    button_refresh['bg'] = '#f0f0f0'

def get_variables():
    clear_table_variables()
    database  = Database()
    variables = database.get_local_variables()
    database.close()
    name_of_variables = {
        "temp" : "Temperatura",
        "ha" : "Humedad ambiente",
        "hs" : "Humedad suelo",
        "rad": "Radiación solar",
        "co2": "Dioxio de carbono" 
    }
    unity_of_variables = {
        "temp" : "°C",
        "ha" : "%",
        "hs" : "%",
        "rad": "\u03BCmol/s\u00B7m\u00B2",
        "co2": "ppm"
    }
    for variable in variables:
        table_variables.insert("", END, values=(name_of_variables[variable[0]], variable[1], unity_of_variables[variable[0]], variable[0]))
    button_refresh['bg'] = '#f0f0f0'

def get_intervals():
    clear_table_intervals()
    database  = Database()
    interval = database.get_local_intervals()
    database.close()
    table_intervals.insert("", END, values=(interval, "Minutos"))
    button_refresh['bg'] = '#f0f0f0'

def refresh_table():
    get_node()
    clear_inputs()
    mensage["text"] = ''

def refresh_umbral():
    get_variables()
    clear_inputs()
    mensage_variables["text"] = ''

def refresh_interval():
    get_intervals()
    clear_inputs()
    mensage_intervals["text"] = ''

def validation_procces(proccess):
    database  = Database()
    macs_tuple = database.get_all_macs()
    ids_tuple = database.get_all_id()
    database.close()
    macs = []
    ids = []
    for mac in macs_tuple:
        macs.append(mac[0].lower())
    for id in ids_tuple:
        ids.append(id[0])
    if proccess == "ADD":
        validators= {
            "id" : id_node.get() != 0 and id_node.get() not in ids,
            "mac" : False if re.match("^([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})$", mac_node.get().lower()) == None or mac_node.get().lower() in macs else True,
            "latitude" : latitude_node.get() != 0,
            "longitude" : longitude_node.get() != 0
        }
        return validation_inputs(validators)
    elif proccess == "UPDATE":
        validators= {
            "id" : id_node.get() != 0,
            "mac" : False if re.match("^([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})$", mac_node.get().lower()) == None else True,
            "latitude" : latitude_node.get() != 0,
            "longitude" : longitude_node.get() != 0
        }
        return validation_inputs(validators)

def add_node():
    validation = validation_procces("ADD")
    if validation[0]:
        data_to_firebase = {
            "mac": mac_node.get().lower(),
            "nodeStatus": True if status_node.get() == "Activo" else False,
            "latitude": latitude_node.get(),
            "longitude": longitude_node.get(),
            "nodeId": id_node.get()
        }
        status = firebase.add_new_node(data_to_firebase)
        if status:
            mensage["text"] = "Se ha agegado el nodo correctamente"
            mensage["fg"] = "green"
            time.sleep(2)
            clear_inputs()
            button_refresh['bg'] = 'yellow'
            get_node()
        else:
            mensage["text"] = "Ha ocurrido un error al agregar el nodo, intente de nuevo"
            mensage["fg"] = "red"
    else:
        mensage["text"] = validation[1]
        mensage["fg"] = "red"

def delete_node():
    try:
        selected_item = main_table.focus()
        if selected_item:
            id = main_table.item(main_table.focus())['values'][5]
            status = firebase.delete_node(id)
            if status:
                mensage["text"] = "Se ha eliminado el nodo correctamente"
                mensage["fg"] = "green"
                clear_inputs()
                time.sleep(2)
                button_refresh['bg'] = 'yellow'
                get_node()
            else:
                mensage["text"] = "Ha ocurrido un error al eliminar el nodo, intente de nuevo"
                mensage["fg"] = "red"
        else:
            mensage["text"] = "Seleccione un nodo para eliminar!!"
            mensage["fg"] = "red"
    except Exception as e:
        print(str(e))

def update_node():
    try:
        selected_item = main_table.focus()
        if selected_item:
            id = main_table.item(main_table.focus())['values'][5]
            database  = Database()
            previous_data_tuple = database.get_local_node(id)
            database.close()
            previous_data = {
                "mac": previous_data_tuple[0].lower(),
                "nodeId": previous_data_tuple[1],
                "nodeStatus": True if previous_data_tuple[2] == 1 else False,
                "latitude": previous_data_tuple[3],
                "longitude": previous_data_tuple[4],
            }
            data_to_firebase = {
                "mac": mac_node.get().lower(),
                "nodeStatus": True if status_node.get() == "Activo" else False,
                "latitude": latitude_node.get(),
                "longitude": longitude_node.get(),
                "nodeId": id_node.get()
            }
            if previous_data != data_to_firebase:
                validation = validation_procces("UPDATE")
                if validation[0]:
                    status = firebase.update_node(id, data_to_firebase)
                    if status:
                        mensage["text"] = "Se ha actualizado el nodo correctamente"
                        mensage["fg"] = "green"
                        time.sleep(2)
                        clear_inputs()
                        button_refresh['bg'] = 'yellow'
                        get_node()
                    else:
                        mensage["text"] = "Ha ocurrido un error al actualizar el nodo, intente de nuevo"
                        mensage["fg"] = "red"
                else:
                    mensage["text"] = validation[1]
                    mensage["fg"] = "red"
            else:
                mensage["text"] = "Modifica al menos un campo"
                mensage["fg"] = "red"
        else:
            mensage["text"] = "Seleccione un nodo para actualizar!!"
            mensage["fg"] = "red"
    except Exception as e:
        print(str(e))

def update_umbral():
    try:
        selected_item = table_variables.focus()
        if selected_item:
            variable = table_variables.item(table_variables.focus())['values'][3]
            database  = Database()
            previous_data_tuple = database.get_local_thresholds(variable)
            database.close()
            name_of_variables_firebase = {
                "temp" : "Temperatura",
                "ha" : "Humedad",
                "hs" : "HumedadS",
                "rad": "Rad",
                "co2": "CO2" 
            }
            previous_data = {
                name_of_variables_firebase[variable]: previous_data_tuple[1]
            }
            data_to_firebase = {
                name_of_variables_firebase[variable]: threshold.get()
            }
            if previous_data != data_to_firebase:
                status = firebase.update_thresholds(data_to_firebase)
                if status:
                    mensage_variables["text"] = "Se ha actualizado el umbral de alerta correctamente"
                    mensage_variables["fg"] = "green"
                    time.sleep(2)
                    clear_inputs()
                    button_refresh['bg'] = 'yellow'
                    get_variables()
                else:
                    mensage_variables["text"] = "Ha ocurrido un error al actualizar el umbral, intente de nuevo"
                    mensage_variables["fg"] = "red"
            else:
                mensage_variables["text"] = "Modifica el umbral de alerta"
                mensage_variables["fg"] = "red"
        else:
            mensage_variables["text"] = "Seleccione una variable para actualizar su umbral!!"
            mensage_variables["fg"] = "red"
    except Exception as e:
        print(str(e))

def update_interval():
    try:
        database  = Database()
        previous_data_tuple = database.get_local_intervals()
        database.close()
        previous_data = {
            "minutes": previous_data_tuple
        }
        data_to_firebase = {
            "minutes": interval.get() if unity_interval.get() == "Minutos" else interval.get()*60
        }
        if previous_data != data_to_firebase:
            status = firebase.update_interval(data_to_firebase)
            if status:
                mensage_intervals["text"] = "Se ha actualizado el periodo de muestreo correctamente"
                mensage_intervals["fg"] = "green"
                time.sleep(2)
                clear_inputs()
                button_refresh['bg'] = 'yellow'
                get_intervals()
            else:
                mensage_intervals["text"] = "Ha ocurrido un error al actualizar el periodo de muestreo, intente de nuevo"
                mensage_intervals["fg"] = "red"
        else:
            mensage_intervals["text"] = "Modifica el periodo de muestreo"
            mensage_intervals["fg"] = "red"
    except Exception as e:
        print(str(e))


try:
    firebase.init_firebase()
    get_node()
    get_variables()
    get_intervals()
    window.mainloop()
except KeyboardInterrupt:
    print("\nSaliendo...\n")
print("\nSaliendo...\n")