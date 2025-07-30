from datetime import datetime
import re

def analyze_heartbeat(input_log_path, output_log_path, target_key):
    timestamp_pattern = r"Timestamp (\d{2}:\d{2}:\d{2})"
    filtered_lines = []

    # Читаємо файл та фільтруємо строки з цільовим ключем
    with open(input_log_path, "r") as file:
        for line in file:
            if target_key in line:
                match = re.search(timestamp_pattern, line)
                if match:
                    timestamp_str = match.group(1)
                    timestamp_dt = datetime.strptime(timestamp_str, "%H:%M:%S")
                    filtered_lines.append((timestamp_dt, line.strip()))

    # Сортуємо за часом у зворотному порядку (від нового до старого)
    filtered_lines.sort(reverse=True)

    # Аналізуємо інтервали між послідовними heartbeat
    output_lines = []
    for i in range(len(filtered_lines) - 1):
        current_time, _ = filtered_lines[i]
        next_time, _ = filtered_lines[i + 1]
        delta_seconds = int((current_time - next_time).total_seconds())

        if 31 < delta_seconds < 33:
            output_lines.append(f"{next_time.strftime('%H:%M:%S')} WARNING: Heartbeat interval = {delta_seconds} seconds\n")
        elif delta_seconds >= 33:
            output_lines.append(f"{next_time.strftime('%H:%M:%S')} ERROR: Heartbeat interval = {delta_seconds} seconds\n")

    # Записуємо у файл результат
    with open(output_log_path, "w") as log_file:
        log_file.writelines(output_lines)

    print(f"Готово. Результат записано у файл: {output_log_path}")


# Запуск функції
if __name__ == "__main__":
    analyze_heartbeat(
        input_log_path="hblog.txt",
        output_log_path="hb_test.log",
        target_key="Key TSTFEED0300|7E3E|0400"
    )