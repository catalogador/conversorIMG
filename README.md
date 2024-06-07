Conversor de Imagens
=====================

Este repositório contém um script em Python que permite converter imagens entre diferentes formatos usando uma interface gráfica simples criada com Tkinter.

Funcionalidades
---------------

- Selecionar uma imagem de entrada.
- Escolher o formato de saída e salvar a imagem convertida.
- Suporte para os seguintes formatos de imagem: JPEG, PNG, BMP, GIF, TIFF.

Requisitos
----------

- Python 3.x
- Bibliotecas:
    - Pillow (biblioteca de manipulação de imagens)
    - Tkinter (biblioteca para interface gráfica)

Instalação
-----------

Clone este repositório para o seu ambiente local:

.. code-block:: sh

    git clone https://github.com/seu-usuario/conversor-de-imagens.git
    cd conversor-de-imagens

Crie um ambiente virtual (opcional, mas recomendado):

.. code-block:: sh

    python -m venv venv
    source venv/bin/activate  # No Windows use `venv\Scripts\activate`

Instale as dependências necessárias:

.. code-block:: sh

    pip install pillow

Uso
---

Execute o script ``converter.py``:

.. code-block:: sh

    python converter.py

Uma janela de diálogo aparecerá pedindo para selecionar a imagem que você deseja converter.

Após selecionar a imagem, uma segunda janela aparecerá pedindo para escolher o formato e o local onde deseja salvar a imagem convertida.

O script exibirá uma mensagem informando se a conversão foi bem-sucedida ou se ocorreu algum erro.
