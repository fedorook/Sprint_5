from src.locators import ConstructorSectionLocators

def is_active(tab_element):
    return "current" in tab_element.get_attribute("class")

def test_constructor_tab_navigation(driver):
    sauces_tab = driver.find_element(*ConstructorSectionLocators.SAUCES_TAB)
    buns_tab = driver.find_element(*ConstructorSectionLocators.BUNS_TAB)
    fillings_tab = driver.find_element(*ConstructorSectionLocators.FILLINGS_TAB)

    # Click "Соусы"
    sauces_tab.click()
    assert is_active(sauces_tab)
    assert not is_active(buns_tab)
    assert not is_active(fillings_tab)

    # Click "Начинки"
    fillings_tab.click()
    assert is_active(fillings_tab)
    assert not is_active(buns_tab)
    assert not is_active(sauces_tab)

    # Click "Булки"
    buns_tab.click()
    assert is_active(buns_tab)
    assert not is_active(sauces_tab)
    assert not is_active(fillings_tab)
