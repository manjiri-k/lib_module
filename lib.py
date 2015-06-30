from openerp.osv import fields, osv

class lib_lib(osv.osv):
    _name="lib.lib"
    _rec_name="Lib_branch"
    
    _columns={'Lib_branch':fields.selection(string="Name of branch",selection=[('patel nagar','patel nagar'),('karol baugh','karol baugh'),('Rajiv Chowk','Rajiv Chowk')]),
               'Building_no':fields.char(string='Name of library',size=50),
              'street_number':fields.float(string="Marks",digits=(4,2)),
              'Landmark':fields.text(string="Landmark"),
              'pincode':fields.integer("pin_code",size=6),
              'books_in_lib':fields.many2one('books.books',string="Books")}
    _defaults={'Lib_branch':'patel nagar',
               'Building_no':"27/A",
              'street_number':12,
              'Landmark':"Rajiv metro station",
              'pincode':123456
               }

class books_books(osv.osv):
    _name='books.books'  
    _columns={"name":fields.char(string='book name'),
              "author":fields.char(string="author of the book"),
              "book_lib_no":fields.float(string="library book number"),
              "book_on_shelf":fields.boolean(string="book on shelf"),
              "issued_date":fields.date(string="book issued on"),
              "returned_date":fields.datetime(string="date returned"),
              'book_available_in':fields.one2many('lib.lib','books_in_lib',string="Libraries for this book"),
              }
    

    