import pandas as pd
import numpy as np
import os

# =========================
# CONFIGURACIÓN GENERAL
# =========================
regiones = ["Norte", "Sur", "Este", "Oeste"]

encargados_por_region = {
    "Norte": {
        "nombre": "Carlos Méndez",
        "foto": "https://raw.githubusercontent.com/JUANCITOPENA/GENERADOR_IMAGENES_PERSONAS/refs/heads/main/FOTOS_PERSONAS_UBER_MAS/mpersona_9.png"
    },
    "Sur": {
        "nombre": "Ana Rodríguez",
        "foto": "https://raw.githubusercontent.com/JUANCITOPENA/GENERADOR_IMAGENES_PERSONAS/refs/heads/main/FOTOS_PERSONAS_UBER_MAS/fpersona_1.png"
    },
    "Este": {
        "nombre": "Luis Pérez",
        "foto": "https://raw.githubusercontent.com/JUANCITOPENA/GENERADOR_IMAGENES_PERSONAS/refs/heads/main/FOTOS_PERSONAS_UBER_MAS/mpersona_6.png"
    },
    "Oeste": {
        "nombre": "María Gómez",
        "foto": "https://raw.githubusercontent.com/JUANCITOPENA/GENERADOR_IMAGENES_PERSONAS/refs/heads/main/FOTOS_PERSONAS_UBER_MAS/fpersona_10.png"
    }
}

categorias = [
    "Camisetas", "Pantalones", "Camisas",
    "Chaquetas", "Vestidos", "Faldas"
]

productos_con_imagen = {
    "Camiseta Básica": "https://acrearpublicidad.com/wp-content/uploads/2020/08/camisa-oxford-dama.png",
    "Vestido Formal": "https://png.pngtree.com/png-vector/20260120/ourmid/pngtree-red-formal-dress-mockup-styled-elegantly-for-fashion-presentation-png-image_18510586.webp",
    "Falda Plisada": "https://elmachetazo.vtexassets.com/arquivos/ids/728925/Falda-Escolar-Azul-Secundaria%7CPlisada%7CTalla-8_1.png?v=638756066615100000",
    "Abrigo Invierno": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTdUnDssPWRRtW_zFOmfoGwYpi9k-CSeYRHHw&s",
    "Pantalón Chino": "https://uniformesroger.com/WebRoot/Store/Shops/UniformesRoger/671D/2E33/C751/BC89/9B86/2E10/8536/374A/1041421536.png",
    "Suéter Lana": "https://png.pngtree.com/png-vector/20240730/ourmid/pngtree-adorable-designs-handmade-baby-sweaters-for-every-season-png-image_13305047.png",
    "Chaqueta Cuero": "https://dainese-cdn.thron.com/delivery/public/image/dainese/793b39d8-3f77-47af-b1b1-5341df963231/px6qct/std/960x960/201533877_001_1.png?format=webp&quality=auto-medium",
    "Falda Lápiz": "https://media.balmain.com/image/upload/f_auto,q_auto,dpr_auto,e_sharpen:85/c_fill,w_432,h_584/sfcc/balmain/hi-res/FF1LBA97CF690FKF?_i=AG",
    "Camisa Oxford": "https://camisasferruche.com/wp-content/uploads/2022/08/CAMISA-OXFORD-VERDE-ML.png",
    "Blusa Manga Larga": "https://handlergroup.com/cdn/shop/products/SunD3_4PNaranja-1_650x.png?v=1640743849",
    "Jean Slim Fit": "https://jeanpool.com.au/cdn/shop/files/557B4296-4787-4CEE-898F-D4579E5F5597.png?v=1747551408&width=1080",
    "Chaqueta Denim": "https://png.pngtree.com/png-vector/20240824/ourmid/pngtree-denim-jacket-isolated-for-man-wear-png-image_13603828.png",
    "Suéter Algodón": "https://assets.theplace.com/image/upload/t_plp_img_m,f_auto,q_auto/v1/ecom/assets/products/tcp/3057022/3057022_1206.png",
    "Vestido Casual": "https://cdnx.jumpseller.com/kadrihel1/image/5627848/resize/635/635?1646060241",
    "Blusa Sin Mangas": "https://www.thorsteinar-outlet.de/media/6c/0e/dd/1748339570/1_10116.png?1749730504"
}

productos = list(productos_con_imagen.keys())

# =========================
# FUNCIÓN GENERADORA
# =========================
def generar_inventario_por_rango(
    fecha_inicio: str,
    fecha_fin: str,
    registros_por_dia: int = 3,
    ruta_salida: str = "."
):
    fechas = pd.date_range(fecha_inicio, fecha_fin)
    data = []

    for fecha in fechas:
        for _ in range(registros_por_dia):
            region = np.random.choice(regiones)
            encargado = encargados_por_region[region]

            producto = np.random.choice(productos)

            entradas = np.random.randint(50, 300)
            salidas = np.random.randint(10, entradas)

            data.append({
                "Fecha": fecha,
                "Región": region,
                "Encargado": encargado["nombre"],
                "Foto_Encargado": encargado["foto"],
                "Categoría": np.random.choice(categorias),
                "Producto": producto,
                "Foto_Producto": productos_con_imagen[producto],
                "Entradas": entradas,
                "Salidas": salidas,
                "Stock Final": entradas - salidas,
                "Rotación (%)": round(salidas / entradas, 4)
            })

    df = pd.DataFrame(data)

    df["Año"] = df["Fecha"].dt.year
    df["Mes"] = df["Fecha"].dt.month

    os.makedirs(ruta_salida, exist_ok=True)

    for (anio, mes), df_mes in df.groupby(["Año", "Mes"]):
        nombre_mes = df_mes["Fecha"].dt.strftime("%B").iloc[0].upper()
        archivo = os.path.join(
            ruta_salida, f"inventario_{nombre_mes}_{anio}.xlsx"
        )
        df_mes.drop(columns=["Año", "Mes"]).to_excel(archivo, index=False)
        print(f"✔ Archivo generado: {archivo}")

# =========================
# EJECUCIÓN
# =========================
generar_inventario_por_rango(
    fecha_inicio="2025-01-01",
    fecha_fin="2026-01-28",
    registros_por_dia=3,
    ruta_salida=r"C:\Users\User\Desktop\CONSOLIDAR DATOS\Archivo Consolidado"
)
