import asyncio
import logging

from aiogram import Bot
from aiogram import Dispatcher
from aiogram import types
from aiogram.filters import CommandStart, Command

import tockeen
dp = Dispatcher()


@dp.message(CommandStart())
async def handle_start(message: types.Message):
    await message.answer(text=f'Здравствуй, {message.from_user.first_name}')


@dp.message(Command('help'))
async def handle_help(message: types.Message):
    text = 'Я бот, который отвечает на вопросы для теста по операционным системам. Ты можешь выбрать номер вопроса с помощью меню, а я постараюсь ответить.\n'
    await message.answer(text=text)


@dp.message(Command('question1'))
async def handle_help(message: types.Message):
    text = 'Что такое LA? В каких единицах измеряется?\n LA (load average) — параметр, определяющий среднюю нагрузку на систему за период времени (1 мин, 5 минут, 15 минут). Изменяется в количестве задач на одно ядро процессора. На нагрузку системы также влияет количество задач ввода-вывода и задержка сети. Также влияние на расчета LA оказывает: 1. Технология Hyper-Threading, которая делит одно физическое ядро на 2 логических, 2. Технология Turbo Bust, которая позволяет разгонять тактовую частоту процессора и работать на частоте выше заявленной, т.е. выше номинальной частоты'
    entity_bold = types.MessageEntity(
        type='bold',
        offset=0,
        length=len('Что такое LA? В каких единицах измеряется?'),
    )
    entities = [entity_bold]
    await message.answer(text=text, entities=entities)


@dp.message(Command('question2'))
async def handle_help(message: types.Message):
    text = 'Что будет если на сервере LA = 100?\n Вероятно, что на сервере будет наблюдаться замедленная работа сервисов, но если параметр LA равен количеству ядер в системе или количеству потоков в системе, то данная нагрузка является нормальной'
    entity_bold = types.MessageEntity(
        type='bold',
        offset=0,
        length=len('Что будет если на сервере LA = 100?'),
    )
    entities = [entity_bold]
    await message.answer(text=text, entities=entities)


@dp.message(Command('question3'))
async def handle_help(message: types.Message):
    text = 'Почему при высоких показателях значения LA на сервере может не наблюдаться проблем (консоль ssh отзывается, сервисы работают в обычном режиме)?\n На параметр нагрузки LA влияет также и ожидание ввода-вывода (параметр wa в утилите top) в дисков и задержка сети. Данные параметры могут не влиять на работу основных сервисов в системе, но учитываются при расчете общей нагрузки на систему'
    entity_bold = types.MessageEntity(
        type='bold',
        offset=0,
        length=len('Почему при высоких показателях значения LA на сервере может не наблюдаться проблем (консоль ssh отзывается, сервисы работают в обычном режиме)?'),
    )
    entities = [entity_bold]
    await message.answer(text=text, entities=entities)


@dp.message(Command('question4'))
async def handle_help(message: types.Message):
    text = 'Представлен вывод команды top. Что означает каждая запись в выводе? \n top - 21:29:24 up 14:18, 1 user, load average: 0,78, 1,48, 1,10 \n Tasks: 277 total, 3 running, 274 sleeping, 0 stopped, 0 zombie \n %Cpu(s): 12,4 us, 2,5 sy, 0,1 ni, 84,8 id, 0,1 wa, 0,0 hi, 0,1 si, 0,0 st \n KiB Mem : 7106404 total, 306972 free, 3127144 used, 3672288 buff/cache \n KiB Swap: 8191996 total, 8191996 free, 0 used. 3270520 avail Mem\n top – название утилиты\n 21:29:24 – текущее время системы\n up 14:18 – сколько часов:минут система работает с момента последнего запуска\n 1 user – количество пользователей авторизованных в системе\n load average: 0,78, 1,48, 1,10 – параметр средней нагрузки на систему за период времени 1 минута, 5 минут, 15 минут\n 277 total – всего процессов в системе\n 3 running – количество процессов в работе\n 274 sleeping – количество процессов в состоянии sleeping: ожидает какого-либо события или сигнала\n 0 stopped – количество приостановленных процессов сигналом STOP или выполнением трассировки\n 0 zombie – количество зомби-процессов, которые завершили своё выполнение, но присутствующие в системе, чтобы дать родительскому процессу считать свой код завершения\n KiB Mem – количество оперативной памяти в кибибайтах (кратно 1024): 7106404 total — всего доступно оперативной памяти в системе, 306972 free — свободно оперативной памяти для использования, 3127144 used — использовано оперативной памяти, 3672288 buff/cache — буферизовано/закешировано оперативной памяти\n KiB Swap – количество swap-памяти в кибибайтах (кратно 1024), которые выделено на диске: 8191996 total – всего выделено swap-памяти, 8191996 free – свободно swap-памяти 0 used – использовано swap-памяти, 3270520 avail Mem – доступно для использования swap-памяти'
    entity_bold = types.MessageEntity(
        type='bold',
        offset=0,
        length=len('Представлен вывод команды top. Что означает каждая запись в выводе? \n top - 21:29:24 up 14:18, 1 user, load average: 0,78, 1,48, 1,10 \n Tasks: 277 total, 3 running, 274 sleeping, 0 stopped, 0 zombie \n %Cpu(s): 12,4 us, 2,5 sy, 0,1 ni, 84,8 id, 0,1 wa, 0,0 hi, 0,1 si, 0,0 st \n KiB Mem : 7106404 total, 306972 free, 3127144 used, 3672288 buff/cache \n KiB Swap: 8191996 total, 8191996 free, 0 used. 3270520 avail Mem'),
    )
    entities = [entity_bold]
    await message.answer(text=text, entities=entities)


