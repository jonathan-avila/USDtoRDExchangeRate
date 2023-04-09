import gooeypie as gp
from math import ceil


app = gp.GooeyPieApp('Cálculo de Tasas')


tasa_baja = gp.Label(app, "Cual es la tasa regular? ")
tasa_baja_inp = gp.Input(app)


tasa_alta =  gp.Label(app, "Cual es la tasa alta? ")
tasa_alta_inp = gp.Input(app)


remeza_dol = gp.Label(app, "Cual es la remeza en dolares? ")
remeza_dol_inp = gp.Input(app)



remeza_pesos = gp.Label(app, " O Cual es la remeza en pesos? ")
remeza_pesos_inp = gp.Input(app)

ajuste_lbl = gp.Label(app, "Ajuste de Tarifa:")
ajuste_inp = gp.Input(app)



tr = gp.Checkbox(app, "Tasa Regular")
st = gp.Checkbox(app, "Super Tasa")
td = gp.Checkbox(app, "Tasa del Dólar")

submit_btn = gp.Button(app, "Someter", None)
submit_btn.width = 10
clear_rmt_btn = gp.Button(app, "Limpiar Remeza", None)
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
        return(round(total * 1.05, 2))
    return total

def format_output(total):
    return f"{total:,.2f}"

def print_error():
    result_txt_box.clear()
    result_txt_box.append("Hubo un error en los datos de entrada. Asegúrrese de ingresarlos correctamente.")

def tasa_calc(event):
    tasa_baja_val = Store_val(tasa_baja_inp.text)
    tasa_alta_val = Store_val(tasa_alta_inp.text)
    remeza_dol_val = Store_val(remeza_dol_inp.text)
    remeza_pesos_val = Store_val(remeza_pesos_inp.text)
    ajuste_val = Store_val(ajuste_inp.text)
    if ajuste_val.val == "": 
        ajuste_val.val = "0"
        ajuste_inp.text = "0"
    
    inps = [tasa_alta_val, tasa_baja_val, remeza_dol_val, remeza_pesos_val, ajuste_val]
    for element in inps:
        element.val = element.val.replace(',','')
        if element.val:
            element.val = float(element.val)
            if not isinstance(element.val, float):
                print_error()
                return

    
    result_txt_box.clear()
    if tr.checked and tasa_baja_val.val != "":
        if  remeza_dol_val.val != "" and remeza_pesos_val.val == "":
            product = tasa_baja_val.val * remeza_dol_val.val
            result_txt_box.append("Total Para Recibir: RD$ " + format_output(product) + "\n")
            if remeza_dol_val.val < 500:
                result_txt_box.append("Pago Total: USD$ " + format_output(remeza_dol_val.val + 2 + ajuste_val.val))
            elif remeza_dol_val.val < 1000:
                result_txt_box.append("Pago Total: USD$ " + format_output(remeza_dol_val.val + 5 + ajuste_val.val))
            else:
                result_txt_box.append("Pago Total: USD$ " + format_output(remeza_dol_val.val + 10 + ajuste_val.val))

        elif remeza_dol_val.val == "" and remeza_pesos_val.val != "":
            quotient = remeza_pesos_val.val / tasa_baja_val.val
            total = round_up(quotient)
            result_txt_box.append("Total Para Recibir: RD$ " + format_output(remeza_pesos_val.val) + "\n")
            if total < 500:
                result_txt_box.append("Pago Total: USD$ " + format_output(total + 2 + ajuste_val.val))
            elif total < 1000:
                result_txt_box.append("Pago Total: USD$ " + format_output(total + 5 + ajuste_val.val))
            else:
                result_txt_box.append("Pago Total: USD$ " + format_output(total + 10 + ajuste_val.val))
    
    elif st.checked and tasa_alta_val.val != "":
        if  remeza_dol_val.val != "" and remeza_pesos_val.val == "":
            product = round(tasa_alta_val.val * remeza_dol_val.val)
            result_txt_box.append("Total Para Recibir: RD$ " + format_output(product) + "\n")
            if remeza_dol_val.val < 100:
                total = round_up(remeza_dol_val.val)
                result_txt_box.append("Pago Total: USD$ " + format_output(total + 5 + ajuste_val.val))
            else:
                total = round_up(remeza_dol_val.val, True)
                result_txt_box.append("Pago Total: USD$ " + format_output(total + ajuste_val.val))

        elif remeza_dol_val.val == "" and remeza_pesos_val.val != "":
            quotient = remeza_pesos_val.val / tasa_alta_val.val
            total = round_up(quotient)
            result_txt_box.append("Total Para Recibir: RD$ " + format_output(remeza_pesos_val.val) + "\n")
            if quotient < 100:
                result_txt_box.append("Pago Total: USD$ " + format_output(total + 5 + ajuste_val.val))
            else:
                total = round_up(quotient, True)
                result_txt_box.append("Pago Total: USD$ " + format_output(total + ajuste_val.val))
    
    if td.checked and remeza_dol_val.val != "" and remeza_pesos_val.val == "":
        remeza_dol = remeza_dol_val.val
        if remeza_dol < 20:
            result_txt_box.append("Envío de dinero es muy bajo. El mínimo para enviar es 20 dólares.\n")
            return
        result_txt_box.append("Remeza Para Recibir USD$ " + format_output(remeza_dol) + "\n")
        if remeza_dol <= 50:
            print(type(remeza_dol))
            print(type(ajuste_val.val))
            result_txt_box.append("Pago Total: USD$ " + format_output(remeza_dol + 5 + ajuste_val.val))
        elif remeza_dol <= 100:
            result_txt_box.append("Pago Total: USD$ " + format_output(remeza_dol + 6 + ajuste_val.val))
        else:
            total = remeza_dol * 1.03 + 5
            result_txt_box.append("Pago Total: USD$ " + format_output(total + ajuste_val.val))

    if result_txt_box.text == "":
        print_error()
        return

