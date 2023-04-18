import gooeypie as gp
from math import ceil, floor


app = gp.GooeyPieApp('Cálculo de Tasas')


tasa_regular = gp.Label(app, "Cual es la Tasa Regular? ")
tasa_regular_inp = gp.Input(app)


super_tasa =  gp.Label(app, "Cual es la Super Tasa? ")
super_tasa_inp = gp.Input(app)


remesa_dol = gp.Label(app, "Cual es la Remesa en Dolares? ")
remesa_dol_inp = gp.Input(app)


remesa_pesos = gp.Label(app, "O Cual es la Remesa en Pesos? ")
remesa_pesos_inp = gp.Input(app)

pago_total = gp.Label(app, "O Cual es el Pago Total que \n          Desea el Cliente? ")
pago_total_inp = gp.Input(app)

ajuste_lbl = gp.Label(app, "Ajuste de Tarifa:")
ajuste_inp = gp.Input(app)


tr = gp.Checkbox(app, "Tasa Regular")
st = gp.Checkbox(app, "Super Tasa")
td = gp.Checkbox(app, "Tasa del Dólar")

submit_btn = gp.Button(app, "Ingresar", None)
submit_btn.width = 10
clear_rmt_btn = gp.Button(app, "Limpiar Remesa", None)
clear_all_btn = gp.Button(app, "Limpiar Todo", None)
result_lbl =gp.Label(app,"Resultado: ")
result_txt_box = gp.Textbox(app)

class Store_val:
    def __init__(self, val):
        self.val = val

def just_one_checked_box(event):
    if tr.checked:
        st.disabled = True
        td.disabled = True
    
    elif st.checked:
        tr.disabled = True
        td.disabled = True
    
    elif td.checked:
        tr.disabled = True
        st.disabled = True

    else:
        tr.disabled = False
        st.disabled = False
        td.disabled = False
    

def round_up(val, mult=False):
    total = val * 100
    total = ceil(total)
    total = total / 100
    if mult:
        return(round_up(total * 1.05)) #recursive call
    return total

def round_down(val):
    total = val * 100
    total = floor(total)
    total = total / 100
    return total

def format_output(total):
    return f"{total:,.2f}"

def print_error():
    result_txt_box.clear()
    result_txt_box.append("HUBO UN ERROR EN LOS DATOS DE ENTRADA. ASEGÚRESE DE INGRESARLOS CORRECTAMENTE.")