@dp.message(Command('question5'))
async def handle_help(message: types.Message):
    text = 'Как в утилите top в Linux посмотреть нагрузку на каждое ядро процессора?\n В утилите top нажать 1, чтобы отобразить все ядра в системе'
    entity_bold = types.MessageEntity(
        type='bold',
        offset=0,
        length=len('Как в утилите top в Linux посмотреть нагрузку на каждое ядро процессора?'),
    )
    entities = [entity_bold]
    await message.answer(text=text, entities=entities)


@dp.message(Command('question6'))
async def handle_help(message: types.Message):
    text = 'Как в утилите top в Linux посмотреть какой командой был запущен процесс?\n В утилите top нажать c, чтобы отобразить команды, которыми были запущены процессы'
    entity_bold = types.MessageEntity(
        type='bold',
        offset=0,
        length=len('Как в утилите top в Linux посмотреть какой командой был запущен процесс?'),
    )
    entities = [entity_bold]
    await message.answer(text=text, entities=entities)


@dp.message(Command('question7'))
async def handle_help(message: types.Message):
    text = 'Где хранятся имена файлов/директорий?\n Inodes не содержат имён файлов, только другие метаданные файла\n Каталоги Unix представляют собой списки ассоциативных структур, каждая из которых содержит одно имя файла и один номер индекса\n Драйвер файловой системы должен найти каталог, ищущий определенное имя файла, а затем преобразовать имя файла в правильный соответствующий номер индекса'
    entity_bold = types.MessageEntity(
        type='bold',
        offset=0,
        length=len('Где хранятся имена файлов/директорий?'),
    )
    entities = [entity_bold]
    await message.answer(text=text, entities=entities)


@dp.message(Command('question8'))
async def handle_help(message: types.Message):
    text = 'Как удалить файл с именем -rf?\n rm ./-rf'
    entity_bold = types.MessageEntity(
        type='bold',
        offset=0,
        length=len('Как удалить файл с именем -rf?'),
    )
    entities = [entity_bold]
    await message.answer(text=text, entities=entities)


@dp.message(Command('question9'))
async def handle_help(message: types.Message):
    text = 'Как посмотреть описание дескриптора? Как посмотреть время последней модификации файла?\n Посмотреть полную информацию по дискриптору возможно командой stat <path_to_file>. Время модификации:\n stat --format=%y dira'
    entity_bold = types.MessageEntity(
        type='bold',
        offset=0,
        length=len('Как посмотреть описание дескриптора? Как посмотреть время последней модификации файла?'),
    )
    entities = [entity_bold]
    await message.answer(text=text, entities=entities)


@dp.message(Command('question10'))
async def handle_help(message: types.Message):
    text = 'Для чего нужна переменная окружения PATH?\n Переменная окружения PATH содержит абсолютные пути директорий, в которых производится поиск исполняемых файлов при вводе команд'
    entity_bold = types.MessageEntity(
        type='bold',
        offset=0,
        length=len('Для чего нужна переменная окружения PATH?'),
    )
    entities = [entity_bold]
    await message.answer(text=text, entities=entities)


@dp.message(Command('question11'))
async def handle_help(message: types.Message):
    text = 'Как посмотреть нагрузку на диски?\n Установить утилиту sysstat, проверить нагрузку на диски iostat -xtc'
    entity_bold = types.MessageEntity(
        type='bold',
        offset=0,
        length=len('Как посмотреть нагрузку на диски?'),
    )
    entities = [entity_bold]
    await message.answer(text=text, entities=entities)


@dp.message(Command('question12'))
async def handle_help(message: types.Message):
    text = 'Что такое файл в понятиях Unix-like операционных системах?\n Файлы – это объекты, в которые мы записываем информацию и наши данные, исполняемые файлы, но кроме этих привычных нам понятий здесь есть файлы специального назначения – файлы устройств, файлы туннелей, сокетов и многое другое\n Типы файлов в Linux:\n ⁃ Обычные файлы, для хранения информации;\n ⁃ Специальные файлы – для устройств и туннелей;\n ⁃ Директории'
    entity_bold = types.MessageEntity(
        type='bold',
        offset=0,
        length=len('Что такое файл в понятиях Unix-like операционных системах?'),
    )
    entities = [entity_bold]
    await message.answer(text=text, entities=entities)


