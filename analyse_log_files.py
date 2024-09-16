#[Дата] [Время] [Уровень] Сообщение
import sys 
def parse_log_line(line: str) ->dict:
    parts= line.split(' ', 3) #разбиваем строку на 4 части 
    if len(parts) == 4: #если формат верный 
        return {
            "date": parts[0],
            "time": parts[1],
            "level": parts[2],
            "message": parts[3]
        }
    else:
        return{} #если формат неверный возвращаем пустой словарь
#загрузка логов
def load_logs(file_path: str) ->list:
    logs=[]
    try:
        with open(file_path, "r") as file:
            for line in file:
                parsed_log= parse_log_line(line.strip()) #убираем пробелы и передаем строку в функцию parse_log_line
                logs.append(parsed_log) #добавляем строку словарь в список logs
    except FileNotFoundError:
        print(f"Ошибка: Файл {file_path} не найден")
    return logs

def filter_logs_by_level(logs: list, level:str) ->list:
    return [log for log in logs if log["level"] == level]

def count_logs_by_level(logs: list) -> dict:
    log_counts = {"INFO": 0, "ERROR": 0, "DEBUG": 0, "WARNING": 0}
    for log in logs:
        if log ["level"] in log_counts: 
            log_counts[log["level"]] += 1 #увеличиваем счетчик 
    return log_counts
            
def display_log_counts(counts: dict):
    for level, count in counts.items():
        print(f"{level}: {count} записей")






def main():
    # получаем путь к файлу логов из аргументов
    log_file_path = sys.argv[1]  
    # загружаем логи из указанного файла
    logs = load_logs(log_file_path)  
    # проверяем, передан ли второй аргумент (уровень логирования)
    if len(sys.argv) == 3:
        # получаем уровень логирования и переводим его в верхний регистр
        level = sys.argv[2].upper()  
        # фильтруем логи по уровню
        filtered_logs = filter_logs_by_level(logs, level)   
        # выводим отфильтрованные логи
        for log in filtered_logs:
            print(f"{log['date']} {log['time']} {log['level']} {log['message']}")
    else:
        # если уровень не передан, считаем количество логов для каждого уровня
        log_counts = count_logs_by_level(logs)  
        # выводим количество логов для каждого уровня
        display_log_counts(log_counts)
    

if __name__ == "__main__":
    main()
    
    
    #python3  analyse_log_files.py log_file.log
    #python3 analyse_log_files.py log_file.log ERROR
