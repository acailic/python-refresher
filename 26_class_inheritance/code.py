class Device:
    def __init__(self, name, conected_by):
        self.name = name
        self.conected_by = conected_by
        self.connected = True

    def __str__(self):
        return f"Device {self.name} ({self.conected_by})"

    def disconnected(self):
        self.connected = False
        print("Disconnected.")


class Printer(Device):
    def __init__(self, name, connected_by, capacity):
        super().__init__(name, connected_by)
        self.capacity = capacity
        self.remaning_page = capacity

    def __str__(self):
        return f"{super().__str__()} ({self.remaning_page} pages remaining)"

    def printer(self, pages):
        if not self.connected:
            print("Your printer is not connected!")
            return
        print(f"Printing {pages} pages.")
        self.remaning_page -= pages


printer = Device("Printer", "USB")
print(printer)
printer.disconnected()
printerLaze = Printer("PrinterWifi", "USB", 500)

printerLaze.disconnected()
printerLaze.printer(22)