@dp.message(Command('question13'))
async def handle_help(message: types.Message):
    text = 'Что такое RAID? Какие массивы бывают?\n RAID (Redundant Array of Independent Disks) – избыточный массив независимых дисков, технология виртуализации данных для объединения нескольких физических дисковых устройств в логический модуль для повышения отказоустойчивости и производительности\n В зависимости от количества дисков и класса отказоустойчивости существуют следующие основные типы RAID:\n - RAID 0;\n - RAID 1;\n - RAID 5;\n - RAID 6;\n - RAID 10'
    entity_bold = types.MessageEntity(
        type='bold',
        offset=0,
        length=len('Что такое RAID? Какие массивы бывают?'),
    )
    entities = [entity_bold]
    await message.answer(text=text, entities=entities)


@dp.message(Command('question14'))
async def handle_help(message: types.Message):
    text = 'При каком количестве одновременно вышедших из строя дисков обеспечивает работоспособность RAID 6?\n 2 диска'
    entity_bold = types.MessageEntity(
        type='bold',
        offset=0,
        length=len('При каком количестве одновременно вышедших из строя дисков обеспечивает работоспособность RAID 6?'),
    )
    entities = [entity_bold]
    await message.answer(text=text, entities=entities)


@dp.message(Command('question15'))
async def handle_help(message: types.Message):
    text = 'В чем разница между объявлением переменной export VAR="VALUE" и VAR="VALUE" в bash?\n При объявлении переменной через export – переменная будет доступна в любых других процессах, при обычном объявлении переменной – переменная будет доступна только в запущенном процессе'
    entity_bold = types.MessageEntity(
        type='bold',
        offset=0,
        length=len('В чем разница между объявлением переменной export VAR="VALUE" и VAR="VALUE" в bash?'),
    )
    entities = [entity_bold]
    await message.answer(text=text, entities=entities)


@dp.message(Command('question16'))
async def handle_help(message: types.Message):
    text = 'Как остановить выполнение скрипта в bash при возникновении ошибки в команде?\n Команда set -e завершит скрипт с ошибкой, в случае, если в нижеследующем bash коде будет обнаружена ошибка. По-умолчанию bash скрипт продолжает работу, если в ходе выполнения возникла ошибка'
    entity_bold = types.MessageEntity(
        type='bold',
        offset=0,
        length=len('Как остановить выполнение скрипта в bash при возникновении ошибки в команде?'),
    )
    entities = [entity_bold]
    await message.answer(text=text, entities=entities)


@dp.message(Command('question17'))
async def handle_help(message: types.Message):
    text = 'Что в bash скрипте означает команда set -euo pipefail?\n Команда set устанавливает аттрибуты оболочки с опеределенных опций. Опция -e – означает, что скрипт будет остановлен, когда произойдет ошибка в ходе его выполнения. Опция -u – означает, что скрипт будет остановлен, если в ходе скрипта, будет обнаружена переменная, которая не определена. Опция -o pipefail – означает, что скрипт будет остановлен, если в ходе пайплайна команд будет выявлена ошибка'
    entity_bold = types.MessageEntity(
        type='bold',
        offset=0,
        length=len('Что в bash скрипте означает команда set -euo pipefail?'),
    )
    entities = [entity_bold]
    await message.answer(text=text, entities=entities)


@dp.message(Command('question18'))
async def handle_help(message: types.Message):
    text = 'Как активировать debug режим в bash?\n Команда set -x в начале скрипта активирует вывод в консоль debug информации'
    entity_bold = types.MessageEntity(
        type='bold',
        offset=0,
        length=len('Как активировать debug режим в bash?'),
    )
    entities = [entity_bold]
    await message.answer(text=text, entities=entities)


@dp.message(Command('question19'))
async def handle_help(message: types.Message):
    text = 'Что значит $@ в bash?\n $@ – все параметры переданные скрипту'
    entity_bold = types.MessageEntity(
        type='bold',
        offset=0,
        length=len('Что значит $@ в bash?'),
    )
    entities = [entity_bold]
    await message.answer(text=text, entities=entities)


@dp.message(Command('question20'))
async def handle_help(message: types.Message):
    text = 'Какой код сигнала будет выполнен при исполнении команды kill?\n Сигнал SIGTERM (код 15) – это сигнал по-умолчанию отправляемый при вызове команды kill. Это указывает процессу на завершение работы и обычно считается сигналом для использования при чистом завершении работы'
    entity_bold = types.MessageEntity(
        type='bold',
        offset=0,
        length=len('Какой код сигнала будет выполнен при исполнении команды kill?'),
    )
    entities = [entity_bold]
    await message.answer(text=text, entities=entities)


