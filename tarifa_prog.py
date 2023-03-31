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


tr = gp.Checkbox(app, "Tasa Regular")
st = gp.Checkbox(app, "Super Tasa")
td = gp.Checkbox(app, "Tasa del Dólar")

submit_btn = gp.Button(app, "Someter", None)
clear_btn = gp.Button(app, "Limpiar", None)
result_lbl =gp.Label(app,"Resultado: ")
result_txt_box = gp.Textbox(app)

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

def print_error():
    result_txt_box.clear()
    result_txt_box.append("Hubo un error en los datos de entrada. Asegúrrese de ingresarlos correctamente.")

def tasa_calc(event):
    all_input = tasa_baja_inp.text + tasa_alta_inp.text + remeza_dol_inp.text + remeza_pesos_inp.text
    all_input = all_input.replace('.', '')
    if not all_input.isnumeric():
        print_error()
        return
    result_txt_box.clear()
    if tr.checked and tasa_baja_inp.text != "":
        if  remeza_dol_inp.text != "" and remeza_pesos_inp.text == "":
            product = float(tasa_baja_inp.text) * float(remeza_dol_inp.text)
            result_txt_box.append("Total Para Recibir: RD$ " + str(product) + "\n")
            remezas_output = float(remeza_dol_inp.text)
            if float(remeza_dol_inp.text) < 500:
                result_txt_box.append("Pago Total: USD$ " + str(remezas_output + 2))
            elif float(remeza_dol_inp.text) < 1000:
                result_txt_box.append("Pago Total: USD$ " + str(remezas_output + 5))
            else:
                result_txt_box.append("Pago Total: USD$ " + str(remezas_output + 10))

        elif remeza_dol_inp.text == "" and remeza_pesos_inp.text != "":
            quotient = float(remeza_pesos_inp.text) / float(tasa_baja_inp.text)
            total = round_up(quotient)
            result_txt_box.append("Total Para Recibir: RD$ " + remeza_pesos_inp.text + "\n")
            if total < 500:
                result_txt_box.append("Pago Total: USD$ " + str(total + 2))
            elif total < 1000:
                result_txt_box.append("Pago Total: USD$ " + str(total + 5))
            else:
                result_txt_box.append("Pago Total: USD$ " + str(total + 10))
    
    elif st.checked and tasa_alta_inp.text != "":
        if  remeza_dol_inp.text != "" and remeza_pesos_inp.text == "":
            product = round(float(tasa_alta_inp.text) * float(remeza_dol_inp.text),2)
            result_txt_box.append("Total Para Recibir: RD$ " + str(product) + "\n")
            remezas_output = float(remeza_dol_inp.text)
            if float(remeza_dol_inp.text) < 100:
                total = round_up(remezas_output)
                result_txt_box.append("Pago Total USD$ " + str(total + 5))
            else:
                total = round_up(remezas_output, True)
                result_txt_box.append("Pago Total USD$ " + str(total))

        elif remeza_dol_inp.text == "" and remeza_pesos_inp.text != "":
            quotient = float(remeza_pesos_inp.text) / float(tasa_alta_inp.text)
            total = round_up(quotient)
            result_txt_box.append("Total Para Recibir: RD$ " + remeza_pesos_inp.text + "\n")
            if quotient < 100:
                result_txt_box.append("Pago Total USD$ " + str(total+5))
            else:
                total = round_up(quotient, True)
                result_txt_box.append("Pago Total USD$ " + str(total))
    
    if td.checked and remeza_dol_inp.text != "" and remeza_pesos_inp.text == "":
        remeza_dol = float(remeza_dol_inp.text)
        if remeza_dol < 20:
            result_txt_box.append("Envio de dinero es muy bajo. Tienen que enviar 20 dolares o mas.\n")
            return
        result_txt_box.append("Remeza Para Recibir USD$ " + str(remeza_dol) + "\n")
        if remeza_dol <= 50:
            result_txt_box.append("Pago Total USD$ " + str(remeza_dol + 5))
        elif remeza_dol <= 100:
            result_txt_box.append("Pago Total USD$ " + str(remeza_dol + 6))
        else:
            total = remeza_dol * 1.03 + 5
            result_txt_box.append("Pago Total USD$ " + str(total))

    if result_txt_box.text == "":
        print_error()

def clear_all(event):
    remeza_pesos_inp.clear()
    remeza_dol_inp.clear()
    tasa_baja_inp.clear()
    tasa_alta_inp.clear()
    tr.checked = False
    st.checked = False
    td.checked = False
    tr.disabled = False
    st.disabled = False
    td.disabled = False
    result_txt_box.clear()


app.set_grid(6,3)
app.set_row_weights(1,1,1,1,1,1)
app.set_column_weights(1,1,1)
app.add(tasa_baja, 1,1, align='left')
app.add(remeza_dol, 1,2, align='left')
app.add(remeza_pesos, 3,2, align='left')
app.add(remeza_pesos_inp, 4,2, align='left')
app.add(tr, 1,3)
app.add(tasa_baja_inp, 2,1, align='left')
app.add(remeza_dol_inp, 2,2, align='left')
app.add(st, 2,3)
app.add(tasa_alta, 3,1, align='left')
app.add(td, 3,3)
app.add(submit_btn, 4,3, fill="True")
app.add(clear_btn, 5,3, align="center")
app.add(tasa_alta_inp, 4,1, align='left')
app.add(result_lbl, 5,1, align='left')
app.add(result_txt_box, 6,1, align='center',column_span=3, fill="True")

tr.add_event_listener("change", just_one_checked_box)
st.add_event_listener("change", just_one_checked_box)
td.add_event_listener("change", just_one_checked_box)
submit_btn.add_event_listener("press", tasa_calc)
clear_btn.add_event_listener("press", clear_all)

app.width = 500
app.length = 500


app.run()
