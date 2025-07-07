import xml.etree.ElementTree as ET
import logging

# Налаштування логера вручну, щоб задати кодування
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

file_handler = logging.FileHandler('xml__Cheredniuk.log', encoding='utf-8')
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)

# Додаємо handler до логера
logger.addHandler(file_handler)

def find_incoming_by_group_number(xml_path, target_number):
    try:
        tree = ET.parse(xml_path)
        root = tree.getroot()

        for group in root.findall('group'):
            number = group.find('number')
            if number is not None and number.text == str(target_number):
                incoming = group.find('timingExbytes/incoming')
                if incoming is not None:
                    logger.info(f"Для group/number {target_number}: incoming = {incoming.text}")
                    return incoming.text
                else:
                    logger.info(f"Для group/number {target_number} елемент incoming не знайдено.")
                    return None

        logger.info(f"Групу з number = {target_number} не знайдено.")
        return None

    except Exception as e:
        logger.error(f"Помилка при обробці XML: {e}")
        return None

# Виклик функції
xml_file = 'work_with_xml/groups.xml'
find_incoming_by_group_number(xml_file, 101)