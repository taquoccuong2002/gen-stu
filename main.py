from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import random
import datetime
import vn_fullname_generator as generator


#open chrome browser at http://tn.ntt.edu.vn/XemKetQuaHocTap.aspx?MenuID=354
import random
from datetime import datetime, timedelta

import random
from datetime import datetime
from faker import Faker

faker = Faker()

student_class = ["Công nghệ thông tin", "Kinh tế", "Xã hội học", "Y dược", "Ngôn ngữ Anh", "Quản trị kinh doanh", "Kế toán", "Luật", "Giáo dục", "Nông nghiệp"]
major_code = ['CNTT','KT','XHH','YD','NN','QTKD','KT','L','GD','NN']
def generate_student_info():
    name = generator.generate(random.randint(0,1))
    code = random.randint(0,len(student_class)-1)
    major = student_class[code]
    birthdate = datetime(random.randint(2000, 2005), random.randint(1, 12), random.randint(1, 28))
    class_ = f"{birthdate.year % 100 + 20}{major_code[code]}{random.randint(1000, 9999)}"
    student_id = f"{random.randint(10000000, 99999999)}"
    convert_day = birthdate.strftime('%d/%m/%Y')
    return student_id, name, class_, major, convert_day
#add text to image

def generation_stu_id(school_code):
    School = {"UEH": "University of Economics\n       Ho Chi Minh City".center(30),
              "UIT": "         University of \nInformation Technology",
              "HCMUS": "    Ho Chi Minh City \nUniversity of Science",
              "FPT": "FPT University",
              "HCMUSSH": "        Ho Chi Minh City \nUniversity of Social Sciences\n         and Humanities",
                "HCMUTE": "     Ho Chi Minh City \nUniversity of Technology \n      and Education",

              }
    school_name = School[school_code]

    # Importing Image module from PIL package
    from PIL import Image, ImageEnhance
    im1 = Image.open(r"NTTCard-Recovered-Recovered-Recovered.jpg")
    # create white background same size as im1
    #open random image in folder hinh
    import random
    import os
    path = "hinh"
    list_file = os.listdir(path)
    random_file = random.choice(list_file)
    im2 = Image.open("hinh/{0}".format(random_file))
    im2 = im2.resize((777, 997))
    im2 = im2.convert("RGBA")

    # pasting im2 on im1
    im2.putalpha(ImageEnhance.Brightness(im2.split()[3]).enhance(0.85))
    new = Image.new('RGBA', im1.size, (255, 255, 255, 255))
    new_w, new_h = new.size
    offset = ((new_w - im1.size[0]) // 2, (new_h - im1.size[1]) // 2)
    new.paste(im1, offset)
    new.paste(im2, (1211,1611),im2)

    I1 = ImageDraw.Draw(new)

    # Custom font style and font size
    myFont = ImageFont.truetype('Arial.ttf', 130)
    student_id, name, class_, major, convert_day = generate_student_info()

    # Add Text to an image
    I1.text((1560, 2765), name, font=myFont, fill=(255, 0, 0),stroke_width=3,stroke_fill='red',anchor='mm')
    #auto wrap text
    I1.text((1561, 857), school_name, font=myFont, fill=(0, 0, 0),stroke_width=3,anchor='mm')
    myFont = ImageFont.truetype('Arial.ttf', 105)
    I1.text((857, 2860), student_id, font=myFont, fill=(0, 0, 0),stroke_width=1)
    I1.text((857, 3077), class_, font=myFont, fill=(0, 0, 0),stroke_width=1)
    I1.text((857, 3273), major, font=myFont, fill=(0, 0, 0),stroke_width=1)
    I1.text((1965, 2870), convert_day, font=myFont, fill=(0, 0, 0),stroke_width=1)
    new.convert('RGB').save('new.jpg')
#ceate api user input email -> get student id -> get info -> generate image -> show image
from flask import Flask, request, jsonify, send_file
app = Flask(__name__)
@app.route('/api', methods=['GET'])
def api():
    school_code = request.args.get('school_code')
    try:
        generation_stu_id(school_code)
        return send_file('new.jpg', mimetype='image/jpg')
    except:
        return Exception
if __name__ == '__main__':
    app.run(host = '0.0.0.0')