@dp.message(Command('question21'))
async def handle_help(message: types.Message):
    text = 'Как выполнить фильтрацию вывода команды, чтобы на экран были выведены только ошибки (STDERR), игнорируя STDOUT?\n cmd 2>&1 >/dev/null | grep pattern'
    entity_bold = types.MessageEntity(
        type='bold',
        offset=0,
        length=len('Как выполнить фильтрацию вывода команды, чтобы на экран были выведены только ошибки (STDERR), игнорируя STDOUT?'),
    )
    entities = [entity_bold]
    await message.answer(text=text, entities=entities)


@dp.message(Command('question22'))
async def handle_help(message: types.Message):
    text = 'Какую команду необходимо выполнить, чтобы посмотреть какие пользователи вошли в систему в систему?\n Команда w покажет список пользователей, которые вошли на сервер'
    entity_bold = types.MessageEntity(
        type='bold',
        offset=0,
        length=len('Какую команду необходимо выполнить, чтобы посмотреть какие пользователи вошли в систему в систему?'),
    )
    entities = [entity_bold]
    await message.answer(text=text, entities=entities)


@dp.message(Command('question23'))
async def handle_help(message: types.Message):
    text = 'Какой файл необходимо отредактировать, чтобы отключить ssh аутентификацию по паролю?\n Необходимо редактировать файл\n /etc/ssh/sshd_config\n отвечающий за конфигурацию сервиса ssh'
    entity_bold = types.MessageEntity(
        type='bold',
        offset=0,
        length=len('Какой файл необходимо отредактировать, чтобы отключить ssh аутентификацию по паролю?'),
    )
    entities = [entity_bold]
    await message.answer(text=text, entities=entities)


@dp.message(Command('question24'))
async def handle_help(message: types.Message):
    text = 'В каком файле находится информация о смонтированных каталогах в файловую систему?\n Файл\n /etc/fstab\n содержит информацию о смонтированных каталогах в файловую систему'
    entity_bold = types.MessageEntity(
        type='bold',
        offset=0,
        length=len('В каком файле находится информация о смонтированных каталогах в файловую систему?'),
    )
    entities = [entity_bold]
    await message.answer(text=text, entities=entities)


@dp.message(Command('question25'))
async def handle_help(message: types.Message):
    text = 'Что выведет команда cat a и почему?\n mkdir /tmp/abc\n cd /tmp/abc\n ls >a 2>b\n cat a\n cat a выведет\n a\n b\n  Обработка команды идёт справа налево. Сначала создается файл b, потом создается файл a, команда ls отображает список файлов в текущей директории (файлы a и b уже созданы) в одну колонну и перенаправляет стандартный поток вывода (>) в файл a, а стандартный поток ошибок 2 в файл b'
    entity_bold = types.MessageEntity(
        type='bold',
        offset=0,
        length=len('Что выведет команда cat a и почему?\n mkdir /tmp/abc\n cd /tmp/abc\n ls >a 2>b\n cat a'),
    )
    entities = [entity_bold]
    await message.answer(text=text, entities=entities)


@dp.message(Command('question26'))
async def handle_help(message: types.Message):
    text = 'В bash-скрипте указан атрибут оболочки set -x. В одной из команд происходит ошибка и скрипт завершает свою работу. Как сделать, чтобы при возникновении ошибки в определенной команде скрипт продолжил свою работу?\n 1 вариант: указать || true после выполнения команды с ошибкой.\n <command with error> ||true\n 2 вариант: до выполнения данной команды указать set +e для игнорирования ошибок, начиная со следующей строки и после выполнения команды указать set -e для завершения работы скрипта в случае ошибки, начиная со следующей строки.\n set -e\n <command 1>\n <command 2>\n set +e\n <command 3 wih error>\n set -e'
    entity_bold = types.MessageEntity(
        type='bold',
        offset=0,
        length=len('В bash-скрипте указан атрибут оболочки set -x. В одной из команд происходит ошибка и скрипт завершает свою работу. Как сделать, чтобы при возникновении ошибки в определенной команде скрипт продолжил свою работу?'),
    )
    entities = [entity_bold]
    await message.answer(text=text, entities=entities)


@dp.message(Command('question27'))
async def handle_help(message: types.Message):
    text = 'Что такое системный вызов, какие они бывают?\n Системный вызов – обращение программы к ядру операционной системы для выполнения какой-либо операции.\n В Unix, Unix-like и других POSIX-совместимых операционных системах популярными системными вызовами являются:\n ⁃ open;\n ⁃ read;\n ⁃ write;\n ⁃ close;\n ⁃ wait;\n ⁃ exec;\n ⁃ fork;\n ⁃ exit;\n ⁃ kill'
    entity_bold = types.MessageEntity(
        type='bold',
        offset=0,
        length=len('Что такое системный вызов, какие они бывают?'),
    )
    entities = [entity_bold]
    await message.answer(text=text, entities=entities)


