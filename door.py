"""
Dieses Modul beschreibt eine Tür mit den
 Attributen Farbe, Zustand (offen/geschlossen) und Verriegelung.
Es enthält die Klassen Door und DoorLock.
"""

class Door:
    """
    Diese Klasse beschreibt eine Tür mit der Eigenschaft color (Farbe) und den Zuständen
    door_is_open (für geöffnete Tür) sowie door_is_locked (für verriegelte Tür).
    Die Tür überwacht die beiden Zustände und verhindert so Aktionen, die nicht möglich sind.
    Das Verriegeln selbst delegiert die Tür an ein Objekt vom Typ DoorLock (Türschloss).
    """

    def __init__(self, ref2door_lock, base_color):
        """
        Erzeugt ein Tür-Objekt.
        :param ref2door_lock: Referenz auf ein DoorLock-Objekt.
        :param base_color: Farbe der Tür.
        """
        self._the_door_lock = ref2door_lock
        self.color = base_color
        self._door_is_open = False
        self._door_is_locked = False  # Private Variable zur Speicherung des Zustands

    def open_the_door(self):
        """
        Methode für das Öffnen der Tür.
        Das ist aber nur möglich, wenn die Tür nicht verriegelt ist.
        """
        if not self.door_is_locked:
            self._door_is_open = True

    def close_the_door(self):
        """
        Methode für das Schließen der Tür.
        Das geht immer, auch wenn die Tür schon geschlossen oder verriegelt ist.
        """
        self._door_is_open = False

    def lock_the_door(self):
        """
        Methode für das Verriegeln der Tür.
        Das ist nur möglich, wenn die Tür geschlossen ist.
        Für das Verriegeln ist aber das Türschloss zuständig.
        """
        if not self.door_is_open:
            self.door_is_locked = self._the_door_lock.lock()  # Verwenden des Setters

    def unlock_the_door(self):
        """
        Methode für das Entriegeln der Tür.
        Das ist nur möglich, wenn die Tür verriegelt ist.
        Für das Entriegeln ist aber das Türschloss zuständig.
        """
        if self.door_is_locked:
            self.door_is_locked = self._the_door_lock.unlock()  # Verwenden des Setters

    def test(self):
        """
        Gibt alle Attribute der Tür aus.
        """
        print(f'Türfarbe: {self.color}')
        print(f'Türe offen: {self._door_is_open}')
        print(f'Türe verriegelt: {self.door_is_locked}')

    @property
    def door_is_open(self):
        """
        Getter-Methode für den Zustand door_is_open.
        :return: True, wenn die Tür offen ist, sonst False.
        """
        return self._door_is_open

    @property
    def door_is_locked(self):
        """
        Getter-Methode für den Zustand door_is_locked.
        :return: True, wenn die Tür verriegelt ist, sonst False.
        """
        return self._door_is_locked

    @door_is_locked.setter
    def door_is_locked(self, value):
        """
        Setter-Methode für den Zustand door_is_locked.
        :param value: Neuer Verriegelungszustand der Tür.
        """
        self._door_is_locked = value

    @property
    def color(self):
        """
        Getter-Methode für die Eigenschaft color.
        :return: Die Farbe des Objekts.
        """
        return self._color

    @color.setter
    def color(self, new_color):
        """
        Setter-Methode für die Eigenschaft color.
        :param new_color: Neue Farbe der Tür.
        """
        self._color = new_color


class DoorLock:
    """
    Dummy-Klasse, damit in der Klasse Door kein Fehler auftritt.
    """

    def __init__(self):
        print("Ein Schloss wurde erzeugt")

    def lock(self):
        """
        Methode zum Verriegeln des Schlosses.
        :return: True, wenn das Schloss verriegelt ist.
        """
        return True

    def unlock(self):
        """
        Methode zum Entriegeln des Schlosses.
        :return: False, wenn das Schloss entriegelt ist.
        """
        return False


if __name__ == "__main__":
    print("Test für Tür-Objekt")
    the_door_lock = DoorLock()
    the_door = Door(the_door_lock, "grün")
    the_door.test()
    print("-- Türe jetzt öffnen --")
    the_door.open_the_door()
    the_door.test()
