import tkinter as tk
from tkinter import *
import barcode
from barcode.writer import ImageWriter


# Interface



number = input("Digite o codigo: ")

barcode_format = barcode.get_barcode_class("upc")
my_barcode = barcode_format(number, writer=ImageWriter())
my_barcode.save("Está pronto!")