@dp.message(Command('question28'))
async def handle_help(message: types.Message):
    text = ' Что такое сигнал в Unix, зачем они нужны и разница между 9 и 15 сигналами?\n Сигнал – в Unix-like операционных системах – асинхронное (в случайное время) уведомление процесса для обработки какого-либо события. Один из основных способов взаимодействия между процессами.\n Посылка сигналов от одного процесса к другому обычно осуществляется при помощи системного вызова kill. Его первый параметр – PID процесса, которому посылается сигнал; второй параметр – номер сигнала.\n kill(1111, SIGTERM);'
    entity_bold = types.MessageEntity(
        type='bold',
        offset=0,
        length=len('Что такое сигнал в Unix, зачем они нужны и разница между 9 и 15 сигналами?'),
    )
    entities = [entity_bold]
    await message.answer(text=text, entities=entities)


@dp.message(Command('question29'))
async def handle_help(message: types.Message):
    text = 'Что такое inode? Какая информация там хранится?\n Inode (индексный дескриптор) – структура данных, в которой хранятся метаданные файла и перечислены блоки с данными файла. Хранит всю информацию, кроме имени файла и данных. Каждый файл в данном каталоге является записью с именем файла и номером индекса. Вся остальная информация о файле извлекается из таблицы индексов путем ссылки на номер индекса. Номера inodes уникальны на уровне раздела. Каждый раздел как собственная таблица индексов. Если у вас закончились inode, вы не можете создавать новые файлы, даже если у вас есть свободное место на данном разделе.\n Inodes хранит метаданные о файле, к которому он относится. Эти метаданные содержат всю информацию об указанном файле.\n ⁃ Размер;\n ⁃ Разрешение;\n ⁃ Владелец/групп;\n ⁃ Расположение жесткого диска;\n ⁃ Дата/время;\n ⁃ Любая другая необходимая информация'
    entity_bold = types.MessageEntity(
        type='bold',
        offset=0,
        length=len('Что такое inode? Какая информация там хранится?'),
    )
    entities = [entity_bold]
    await message.answer(text=text, entities=entities)


@dp.message(Command('question30'))
async def handle_help(message: types.Message):
    text = 'Что такое hard link? В чем разница между hard link и soft link? Примеры их практического применения.\n Hard link: Ссылка на файл в файловой системе с использованием такого же inode идентификатора, как у файла, на который ссылаемся. Создадим файл realFile.\n touch realFile\n Создадим hard link командой ln <целевой_файл> <файл_ссылка>:\n ln realFile hardLink\n Проверим, что inode у файла realFile и hard ссылке hardLink имеют одинаковый идентификатор.\n $ ls -li\n итого 0\n 2359720 -rw-r--r-- 2 rmntrvn rmntrvn 0 апр 25 23:24 hardLink\n 2359720 -rw-r--r-- 2 rmntrvn rmntrvn 0 апр 25 23:24 realFile\n Как видно realFile и hardLink имеют одинаковый идентификатор inode.\n Soft link: Создадим soft ссылку на файл realFile.\n ln -s realFile softLink\n Проверим, что чистовой идентификатор softLink отличается от числового идентификатора realFile.\n $ ls -li\n итого 0\n 2359720 -rw-r--r-- 2 rmntrvn rmntrvn 0 апр 25 23:24 hardLink\n 2366763 lrwxrwxrwx 1 rmntrvn rmntrvn 8 апр 25 23:29 softLink -> realFile\n Некоторые нюансы:\n Soft ссылки используют различные номера inode, чем основные файлы.\n Soft ссылки становятся полезными, если исходный файл был удален.\n Soft ссылки могут быть созданы из каталогов.\n Soft ссылка может быть создана на пересечении файловых систем.\n Hard ссылка может размещаться только на том же логическом разделе, что и оригинальный файл. Это связано с независимой идентификацией файлов на разных разделах.\n Создание жестких ссылок не поддерживается для папок — только для файлов.\n Файловая система должна поддерживать работу с hard ссылками'
    entity_bold = types.MessageEntity(
        type='bold',
        offset=0,
        length=len('Что такое hard link? В чем разница между hard link и soft link? Примеры их практического применения'),
    )
    entities = [entity_bold]
    await message.answer(text=text, entities=entities)


@dp.message(Command('question31'))
async def handle_help(message: types.Message):
    text = 'Какие состояния процессов существуют? Что значит состояние процесса D?'
    entity_bold = types.MessageEntity(
        type='bold',
        offset=0,
        length=len('Какие состояния процессов существуют? Что значит состояние процесса D?'),
    )
    entities = [entity_bold]
    await message.answer(text=text, entities=entities)


