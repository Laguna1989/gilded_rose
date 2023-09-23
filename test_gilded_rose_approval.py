import pytest
from approvaltests import verify, verify_all_combinations

from gilded_rose import GildedRose, Item


def test_gildedrose_unit():
    items = [Item("foo", 50, 50)]
    gilded_rose = GildedRose(items)

    gilded_rose.update_quality()

    assert items[0].name == "foo"


def test_gilded_rose_approval_single_item():
    items = [Item("foo", 50, 50)]
    gilded_rose = GildedRose(items)

    gilded_rose.update_quality()

    verify(items)


def test_gilded_rose_approval_multiple_items():
    items = [
        Item("foo", 50, 50),
        Item("Sulfuras, Hand of Ragnaros", 100, 10),
        Item("Sulfuras, Hand of Ragnaros", 5, 5)
    ]
    gilded_rose = GildedRose(items)

    gilded_rose.update_quality()

    verify(items)


def make_item_and_update(name, sell_in, quality, days_to_update):
    items = [Item(name, sell_in, quality)]
    gilded_rose = GildedRose(items)
    for _ in range(days_to_update):
        gilded_rose.update_quality()
    return items


def test_gilded_rose_approval_all_items():
    names = ["foo", "Sulfuras, Hand of Ragnaros", "Aged Brie", "Backstage passes to a TAFKAL80ETC concert"
             ]
    sell_ins = [-10, -5, -1, 0, 1, 2, 5, 10, 20, 50, 100]
    qualitites = [0, 1, 2, 5, 10, 20, 50, 100]
    days_to_update = [0, 1, 2, 5, 10]

    verify_all_combinations(make_item_and_update, [names, sell_ins, qualitites, days_to_update])
