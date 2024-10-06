#api là một module trong odoo, giúp chúng ta tương tác với dữ liệu trong database
#fields giúp chúng ta khai báo các trường trong database
#models giúp chúng ta tạo các model trong odoo
#tools giúp chúng ta tương tác với các công cụ trong odoo
from odoo import api, fields, models, tools, _
class Player(models.Model):
    _name = "player" #tên bảng trong database
    _description = "Bảng chứa thông tin player"
    #khai báo các trường trong bảng player 
    name = fields.Char(string="Name", required=True) 
    image = fields.Binary(string="Image") 
    gender = fields.Selection([('male','female')], string='Gender', default='male') 
    phone = fields.Char(string="Phone")
    email = fields.Char(string="Email")
    day_of_birth = fields.Datetime(string="Day of birth")