def clear_rmt(event):
    remeza_pesos_inp.clear()
    remeza_dol_inp.clear()
    tr.checked = False
    st.checked = False
    td.checked = False
    tr.disabled = False
    st.disabled = False
    td.disabled = False
    result_txt_box.clear()


def clear_all(event):
    tasa_baja_inp.clear()
    tasa_alta_inp.clear()
    ajuste_inp.text = "0"
    clear_rmt(event)


app.set_grid(8,3)
app.set_row_weights(1,1,1,1,1,1,1,1)
app.set_column_weights(1,1,1)
app.add(tasa_baja, 1,1, align='left')
app.add(remeza_dol, 1,2, align='center')
app.add(remeza_pesos, 3,2, align='center')
app.add(remeza_pesos_inp, 4,2, align='center')
app.add(tr, 1,3)
app.add(tasa_baja_inp, 2,1, align='left')
app.add(remeza_dol_inp, 2,2, align='center')
app.add(st, 2,3)
app.add(tasa_alta, 3,1, align='left')
app.add(td, 3,3)
app.add(submit_btn, 6,2, align='center', fill=True, stretch=True, row_span=2)
app.add(clear_rmt_btn, 6,3, fill=True)
app.add(clear_all_btn, 7,3, fill=True)
app.add(tasa_alta_inp, 4,1, align='left')
app.add(ajuste_lbl,5,1, align='left')
app.add(ajuste_inp,6,1,align='left')
app.add(result_lbl, 7,1, align='left')
app.add(result_txt_box, 8,1, align='center',column_span=3, fill="True")

tr.add_event_listener("change", just_one_checked_box)
st.add_event_listener("change", just_one_checked_box)
td.add_event_listener("change", just_one_checked_box)
submit_btn.add_event_listener("press", tasa_calc)
clear_rmt_btn.add_event_listener("press", clear_rmt)
clear_all_btn.add_event_listener("press", clear_all)

app.width = 500
app.length = 500


app.run()