@dp.message(Command('question32'))
async def handle_help(message: types.Message):
    text = 'Что такое процесс-зомби и процесс-сирота? Можно ли самостоятельно сделать зомби?\n Процесс-зомби – дочерний процесс в Unix-системе, завершивший своё выполнение, но ещё присутствующий в списке процессов операционной системы, чтобы дать родительскому процессу считать код завершения.\n Удаление зомби возлагается на родительский процесс или системный вызов wait() также может это выполнить, поэтому перед ее вызовом не нужно проверять, продолжает ли выполняться требуемый дочерний процесс. Если родительский процесс не удалит своих потомков, то они останутся в состоянии зомби.\n Убить зомби-процесс невозможно. Чтобы убить зомби-процесс нужно найти родительский процесс и завершить его или перезапустить. Найти зомби-процессы и их родителей можно следующей командой:\n ps ajx | grep -w Z\n PID’ы процессов родителей в 3 колонке. Убить процесс следующей командой:\n kill -9 <PID процесса родителя>\n Процесс-сирота — в семействе операционных систем UNIX вспомогательный процесс, чей основной процесс (или связь с ним) был завершен нештатно (не подав сигнала на завершение работы).\n Отличие в том, что процесс-сирота (orphan process) всё еще активен. Его родительский процесс был по какой-либо причине прерван, и сирота теперь переходит под руководство init, чей ID процесса равен 1. PPID orphan процесса получит значение 1. Пользователь также может создать подобный процесс, отсоединив его от терминала. Сиротские процессы используют много ресурсов, их легко найти с помощью top или htop.\ В отличии от процесса-сироты, зомби-процесс неактивен, но контролируется родительским процессом, пока тот не решит, что статус выхода дочерних процессов больше не нужен. Он не использует ресурсы и не может быть запланирован для выполнения. Иногда родительский процесс удерживает дочерний процесс в состоянии зомби, чтобы гарантировать, что будущие дочерние процессы не получат тот же PID. Если вы уничтожите родителя зомби-процесса, зомби-процесс тоже умрет. Для этого найдите родительский PID (PPID) зомби и отправьте ему сигнал SIGCHLD (17): kill -17 ppid'
    entity_bold = types.MessageEntity(
        type='bold',
        offset=0,
        length=len('Что такое процесс-зомби и процесс-сирота? Можно ли самостоятельно сделать зомби?'),
    )
    entities = [entity_bold]
    await message.answer(text=text, entities=entities)


@dp.message(Command('question33'))
async def handle_help(message: types.Message):
    text = 'Что такое файловый дескриптор? Какая информация там хранится?\n Файловый дескриптор – неотрицательное целое число, которое используется в интерфейсе между пространством пользователя и пространством ядра (kernel) для идентификации ресурсов файла / сокета. Когда создаётся новый поток ввода-вывода, ядро возвращает процессу, создавшему поток ввода-вывода, его файловый дескриптор'
    entity_bold = types.MessageEntity(
        type='bold',
        offset=0,
        length=len('Что такое файловый дескриптор? Какая информация там хранится?'),
    )
    entities = [entity_bold]
    await message.answer(text=text, entities=entities)


@dp.message(Command('question34'))
async def handle_help(message: types.Message):
    text = 'Что такое buffer/cache память? Для чего нужна?'
    entity_bold = types.MessageEntity(
        type='bold',
        offset=0,
        length=len('Что такое buffer/cache память? Для чего нужна?'),
    )
    entities = [entity_bold]
    await message.answer(text=text, entities=entities)


@dp.message(Command('question35'))
async def handle_help(message: types.Message):
    text = 'Представлен вывод команды free.\n $ free -m\n total        used        free      shared  buff/cache   available\n Mem:           6930        3598         843         183        2489        2919\n Swap:         15999           4       15995\n Почему доступной (available) памяти сейчас 2919, если свободной (free) памяти 843?\n Total. Эта цифра представляет всю существующую память.\n Used. Вычисление общего значения оперативной памяти системы за вычетом выделенной свободной, разделяемой, буферной и кэш-памяти.\n used = total - free - buff/cache\n Free – свободная память в системе.\n Shared – память, используемая (преимущественно) в tmpfs\n Buffer, и Cache идентифицируют память, используемую для нужд ядра / операционной системы. Буфер и кеш складываются вместе, а сумма указывается в разделе «buff/cache».\n Available – примерное количество оперативной памяти, доступное для запуска новых приложений без использования ими раздела подкачки. В отличие от поля free, это поле принимает в расчёт страницу cache и также то, что не вся рекуперируемая (пригодная для повторного использования) память будет возвращена для рекуперации из-за того, что элементы используются в данный момент'
    entity_bold = types.MessageEntity(
        type='bold',
        offset=0,
        length=len('Представлен вывод команды free.\n $ free -m\n total        used        free      shared  buff/cache   available\n Mem:           6930        3598         843         183        2489        2919\n Swap:         15999           4       15995\n Почему доступной (available) памяти сейчас 2919, если свободной (free) памяти 843?'),
    )
    entities = [entity_bold]
    await message.answer(text=text, entities=entities)


