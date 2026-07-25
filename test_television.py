from television import Television


def test_init_sets_default_values() -> None:
    tv = Television()

    assert str(tv) == 'Power = False, Channel = 0, Volume = 0'


def test_power_turns_television_on_and_off() -> None:
    tv = Television()

    tv.power()
    assert str(tv) == 'Power = True, Channel = 0, Volume = 0'

    tv.power()
    assert str(tv) == 'Power = False, Channel = 0, Volume = 0'


def test_mute_toggles_only_when_power_is_on() -> None:
    tv = Television()
    tv.power()
    tv.volume_up()

    tv.mute()
    assert str(tv) == 'Power = True, Channel = 0, Volume = 0'

    tv.mute()
    assert str(tv) == 'Power = True, Channel = 0, Volume = 1'

    tv.power()
    tv.mute()
    assert str(tv) == 'Power = False, Channel = 0, Volume = 1'


def test_channel_up_ignores_power_off_and_wraps_after_maximum() -> None:
    tv = Television()

    tv.channel_up()
    assert str(tv) == 'Power = False, Channel = 0, Volume = 0'

    tv.power()
    tv.channel_up()
    assert str(tv) == 'Power = True, Channel = 1, Volume = 0'

    tv.channel_up()
    tv.channel_up()
    tv.channel_up()
    assert str(tv) == 'Power = True, Channel = 0, Volume = 0'


def test_channel_down_ignores_power_off_and_wraps_before_minimum() -> None:
    tv = Television()

    tv.channel_down()
    assert str(tv) == 'Power = False, Channel = 0, Volume = 0'

    tv.power()
    tv.channel_down()
    assert str(tv) == 'Power = True, Channel = 3, Volume = 0'


def test_volume_up_ignores_power_off_unmutes_and_stops_at_maximum() -> None:
    tv = Television()

    tv.volume_up()
    assert str(tv) == 'Power = False, Channel = 0, Volume = 0'

    tv.power()
    tv.volume_up()
    assert str(tv) == 'Power = True, Channel = 0, Volume = 1'

    tv.mute()
    tv.volume_up()
    assert str(tv) == 'Power = True, Channel = 0, Volume = 2'

    tv.volume_up()
    assert str(tv) == 'Power = True, Channel = 0, Volume = 2'


def test_volume_down_ignores_power_off_unmutes_and_stops_at_minimum() -> None:
    tv = Television()

    tv.volume_down()
    assert str(tv) == 'Power = False, Channel = 0, Volume = 0'

    tv.power()
    tv.volume_up()
    tv.volume_up()
    tv.volume_down()
    assert str(tv) == 'Power = True, Channel = 0, Volume = 1'

    tv.mute()
    tv.volume_down()
    assert str(tv) == 'Power = True, Channel = 0, Volume = 0'

    tv.volume_down()
    assert str(tv) == 'Power = True, Channel = 0, Volume = 0'
