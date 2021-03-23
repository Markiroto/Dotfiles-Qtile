#  ________  _________  ___  ___       _______      
# |\   __  \|\___   ___\\  \|\  \     |\  ___ \     
# \ \  \|\  \|___ \  \_\ \  \ \  \    \ \   __/|    
#  \ \  \\\  \   \ \  \ \ \  \ \  \    \ \  \_|/__  
#   \ \  \\\  \   \ \  \ \ \  \ \  \____\ \  \_|\ \ 
#    \ \_____  \   \ \__\ \ \__\ \_______\ \_______\
#     \|___| \__\   \|__|  \|__|\|_______|\|_______|
#           \|__|                                   


# -*- coding: utf-8 -*-
import os
import re
import socket
import subprocess
from libqtile import qtile
from libqtile.config import Click, Drag, Group, KeyChord, Key, Match, Screen
from libqtile.command import lazy
from libqtile import layout, bar, widget, hook
from libqtile.lazy import lazy
from typing import List  # noqa: F401

mod = "mod4"                                     # Sets mod key to SUPER/WINDOWS
myTerm = "kitty"                             # My terminal of choice

keys = [
         Key([mod, "shift"], "Return",
             lazy.spawn(myTerm),
             desc='Launches My Terminal'
             ),
         Key([mod], "r",
             lazy.spawn("rofi -show drun -font 'JetBrainsMono Nerd Font 12'"),
             desc='Run Launcher'
             ),
         Key([mod], "Tab",
             lazy.next_layout(),
             desc='Toggle through layouts'
             ),
         Key([mod], "q",
             lazy.window.kill(),
             desc='Kill active window'
             ),
         Key([mod, "shift"], "r",
             lazy.restart(),
             desc='Restart Qtile'
             ),
         Key([mod, "shift"], "q",
             lazy.shutdown(),
             desc='Shutdown Qtile'
             ),
         Key([mod], "x",
            lazy.spawn("arcolinux-logout"),
            desc='Logout'
            ),
         Key([mod, "shift"], "x",
            lazy.spawn("betterlockscreen -s blur --text 'This Computer is Locked UwU'"),
            desc='Suspend and Lock'
            ),
         Key(["mod1", "shift"], "s",
             lazy.spawn("flameshot gui"),
             desc='Screenshot'
             ),
         ### Window controls
         Key([mod], "k",
             lazy.layout.down(),
             desc='Move focus down in current stack pane'
             ),
         Key([mod], "j",
             lazy.layout.up(),
             desc='Move focus up in current stack pane'
             ),
         Key([mod, "shift"], "k",
             lazy.layout.shuffle_down(),
             desc='Move windows down in current stack'
             ),
         Key([mod, "shift"], "j",
             lazy.layout.shuffle_up(),
             desc='Move windows up in current stack'
             ),
         Key([mod], "h",
             lazy.layout.shrink(),
             lazy.layout.decrease_nmaster(),
             desc='Shrink window (MonadTall), decrease number in master pane (Tile)'
             ),
         Key([mod], "l",
             lazy.layout.grow(),
             lazy.layout.increase_nmaster(),
             desc='Expand window (MonadTall), increase number in master pane (Tile)'
             ),
         Key([mod], "n",
             lazy.layout.normalize(),
             desc='normalize window size ratios'
             ),
         Key([mod], "m",
             lazy.layout.maximize(),
             desc='toggle window between minimum and maximum sizes'
             ),
         Key([mod, "shift"], "f",
             lazy.window.toggle_floating(),
             desc='toggle floating'
             ),
         Key([mod, "shift"], "m",
             lazy.window.toggle_fullscreen(),
             desc='toggle fullscreen'
             ),
]

group_names = [("I", {'layout': 'monadtall'}),
               ("II", {'layout': 'monadtall'}),
               ("III", {'layout': 'monadtall'}),
               ("IV", {'layout': 'monadtall'}),
               ("V", {'layout': 'monadtall'}),
               ("VI", {'layout': 'monadtall'}),
               ("VII", {'layout': 'monadtall'}),
               ("VIII", {'layout': 'monadtall'}),
               ("IX", {'layout': 'monadtall'})]

groups = [Group(name, **kwargs) for name, kwargs in group_names]

for i, (name, kwargs) in enumerate(group_names, 1):
    keys.append(Key([mod], str(i), lazy.group[name].toscreen()))        # Switch to another group
    keys.append(Key([mod, "shift"], str(i), lazy.window.togroup(name))) # Send current window to another group

layout_theme = {"border_width": 3,
                "margin": 10,
                "border_normal": "4C566A",
                "border_focus": "5E81AC"
                }

