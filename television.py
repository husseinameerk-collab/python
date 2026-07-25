class Television:
    """Represent a television with power, mute, channel, and volume controls."""

    MIN_VOLUME: int = 0
    MAX_VOLUME: int = 2
    MIN_CHANNEL: int = 0
    MAX_CHANNEL: int = 3

    def __init__(self) -> None:
        """Set the television to its starting state."""
        self.__status = False
        self.__muted = False
        self.__volume = Television.MIN_VOLUME
        self.__channel = Television.MIN_CHANNEL

    def power(self) -> None:
        """Turn the television on or off."""
        self.__status = not self.__status

    def mute(self) -> None:
        """Toggle mute when the television is powered on."""
        if self.__status:
            self.__muted = not self.__muted

    def channel_up(self) -> None:
        """Move to the next channel when the television is powered on."""
        if self.__status:
            self.__channel += 1
            if self.__channel > Television.MAX_CHANNEL:
                self.__channel = Television.MIN_CHANNEL

    def channel_down(self) -> None:
        """Move to the previous channel when the television is powered on."""
        if self.__status:
            self.__channel -= 1
            if self.__channel < Television.MIN_CHANNEL:
                self.__channel = Television.MAX_CHANNEL

    def volume_up(self) -> None:
        """Increase volume when powered on, unmuting first if needed."""
        if self.__status:
            self.__muted = False
            self.__volume = min(self.__volume + 1, Television.MAX_VOLUME)

    def volume_down(self) -> None:
        """Decrease volume when powered on, unmuting first if needed."""
        if self.__status:
            self.__muted = False
            self.__volume = max(self.__volume - 1, Television.MIN_VOLUME)

    def __str__(self) -> str:
        """Return the current power, channel, and displayed volume."""
        volume = Television.MIN_VOLUME if self.__muted else self.__volume
        return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {volume}'
