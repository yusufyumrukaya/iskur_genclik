from flask import Flask, request, send_file
from PIL import Image, ImageDraw, ImageFont
import os

app = Flask(__name__)

# A4 boyutları ve diğer sabitler (Python kodundan aldım)
a4_width_mm = 210
a4_height_mm = 297
dpi = 300
a4_width_pixels = int(a4_width_mm / 25.4 * dpi)
a4_height_pixels = int(a4_height_mm / 25.4 * dpi)

def create_petition(ad_soyad, ogrenci_no, cep_telefonu, eposta, egitim_yili, yariyil, dersler):
    # Beyaz A4 resmi oluştur
    a4_image = Image.new("RGB", (a4_width_pixels, a4_height_pixels), "white")
    draw = ImageDraw.Draw(a4_image)

    # Yazı tipleri
    font_path = "arialuni.ttf"
    font_bold_path = "arialbd.ttf"
    font_size_baslik = 47
    font_size = 45
    font_baslik = ImageFont.truetype(font_path, font_size_baslik)
    font = ImageFont.truetype(font_path, font_size)
    font_bold = ImageFont.truetype(font_bold_path, font_size)

    # Başlıkları ekle
    text_color = (0, 0, 0)
    y_offset = 60
    draw.text((970, 200), "YILDIZ TEKNİK ÜNİVERSİTESİ", font=font_baslik, fill=text_color)
    draw.text((990, 200 + y_offset), "FEN-EDEBİYAT FAKÜLTESİ", font=font_baslik, fill=text_color)
    draw.text((910, 200 + 2 * y_offset), "MATEMATİK BÖLÜM BAŞKANLIĞI'NA", font=font_baslik, fill=text_color)
    draw.text((920, 200 + 3 * y_offset), "ÇAKIŞAN DERS EKLEME DİLEKÇESİ", font=font_baslik, fill=text_color)

    # Tablo (Kişisel Bilgiler)
    table_x = 300
    table_y = 600
    cell_width = 1800
    cell_height = 75
    row_labels = ["Adı Soyadı", "Öğrenci Numarası", "Cep Telefonu", "e-posta"]
    values = [ad_soyad, ogrenci_no, cep_telefonu, eposta]

    line_x = table_x + 390
    line_start_y = table_y
    line_end_y = table_y + len(row_labels) * cell_height

    for i, (label, value) in enumerate(zip(row_labels, values)):
        y = table_y + i * cell_height
        draw.rectangle([(table_x, y), (table_x + cell_width, y + cell_height)], outline="black")
        draw.text((table_x + 10, y + 15), label, font=font, fill="black")
        draw.text((table_x + 410, y + 15), ":", font=font, fill="black")
        draw.text((table_x + 450, y + 15), value, font=font, fill="black")

    draw.line([(line_x, line_start_y), (line_x, line_end_y)], fill="black", width=1)

    # Metin
    metin_x = 300
    metin_y = table_y + len(row_labels) * cell_height + 200
    metin_font = ImageFont.truetype(font_path, 45)
    metin = (f"{egitim_yili} Eğitim-Öğretim yılı {yariyil} Yarıyılında daha önce alıp, F0 dışında bir not "
             f"\nile başarısız olduğum ders ile ilk defa alacağım ders çakışmaktadır. Aşağıda belirtilen dersin "
             f"\nöğrenci otomasyon sistemine işlenmesi için gereğini arz ederim.")
    draw.text((metin_x, metin_y), metin, font=metin_font, fill="black")

    # Ek metinler
    draw.text((metin_x, metin_y + 370), "Ek 1: Öğrenci transkripti", font=metin_font, fill="black")
    draw.text((metin_x, metin_y + 450), "Ek 2: OBS ders programı", font=metin_font, fill="black")

    # Ders Tablosu
    ders_table_x = 300
    ders_table_y = metin_y + 800
    ders_cell_height = 70
    kodu_width = 250
    adi_width = 650
    grubu_width = 200
    x_positions = [ders_table_x, ders_table_x + kodu_width, ders_table_x + kodu_width + adi_width,
                   ders_table_x + kodu_width * 2 + adi_width, ders_table_x + kodu_width * 2 + adi_width * 2]
    widths = [kodu_width, adi_width, kodu_width, adi_width, grubu_width]
    ders_row_labels = ["Kodu", "Adı", "Kodu", "Adı", "Grubu"]

    # Üst başlıklar
    draw.rectangle([(ders_table_x, ders_table_y - ders_cell_height), (ders_table_x + kodu_width + adi_width, ders_table_y)], outline="black")
    draw.text((ders_table_x + 10, ders_table_y - ders_cell_height + 15), "                OBS'den seçtiğim dersin", font=font_bold, fill="black")
    draw.rectangle([(ders_table_x + kodu_width + adi_width, ders_table_y - ders_cell_height),
                    (ders_table_x + kodu_width * 2 + adi_width * 2 + grubu_width, ders_table_y)], outline="black")
    draw.text((ders_table_x + kodu_width + adi_width + 10, ders_table_y - ders_cell_height + 15), "              Çakışma nedeniyle eklenecek ders", font=font_bold, fill="black")

    # Tablo başlıkları
    for i, (x, width, label) in enumerate(zip(x_positions, widths, ders_row_labels)):
        draw.rectangle([(x, ders_table_y), (x + width, ders_table_y + ders_cell_height)], outline="black")
        text_bbox = draw.textbbox((0, 0), label, font=font_bold)
        text_width = text_bbox[2] - text_bbox[0]
        text_x = x + (width - text_width) // 2
        text_y = ders_table_y + (ders_cell_height - (text_bbox[3] - text_bbox[1])) // 2
        draw.text((text_x, text_y), label, font=font_bold, fill="black")

    # Ders satırları
    for i, ders in enumerate(dersler):
        y = ders_table_y + (i + 1) * ders_cell_height
        values = [ders["kodu1"], ders["adi1"], ders["kodu2"], ders["adi2"], ders["grubu"]]
        for j, (x, width, value) in enumerate(zip(x_positions, widths, values)):
            draw.rectangle([(x, y), (x + width, y + ders_cell_height)], outline="black")
            if value:  # Boş değilse yaz
                text_bbox = draw.textbbox((0, 0), value, font=font)
                text_width = text_bbox[2] - text_bbox[0]
                text_x = x + (width - text_width) // 2
                text_y = y + (ders_cell_height - (text_bbox[3] - text_bbox[1])) // 2
                draw.text((text_x, text_y), value, font=font, fill="black")

    # Resmi kaydet
    output_path = "Dilekce_a4_formati.jpg"
    a4_image.save(output_path)
    return output_path

