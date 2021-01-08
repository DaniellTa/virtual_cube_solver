from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def reverse(move):
    if move[-1] == "'":
        return move[:-1]
    elif move[-1] != "2":
        return f"{move}'"
    return move


def rev_scram(moves):
    n = []
    for move in moves:
        if move[-1] == "2":
            n.extend([move[0], move[0]])
        else:
            n.append(reverse(move))
    return n[::-1]


def move_to_key(move):
    d = {
        "B": "W",
        "R": "I",
        "L'": "E",
        "B'": "O",
        "D": "S",
        "L": "D",
        "U'": "F",
        "F'": "G",
        "F": "H",
        "U": "J",
        "R'": "K",
        "D'": "L"
    }
    return d[move]

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)

driver.get("https://cstimer.net/")


driver.find_element_by_class_name("icon").click()

tabs = driver.find_elements_by_class_name("tab")
for i in tabs:
    if i.text == "timer":
        i.click()

driver.find_element_by_xpath(
    '/html/body/div[4]/div[2]/table/tbody/tr/td[2]/div/table/tbody/tr[42]/td[1]/select').click()

driver.find_element_by_xpath(
    '/html/body/div[4]/div[2]/table/tbody/tr/td[2]/div/table/tbody/tr[42]/td[1]/select/option[5]').click()

driver.find_element_by_xpath('/html/body/div[4]/div[3]/input[1]').click()

body = driver.find_element_by_tag_name("body")
body.click()

while True:
    stop = input("Press enter: ")
    scram = driver.find_element_by_xpath('//*[@id="scrambleTxt"]/div').text
    if not stop:
        body.send_keys(Keys.SPACE)
        sol = []
        for i in rev_scram(scram.split(" ")):
            sol.append(move_to_key(i))
        body.send_keys("".join(sol))
    else:
        driver.quit()
        break