def tasa_calc(event):
    tasa_regular_val = Store_val(tasa_regular_inp.text)
    super_tasa_val = Store_val(super_tasa_inp.text)
    remesa_dol_val = Store_val(remesa_dol_inp.text)
    remesa_pesos_val = Store_val(remesa_pesos_inp.text)
    pago_total_val = Store_val(pago_total_inp.text)
    ajuste_val = Store_val(ajuste_inp.text)
    if ajuste_val.val == "": 
        ajuste_val.val = "0"
        ajuste_inp.text = "0"
    
    inps = [super_tasa_val, tasa_regular_val, remesa_dol_val, remesa_pesos_val, pago_total_val, ajuste_val]
    for element in inps:
        element.val = element.val.replace(',','')
        if element.val:
            if element.val.replace('.','').isnumeric():
                element.val = float(element.val)
            else:
                print_error()
                return

    
    result_txt_box.clear()
    if tr.checked and tasa_regular_inp.text != "":
        if  remesa_dol_inp.text != "" and remesa_pesos_inp.text == "" and pago_total_inp.text == "":
            result_txt_box.append("Monto: USD$ " + format_output(remesa_dol_val.val) + "\n")
            product = tasa_regular_val.val * remesa_dol_val.val
            result_txt_box.append("Total Para Recibir: RD$ " + format_output(product) + "\n")
            if remesa_dol_val.val < 500:
                result_txt_box.append("Pago Total: USD$ " + format_output(remesa_dol_val.val + 2 + ajuste_val.val))
            elif remesa_dol_val.val < 1000:
                result_txt_box.append("Pago Total: USD$ " + format_output(remesa_dol_val.val + 5 + ajuste_val.val))
            else:
                result_txt_box.append("Pago Total: USD$ " + format_output(remesa_dol_val.val + 10 + ajuste_val.val))

        elif remesa_dol_inp.text == "" and remesa_pesos_inp.text != "" and pago_total_inp.text == "":
            quotient = remesa_pesos_val.val / tasa_regular_val.val
            quotient = round_up(quotient)
            enhanced_accuracy_val_pesos = quotient * tasa_regular_val.val
            result_txt_box.append("Monto: USD$ " + format_output(quotient) + "\n")
            result_txt_box.append("Total Para Recibir: RD$ " + format_output(enhanced_accuracy_val_pesos) + "\n")
            if quotient < 500:
                result_txt_box.append("Pago Total: USD$ " + format_output(quotient + 2 + ajuste_val.val))
            elif quotient < 1000:
                result_txt_box.append("Pago Total: USD$ " + format_output(quotient + 5 + ajuste_val.val))
            else:
                result_txt_box.append("Pago Total: USD$ " + format_output(quotient + 10 + ajuste_val.val))
        elif remesa_dol_inp.text == "" and remesa_pesos_inp.text == "" and pago_total_inp.text != "":
            if pago_total_val.val < 502 + ajuste_val.val:
                rmt = pago_total_val.val - 2 - ajuste_val.val
                result_txt_box.append("Monto: USD$ " + format_output(rmt) + '\n')
            elif pago_total_val.val < 1005 + ajuste_val.val:
                rmt = pago_total_val.val - 5 - ajuste_val.val
                result_txt_box.append("Monto: USD$ " + format_output(rmt) + '\n' )
            else:
                rmt = pago_total_val.val - 10 - ajuste_val.val
                result_txt_box.append("Monto: USD$ " + format_output(rmt)  + '\n')
            product = tasa_regular_val.val * rmt
            result_txt_box.append("Total Para Recibir: RD$ " + format_output(product) + "\n")
            result_txt_box.append("Pago Total: USD$ " + format_output(pago_total_val.val))
            
    
    elif st.checked and super_tasa_inp.text != "":
        if  remesa_dol_inp.text != "" and remesa_pesos_inp.text == "" and pago_total_inp.text == "":
            result_txt_box.append("Monto: USD$ " + format_output(remesa_dol_val.val) + "\n")
            product = round_up(super_tasa_val.val * remesa_dol_val.val)
            result_txt_box.append("Total Para Recibir: RD$ " + format_output(product) + "\n")
            if remesa_dol_val.val < 100:
                total = round_up(remesa_dol_val.val)
                result_txt_box.append("Pago Total: USD$ " + format_output(total + 5 + ajuste_val.val))
            else:
                total = round_up(remesa_dol_val.val, True)
                result_txt_box.append("Pago Total: USD$ " + format_output(total + ajuste_val.val))

        elif remesa_dol_inp.text == "" and remesa_pesos_inp.text != "" and pago_total_inp.text == "":
            quotient = remesa_pesos_val.val / super_tasa_val.val
            quotient = round_up(quotient)
            enhanced_accuracy_val_pesos = quotient * super_tasa_val.val
            result_txt_box.append("Monto: USD$ " + format_output(quotient) + "\n")
            result_txt_box.append("Total Para Recibir: RD$ " + format_output(enhanced_accuracy_val_pesos) + "\n")
            if quotient < 100:
                result_txt_box.append("Pago Total: USD$ " + format_output(quotient + 5 + ajuste_val.val))
            else:
                total = round_up(quotient, True)
                result_txt_box.append("Pago Total: USD$ " + format_output(total + ajuste_val.val))
        elif remesa_dol_inp.text == "" and remesa_pesos_inp.text == "" and pago_total_inp.text != "":
            if pago_total_val.val < 105 + ajuste_val.val:
                rmt = round_up(pago_total_val.val - 5 - ajuste_val.val)
                result_txt_box.append("Monto: USD$ " + format_output(rmt) + '\n' )
            else:
                reverse_tarifa =  105 / 100
                rmt = round((pago_total_val.val - ajuste_val.val) / (reverse_tarifa), 2)
                result_txt_box.append("Monto: USD$ " + format_output(rmt)  + '\n')
            result_txt_box.append("Total Para Recibir: RD$ " + format_output(rmt * super_tasa_val.val) + "\n")
            result_txt_box.append("Pago Total: RD$ " + format_output(pago_total_val.val))
    
    elif td.checked and remesa_pesos_inp.text == "":
        if remesa_dol_inp.text != "" and pago_total_inp.text == "":
            result_txt_box.append("Monto: USD$ " + format_output(remesa_dol_val.val) + "\n")
            if remesa_dol_val.val < 20:
                result_txt_box.append("Envío de dinero es muy bajo. El mínimo para enviar es 20 dólares.\n")
                return
            result_txt_box.append("Remesa Para Recibir: USD$ " + format_output(remesa_dol_val.val) + "\n")
            if remesa_dol_val.val <= 50:
                result_txt_box.append("Pago Total: USD$ " + format_output(remesa_dol_val.val + 5 + ajuste_val.val))
            elif remesa_dol_val.val <= 100:
                result_txt_box.append("Pago Total: USD$ " + format_output(remesa_dol_val.val + 6 + ajuste_val.val))
            else:
                total = remesa_dol_val.val * 1.03 + 5
                result_txt_box.append("Pago Total: USD$ " + format_output(total + ajuste_val.val))
        elif remesa_dol_inp.text == "" and pago_total_inp.text != "":
            if pago_total_val.val < 25 + ajuste_val.val:
                result_txt_box.append("Envío de dinero es muy bajo. El mínimo para enviar es 20 dólares.\n")
                return
            if pago_total_val.val <= 55 + ajuste_val.val:
                rmt = pago_total_val.val - 5 - ajuste_val.val
                result_txt_box.append("Monto: USD$ " + format_output(rmt) + '\n')
                result_txt_box.append("Remesa Para Recibir: USD$ " + format_output(rmt) + "\n")
                result_txt_box.append("Pago Total: USD$ " + format_output(pago_total_val.val))
            elif pago_total_val.val <= 106 + ajuste_val.val:
                rmt = pago_total_val.val - 6 - ajuste_val.val
                result_txt_box.append("Monto: USD$ " + format_output(rmt) + '\n')
                result_txt_box.append("Remesa Para Recibir: USD$ " + format_output(rmt) + "\n")
                result_txt_box.append("Pago Total: USD$ " + format_output(pago_total_val.val))
            else:
                reverse_tarifa =  103 / 100
                rmt = round((pago_total_val.val - ajuste_val.val - 5) / (reverse_tarifa), 2)
                result_txt_box.append("Monto: USD$ " + format_output(rmt) + '\n')
                result_txt_box.append("Remesa Para Recibir: USD$ " + format_output(rmt) + "\n")
                result_txt_box.append("Pago Total: USD$ " + format_output(pago_total_val.val))

    if result_txt_box.text == "":
        print_error()
        return

