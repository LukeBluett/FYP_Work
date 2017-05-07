#!/usr/bin/env python3

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GObject

import xmlrpc.client


def on_ButtonStart_clicked(button):
    container = entry_start.get_text()
    print(container)
    proxy.start_container(container, "Test")

def on_ButtonStop_clicked(button):
    container = entry_stop.get_text()
    print(container)
    proxy.stop_container(container, "Test")

def on_ButtonPull_clicked(button):
    container = entry_pull.get_text()
    print(container)
    proxy.pull_container(container, "Test")

def on_ButtonQuit_clicked(button):
    quit()

proxy = xmlrpc.client.ServerProxy("http://localhost:8003/")


builder = Gtk.Builder()
builder.add_from_file("GUI.glade")

button_start = builder.get_object("ButtonStart")
button_start.connect("clicked", on_ButtonStart_clicked)

button_stop = builder.get_object("ButtonStop")
button_stop.connect("clicked", on_ButtonStop_clicked)

button_pull = builder.get_object("ButtonPull")
button_pull.connect("clicked", on_ButtonPull_clicked)

button_quit = builder.get_object("ButtonQuit")
button_quit.connect("clicked", on_ButtonQuit_clicked)

entry_start = builder.get_object("EntryStart")
entry_stop = builder.get_object("EntryStop")
entry_pull = builder.get_object("EntryPull")

window = builder.get_object("Window")
window.show_all()

Gtk.main()

