
<div class="container">

  <h1>Telegram Media Saver Bot 🤖📸</h1>

  <p>Простой и удобный Telegram-бот на базе <strong>aiogram 3</strong>, который автоматически сохраняет все отправленные ему фотографии, видео и медиафайлы (документы с MIME-типом <code>image/*</code> или <code>video/*</code>) в указанную папку на вашем компьютере.</p>

  <p>Бот показывает прогресс в реальном времени: сообщает, сколько файлов уже сохранено, и уведомляет о завершении «пачки» файлов.</p>

  <hr>

  <h2>✨ Возможности</h2>
  <ul>
    <li>📥 Автоматическое скачивание <strong>фотографий</strong> (берётся максимальное качество).</li>
    <li>🎬 Скачивание <strong>видео</strong> с сохранением оригинального имени файла.</li>
    <li>📄 Скачивание <strong>документов</strong>, если их MIME-тип начинается с <code>image/</code> или <code>video/</code>.</li>
    <li>📊 Прогресс-бар в чате: сообщение обновляется по мере поступления файлов.</li>
    <li>⏱️ Умное определение конца «пачки»: если файлы не приходят 4 секунды, бот подводит итог.</li>
    <li>🧵 Асинхронная работа — можно отправлять несколько файлов подряд без задержек.</li>
    <li>🔐 Токен хранится в <code>.env</code> — не попадает в репозиторий.</li>
  </ul>

  <hr>

  <h2>📋 Требования</h2>
  <ul>
    <li>Python <strong>3.9+</strong></li>
    <li>Установленный пакетный менеджер <code>pip</code></li>
    <li>Аккаунт Telegram и бот, созданный через <a href="https://t.me/BotFather" target="_blank">@BotFather</a></li>
  </ul>

  <hr>

  <h2>🚀 Установка</h2>

  <h3>1. Клонируйте репозиторий</h3>
  <pre><code>git clone https://github.com/hellround-dev/media_tg_bot.git
cd media_tg_bot</code></pre>

  <h3>2. Создайте и активируйте виртуальное окружение (рекомендуется)</h3>
  <pre><code>python -m venv venv

# macOS / Linux
source venv/bin/activate

# Windows
venv\Scripts\activate</code></pre>

  <h3>3. Установите зависимости</h3>
  <pre><code>pip install aiogram python-dotenv</code></pre>
  <blockquote>
    💡 Можно также установить командой <code>pip install -r requirements.txt</code>.
  </blockquote>

  <h3>4. Получите токен бота</h3>
  <ol>
    <li>Откройте <a href="https://t.me/BotFather" target="_blank">@BotFather</a> в Telegram.</li>
    <li>Отправьте команду <code>/newbot</code>.</li>
    <li>Придумайте имя и username для бота.</li>
    <li>Скопируйте полученный <strong>токен</strong> (вида <code>123456789:ABCdefGhIJKlmNoPQRsTUVwxyZ</code>).</li>
  </ol>

  <h3>5. Настройте переменные окружения</h3>
  <p>Создайте в корне проекта файл <code>.env</code> и вставьте туда свой токен:</p>
  <pre><code>TOKEN="123456789:ABCdefGhIJKlmNoPQRsTUVwxyZ"</code></pre>

  <hr>

  <h2>⚙️ Настройка пути для сохранения</h2>
  <p>По умолчанию файлы сохраняются в папку:</p>
  <pre><code>/Users/hellround/Desktop/Media</code></pre>
  <p>Этот путь задан в переменной <code>DOWNLOAD_DIR</code> в файле <code>media_tg_bot.py</code>. <strong>Обязательно измените его</strong> на удобный вам путь, например:</p>
  <pre><code>DOWNLOAD_DIR = "/home/user/Downloads/Media"   # Linux / macOS
# или
DOWNLOAD_DIR = r"C:\Users\user\Downloads\Media"   # Windows</code></pre>
  <p>Папка создаётся автоматически при первом запуске, если её нет.</p>

  <hr>

  <h2>▶️ Запуск</h2>
  <pre><code>python media_tg_bot.py</code></pre>
  <p>После запуска в консоли появится:</p>
  <pre><code>Инициализация сети...
Бот запущен и готов устанавливать файлы</code></pre>
  <p>Теперь отправьте в чат с ботом любое фото, видео или медиафайл — и он начнёт их сохранять. В чате будет отображаться прогресс, а по завершении — итоговое сообщение с количеством сохранённых файлов.</p>

  <hr>

  <h2>📂 Структура проекта</h2>
  <pre><code>media-tg-bot/
├── media_tg_bot.py      # Основной скрипт бота
├── .env                 # Ваш токен (не коммитится!)
├── .env.example         # Пример файла окружения
├── requirements.txt     # Зависимости (опционально)
├── .gitignore           # Игнорируемые файлы
└── README.md            # Этот файл</code></pre>

  <hr>

  <h2>🔒 Безопасность</h2>
  <ul>
    <li>Файл <code>.env</code> добавлен в <code>.gitignore</code> и <strong>не попадает</strong> в репозиторий.</li>
    <li>В репозитории присутствует только <code>.env.example</code> с пустым значением <code>TOKEN</code>.</li>
    <li>Если вы случайно закоммитили токен — <strong>немедленно</strong> отзовите его через <code>@BotFather</code> (<code>/revoke</code>) и сгенерируйте новый.</li>
  </ul>
  <p>Пример <code>.env.example</code>:</p>
  <pre><code>TOKEN=</code></pre>

  <hr>

  <h2>🛠️ Как это работает</h2>
  <ol>
    <li>Бот слушает сообщения с типами <code>photo</code>, <code>video</code> и <code>document</code> (с медиа-MIME-типом).</li>
    <li>Для каждого файла вызывается <code>bot.get_file()</code> и <code>bot.download_file()</code>.</li>
    <li>Имя файла формируется из <code>time.time_ns()</code> + оригинального имени / <code>file_id</code>, чтобы избежать коллизий.</li>
    <li>Функция <code>handle_progress</code> создаёт одно сообщение-статус и обновляет его, а также запускает задачу <code>wait_for_batch_end</code>, которая через 4 секунды тишины подводит итог.</li>
    <li>По завершении «пачки» счётчик сбрасывается, сообщение редактируется финальным текстом.</li>
  </ol>

  <hr>

  <h2>❓ FAQ</h2>
  <p><strong>Бот не запускается, пишет <code>TOKEN не найден</code>.</strong><br>
  Убедитесь, что файл <code>.env</code> лежит в той же директории, что и скрипт, и содержит строку <code>TOKEN=ваш_токен</code>.</p>

  <p><strong>Файлы не сохраняются.</strong><br>
  Проверьте, что путь <code>DOWNLOAD_DIR</code> существует или может быть создан, и что у процесса есть права на запись.</p>

  <p><strong>Можно ли сохранять файлы из групповых чатов?</strong><br>
  Да, бот работает в любых чатах, куда его добавили. Но учтите, что в группах Telegram может ограничивать доступ бота к истории сообщений — для скачивания нужен доступ к конкретному сообщению (он есть у бота при получении апдейта).</p>

  <p><strong>Поддерживаются ли кружки (видеосообщения)?</strong><br>
  В текущей версии обрабатываются <code>photo</code>, <code>video</code> и <code>document</code>. Видеосообщения (<code>video_note</code>) можно добавить по аналогии с <code>video</code>.</p>

  <hr>

  <h2>🤝 Вклад</h2>
  <p>Приветствуются pull request'ы и issue! Если нашли баг или хотите добавить фичу — открывайте issue.</p>

  <hr>

  <h2>📄 Лицензия</h2>
  <p>Проект распространяется под лицензией <strong>MIT</strong>. Подробности — в файле <code>LICENSE</code>.</p>

  <hr>

  <h2>⭐ Поддержка</h2>
  <p>Если бот оказался полезен — поставьте звёздочку ⭐ на GitHub! Это лучший способ сказать спасибо.</p>

</div>
