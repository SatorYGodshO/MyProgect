from kivy.uix.boxlayout import BoxLayout
from kivy.metrics import dp
from kivy.properties import StringProperty
from kivy.uix.button import Button
from kivymd.app import MDApp
from kivymd.uix.textfield import MDTextField
import json



class Conteiner(BoxLayout):
    def table( self, item ):
        self.lenn = len(Case.dict_name)
        self.tables.clear_widgets( )
        self.it_for_calc_doc = iter( Case.dict_doc )
        self.it_for_calc_sklad = iter( Case.dict_sklad )
        self.it_name = iter( Case.dict_name )
        self.it_doc = iter( Case.dict_doc )
        self.it_sklad = iter( Case.dict_sklad )
        self.tables.add_widget(
            ItemTable(
                name = str( "Наименование" ),
                base = str( "Документально" ),
                stock = str( "На складе" ),
                write = str( "Подлежит списанию" )
            )
        )

        for i in range(self.lenn):

            self.tables.add_widget(
                ItemTable(
                    name = str( Case.name( self ) ),
                    base = str( Case.doc( self ) ),
                    stock =str(Case.sklad( self )),
                    write = str(Case.calc(self)),
                    butts = str("Изменить"),
                    itemes = str(i+1)
                    )
            )
    def table2(self):
        self.lenn = len(Case.dict_name)
        self.tables2.clear_widgets( )
        self.it_for_calc_doc = iter( Case.dict_doc )
        self.it_for_calc_sklad = iter( Case.dict_sklad )
        self.it_for_calc_sklad2 = iter(Case.dict_sklad)
        self.it_for_calc_sklad3 = iter(Case.dict_sklad)
        self.it_name = iter( Case.dict_name )
        self.it_doc = iter( Case.dict_doc )
        self.it_sklad = iter( Case.dict_sklad )
        self.it_value_opt = iter(Case.dict_value_opt)
        self.it_value_sell = iter(Case.dict_value_sell)
        self.it_value_opt_for_calc = iter(Case.dict_value_opt)
        self.it_sklad_calc2 = iter(Case.dict_sklad)
        self.it_value_sell_for_calc = iter(Case.dict_value_sell)
        self.it_sklad_calc3 = iter(Case.dict_sklad)
        self.it_for_calc_dict_sell = iter(Case.dict_value_sell)
        self.it_for_calc_dict_opt = iter(Case.dict_value_opt)
        self.tables2.add_widget(
            ItemTable2(
                name = str( "Наименование" ),
                base = str( "Цена оптом" ),
                stock = str( "Цена при продаже" ),
                qwertt = str("Цена на продажу"),
                write = str( "Цена на складе" ),
                value = str("Розничная цена")
            )
        )
        for i in range(self.lenn):

            self.tables2.add_widget(
                ItemTable2(
                    name = str( Case.name( self ) ),
                    base = str( Case.value_opt( self ) + " BYN"),
                    stock =str(Case.value_sell(self) + " BYN"),
                    qwertt = str(str(round(Case.value_calc_sel(self), 2)) + " BYN"),
                    write = str(str(round(Case.value_calc_opt(self), 2)) + " BYN"),
                    value = str(str(round(Case.value_value(self), 2)) + " BYN")

                    )
            )
    def text_input( self):
        self.hint_name = "Наименование"
        self.hint_doc = "Документально"
        self.hint_opt = "Цена Оптом"
        self.hint_sell = "Цена продажи"
        self.hint_sklad = "На складе"

        self.text_fild.clear_widgets()
        self.text_inputs_name = MDTextField(
            pos_hint= { "center_y": .2 },
            hint_text=  self.hint_name
        )
        self.text_inputs_doc = MDTextField(
            pos_hint = { "center_y": .6 },
            hint_text = self.hint_doc
        )
        self.text_inputs_opt = MDTextField(
            pos_hint={"center_y": .1},
            hint_text = self.hint_opt
        )
        self.text_inputs_sell = MDTextField(
            pos_hint={"center_y": .6},
            hint_text= self.hint_sell
        )
        self.text_inputs_sklad = MDTextField(
            pos_hint = { "center_y": .4 },
            hint_text= self.hint_sklad
        )
        self.text_fild.add_widget(
            self.text_inputs_name
        )
        self.text_fild.add_widget(
            self.text_inputs_doc
        )
        self.text_fild.add_widget(
            self.text_inputs_sell
        )
        self.text_fild.add_widget(
            self.text_inputs_opt
        )
        self.text_fild.add_widget(
            self.text_inputs_sklad
        )
        self.text_fild.add_widget(
            Button(
                size_hint_y = None,
                text= "Добавить",
                padding= "40dp",
                height= dp(30),
                on_press = self.appendes
            )
        )
    def on_text( self, instance, value ):
        self.on_text.text = print( self.on_text )
    def appendes( self, instance ):
        if self.text_inputs_name.text != "":
            Case.dict_name.append(self.text_inputs_name.text)
            Case.dict_doc.append( self.text_inputs_doc.text )
            Case.dict_sklad.append( self.text_inputs_sklad.text )
            Case.dict_value_opt.append(self.text_inputs_opt.text)
            Case.dict_value_sell.append(self.text_inputs_sell.text)
    def text_del( self ):
        self.hint_del = "Наименование"
        self.text_fild1.clear_widgets()
        self.text_inputs_name = MDTextField(
            pos_hint = { "center_y": .4 },
            hint_text=  self.hint_del

        )
        self.text_fild1.add_widget(
            self.text_inputs_name
        )
        self.text_fild1.add_widget(
            Button(
                size_hint_y = None,
                text = "Удалить",
                padding = "40dp",
                height = dp( 30 ),
                on_press = self.dell
            )
        )
    def dell( self, *args ):
        if self.text_inputs_name.text in Case.dict_name:
            index = Case.dict_name.index(self.text_inputs_name.text)
            del Case.dict_name[index]
            del Case.dict_doc[ index ]
            del Case.dict_sklad[index]
            del Case.dict_value_opt[index]
            del Case.dict_value_sell[index]
        else:
            self.text_inputs_name.text = "Такого наименования нету"

    def edit_text( self, *args ):
        self.text_fild2.clear_widgets( )
        self.text_inputs_name = MDTextField(
            pos_hint = { "center_y": .2 },
            hint_text = "Наименование старое"
        )
        self.text_inputs_name2= MDTextField(
            pos_hint = { "center_y": .8 },
            hint_text = "Наименование новое"
        )
        self.text_inputs_doc2 = MDTextField(
            pos_hint = { "center_y": .6 },
            hint_text = "Документально"
        )
        self.text_inputs_sklad2= MDTextField(
            pos_hint = { "center_y": .4 },
            hint_text = "На складе"
        )
        self.text_inputs_opt2 = MDTextField(
            pos_hint={"center_y": .4},
            hint_text="Оптовая цена"
        )
        self.text_inputs_sell2 = MDTextField(
            pos_hint={"center_y": .4},
            hint_text=  "Цена при реализации"
        )
        self.text_fild2.add_widget(
            self.text_inputs_name
        )
        self.text_fild2.add_widget(
            self.text_inputs_name2
        )
        self.text_fild2.add_widget(
            self.text_inputs_doc2
        )
        self.text_fild2.add_widget(
            self.text_inputs_sklad2
        )
        self.text_fild2.add_widget(
            self.text_inputs_sell2
        )
        self.text_fild2.add_widget(
            self.text_inputs_opt2
        )
        self.text_fild2.add_widget(
            Button(
                size_hint_y = None,
                text = "Изменить",
                padding = "40dp",
                height = dp( 30 ),

                on_press = self.edit
            )
        )
    def edit(self, *args):

        if self.text_inputs_name.text in Case.dict_name:
            index = Case.dict_name.index( self.text_inputs_name.text )
            if self.text_inputs_name2.text != "":
                Case.dict_name[index] = self.text_inputs_name2.text
            if self.text_inputs_doc2.text != "":
                Case.dict_doc[index] = self.text_inputs_doc2.text
            if self.text_inputs_sklad2.text != "":
                Case.dict_sklad[index] = self.text_inputs_sklad2.text
            if self.text_inputs_opt2.text != "":
                Case.dict_value_opt[index] = self.text_inputs_opt2.text
            if self.text_inputs_sell2.text != "":
                Case.dict_value_sell[index] = self.text_inputs_sell2.text

        else:
            self.text_inputs_name.text = "Такого наименования нету"
