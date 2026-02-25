import flet as ft

def main(page: ft.Page):
    page.title = "Calculadora de Propinas"
    page.window_width = 400
    page.window_height = 600
    page.padding = 20
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    
    monto = ft.TextField(label="Monto de cuenta", width=280)
    porcentaje = ft.Text("0%", size=24)
    total = ft.Text("0", size=32, weight=ft.FontWeight.BOLD)
    
    cantidad_propina = ft.Text("$0", size=20)
    
    def calcular(p):
        def _calcular(e):
            try:
                m = float(monto.value)
                propina = m * (p / 100)
                total.value = str(int(m + propina))
                porcentaje.value = f"{p}%"
                cantidad_propina.value = f"${propina:.0f}"
                page.update()
            except:
                total.value = "Error - Ingresa un número"
                page.update()
        return _calcular
    
    page.add(
        ft.Column([
            ft.Text("PROPINAS", size=28, weight=ft.FontWeight.BOLD),
            ft.Divider(height=20),
            
            monto,
            ft.Divider(height=20),
            
            ft.Column([
                ft.Row([
                    ft.ElevatedButton("5%", on_click=calcular(5), expand=True),
                    ft.ElevatedButton("8%", on_click=calcular(8), expand=True),
                    ft.ElevatedButton("10%", on_click=calcular(10), expand=True),
                    ft.ElevatedButton("13%", on_click=calcular(13), expand=True),
                    ft.ElevatedButton("15%", on_click=calcular(15), expand=True),
                    ft.ElevatedButton("18%", on_click=calcular(18), expand=True),
                    ft.ElevatedButton("20%", on_click=calcular(20), expand=True),
                    ft.ElevatedButton("25%", on_click=calcular(25), expand=True),
                ]),
            ]),
            
            ft.Divider(height=20),
            ft.Text("Cantidad de propina", size=14),
            cantidad_propina,
            
            ft.Divider(height=20),
            ft.Text("Total a pagar", size=16),
            total
        ])
    )

ft.app(target=main)