from kivy.metrics import dp
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager
from kivy.uix.scrollview import ScrollView
from kivy.uix.stacklayout import StackLayout

from datetime import datetime, date
from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivymd.uix.anchorlayout import MDAnchorLayout
from kivymd.uix.behaviors import CommonElevationBehavior
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDIconButton
from kivymd.uix.card import MDCard
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.label import MDLabel

from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.pickers import MDDatePicker

from kivymd.uix.selectioncontrol.selectioncontrol import MDCheckbox
from kivymd.uix.snackbar import MDSnackbar

from DataBase import Database
from DataBase2 import Database2
from DataBase3 import Database3
from DataBase4 import Database4
from DataBase5 import Database5
db = Database()
db2 = Database2()
db3 = Database3()
db4 = Database4()
db5 = Database5()

from KV import KV
import json
Builder.load_string(KV)

from kivymd.uix.screen import MDScreen
from kivy.uix.screenmanager import NoTransition

from kivy.core.window import Window
Window.size = (510, 840)

from kivymd.uix.pickers import MDDatePicker # Here, instead of kivymd,uix.picker

# add the following just under the imports
if platform == "android":
    from android.permissions import request_permissions, Permission
    request_permissions([Permission.READ_EXTERNAL_STORAGE, Permission.WRITE_EXTERNAL_STORAGE])


class TaskScreen(MDScreen):
    pass

class NewTaskScreen(MDScreen):
    pass
class NewQuestScreen(MDScreen):
    pass
class NewProfileScreen(MDScreen):
    pass
class TaskLayout(ScrollView):
    pass
class QuestScreen(MDScreen):
    pass
class PassiveScreen(MDScreen):
    pass
class CalendarScreen(MDScreen):
    pass

class ProfileScreen(MDScreen):
    lvl_text = '0'
    value_text = 0
    max_text = 1000

class NavigationBar(CommonElevationBehavior, MDBoxLayout):
    pass