class ItemTable2( BoxLayout):
    itemes = StringProperty()
    value = StringProperty()
    butts = StringProperty()
    name = StringProperty( )
    base = StringProperty( )
    stock = StringProperty( )
    write = StringProperty( )
    qwertt = StringProperty()
class ItemTable( BoxLayout):
    itemes = StringProperty()
    butts = StringProperty()
    name = StringProperty( )
    base = StringProperty( )
    stock = StringProperty( )
    write = StringProperty( )
class Case:
    dict_name = []
    dict_doc = []
    dict_sklad = []
    dict_value_opt = []
    dict_value_sell = []
    x = ""
    def load(self):
        with open("data_name.json", "r") as load_file1:
            print(load_file1)
            self.dict_name = json.load(load_file1)
        with open("data_doc.json", "r") as load_file2:
            self.dict_doc = json.load(load_file2)
        with open("data_sklad.json", "r") as load_file3:
            self.dict_sklad = json.load(load_file3)
        with open("dict_opt.json", "r") as load_file4:
            print(load_file4)
            self.dict_value_opt = json.load(load_file4)
        with open("dict_sell.json", "r") as load_file5:
            self.dict_value_sell = json.load(load_file5)
    def save(self):
        with open("data_name.json", "w") as write_file1:
            json.dump(self.dict_name, write_file1)
        with open("data_doc.json", "w") as write_file2:
            json.dump(self.dict_doc, write_file2)
        with open("data_sklad.json", "w") as write_file3:
            json.dump(self.dict_sklad, write_file3)
        with open("dict_opt.json", "w") as write_file4:
            json.dump(self.dict_value_opt, write_file4)
        with open("dict_sell.json", "w") as write_file5:
            json.dump(self.dict_value_sell, write_file5)
    def value_calc_sel(self):
        self.item13 = float(next(self.it_for_calc_sklad2)) * float(next(self.it_for_calc_dict_sell))
        return self.item13
    def value_calc_opt(self):
        self.item12 = float(next(self.it_for_calc_sklad3)) * float(next(self.it_for_calc_dict_opt))
        return self.item12
    def value_value(self):
        item = self.item13 - self.item12
        return item
    def value_for_sell(self, item, *args):
        if item == 1:
            self.item = float(next(self.it_value_opt_for_calc)) * int(self.it_sklad_calc2)
            return self.item
    def value_sell(self, *args):
        item = next(self.it_value_sell)
        return  item
    def value_opt(self, *args):
        item = next(self.it_value_opt)
        return item
    def sklad( self, *args ):
        item = next( self.it_sklad )
        return item
    def doc( self, *args ):
        item = next( self.it_doc )
        return item
    def name( self, *args ):
        item = next( self.it_name)
        return item
    def calc( self, *args ):
        item = int(next(self.it_for_calc_doc)) - int(next(self.it_for_calc_sklad))
        return item
class BarAPP( MDApp ):

    def build( self ):
        self.theme_cls.material_style = "M3"
        self.theme_cls.theme_style = "Dark"
        Case.load(Case)
        return Conteiner( )

    def __del__(self):
        print("Вызов __Del__")
        Case.save(Case)

if __name__ == "__main__":
    BarAPP( ).run( )