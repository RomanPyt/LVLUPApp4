KV = '''


<TaskScreen>:
    MDBoxLayout:
        size_hint: 1, .06
        pos_hint: {'center_x': .5, 'center_y': .96}
        MDRectangleFlatButton:
            id: button
            text: app.button_text_day
            font_size: '30dp'
            bold: True
            pos_hint: {"center_x": .5, "center_y": .52}
            theme_text_color: "Custom"
            text_color: "white"
            line_color: 0, 0, 0, 0
            on_release: app.menu_open()
        MDIconButton:
            icon: 'plus'
            icon_size: '30dp'
            #pos_hint: {'center_x': .4, 'center_y': .05}
            on_release: root.manager.current = 'newtask'
    NavigationBar:
        size_hint: .5, .1
        pos_hint: {'center_x': .5, 'center_y': .1}
        elevation: 2
        md_bg_color: '#444444'
        radius: [16]
        MDFloatLayout:
            MDFloatingActionButton:
                pos_hint: {'center_x': .2, 'center_y': .5}
                icon: 'all-inclusive'
                icon_size: '35dp'
                #theme_text_color: 'Custom'
                #text_color: .28, .11, .51, 1
                md_bg_color: '#5b5b5b'
                on_release:
                    root.manager.current = 'taskscreen'
            MDIconButton:
                pos_hint: {'center_x': .5, 'center_y': .5}
                icon: 'book-arrow-up'
                icon_size: '35dp'
                on_release:
                    root.manager.current = 'questscreen'
            MDIconButton:
                pos_hint: {'center_x': .8, 'center_y': .5}
                icon: 'account-box'
                icon_size: '35dp'
                on_release:
                    root.manager.current = 'profilescreen'





<NewTaskScreen>:
    MDCard:
        radius: [16]
        size_hint: .9, .55
        pos_hint: {"center_x": .5, "center_y": .57}
        elevation: 2
        shadow_softness: 4
        shadow_offset: (2, -2)
    MDCard:
        radius: [16]
        size_hint: .5, .25
        pos_hint: {"center_x": .34, "center_y": .69}
        elevation: 2
        shadow_softness: 4
        shadow_offset: (2, -2)
        md_bg_color: '#444444'
    MDTextField:
        id: task_name
        size_hint: .4, None
        pos_hint: {'center_x': .345, 'center_y': .765}
        hint_text_color_focus: '#444444'
        line_color_focus: "darkgrey"
        text_color_focus: "darkgrey"
        hint_text: 'Name'
    MDTextField:
        id: task_exp
        size_hint: .4, None
        pos_hint: {'center_x': .345, 'center_y': .65}
        hint_text_color_focus: '#444444'
        line_color_focus: "darkgrey"
        text_color_focus: "darkgrey"
        hint_text: 'Exp.'
    MDRaisedButton:
        text: "Create"
        md_bg_color: '#444444'
        font_size: '15dp'
        bold: True
        pos_hint: {'center_x': .8, 'center_y': .35}
        on_release: 
            app.new_task_name()
            root.manager.current = 'taskscreen'
            app.delete_task_lay()
            app.build_task(app.text_day)
    MDRaisedButton:
        text: "Cancel"
        md_bg_color: '#444444'
        font_size: '15dp'
        bold: True
        pos_hint: {'center_x': .2, 'center_y': .35}
        on_release: 
            root.manager.current = 'taskscreen'
    MDBoxLayout:
        size_hint: .4, .4
        orientation: 'vertical'
        pos_hint: {'center_x': .8, 'center_y': .62}

        MDFloatLayout:
            MDCard:
                radius: [16]
                size_hint: .8, 1
                pos_hint: {"center_x": .4, "center_y": .5}
                elevation: 2
                shadow_softness: 4
                shadow_offset: (2, -2)
            MDSwitch:
                id: monday_switch
                pos_hint: {'center_x': .5, 'center_y': .32}

            MDLabel:
                pos_hint: {'center_x': .55, 'center_y': .53}
                text: 'Monday'
        MDFloatLayout:
            MDCard:
                radius: [16]
                size_hint: .8, 1
                pos_hint: {"center_x": .4, "center_y": .5}
                elevation: 2
                shadow_softness: 4
                shadow_offset: (2, -2)
            MDSwitch:
                id: tuesday_switch
                pos_hint: {'center_x': .5, 'center_y': .32}

            MDLabel:
                pos_hint: {'center_x': .55, 'center_y': .53}
                text: 'Tuesday'
        MDFloatLayout:
            MDCard:
                radius: [16]
                size_hint: .8, 1
                pos_hint: {"center_x": .4, "center_y": .5}
                elevation: 2
                shadow_softness: 4
                shadow_offset: (2, -2)
            MDSwitch:
                id: wednesday_switch
                pos_hint: {'center_x': .5, 'center_y': .32}

            MDLabel:
                pos_hint: {'center_x': .55, 'center_y': .53}
                text: 'Wednesday'
        MDFloatLayout:
            MDCard:
                radius: [16]
                size_hint: .8, 1
                pos_hint: {"center_x": .4, "center_y": .5}
                elevation: 2
                shadow_softness: 4
                shadow_offset: (2, -2)
            MDSwitch:
                id: thursday_switch
                pos_hint: {'center_x': .5, 'center_y': .32}

            MDLabel:
                pos_hint: {'center_x': .55, 'center_y': .53}
                text: 'Thursday'
        MDFloatLayout:
            MDCard:
                radius: [16]
                size_hint: .8, 1
                pos_hint: {"center_x": .4, "center_y": .5}
                elevation: 2
                shadow_softness: 4
                shadow_offset: (2, -2)
            MDSwitch:
                id: friday_switch
                pos_hint: {'center_x': .5, 'center_y': .32}

            MDLabel:
                pos_hint: {'center_x': .55, 'center_y': .53}
                text: 'Friday'
        MDFloatLayout:
            MDCard:
                radius: [16]
                size_hint: .8, 1
                pos_hint: {"center_x": .4, "center_y": .5}
                elevation: 2
                shadow_softness: 4
                shadow_offset: (2, -2)
            MDSwitch:
                id: saturday_switch
                pos_hint: {'center_x': .5, 'center_y': .32}

            MDLabel:
                pos_hint: {'center_x': .55, 'center_y': .53}
                text: 'Saturday'
        MDFloatLayout:
            MDCard:
                radius: [16]
                size_hint: .8, 1
                pos_hint: {"center_x": .4, "center_y": .5}
                elevation: 2
                shadow_softness: 4
                shadow_offset: (2, -2)
            MDSwitch:
                id: sunday_switch
                pos_hint: {'center_x': .5, 'center_y': .32}

            MDLabel:
                pos_hint: {'center_x': .55, 'center_y': .53}
                text: 'Sunday'


<QuestScreen>:
    MDBoxLayout:
        size_hint: 1, .06
        pos_hint: {'center_x': .5, 'center_y': .95}
        MDLabel:
            padding: '10dp'
            text: 'Quests'
            #pos_hint: {'center_y': .95}
            #halign: 'left'
            font_size: '30dp'
            bold: True
        MDIconButton:
            icon: 'plus'
            icon_size: '30dp'
            #pos_hint: {'center_x': .9, 'center_y': .1}
            on_release: root.manager.current = 'newquest'
    
    
    NavigationBar:
        size_hint: .5, .1
        pos_hint: {'center_x': .5, 'center_y': .1}
        elevation: 2
        md_bg_color: '#444444'
        radius: [16]
        MDFloatLayout:
            MDIconButton:
                pos_hint: {'center_x': .2, 'center_y': .5}
                icon: 'all-inclusive'
                icon_size: '35dp'
                on_release:
                    root.manager.current = 'taskscreen'
            MDFloatingActionButton:
                pos_hint: {'center_x': .5, 'center_y': .5}
                icon: 'book-arrow-up'
                icon_size: '35dp'
                #theme_text_color: 'Custom'
                #text_color: .28, .11, .51, 1
                md_bg_color: '#5b5b5b'
                on_release:
                    root.manager.current = 'questscreen'

            MDIconButton:
                pos_hint: {'center_x': .8, 'center_y': .5}
                icon: 'account-box'
                icon_size: '35dp'
                on_release:
                    root.manager.current = 'profilescreen'




<NewQuestScreen>:
    MDCard:
        radius: [16]
        size_hint: .6, .4
        pos_hint: {"center_x": .5, "center_y": .58}
        elevation: 2
        shadow_softness: 4
        shadow_offset: (2, -2)
    MDCard:
        radius: [16]
        size_hint: .5, .3
        pos_hint: {"center_x": .5, "center_y": .6}
        elevation: 2
        shadow_softness: 4
        shadow_offset: (2, -2)
        md_bg_color: '#444444'
    MDTextField:
        id: quest_name
        size_hint: .4, None
        pos_hint: {'center_x': .5, 'center_y': .7}
        hint_text_color_focus: '#444444'
        line_color_focus: "darkgrey"
        text_color_focus: "darkgrey"
        hint_text: 'Name'
    MDTextField:
        id: quest_exp
        size_hint: .4, None
        pos_hint: {'center_x': .5, 'center_y': .6}
        hint_text_color_focus: '#444444'
        line_color_focus: "darkgrey"
        text_color_focus: "darkgrey"
        hint_text: 'Exp.'
    MDRectangleFlatIconButton:
        id: date_button
        line_color: 'white'
        text_color: 'white'
        icon_color: 'white'
        text: "Data"
        icon: 'calendar'
        pos_hint: {'center_x': .5, 'center_y': .5}
        on_release: app.show_date_picker()
    MDRaisedButton:
        text: "Create"
        md_bg_color: '#444444'
        font_size: '15dp'
        bold: True
        pos_hint: {'center_x': .65, 'center_y': .415}
        on_release: 
            root.manager.current = 'questscreen'
            app.new_quest_name()
            app.delete_quest_lay()
            app.build_quest()
    MDRaisedButton:
        text: "Cancel"
        md_bg_color: '#444444'
        font_size: '15dp'
        bold: True
        pos_hint: {'center_x': .35, 'center_y': .415}
        on_release: 
            root.manager.current = 'questscreen'




<ProfileScreen>:
    MDCard:
        radius: [16]
        size_hint: .3, .15
        pos_hint: {"center_x": .18, "center_y": .9}
        elevation: 2
        shadow_softness: 4
        shadow_offset: (2, -2)
    MDAnchorLayout:
        size_hint: .3, .15
        pos_hint: {"center_x": .18, "center_y": .9}
        MDLabel:
            halign: 'center'
            valign: 'center'
            id: lvl_text
            text: root.lvl_text
            #pos_hint: {'center_x': .55, 'center_y': .9}
            font_size: '50dp'
            bold: True
    MDProgressBar:
        id: progressbar
        pos_hint: {'center_x': .5, 'center_y': .78}
        size_hint: .9, 1
        color: 'white'
        radius: [10]
        max: root.max_text
        value: root.value_text
    MDIconButton:
        icon: 'dots-vertical'
        icon_size: '35dp'
        pos_hint: {'center_x': .94, 'center_y': .95}
        on_release:
            root.manager.current = 'newprofile'
    MDLabel:
        id: profile_name
        text: app.profile_name
        bold: True
        font_size: '20dp'
        pos_hint: {'center_x': .85, 'center_y': .95}
    MDLabel:
        id: profile_title
        text: app.profile_title
        bold: False
        font_size: '18dp'
        pos_hint: {'center_x': .85, 'center_y': .92}
    MDLabel:
        id: profile_job
        text: app.profile_job
        bold: False
        font_size: '18dp'
        pos_hint: {'center_x': .85, 'center_y': .89}
    MDLabel:
        id: profile_grl
        text: app.profile_grl
        bold: False
        font_size: '18dp'
        pos_hint: {'center_x': .85, 'center_y': .86}
    
    MDCard:
        size_hint: .42, .001
        line_color: 'grey'
        md_bg_color: 'grey'
        pos_hint: {'center_x': .71, 'center_y': .705}
    MDCard:
        size_hint: .05, .001
        line_color: 'grey'
        md_bg_color: 'grey'
        pos_hint: {'center_x': .06, 'center_y': .705}
        
    MDLabel:
        text: 'Information'
        bold: True
        font_size: '32dp'
        pos_hint: {'center_x': .628, 'center_y': .71}
    
    MDLabel:
        id: profile_goal
        text: app.profile_goal
        bold: True
        font_size: '30dp'
        pos_hint: {'center_x': .55, 'center_y': .64}
        
    MDLabel:
        text: 'Laws: '
        bold: True
        font_size: '30dp'
        pos_hint: {'center_x': .55, 'center_y': .57}
    
    MDLabel:
        id: profile_law1
        text: app.profile_law1
        bold: False
        font_size: '25dp'
        pos_hint: {'center_x': .71, 'center_y': .53}
    
    MDLabel:
        id: profile_law2
        text: app.profile_law2
        bold: False
        font_size: '25dp'
        pos_hint: {'center_x': .71, 'center_y': .49}
    
    MDLabel:
        id: profile_law3
        text: app.profile_law3
        bold: False
        font_size: '25dp'
        pos_hint: {'center_x': .71, 'center_y': .45}
    
    MDLabel:
        id: profile_law4
        text: app.profile_law4
        bold: False
        font_size: '25dp'
        pos_hint: {'center_x': .71, 'center_y': .41}
    
    MDLabel:
        id: profile_law5
        text: app.profile_law5
        bold: False
        font_size: '25dp'
        pos_hint: {'center_x': .71, 'center_y': .37}
    
    MDLabel:
        id: profile_law6
        text: app.profile_law6
        bold: False
        font_size: '25dp'
        pos_hint: {'center_x': .71, 'center_y': .33}
    
    MDLabel:
        id: profile_law7
        text: app.profile_law7
        bold: False
        font_size: '25dp'
        pos_hint: {'center_x': .71, 'center_y': .29}
    
    
    
        
    NavigationBar:
        size_hint: .5, .1
        pos_hint: {'center_x': .5, 'center_y': .1}
        elevation: 2
        md_bg_color: '#444444'
        radius: [16]
        MDFloatLayout:
            MDIconButton:
                pos_hint: {'center_x': .2, 'center_y': .5}
                icon: 'all-inclusive'
                icon_size: '35dp'
                on_release:
                    root.manager.current = 'taskscreen'
            MDIconButton:
                pos_hint: {'center_x': .5, 'center_y': .5}
                icon: 'book-arrow-up'
                icon_size: '35dp'
                on_release:
                    root.manager.current = 'questscreen'

            MDFloatingActionButton:
                pos_hint: {'center_x': .8, 'center_y': .5}
                icon: 'account-box'
                icon_size: '35dp'
                #theme_text_color: 'Custom'
                #text_color: .28, .11, .51, 1
                md_bg_color: '#5b5b5b'
                on_release:
                    root.manager.current = 'profilescreen'

<NewProfileScreen>:
    MDCard:
        radius: [16]
        size_hint: .7, .76
        pos_hint: {"center_x": .5, "center_y": .54}
        elevation: 2
        shadow_softness: 4
        shadow_offset: (2, -2)
    MDRaisedButton:
        text: "Create"
        md_bg_color: '#444444'
        font_size: '15dp'
        bold: True
        pos_hint: {'center_x': .65, 'center_y': .115}
        on_release: 
            root.manager.current = 'profilescreen'
            app.new_profile()
            app.build_profile()
    MDRaisedButton:
        text: "Cancel"
        md_bg_color: '#444444'
        font_size: '15dp'
        bold: True
        pos_hint: {'center_x': .35, 'center_y': .115}
        on_release: 
            root.manager.current = 'profilescreen'
    
    MDTextField:
        id: profile_name
        size_hint: .5, None
        pos_hint: {'center_x': .5, 'center_y': .88}
        hint_text_color_focus: '#444444'
        line_color_focus: "darkgrey"
        text_color_focus: "darkgrey"
        hint_text: 'Name'
    MDTextField:
        id: profile_title
        size_hint: .5, None
        pos_hint: {'center_x': .5, 'center_y': .82}
        hint_text_color_focus: '#444444'
        line_color_focus: "darkgrey"
        text_color_focus: "darkgrey"
        hint_text: 'Title'
    MDTextField:
        id: profile_job
        size_hint: .5, None
        pos_hint: {'center_x': .5, 'center_y': .76}
        hint_text_color_focus: '#444444'
        line_color_focus: "darkgrey"
        text_color_focus: "darkgrey"
        hint_text: 'Job'
    MDTextField:
        id: profile_grl
        size_hint: .5, None
        pos_hint: {'center_x': .5, 'center_y': .7}
        hint_text_color_focus: '#444444'
        line_color_focus: "darkgrey"
        text_color_focus: "darkgrey"
        hint_text: 'Girlfriend'
    MDTextField:
        id: profile_goal
        size_hint: .5, None
        pos_hint: {'center_x': .5, 'center_y': .64}
        hint_text_color_focus: '#444444'
        line_color_focus: "darkgrey"
        text_color_focus: "darkgrey"
        hint_text: 'Goal'
    MDTextField:
        id: profile_law1
        size_hint: .5, None
        pos_hint: {'center_x': .5, 'center_y': .58}
        hint_text_color_focus: '#444444'
        line_color_focus: "darkgrey"
        text_color_focus: "darkgrey"
        hint_text: 'Law 1'
    MDTextField:
        id: profile_law2
        size_hint: .5, None
        pos_hint: {'center_x': .5, 'center_y': .52}
        hint_text_color_focus: '#444444'
        line_color_focus: "darkgrey"
        text_color_focus: "darkgrey"
        hint_text: 'Law 2'
    MDTextField:
        id: profile_law3
        size_hint: .5, None
        pos_hint: {'center_x': .5, 'center_y': .46}
        hint_text_color_focus: '#444444'
        line_color_focus: "darkgrey"
        text_color_focus: "darkgrey"
        hint_text: 'Law 3'
    MDTextField:
        id: profile_law4
        size_hint: .5, None
        pos_hint: {'center_x': .5, 'center_y': .4}
        hint_text_color_focus: '#444444'
        line_color_focus: "darkgrey"
        text_color_focus: "darkgrey"
        hint_text: 'Law 4'
    MDTextField:
        id: profile_law5
        size_hint: .5, None
        pos_hint: {'center_x': .5, 'center_y': .34}
        hint_text_color_focus: '#444444'
        line_color_focus: "darkgrey"
        text_color_focus: "darkgrey"
        hint_text: 'Law 5'
    MDTextField:
        id: profile_law6
        size_hint: .5, None
        pos_hint: {'center_x': .5, 'center_y': .28}
        hint_text_color_focus: '#444444'
        line_color_focus: "darkgrey"
        text_color_focus: "darkgrey"
        hint_text: 'Law 6'
    MDTextField:
        id: profile_law7
        size_hint: .5, None
        pos_hint: {'center_x': .5, 'center_y': .22}
        hint_text_color_focus: '#444444'
        line_color_focus: "darkgrey"
        text_color_focus: "darkgrey"
        hint_text: 'Law 7'
    


'''