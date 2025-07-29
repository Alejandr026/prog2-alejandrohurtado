import tkinter as tk
from tkinter import simpledialog, messagebox
import json
import os
import sys
import pandas as pd

# Detectar carpeta del ejecutable o script
BASE_DIR = os.path.dirname(sys.executable if getattr(sys, 'frozen', False) else __file__)
ARCHIVO_TAREAS = os.path.join(BASE_DIR, "tareas_guardadas.json")
ARCHIVO_EXCEL = os.path.join(BASE_DIR, "tareas_exportadas.xlsx")


class KanbanApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Kanban To-Do List")
        self.root.geometry("850x540")
        self.tareas = {
            "Por Hacer": [],
            "En Progreso": [],
            "Completado": []
        }
        self.columnas = {}
        self._crear_columnas()
        self._crear_botones_superiores()
        self._cargar_tareas()

    def _crear_columnas(self):
        contenedor = tk.Frame(self.root)
        contenedor.pack(fill='both', expand=True)
        for nombre in ["Por Hacer", "En Progreso", "Completado"]:
            frame = tk.Frame(contenedor, bg="#eeeeee", width=250, height=450, bd=2, relief='groove')
            frame.pack(side='left', padx=10, pady=10, fill='both', expand=True)
            titulo = tk.Label(frame, text=nombre, bg="#dddddd", font=('Arial', 12, 'bold'))
            titulo.pack(fill='x')
            self.columnas[nombre] = frame

    def _crear_botones_superiores(self):
        barra = tk.Frame(self.root)
        barra.pack(pady=5)
        tk.Button(barra, text="➕ Agregar Tarea", command=self.agregar_tarea).pack(side='left', padx=5)
        tk.Button(barra, text="📤 Exportar a Excel", command=self.exportar_excel).pack(side='left', padx=5)

    def agregar_tarea(self):
        self._editar_tarea()

    def _refrescar_columnas(self):
        colores = {
            "Alta": "#ffcc99",
            "Media": "#dddddd",
            "Baja": "#ccffcc"
        }
        for estado, frame in self.columnas.items():
            for widget in frame.winfo_children()[1:]:
                widget.destroy()
            for tarea in self.tareas[estado]:
                color = colores.get(tarea.get("prioridad", "Media"), "#dddddd")
                card = tk.Frame(frame, bg=color, relief='raised', bd=1, padx=4, pady=4)
                card.pack(pady=5, padx=5, fill='x')

                tk.Label(card, text=tarea["desc"], anchor='w', bg=color, font=('Arial', 10)).pack(fill='x')
                if tarea["asignado"]:
                    tk.Label(card, text=f"👤 {tarea['asignado']}", anchor='w', bg=color, fg='gray').pack(fill='x')

                botones = tk.Frame(card, bg=color)
                botones.pack(fill='x', pady=2)
                tk.Button(botones, text="✏ Editar",
                          command=lambda t=tarea, e=estado: self._editar_tarea(t, e)).pack(side='left')
                tk.Button(botones, text="📤 Mover",
                          command=lambda t=tarea, e=estado: self.mover_tarea(t, e)).pack(side='left')
                tk.Button(botones, text="🗑",
                          command=lambda t=tarea, e=estado: self.eliminar_tarea(t, e)).pack(side='right')

    def _editar_tarea(self, tarea=None, estado_actual="Por Hacer"):
        prioridades_validas = ["alta", "media", "baja"]

        if tarea:
            desc = simpledialog.askstring("Editar Tarea", "Descripción:", initialvalue=tarea["desc"], parent=self.root) or tarea["desc"]
            asignado = simpledialog.askstring("Editar Asignado", "Asignado a:", initialvalue=tarea["asignado"], parent=self.root) or ""
            prioridad = simpledialog.askstring("Editar Prioridad", "Prioridad (Alta, Media, Baja):",
                                               initialvalue=tarea["prioridad"], parent=self.root)
            if not prioridad or prioridad.lower() not in prioridades_validas:
                messagebox.showerror("Error", "Prioridad no válida. Usa: Alta, Media o Baja.", parent=self.root)
                return
            tarea.update({"desc": desc, "asignado": asignado, "prioridad": prioridad.capitalize()})
        else:
            desc = simpledialog.askstring("Tarea", "Descripción:", parent=self.root)
            if not desc:
                return
            for lista in self.tareas.values():
                if any(t["desc"] == desc for t in lista):
                    messagebox.showwarning("Duplicado", "Ya existe una tarea con esa descripción.", parent=self.root)
                    return

            asignado = simpledialog.askstring("Asignado", "¿Quién la hará?", parent=self.root) or ""
            prioridad = simpledialog.askstring("Prioridad", "Prioridad (Alta, Media, Baja):", parent=self.root)
            if not prioridad or prioridad.lower() not in prioridades_validas:
                messagebox.showerror("Error", "Prioridad no válida. Usa: Alta, Media o Baja.", parent=self.root)
                return

            tarea = {"desc": desc, "asignado": asignado, "prioridad": prioridad.capitalize()}
            self.tareas["Por Hacer"].append(tarea)

        self._guardar_tareas()
        self._refrescar_columnas()

    def mover_tarea(self, tarea, estado_actual):
        ventana = tk.Toplevel(self.root)
        ventana.title("Mover Tarea")
        ventana.geometry("300x100")
        ventana.transient(self.root)
        ventana.grab_set()
        ventana.focus_force()

        tk.Label(ventana, text=f"¿Mover '{tarea['desc']}' a:").pack(pady=5)

        opciones = ["Por Hacer", "En Progreso", "Completado"]
        opciones.remove(estado_actual)
        destino = tk.StringVar(ventana)
        destino.set(opciones[0])

        menu = tk.OptionMenu(ventana, destino, *opciones)
        menu.pack(pady=5)

        def confirmar():
            self.tareas[estado_actual].remove(tarea)
            self.tareas[destino.get()].append(tarea)
            self._guardar_tareas()
            self._refrescar_columnas()
            ventana.destroy()

        tk.Button(ventana, text="Mover", command=confirmar).pack(pady=5)

    def eliminar_tarea(self, tarea, estado):
        if messagebox.askyesno("Confirmar", f"¿Eliminar '{tarea['desc']}'?", parent=self.root):
            self.tareas[estado].remove(tarea)
            self._guardar_tareas()
            self._refrescar_columnas()

    def exportar_excel(self):
        tareas_planas = []
        for estado, lista in self.tareas.items():
            for tarea in lista:
                tareas_planas.append({
                    "Descripción": tarea["desc"],
                    "Asignado a": tarea["asignado"],
                    "Prioridad": tarea["prioridad"],
                    "Estado": estado
                })
        df = pd.DataFrame(tareas_planas)
        df.to_excel(ARCHIVO_EXCEL, index=False)
        messagebox.showinfo("Exportado", f"Tareas exportadas a:\n{ARCHIVO_EXCEL}", parent=self.root)

    def _guardar_tareas(self):
        with open(ARCHIVO_TAREAS, "w", encoding="utf-8") as f:
            json.dump(self.tareas, f, ensure_ascii=False, indent=2)

    def _cargar_tareas(self):
        if os.path.exists(ARCHIVO_TAREAS):
            with open(ARCHIVO_TAREAS, "r", encoding="utf-8") as f:
                self.tareas = json.load(f)
            self._refrescar_columnas()


if __name__ == "__main__":
    root = tk.Tk()
    app = KanbanApp(root)
    root.mainloop()