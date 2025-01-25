from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, \
CommandHandler, ContextTypes, CallbackContext, CallbackQueryHandler

async def say_hello(update: Update, context: ContextTypes.DEFAULT_TYPE):

    keyboard = InlineKeyboardMarkup([
        
           [InlineKeyboardButton(text="Pagar mi deuda de Didi Repartidor", callback_data="Deuda")],
           [InlineKeyboardButton(text="Comprar Tarjeta de Crédito", callback_data="Comprar")],
           [InlineKeyboardButton(text="Comprar Comida al 50%", callback_data="Pedir")],
        ])   
            
    await update.message.reply_text("Hola, Por favor selecciona lo que deseas a continuacion:", reply_markup=keyboard)

async def button_controller( update: Update, context: CallbackContext ):
    
    data = update.callback_query.data
    if( data == "Comprar" ):
        await update.callback_query.message.edit_text("Pronto Disponible", reply_markup=None)
        return
    
    data = update.callback_query.data
    if( data == "Deuda" ):
        await update.callback_query.message.edit_text("""Procedimiento para pago de deuda Didi repartidor:

1. Me pasas el número de la cuenta que vas a pagar y me dices cuánto de deuda tiene.

2. Te va a llegar un código que me debes pasar para poder ingresar a tu cuenta.

3. Cuando ingrese, procedo a pagar la deuda en minutos. 💳💵

4.  Te aviso para que entres a tu cuenta y verifiques que se le hizo el pago.

5. Procedes a hacerme el pago del 50% + una pequeña comisión, según tu deuda, por nequi ó daviplata. 

⛔️ Para los nuevos que no vengan recomendados con otra persona que haya hecho el procedimiento, se les cobra por adelantado.

• A los que vengan recomendados, se les paga la deuda por adelantado.

• Si tienes dudas puedes preguntar en mi grupo para más información, hay muchos que son mis clientes.""", reply_markup=None)
        return
    
    data = update.callback_query.data
    if( data == "Pedir" ):
        await update.callback_query.message.edit_text("Pronto Disponible", reply_markup=None)
        return
    
    await update.callback_query.answer( text=data,show_alert=True )
    await update.callback_query.message.reply_text(data)
    

TOKEN = "7464355957:AAHJvHJMx7XKFkxNbxFWB0zL7BqQ-gX348M"
application = ApplicationBuilder().token(TOKEN).build()

application.add_handler( CommandHandler( "start", say_hello ) ) 
application.add_handler( CallbackQueryHandler(button_controller) )

application.run_polling(allowed_updates=Update.ALL_TYPES)