layouts = [
    #layout.MonadWide(**layout_theme),
    #layout.Bsp(**layout_theme),
    #layout.Stack(stacks=2, **layout_theme),
    #layout.Columns(**layout_theme),
    #layout.RatioTile(**layout_theme),
    layout.VerticalTile(**layout_theme),
    layout.Matrix(**layout_theme),
    #layout.Zoomy(**layout_theme),
    layout.MonadTall(**layout_theme),
    layout.Max(**layout_theme),
    layout.Tile(shift_windows=True, **layout_theme),
    layout.Floating(**layout_theme)
]

colors = [["#434C5E", "#434C5E"], # panel background
          ["#3B4252", "#3B4252"], # background for current screen tab
          ["#ECEFF4", "#ECEFF4"], # font color for group names
          ["#ff5555", "#ff5555"], # border line color for current tab
          ["#D08770", "#D08770"], # border line color for 'other tabs' and color for 'even widgets'
          ["#5E81AC", "#5E81AC"], # color for the 'odd widgets'
          ["#A3BE8C", "#A3BE8C"]] # window name

prompt = "{0}@{1}: ".format(os.environ["USER"], socket.gethostname())

##### DEFAULT WIDGET SETTINGS #####
widget_defaults = dict(
    font="JetBrains Mono Nerd Font Mono",
    fontsize = 12,
    padding = 2,
    background=colors[2]
)
extension_defaults = widget_defaults.copy()

def init_widgets_list():
    widgets_list = [
              widget.Sep(
                       linewidth = 0,
                       padding = 5,
                       foreground = colors[2],
                       background = colors[0]
                       ),
              widget.TextBox(
                       text = '◥',
                       background = colors[0],
                       foreground = "#81A1C1",
                       padding = -2,
                       font= "Fira Code",
                       fontsize = 50
                       ),
              widget.Image(
                       filename = "~/.config/qtile/icons/arco.png",
                       scale = "True",
                       mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn("rofi -show drun -font 'JetBrainsMono Nerd Font 12'")}
                       ),
              widget.TextBox(
                       text = '◣',
                       background = colors[0],
                       foreground = "#81A1C1",
                       padding = -2,
                       font = "Fira Code",
                       fontsize = 50
                       ),

             widget.Sep(
                       linewidth = 0,
                       padding = 1,
                       foreground = colors[2],
                       background = colors[0]
                       ),
              widget.GroupBox(
                       font = "JetBrainsMono Nerd Font",
                       fontsize = 12,
                       margin_y = 3,
                       margin_x = 0,
                       padding_y = 5,
                       padding_x = 3,
                       borderwidth = 3,
                       active = colors[2],
                       inactive = colors[2],
                       rounded = False,
                       highlight_color = colors[1],
                       highlight_method = "line",
                       this_current_screen_border = colors[6],
                       this_screen_border = colors [4],
                       other_current_screen_border = colors[6],
                       other_screen_border = colors[4],
                       foreground = colors[2],
                       background = colors[0]
                       ),
              widget.Prompt(
                       prompt = prompt,
                       font = "JetBrainsMono Nerd Font",
                       padding = 10,
                       foreground = colors[3],
                       background = colors[1]
                       ),
              widget.Sep(
                       linewidth = 0,
                       padding = 10,
                       foreground = colors[2],
                       background = colors[0]
                       ),
              widget.WindowName(
                       foreground = colors[2],
                       background = colors[0],
                       padding = 0,
                       font = "JetBrainsMono Nerd Font"
                       ),
              widget.Sep(
                       linewidth = 0,
                       padding = 6,
                       foreground = colors[0],
                       background = colors[0]
                       ),
              widget.TextBox(
                       text = '◥',
                       background = colors[0],
                       foreground = colors[5],
                       padding = -2,
                       font = "Fira Code",
                       fontsize = 50
                       ),
             widget.Net(
                       interface = "wlp0s20f3",
                       format = '📡 ↓{down} ↑ {up}',
                       foreground = colors[2],
                       background = colors[5],
                       mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(myTerm + ' -e nmtui')},
                       padding = 0
                       ),
              widget.TextBox(
                       text='◢',
                       background = colors[5],
                       foreground = colors[4],
                       padding = -2,
                       font = "Fira Code",
                       fontsize = 50
                       ),
              widget.TextBox(
                       text = "💻",
                       padding = 2,
                       foreground = colors[2],
                       background = colors[4],
                       fontsize = 14
                       ),
              widget.CheckUpdates(
                       update_interval = 1800,
                       distro = "Arch_checkupdates",
                       display_format = "{updates} Updates",
                       foreground = colors[2],
                       mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(myTerm + ' -e sudo pacman -Syu')},
                       background = colors[4]
                       ),
              widget.TextBox(
                       text = '◢',
                       background = colors[4],
                       foreground = colors[5],
                       padding = -2,
                       font = "Fira Code",
                       fontsize = 50
                       ),
              widget.TextBox(
                       text = "💾",
                       foreground = colors[2],
                       background = colors[5],
                       padding = 0,
                       fontsize = 14
                       ),
              widget.Memory(
                       foreground = colors[2],
                       background = colors[5],
                       mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(myTerm + ' -e gotop')},
                       padding = 5
                       ),
              widget.TextBox(
                       text = '◢',
                       background = colors[5],
                       foreground = colors[4],
                       padding = -2,
                       font = "Fira Code",
                       fontsize = 50
                       ),
              widget.TextBox(
                      text = " 🎧 Vol:",
                       foreground = colors[2],
                       background = colors[4],
                       padding = 0
                       ),
              widget.Volume(
                       foreground = colors[2],
                       background = colors[4],
                       padding = 5
                       ),
              widget.TextBox(
                       text = '◢',
                       background = colors[4],
                       foreground = colors[5],
                       padding = -2,
                       font = "Fira Code",
                       fontsize = 50
                       ),
              widget.CurrentLayoutIcon(
                       custom_icon_paths = [os.path.expanduser("~/.config/qtile/icons")],
                       foreground = colors[0],
                       background = colors[5],
                       padding = 0,
                       scale = 0.7
                       ),
              widget.CurrentLayout(
                       foreground = colors[2],
                       background = colors[5],
                       padding = 5
                       ),
              widget.TextBox(
                       text = '◢',
                       background = colors[5],
                       foreground = colors[4],
                       padding = -2,
                       font = "Fira Code",
                       fontsize = 50
                       ),
              widget.Clock(
                       foreground = colors[2],
                       background = colors[4],
                       format = "📅 %A, %B %d, %H:%M:%S ",
                       mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(myTerm + ' -e calcurse')}
                       ),
              widget.TextBox(
                      text= '◣',
                      background = colors[0],
                      foreground = colors[4],
                      padding = -2,
                      font = "Fira Code",
                      fontsize = 50
                      ),
              widget.Systray(
                      background = colors[0],
                      padding = 0
                      ),
              ]
    return widgets_list

