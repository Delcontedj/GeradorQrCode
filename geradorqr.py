from qrcode import QRCode
import customtkinter
from customtkinter import END
from customtkinter import CTkEntry


def qrc(event):
    # Dados para o QR Code
    data = codigo_busca.get()

    # Criar o objeto QR Code
    qr = QRCode(
        box_size=10,
        border=4,
    )

    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")

    img.save("qrcode.jpg")

    codigo_busca.delete(0, END)

    frontend.bind('<Return>', qrc)


frontend = customtkinter.CTk()
frontend.title('Gerador de QRCODE')

codigo_busca = CTkEntry(frontend, width=400)
codigo_busca.pack()

frontend.bind('<Return>', qrc)

frontend.mainloop()