@app.route('/')
def index():
    return send_file('index.html')

@app.route('/form-gonder', methods=['POST'])
def form_gonder():
    # Form verilerini al
    ad_soyad = request.form['adSoyad']
    ogrenci_no = request.form['ogrenciNo']
    cep_telefonu = request.form['cepTelefonu']
    eposta = request.form['eposta']
    egitim_yili = request.form['egitimYili']
    yariyil = request.form['yariyil']

    # Ders bilgilerini al
    dersler = []
    for i in range(3):  # 3 satır ders var
        kodu1 = request.form.get(f'dersler[{i}][kodu1]', '')
        adi1 = request.form.get(f'dersler[{i}][adi1]', '')
        kodu2 = request.form.get(f'dersler[{i}][kodu2]', '')
        adi2 = request.form.get(f'dersler[{i}][adi2]', '')
        grubu = request.form.get(f'dersler[{i}][grubu]', '')
        if kodu1 or adi1 or kodu2 or adi2 or grubu:  # En az biri doluysa ekle
            dersler.append({"kodu1": kodu1, "adi1": adi1, "kodu2": kodu2, "adi2": adi2, "grubu": grubu})

    # Dilekçeyi oluştur
    output_path = create_petition(ad_soyad, ogrenci_no, cep_telefonu, eposta, egitim_yili, yariyil, dersler)

    # Oluşturulan dosyayı kullanıcıya gönder
    return send_file(output_path, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)