class DemoApp(MDApp):

    profile_name = "Name: None"
    profile_title = "Title: None"
    profile_job = "Job: None"
    profile_grl = "Girlfriend: None"
    profile_goal = "Goal: None"
    profile_law1 = "1: None"
    profile_law2 = "2: None"
    profile_law3 = "3: None"
    profile_law4 = "4: None"
    profile_law5 = "5: None"
    profile_law6 = "6: None"
    profile_law7 = "7: None"



    def build(self):
        self.theme_cls.theme_style = 'Dark'

        date = datetime.now()
        date_2 = date.today()

        data_get = db5.get_data()
        if data_get != []:
            if data_get[-1][1] != int(date_2.day):
                self.task_incompleted()
                db5.delete_date(data_get[-1][0])
                db5.create_data(int(date_2.day))
        else:
            self.task_incompleted()
            db5.create_data(int(date_2.day))

        self.text_day = date.strftime("%A").lower()
        self.button_text_day = self.text_day.capitalize()

        self.sm = ScreenManager(transition=NoTransition())
        self.sm.add_widget(TaskScreen(name='taskscreen'))
        self.sm.add_widget(QuestScreen(name='questscreen'))
        self.sm.add_widget(PassiveScreen(name='passivescreen'))
        self.sm.add_widget(CalendarScreen(name='calendarscreen'))
        self.sm.add_widget(ProfileScreen(name='profilescreen'))
        self.sm.add_widget(NewProfileScreen(name='newprofile'))
        self.sm.add_widget(NewTaskScreen(name='newtask'))
        self.sm.add_widget(NewQuestScreen(name='newquest'))


        self.current_task_day = date.strftime("%A").lower()
        self.build_task(self.text_day)
        self.build_quest()
        self.build_profile()
        self.build_level()
        return self.sm



    def new_task_name(self):
        print(self.sm.get_screen('newtask').ids.task_name.text)
        print(self.sm.get_screen('newtask').ids.task_exp.text)
        if self.sm.get_screen('newtask').ids.task_name.text != '' and self.sm.get_screen('newtask').ids.task_exp.text != '' and self.sm.get_screen('newtask').ids.task_exp.text.isnumeric():
            if int(self.sm.get_screen('newtask').ids.task_exp.text) <= 500:
                if self.sm.get_screen('newtask').ids.monday_switch.active:
                    db.create_task(self.sm.get_screen('newtask').ids.task_name.text,
                                   self.sm.get_screen('newtask').ids.task_exp.text, "monday")
                if self.sm.get_screen('newtask').ids.tuesday_switch.active:
                    db.create_task(self.sm.get_screen('newtask').ids.task_name.text,
                                   self.sm.get_screen('newtask').ids.task_exp.text, "tuesday")
                if self.sm.get_screen('newtask').ids.wednesday_switch.active:
                    db.create_task(self.sm.get_screen('newtask').ids.task_name.text,
                                   self.sm.get_screen('newtask').ids.task_exp.text, "wednesday")
                if self.sm.get_screen('newtask').ids.thursday_switch.active:
                    db.create_task(self.sm.get_screen('newtask').ids.task_name.text,
                                   self.sm.get_screen('newtask').ids.task_exp.text, "thursday")
                if self.sm.get_screen('newtask').ids.friday_switch.active:
                    db.create_task(self.sm.get_screen('newtask').ids.task_name.text,
                                   self.sm.get_screen('newtask').ids.task_exp.text, "friday")
                if self.sm.get_screen('newtask').ids.saturday_switch.active:
                    db.create_task(self.sm.get_screen('newtask').ids.task_name.text,
                                   self.sm.get_screen('newtask').ids.task_exp.text, "saturday")
                if self.sm.get_screen('newtask').ids.sunday_switch.active:
                    db.create_task(self.sm.get_screen('newtask').ids.task_name.text,
                                   self.sm.get_screen('newtask').ids.task_exp.text, "sunday")



        self.sm.get_screen('newtask').ids.task_name.text = ''
        self.sm.get_screen('newtask').ids.task_exp.text = ''
        self.sm.get_screen('newtask').ids.monday_switch.active = False
        self.sm.get_screen('newtask').ids.tuesday_switch.active = False
        self.sm.get_screen('newtask').ids.wednesday_switch.active = False
        self.sm.get_screen('newtask').ids.thursday_switch.active = False
        self.sm.get_screen('newtask').ids.friday_switch.active = False
        self.sm.get_screen('newtask').ids.saturday_switch.active = False
        self.sm.get_screen('newtask').ids.sunday_switch.active = False
    def build_task(self, day):
        tasks = db.get_tasks()

        self.scroll = ScrollView(do_scroll_y=True, pos_hint={'center_y': .55}, size_hint=(1, .75))
        anchor_lay = MDAnchorLayout(size_hint_y=None, anchor_y='top', height=dp(1500))
        stack_lay = StackLayout(padding=dp(10), spacing=dp(10), size_hint_y=None)
        anchor_lay.add_widget(stack_lay)
        self.scroll.add_widget(anchor_lay)
        self.sm.get_screen('taskscreen').add_widget(self.scroll)

        for task in tasks:
            if task[3] == day:
                date = datetime.now()

                if day == date.strftime("%A").lower():
                    if task[4] == 0:
                        float_lay = MDFloatLayout()
                        check = MDCheckbox(pos_hint={'center_x': .065, 'center_y': .5}, size_hint=(None, None),
                                           size=(dp(64), dp(64)), id=str(task[0]), group=str(task[2]),
                                           on_press=self.task_press, disabled_color='lightgrey')
                        card = MDCard(radius=[16], pos_hint={'center_x': .5, 'center_y': .5}, elevation=2,
                                      shadow_softness=4,
                                      shadow_offset=(2, -2))
                        label_name = Label(text=str(task[1]), strikethrough=False, text_size=(dp(300), None),
                                           font_size=dp(25), bold=True, pos_hint={'center_x': .45, 'center_y': .53})
                        label_exp = Label(text=str(task[2]), text_size=(dp(300), None), font_size=dp(10), bold=True,
                                          pos_hint={'center_x': .455, 'center_y': .3})
                        del_button = MDIconButton(icon='trash-can-outline', pos_hint={'center_x': .9, 'center_y': .5},
                                                  id=str(task[0]),
                                                  on_press=self.del_task)
                        float_lay.add_widget(card)
                        check.color_active = 'grey'
                        float_lay.add_widget(check)
                        float_lay.add_widget(label_name)
                        float_lay.add_widget(label_exp)
                        float_lay.add_widget(del_button)
                        stack_lay.add_widget(float_lay)
                    elif task[4] == 1:
                        float_lay = MDFloatLayout()
                        check = MDCheckbox(pos_hint={'center_x': .065, 'center_y': .5}, size_hint=(None, None),
                                           size=(dp(64), dp(64)), id=str(task[0]), group=str(task[2]),
                                           on_press=self.task_press, disabled_color='lightgrey', active=True)
                        card = MDCard(radius=[16], pos_hint={'center_x': .5, 'center_y': .5}, elevation=2,
                                      shadow_softness=4,
                                      shadow_offset=(2, -2))
                        label_name = Label(text=str(task[1]), strikethrough=False, text_size=(dp(300), None),
                                           font_size=dp(25), bold=True, pos_hint={'center_x': .45, 'center_y': .53})
                        label_exp = Label(text=str(task[2]), text_size=(dp(300), None), font_size=dp(10), bold=True,
                                          pos_hint={'center_x': .455, 'center_y': .3})
                        del_button = MDIconButton(icon='trash-can-outline', pos_hint={'center_x': .9, 'center_y': .5},
                                                  id=str(task[0]),
                                                  on_press=self.del_task)
                        float_lay.add_widget(card)
                        check.color_active = 'grey'
                        float_lay.add_widget(check)
                        float_lay.add_widget(label_name)
                        float_lay.add_widget(label_exp)
                        float_lay.add_widget(del_button)
                        stack_lay.add_widget(float_lay)
                else:
                    float_lay = MDFloatLayout()
                    check = MDCheckbox(pos_hint={'center_x': .065, 'center_y': .5}, size_hint=(None, None),
                                       size=(dp(64), dp(64)), id=str(task[0]), group=str(task[2]),
                                       on_press=self.task_press, disabled_color='lightgrey', active=True)
                    card = MDCard(radius=[16], pos_hint={'center_x': .5, 'center_y': .5}, elevation=2,
                                  shadow_softness=4,
                                  shadow_offset=(2, -2))
                    label_name = Label(text=str(task[1]), strikethrough=False, text_size=(dp(300), None),
                                       font_size=dp(25), bold=True, pos_hint={'center_x': .45, 'center_y': .53})
                    label_exp = Label(text=str(task[2]), text_size=(dp(300), None), font_size=dp(10), bold=True,
                                      pos_hint={'center_x': .455, 'center_y': .3})
                    del_button = MDIconButton(icon='trash-can-outline', pos_hint={'center_x': .9, 'center_y': .5},
                                              id=str(task[0]),
                                              on_press=self.del_task)
                    float_lay.add_widget(card)
                    check.color_active = 'grey'
                    float_lay.add_widget(check)
                    float_lay.add_widget(label_name)
                    float_lay.add_widget(label_exp)
                    float_lay.add_widget(del_button)
                    stack_lay.add_widget(float_lay)


    def delete_task_lay(self):
        self.sm.get_screen('taskscreen').remove_widget(self.scroll)

    def task_press_fake(self, instance):
        instance.active = True

    def task_press(self, instance):
        print(instance.id)
        print(instance.group)
        db.mark_task_as_complete(instance.id)
        print(instance.active)
        if instance.active == True:
            level_list = db4.get_lvl()
            if level_list != []:
                self.lvl_text = level_list[-1][0]
                self.my_max = level_list[-1][2]
                self.my_value = level_list[-1][1]
            else:
                self.lvl_text = '0'
                self.my_max = 1000
                self.my_value = 0

            self.my_value += int(instance.group)
            while self.my_value >= self.my_max:
                self.my_value = self.my_value - self.my_max
                self.lvl_text = str(int(self.lvl_text) + 1)
                if int(self.lvl_text) >= 5:
                    self.my_max = 1000
                elif int(self.lvl_text) >= 10:
                    self.my_max = 2000
                elif int(self.lvl_text) >= 15:
                    self.my_max = 2500
                elif int(self.lvl_text) >= 20:
                    self.my_max = 3500
                elif int(self.lvl_text) >= 25:
                    self.my_max = 4000
                elif int(self.lvl_text) >= 30:
                    self.my_max = 5000
                elif int(self.lvl_text) >= 35:
                    self.my_max = 5500
                elif int(self.lvl_text) >= 40:
                    self.my_max = 6500
                elif int(self.lvl_text) >= 45:
                    self.my_max = 7000
                elif int(self.lvl_text) >= 50:
                    self.my_max = 8000

            instance.active = True
            db4.delete_db()
            db4.create_level_table()
            db4.create_level(self.lvl_text, self.my_value, self.my_max)

            self.sm.get_screen('profilescreen').ids.progressbar.max = self.my_max
            self.sm.get_screen('profilescreen').ids.progressbar.value = self.my_value
            self.sm.get_screen('profilescreen').ids.lvl_text.text = self.lvl_text


            self.delete_task_lay()
            self.build_task(self.text_day)
            self.build_level()




        self.delete_task_lay()
        self.build_task(self.text_day)

    def del_task(self, instance):
        print(instance.id)
        db.delete_task(instance.id)

        self.delete_task_lay()
        self.build_task(self.text_day)


    def task_incompleted(self):
        tasks = db.get_tasks()
        for task in tasks:
            db.mark_task_as_incomplete(task[0])


    def menu_open(self):
        self.menu_items = [
            {
                "text": f"Monday",
                "on_release": lambda x=f"monday": self.menu_callback(x),
            },
            {
                "text": f"Tuesday",
                "on_release": lambda x=f"tuesday": self.menu_callback(x),
            },
            {
                "text": f"Wednesday",
                "on_release": lambda x=f"wednesday": self.menu_callback(x),
            },
            {
                "text": f"Thursday",
                "on_release": lambda x=f"thursday": self.menu_callback(x),
            },
            {
                "text": f"Friday",
                "on_release": lambda x=f"friday": self.menu_callback(x),
            },
            {
                "text": f"Saturday",
                "on_release": lambda x=f"saturday": self.menu_callback(x),
            },
            {
                "text": f"Sunday",
                "on_release": lambda x=f"sunday": self.menu_callback(x),
            }
        ]
        self.drop_menu = MDDropdownMenu(
                caller=self.sm.get_screen('taskscreen').ids.button, items=self.menu_items
            )
        self.drop_menu.open()



    def menu_callback(self, text_item):
        print(text_item)
        self.drop_menu.dismiss()
        self.text_day = text_item
        if self.text_day == 'monday':
            self.sm.get_screen('taskscreen').remove_widget(self.scroll)
            self.build_task('monday')
            self.current_task_day = 'monday'
            self.sm.get_screen('taskscreen').ids.button.text = 'Monday'
        elif self.text_day == 'tuesday':
            self.sm.get_screen('taskscreen').remove_widget(self.scroll)
            self.build_task('tuesday')
            self.current_task_day = 'tuesday'
            self.sm.get_screen('taskscreen').ids.button.text = 'Tuesday'
        elif self.text_day == 'wednesday':
            self.sm.get_screen('taskscreen').remove_widget(self.scroll)
            self.build_task('wednesday')
            self.current_task_day = 'wednesday'
            self.sm.get_screen('taskscreen').ids.button.text = 'Wednesday'
        elif self.text_day == 'thursday':
            self.sm.get_screen('taskscreen').remove_widget(self.scroll)
            self.build_task('thursday')
            self.current_task_day = 'thursday'
            self.sm.get_screen('taskscreen').ids.button.text = 'Thursday'
        elif self.text_day == 'friday':
            self.sm.get_screen('taskscreen').remove_widget(self.scroll)
            self.build_task('friday')
            self.current_task_day = 'friday'
            self.sm.get_screen('taskscreen').ids.button.text = 'Friday'
        elif self.text_day == 'saturday':
            self.sm.get_screen('taskscreen').remove_widget(self.scroll)
            self.build_task('saturday')
            self.current_task_day = 'saturday'
            self.sm.get_screen('taskscreen').ids.button.text = 'Saturday'
        elif self.text_day == 'sunday':
            self.sm.get_screen('taskscreen').remove_widget(self.scroll)
            self.build_task('sunday')
            self.current_task_day = 'sunday'
            self.sm.get_screen('taskscreen').ids.button.text = 'Sunday'

    # Data Picker
    def on_save(self, instance, value, date_range):
        '''
        Events called when the "OK" dialog box button is clicked.

        :type instance: <kivymd.uix.picker.MDDatePicker object>;
        :param value: selected date;
        :type value: <class 'datetime.date'>;
        :param date_range: list of 'datetime.date' objects in the selected range;
        :type date_range: <class 'list'>;
        '''
        self.sm.get_screen('newquest').ids.date_button.text = str(value)
        print(value)

    def on_cancel(self, instance, value):
        '''Events called when the "CANCEL" dialog box button is clicked.'''


    def show_date_picker(self):
        date_dialog = MDDatePicker(
            primary_color='#444444',
            selector_color='#444444',
            text_button_color=(1, 1, 1, 1),
            text_current_color="white",
        )
        date_dialog.bind(on_save=self.on_save, on_cancel=self.on_cancel)
        date_dialog.open()
        #print("'_anim_alpha', '_anim_duration', '_background_origin', '_background_x', '_background_y', '_calendar_layout', '_date_label_text', '_input_date_dialog_open', '_is_open', '_md_bg_color', '_origin_line_color', '_origin_md_bg_color', '_scale_calendar_layout', '_scale_x', '_scale_y', '_scale_year_layout', '_shift_dialog_height', '_window', 'accent_color', 'anchor_x', 'anchor_y', 'angle', 'attach_to', 'auto_dismiss', 'background', 'background_color', 'background_hue', 'background_origin', 'background_palette', 'border', 'center', 'center_x', 'center_y', 'children', 'cls', 'date_range_text_error', 'day', 'device_ios', 'disabled', 'elevation', 'font_name', 'height', 'helper_text', 'hide_duration', 'hide_transition', 'ids', 'input_field_background_color', 'input_field_background_color_focus', 'input_field_background_color_normal', 'input_field_cls', 'input_field_text_color', 'input_field_text_color_focus', 'input_field_text_color_normal', 'line_color', 'line_width', 'max_date', 'max_year', 'md_bg_color', 'min_date', 'min_year', 'mode', 'month', 'motion_filter', 'opacity', 'opposite_colors', 'overlay_color', 'padding', 'parent', 'pos', 'pos_hint', 'primary_color', 'radius', 'right', 'rotate_value_angle', 'rotate_value_axis', 'scale_value_center', 'scale_value_x', 'scale_value_y', 'scale_value_z', 'scale_x', 'scale_y', 'sel_day', 'sel_month', 'sel_year', 'selector_color', 'shadow_color', 'shadow_offset', 'shadow_radius', 'shadow_softness', 'shadow_softness_size', 'show_duration', 'show_transition', 'size', 'size_hint', 'size_hint_max', 'size_hint_max_x', 'size_hint_max_y', 'size_hint_min', 'size_hint_min_x', 'size_hint_min_y', 'size_hint_x', 'size_hint_y', 'specific_secondary_text_color', 'specific_text_color', 'text_button_color', 'text_color', 'text_current_color', 'text_toolbar_color', 'text_weekday_color', 'theme_cls', 'title', 'title_input', 'top', 'widget_style', 'width', 'x', 'y', 'year'")

    def new_quest_name(self):
        print(self.sm.get_screen('newquest').ids.quest_name.text)
        print(self.sm.get_screen('newquest').ids.quest_exp.text)
        db2.create_quest(self.sm.get_screen('newquest').ids.quest_name.text,
                         self.sm.get_screen('newquest').ids.quest_exp.text,
                         self.sm.get_screen('newquest').ids.date_button.text)

    def build_quest(self):
        quests = db2.get_quests()
        self.scroll2 = ScrollView(do_scroll_y=True, pos_hint={'center_y': .55}, size_hint=(1, .75))
        anchor_lay = MDAnchorLayout(size_hint_y=None, anchor_y='top', height=dp(1500))
        stack_lay = StackLayout(padding=dp(10), spacing=dp(10), size_hint_y=.1)
        anchor_lay.add_widget(stack_lay)
        self.scroll2.add_widget(anchor_lay)
        for quest in quests:
            float_lay = MDFloatLayout()
            check = MDIconButton(pos_hint={'center_x': .92, 'center_y': .285}, icon='check-bold',
                                 size_hint=(None, None),
                                 size=(dp(64), dp(64)), id=str(quest[2]), text=str(quest[0]), on_press=self.quest_press)
            card = MDCard(radius=[16], pos_hint={'center_x': .5, 'center_y': .5}, elevation=2, shadow_softness=4,
                          shadow_offset=(2, -2))
            label_name = Label(text=str(quest[1]), text_size=(dp(300), None), font_size=dp(30), bold=True,
                               pos_hint={'center_x': .33, 'center_y': .5})
            label_exp = Label(text=str(quest[2]), text_size=(dp(300), None), font_size=dp(12), bold=True,
                              pos_hint={'center_x': .335, 'center_y': .292}, color='darkgrey')
            label_data = Label(text=str(quest[3]), text_size=(dp(300), None), font_size=dp(25), bold=True,
                               pos_hint={'center_x': .331, 'center_y': .77}, color='grey')
            del_button = MDIconButton(icon='trash-can-outline', pos_hint={'center_x': .92, 'center_y': .77}, id=str(quest[0]),
                                      on_press=self.del_quest)
            float_lay.add_widget(card)
            float_lay.add_widget(check)
            float_lay.add_widget(label_name)
            float_lay.add_widget(label_exp)
            float_lay.add_widget(label_data)
            float_lay.add_widget(del_button)
            stack_lay.add_widget(float_lay)
        self.sm.get_screen('questscreen').add_widget(self.scroll2)

    def quest_press(self, instance):
        print(instance.id)




        db2.delete_quest(instance.text)
        self.delete_quest_lay()
        self.build_quest()



    def del_quest(self, instance):
        print(instance.id)
        db2.delete_quest(instance.id)
        self.delete_quest_lay()
        self.build_quest()

    def delete_quest_lay(self):
        self.sm.get_screen('questscreen').remove_widget(self.scroll2)


    def new_profile(self):
        db3.create_profile(self.sm.get_screen('newprofile').ids.profile_name.text,
                           self.sm.get_screen('newprofile').ids.profile_title.text,
                           self.sm.get_screen('newprofile').ids.profile_job.text,
                           self.sm.get_screen('newprofile').ids.profile_grl.text,
                           self.sm.get_screen('newprofile').ids.profile_goal.text,
                           self.sm.get_screen('newprofile').ids.profile_law1.text,
                           self.sm.get_screen('newprofile').ids.profile_law2.text,
                           self.sm.get_screen('newprofile').ids.profile_law3.text,
                           self.sm.get_screen('newprofile').ids.profile_law4.text,
                           self.sm.get_screen('newprofile').ids.profile_law5.text,
                           self.sm.get_screen('newprofile').ids.profile_law6.text,
                           self.sm.get_screen('newprofile').ids.profile_law7.text)


    def build_profile(self):
        profile = db3.get_profile()
        for i in profile:
            self.sm.get_screen('profilescreen').ids.profile_name.text = f'Name: {str(i[0])}'
            self.sm.get_screen('profilescreen').ids.profile_title.text = f'Title: {i[1]}'
            self.sm.get_screen('profilescreen').ids.profile_job.text = f'Job: {i[2]}'
            self.sm.get_screen('profilescreen').ids.profile_grl.text = f'Girlfriend: {i[3]}'
            self.sm.get_screen('profilescreen').ids.profile_goal.text = f'Goal: {i[4]}'
            self.sm.get_screen('profilescreen').ids.profile_law1.text = f'1: {i[5]}'
            self.sm.get_screen('profilescreen').ids.profile_law2.text = f'2: {i[6]}'
            self.sm.get_screen('profilescreen').ids.profile_law3.text = f'3: {i[7]}'
            self.sm.get_screen('profilescreen').ids.profile_law4.text = f'4: {i[8]}'
            self.sm.get_screen('profilescreen').ids.profile_law5.text = f'5: {i[9]}'
            self.sm.get_screen('profilescreen').ids.profile_law6.text = f'6: {i[10]}'
            self.sm.get_screen('profilescreen').ids.profile_law7.text = f'7: {i[11]}'


    def build_level(self):
        list = db4.get_lvl()
        print(list)
        if list != []:
            self.sm.get_screen('profilescreen').ids.progressbar.max = list[-1][2]
            self.sm.get_screen('profilescreen').ids.progressbar.value = list[-1][1]
            self.sm.get_screen('profilescreen').ids.lvl_text.text = list[-1][0]







DemoApp().run()
