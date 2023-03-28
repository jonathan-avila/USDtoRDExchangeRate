import gooeypie as gp



app = gp.GooeyPieApp('Cálculo de Tasas')



tasa_baja = gp.Label(app, "Cual es la tasa regular? ")
tasa_baja_inp = gp.Input(app)

tasa_alta =  gp.Label(app, "Cual es la tasa alta? ")
tasa_alta_inp = gp.Input(app)

remeza_dol = gp.Label(app, "Cual es la remeza en dolares? ")
remeza_dol_inp = gp.Input(app)

remeza_pesos = gp.Label(app, " O Cual es la remeza en pesos? ")
remeza_pesos_inp = gp.Input(app)


o_lbl = gp.Label(app, "O")


tr = gp.Checkbox(app, "Tasa Regular")
st = gp.Checkbox(app, "Super Tasa")

submit_btn = gp.Button(app, "Someter", None)
result_lbl =gp.Label(app,"Resultado: ")
result_txt_box = gp.Textbox(app)

def just_one_checked_box(event):
    if tr.checked:
        st.disabled = True
    
    elif not tr.checked:
        st.disabled = False

    if st.checked:
        tr.disabled = True
    
    elif not st.checked:
        tr.disabled = False

def tasa_calc(event):
    result_txt_box.clear()
    if tr.checked and tasa_baja_inp.text != "":
        if  remeza_dol_inp.text != "" and remeza_pesos_inp.text == "":
            product = float(tasa_baja_inp.text) * float(remeza_dol_inp.text)
            result_txt_box.append("Total Para Recibir: RD$ " + str(product) + "\n")
            if float(remeza_dol_inp.text) < 500:
                result_txt_box.append("Pago Total: USD$ " + str(float(remeza_dol_inp.text) + 2))
            elif float(remeza_dol_inp.text) < 1000:
                result_txt_box.append("Pago Total: USD$ " + str(float(remeza_dol_inp.text) + 5))
            else:
                result_txt_box.append("Pago Total: USD$ " + str(float(remeza_dol_inp.text) + 10))

        elif remeza_dol_inp.text == "" and remeza_pesos_inp.text != "":
            result_txt_box.append("Total Para Recibir: RD$ " + remeza_pesos_inp.text + "\n")
            quotient = float(remeza_pesos_inp.text) / float(tasa_baja_inp.text)
            if quotient < 500:
                result_txt_box.append("Pago Total: USD$ " + str(round(quotient + 2,2)))
            elif quotient < 1000:
                result_txt_box.append("Pago Total: USD$ " + str(round(quotient + 5),2))
            else:
                result_txt_box.append("Pago Total: USD$ " + str(round(quotient + 10,2)))
    
    elif st.checked and tasa_alta_inp.text != "":
        if  remeza_dol_inp.text != "" and remeza_pesos_inp.text == "":
            product = float(tasa_alta_inp.text) * float(remeza_dol_inp.text)
            result_txt_box.append("Total Para Recibir: RD$ " + str(product) + "\n")
            if float(remeza_dol_inp.text) < 100:
                result_txt_box.append("Pago Total USD$ " + str(float(remeza_dol_inp.text) + 5))
            else:
                result_txt_box.append("Pago Total USD$ " + str(float(remeza_dol_inp.text) * 1.05))

        elif remeza_dol_inp.text == "" and remeza_pesos_inp.text != "":
            result_txt_box.append("Total Para Recibir: RD$ " + remeza_pesos_inp.text + "\n")
            quotient = float(remeza_pesos_inp.text) / float(tasa_alta_inp.text)
            if quotient < 100:
                result_txt_box.append("Pago Total: USD$ " + str(round(quotient + 5,2)))
            else:
                result_txt_box.append("Pago Total: USD$ " + str(round(quotient + 10, 2)))
    

    if result_txt_box.text == "":
        result_txt_box.append("Hubo un error en los datos de entrada. Asegúrrese de ingresarlos correctamente.")

app.set_grid(6,3)
app.set_row_weights(0,0,0,0,0,0)
app.add(tasa_baja, 1,1, align='left')
app.add(remeza_dol, 1,2, align='left')
app.add(remeza_pesos, 3,2, align='left')
app.add(remeza_pesos_inp, 4,2, align='left')
app.add(tr, 1,3)
app.add(tasa_baja_inp, 2,1, align='left')
app.add(remeza_dol_inp, 2,2, align='left')
app.add(st, 2,3)
app.add(tasa_alta, 3,1, align='left')
#app.add(o_lbl,3,2, align='center')
app.add(submit_btn, 3,3, fill='True')
app.add(tasa_alta_inp, 4,1, align='left')
app.add(result_lbl, 5,1, align='left')
app.add(result_txt_box, 6,1, align='center',column_span=3, fill="True")

tr.add_event_listener("change", just_one_checked_box)
st.add_event_listener("change", just_one_checked_box)
submit_btn.add_event_listener("press",tasa_calc)

app.width = 500
app.length = 500


tr.disabled = False
st.disabled = False

app.run()