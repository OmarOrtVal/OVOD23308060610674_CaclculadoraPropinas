import flet as ft

def main(page: ft.Page):
    page.title = "Calculadora de Propinas"
    page.window_width = 300
    page.window_height = 500
    page.padding = 20
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    
    monto = ft.TextField(
        label="Monto de cuenta",
        width=280,
        keyboard_type=ft.KeyboardType.NUMBER
    )
    
    porcentaje = ft.Text("0%", size=24)
    total = ft.Text("$0.00", size=32)
    cantidad_propina = ft.Text("$0.00", size=20)
    mensaje = ft.Text("")
    
    def calcular(e):        
        try:
            m = float(monto.value)
            p = slider_propina.value
            propina = m * (p / 100)
            
            porcentaje.value = f"{int(p)}%"
            cantidad_propina.value = f"${propina:.2f}"
            total.value = f"${m + propina:.2f}"
            mensaje.value = ""
            
        except:
            mensaje.value = "Error - Ingresa solo números"
        
        page.update()
    
    slider_propina = ft.Slider(
        min=5,
        max=25,
        divisions=7,
        value=5,
        label="{value}%",
        width=250,
        on_change=calcular
    )
    
    page.add(
        ft.Column([
            ft.Text("Calculadora de propinas", size=28),
            ft.Divider(height=20),
            
            monto,
            ft.Divider(height=20),
            
            ft.Text("Selecciona el porcentaje"),
            slider_propina,
            porcentaje,
            
            ft.Divider(height=20),
            ft.Text("Cantidad de propina", size=14),
            cantidad_propina,
            
            ft.Divider(height=20),
            ft.Text("Total a pagar", size=16),
            total,
            
            ft.Divider(height=20),
            mensaje
        ],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER)
    )

ft.run(main)
