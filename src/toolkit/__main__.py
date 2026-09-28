import sys

from toolkit.calculator import calculate
from toolkit.converter import converter
from toolkit.errors import ProjectErrors


def main():
    try:
        if len(sys.argv) < 2:
            print('Не указана команда', file=sys.stderr)
            return 2

        command = sys.argv[1]

        if command == '--help' or command == '-h':
            print("""
Toolkit — калькулятор и конвертер единиц измерения.

Использование:

  python3 -m toolkit calc "EXPRESSION"

  python3 -m toolkit convert VALUE --from UNIT --to UNIT

Примеры:

  python3 -m toolkit calc "2+3*4"

  python3 -m toolkit convert 1000 --from mm --to m

Команды:

  calc       Вычислить математическое выражение
  convert    Перевести единицы измерения
  --help     Показать справку
""")
            return 0

        elif command =='calc':
            if len(sys.argv) < 3:
                print('Не указано выражение', file=sys.stderr)
                return 2

            expression = ' '.join(sys.argv[2:])
            result = calculate(expression)
            print(result)
            return 0

        elif command == 'convert':
            if len(sys.argv) != 7 or sys.argv[3] != '--from' or sys.argv[5] != '--to':
                print('Неверные аргументы', file=sys.stderr)
                return 2

            value = float(sys.argv[2])
            from_unit = sys.argv[4]
            to_unit = sys.argv[6]

            result = converter(value, from_unit, to_unit)
            print(result)
            return 0

        else:
            print(f'Неизвестная команда: {command}', file=sys.stderr)
            return 2

    except ProjectErrors as error:
        print(error, file=sys.stderr)
        return 2

if __name__ == '__main__':
    sys.exit(main())


