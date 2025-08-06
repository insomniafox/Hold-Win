# Enjoy Gaming — Hold & Win Simulator

Это простой симулятор игры "Hold & Win", реализованный на Python. Игрок запускает спины, выигрывает монеты или попадает в бонусную игру, где можно получить дополнительные выигрыши.

---

## Как запустить

1. Установите Python 3.10+
2. Клонируйте проект:
   ```bash
   git clone https://github.com/yourname/enjoy-gaming.git
   cd enjoy-gaming
3. Создаете виртуальное окружение и установите зависимости
    ```bash
    python3 -m venv env
    source env/bin/activate
    pip3 install -r requirements.txt
4. Запустите
    ```bash
    python3 main.py

## Файл конфигурации config.yaml

Игра настраивается через YAML. Пример:
```yaml
    initial_balance: 100
    bet_amount: 1
    
    spin_win_min: 0
    spin_win_max: 2
    
    bonus_trigger_chance: 4
    
    bonus_symbol_chance: 10
    bonus_max_turns: 4
    bonus_attempts: 2
    bonus_symbol_min_value: 1
    bonus_symbol_max_value: 1
```

## Пример вывода

```bash
    Game initialized with starting balance: 100
    Simulation completed after 1000000 spins.
    Total bonus games triggered: 39577
    Final balance: 953984
    Total win accumulated: 953884
    Total bet amount: 1000000
    Calculated RTP: 95.39%
```

## Автор
Разработка и тестирование: Данияров Гулжигит

По вопросам — gulyashshsh@gmail.com