@dp.message(Command('question36'))
async def handle_help(message: types.Message):
    text = 'Порядок загрузки дистрибутива Linux.\n 1. Включение компьютера кнопкой\n 2. Загрузить BIOS / UEFI из NVRAM\n 3. Собрать сведения об аппаратуре\n 4. Выбрать устройства для запуска (диск, сеть)\n 5. Идентифицировать системный раздел EFI\n 6. Загрузить BIOS / UEFI из NVRAM\n 7. Определить какое ядро загрузить\n 8. Загрузить ядро\n 9. Создать структуры данных ядра\n 10. Запустить init / systemd как PID 1\n 11. Выполнить сценарии запуска\n 12. Запустить систему'
    entity_bold = types.MessageEntity(
        type='bold',
        offset=0,
        length=len('Порядок загрузки дистрибутива Linux.'),
    )
    entities = [entity_bold]
    await message.answer(text=text, entities=entities)


@dp.message(Command('question37'))
async def handle_help(message: types.Message):
    text = 'Что такое GitFlow?\n GitFlow — альтернативная модель ветвления Git, в которой используются функциональные ветки и несколько основных веток'
    entity_bold = types.MessageEntity(
        type='bold',
        offset=0,
        length=len('Что такое GitFlow?'),
    )
    entities = [entity_bold]
    await message.answer(text=text, entities=entities)


@dp.message(Command('question38'))
async def handle_help(message: types.Message):
    text = 'Чем merge отличается от rebase?\n В merge изменяется только целевая ветка, а история исходных веток остается неизменной в отличие от rebase, в котором перезаписывается история, потому что она передает завершенную работу из одной ветки в другую, и в процессе устраняется нежелательная история'
    entity_bold = types.MessageEntity(
        type='bold',
        offset=0,
        length=len('Чем merge отличается от rebase?'),
    )
    entities = [entity_bold]
    await message.answer(text=text, entities=entities)


@dp.message(Command('question39'))
async def handle_help(message: types.Message):
    text = 'Чем tag отличается от branch?\n Branch всегда указывает на верхнюю часть строки разработки, т.е. с созданием нового коммита указатель ветки продвигается вперед. А teg не изменяется, указывая всегда на один и тот же объект'
    entity_bold = types.MessageEntity(
        type='bold',
        offset=0,
        length=len('Чем tag отличается от branch?'),
    )
    entities = [entity_bold]
    await message.answer(text=text, entities=entities)


@dp.message(Command('question40'))
async def handle_help(message: types.Message):
    text = 'В ветке develop есть коммит с изменениями, которые нужно перенести в ветку master. Как это сделать?'
    entity_bold = types.MessageEntity(
        type='bold',
        offset=0,
        length=len('В ветке develop есть коммит с изменениями, которые нужно перенести в ветку master. Как это сделать?'),
    )
    entities = [entity_bold]
    await message.answer(text=text, entities=entities)


@dp.message(Command('question41'))
async def handle_help(message: types.Message):
    text = 'Для чего нужна команда git commit --amend?\n Команда git commit --amend — это удобный способ изменить последний коммит. Она позволяет объединить проиндексированные изменения с предыдущим коммитом без создания нового коммита. Ее можно использовать для редактирования комментария к предыдущему коммиту без изменения состояния кода в нем'
    entity_bold = types.MessageEntity(
        type='bold',
        offset=0,
        length=len('Для чего нужна команда git commit --amend?'),
    )
    entities = [entity_bold]
    await message.answer(text=text, entities=entities)


@dp.message(Command('question42'))
async def handle_help(message: types.Message):
    text = 'Что такое Trunk-based development?\n Trunk-based development - модель ветвления в системен контроля версий, в которой разработчики работают над кодом в единственной ветке под названием ‘trunk’ . Эта модель позволяет не создавать другие долгоживущие ветки и описывает технику как именно это делать'
    entity_bold = types.MessageEntity(
        type='bold',
        offset=0,
        length=len('Что такое Trunk-based development?'),
    )
    entities = [entity_bold]
    await message.answer(text=text, entities=entities)


@dp.message(Command('question43'))
async def handle_help(message: types.Message):
    text = 'Состояние репозитория ушло на много коммитов вперед. Как откатить весь репозиторий к определенному коммиту?\n git revert 9abc8de1'
    entity_bold = types.MessageEntity(
        type='bold',
        offset=0,
        length=len('Состояние репозитория ушло на много коммитов вперед. Как откатить весь репозиторий к определенному коммиту?'),
    )
    entities = [entity_bold]
    await message.answer(text=text, entities=entities)