def clear_rmt(event):
    remesa_pesos_inp.clear()
    remesa_dol_inp.clear()
    tr.checked = False
    st.checked = False
    td.checked = False
    tr.disabled = False
    st.disabled = False
    td.disabled = False
    result_txt_box.clear()


def clear_all(event):
    tasa_regular_inp.clear()
    super_tasa_inp.clear()
    ajuste_inp.text = "0"
    clear_rmt(event)


app.set_grid(9,3)
app.set_row_weights(1,1,1,1,1,1,1,1,1)
app.set_column_weights(1,1,1)
app.add(tasa_regular, 1,1, align='left')
app.add(remesa_dol, 1,2, align='center')
app.add(remesa_pesos, 3,2, align='center')
app.add(remesa_pesos_inp, 4,2, align='center')
app.add(tr, 1,3)
app.add(tasa_regular_inp, 2,1, align='left')
app.add(remesa_dol_inp, 2,2, align='center')
app.add(st, 2,3)
app.add(super_tasa, 3,1, align='left')
app.add(td, 3,3)
app.add(submit_btn, 7,2, align='center', fill=True, stretch=True, row_span=2)
app.add(clear_rmt_btn, 4,3, fill=True)
app.add(clear_all_btn, 5,3, fill=True)
app.add(super_tasa_inp, 4,1, align='left')
app.add(ajuste_lbl,6,1, align='left')
app.add(pago_total, 5, 2, align='center')
app.add(pago_total_inp, 6, 2, align='center')
app.add(ajuste_inp,7,1,align='left')
app.add(result_lbl, 8,1, align='left')
app.add(result_txt_box, 9,1, align='center',column_span=3, fill="True")

tr.add_event_listener("change", just_one_checked_box)
st.add_event_listener("change", just_one_checked_box)
td.add_event_listener("change", just_one_checked_box)
submit_btn.add_event_listener("press", tasa_calc)
clear_rmt_btn.add_event_listener("press", clear_rmt)
clear_all_btn.add_event_listener("press", clear_all)

app.width = 500
app.length = 500


app.run()