def init_widgets_screen1():
    widgets_screen1 = init_widgets_list()
    return widgets_screen1

def init_screens():
    return [Screen(top=bar.Bar(widgets=init_widgets_screen1(), opacity=1.0, size=20))]

if __name__ in ["config", "__main__"]:
    screens = init_screens()
    widgets_list = init_widgets_list()
    widgets_screen1 = init_widgets_screen1()

def window_to_prev_group(qtile):
    if qtile.currentWindow is not None:
        i = qtile.groups.index(qtile.currentGroup)
        qtile.currentWindow.togroup(qtile.groups[i - 1].name)

def window_to_next_group(qtile):
    if qtile.currentWindow is not None:
        i = qtile.groups.index(qtile.currentGroup)
        qtile.currentWindow.togroup(qtile.groups[i + 1].name)

def window_to_previous_screen(qtile):
    i = qtile.screens.index(qtile.current_screen)
    if i != 0:
        group = qtile.screens[i - 1].group.name
        qtile.current_window.togroup(group)

def window_to_next_screen(qtile):
    i = qtile.screens.index(qtile.current_screen)
    if i + 1 != len(qtile.screens):
        group = qtile.screens[i + 1].group.name
        qtile.current_window.togroup(group)

def switch_screens(qtile):
    i = qtile.screens.index(qtile.current_screen)
    group = qtile.screens[i - 1].group
    qtile.current_screen.set_group(group)

mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
main = None
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False

floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    # default_float_rules include: utility, notification, toolbar, splash, dialog,
    # file_progress, confirm, download and error.
    *layout.Floating.default_float_rules,
    Match(title='Confirmation'),  # tastyworks exit box
    Match(wm_class='gnome-calculator'),  # Calculator
    Match(wm_class='olive-editor'),  # olive
    Match(wm_class='pinentry-gtk-2'),  # GPG key password entry
])
auto_fullscreen = True
focus_on_window_activation = "smart"

@hook.subscribe.startup_once
def start_once():
    home = os.path.expanduser('~')
    subprocess.call([home + '/.config/qtile/autostart.sh'])

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