@dp.message(Command('question44'))
async def handle_help(message: types.Message):
    text = 'В репозиторий запушен коммит с изменениями в двух файлах. Как откатить изменения этого коммита?\n git reset --hard HEAD~1'
    entity_bold = types.MessageEntity(
        type='bold',
        offset=0,
        length=len('В репозиторий запушен коммит с изменениями в двух файлах. Как откатить изменения этого коммита?'),
    )
    entities = [entity_bold]
    await message.answer(text=text, entities=entities)


@dp.message(Command('question45'))
async def handle_help(message: types.Message):
    text = 'Что такое Docker? В чем отличие контейнера от образа?\n Docker – это программная платформа для быстрой разработки, тестирования и развертывания приложений. Docker упаковывает ПО в стандартизованные блоки, которые называются контейнерами. Каждый контейнер включает все необходимое для работы приложения: библиотеки, системные инструменты, код и среду исполнения. Контейнер Docker – это автономное запускаемое программное приложение или сервис. С другой стороны, образ Docker – это шаблон, загруженный в контейнер для его запуска, например набор инструкций'
    entity_bold = types.MessageEntity(
        type='bold',
        offset=0,
        length=len('Что такое Docker? В чем отличие контейнера от образа?'),
    )
    entities = [entity_bold]
    await message.answer(text=text, entities=entities)


@dp.message(Command('question46'))
async def handle_help(message: types.Message):
    text = 'Какие инструкции есть у Dockerfile?\n Каждая строка в Dockerfile может содержать инструкцию, все они обрабатываются сверху вниз. Инструкции выглядят так:\n FROM ubuntu:18.04\n COPY . /app\n И только инструкции FROM, RUN, COPY и ADD создают слои в конечном образе'
    entity_bold = types.MessageEntity(
        type='bold',
        offset=0,
        length=len('Какие инструкции есть у Dockerfile?'),
    )
    entities = [entity_bold]
    await message.answer(text=text, entities=entities)


@dp.message(Command('question47'))
async def handle_help(message: types.Message):
    text = 'Чем отличается CMD от ENTRYPOINT в Dockerfile?\n ENTRYPOINT используется для определения основной цели контейнера, и его инструкцию нельзя переопределить, если она явно не указана с помощью флага -entrypoint , в то время как CMD обеспечивает поведение по умолчанию, которое может быть переопределено.'
    entity_bold = types.MessageEntity(
        type='bold',
        offset=0,
        length=len('Чем отличается CMD от ENTRYPOINT в Dockerfile?'),
    )
    entities = [entity_bold]
    await message.answer(text=text, entities=entities)


@dp.message(Command('question48'))
async def handle_help(message: types.Message):
    text = 'Чем отличается COPY от ADD в Dockerfile?\n Во-первых, директива ADD может принимать удаленный URL-адрес в качестве исходного аргумента, во-вторых, директива ADD автоматически расширяет файлы tar в файловую систему образа, в отличие от COPY'
    entity_bold = types.MessageEntity(
        type='bold',
        offset=0,
        length=len('Чем отличается COPY от ADD в Dockerfile?'),
    )
    entities = [entity_bold]
    await message.answer(text=text, entities=entities)


@dp.message(Command('question49'))
async def handle_help(message: types.Message):
    text = 'Какие есть best practices для написания Dockerfile?\n ⁃ Задавать LABEL и не использовать тег latest\n ⁃ Не использовать автоматическое обновление компонентов;\n ⁃ Производить скачивание пакетов безопасным образом;\n ⁃ Не использовать ADD;\n ⁃ Задавать USER в конце Dockerfile;\n ⁃ Использовать gosu вместо sudo в процессе инициализации;\n ⁃ Distroless images и минимальные образы'
    entity_bold = types.MessageEntity(
        type='bold',
        offset=0,
        length=len('Какие есть best practices для написания Dockerfile?'),
    )
    entities = [entity_bold]
    await message.answer(text=text, entities=entities)


@dp.message(Command('question50'))
async def handle_help(message: types.Message):
    text = 'Какие типы сетевых драйверов используются в docker?\n ⁃ none;\n ⁃ bridge;\n ⁃ host;\n ⁃ overlay;\n ⁃ macvlan'
    entity_bold = types.MessageEntity(
        type='bold',
        offset=0,
        length=len('Какие типы сетевых драйверов используются в docker?'),
    )
    entities = [entity_bold]
    await message.answer(text=text, entities=entities)


@dp.message(Command('question51'))
async def handle_help(message: types.Message):
    text = 'Что такое эфемерные контейнеры?\n Эфемерный Контейнер — контейнер специального назначения, который запускается на некоторое время в существующем поде, чтобы выполнить пользовательские действия, например, с целью поиска и устранения причин сбоев'
    entity_bold = types.MessageEntity(
        type='bold',
        offset=0,
        length=len('Что такое эфемерные контейнеры?'),
    )
    entities = [entity_bold]
    await message.answer(text=text, entities=entities)


async def main():
    logging.basicConfig(level=logging.DEBUG)
    bot = Bot(token=tockeen.BOT_TOKEN)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
