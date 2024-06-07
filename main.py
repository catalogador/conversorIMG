import os
from tkinter import Tk, filedialog, messagebox
from PIL import Image

def convert_image(input_path, output_path, output_format):
    try:
        with Image.open(input_path) as img:
            img.save(output_path, format=output_format.upper())
        messagebox.showinfo("Sucesso", f"Imagem convertida com sucesso! Salva em: {output_path}")
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao converter a imagem: {e}")

def main():
    # Criar uma janela oculta principal do Tkinter
    root = Tk()
    root.withdraw()  # Esconder a janela principal
    
    # Abrir o diálogo de seleção de arquivo
    input_path = filedialog.askopenfilename(title="Selecione a imagem para converter",
                                            filetypes=[("Todos os arquivos de imagem", "*.*")])
    
    if not input_path:
        messagebox.showinfo("Informação", "Nenhum arquivo selecionado.")
        return
    
    # Solicitar o formato de saída
    output_format = filedialog.asksaveasfilename(title="Salvar como",
                                                 defaultextension=".jpeg",
                                                 filetypes=[("JPEG", "*.jpeg"),
                                                            ("PNG", "*.png"),
                                                            ("BMP", "*.bmp"),
                                                            ("GIF", "*.gif"),
                                                            ("TIFF", "*.tiff")])
    
    if not output_format:
        messagebox.showinfo("Informação", "Nenhum formato de saída selecionado.")
        return

    # Extrair o caminho e a extensão do arquivo de saída
    output_root, output_ext = os.path.splitext(output_format)
    output_path = f"{output_root}{output_ext}"
    output_format = output_ext[1:]  # Remover o ponto da extensão

    convert_image(input_path, output_path, output_format)

if __name__ == "__main__":
    main()
