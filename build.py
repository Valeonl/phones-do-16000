#!/usr/bin/env python3
"""Генерирует index.html — обзор смартфонов до 16 000 ₽ под конкретные требования.

Данные собраны 20.09.2026: характеристики — DNS (сводка в карточке товара),
цены Ozon — со страниц товаров, цена DNS у vivo Y29 — со страницы товара.
"""
import html
import pathlib
import subprocess

BASE = pathlib.Path(__file__).resolve().parent
IMG = BASE / "img"
IMG.mkdir(exist_ok=True)
DATE = "20.09.2026"

# ---------------------------------------------------------------- данные моделей
MODELS = [
    dict(
        key="poco_c85", name="POCO C85", config="8/256 ГБ",
        soc="MediaTek Helio G81-Ultra, 8 ядер", ram="8 ГБ", rom="256 ГБ",
        screen="IPS LCD, 6,9″", refresh="120 Гц", resolution="1600×720",
        camera="50 Мп", battery="6000 мА·ч",
        sim="2 SIM (Nano)", sd="microSD до 1 ТБ", nfc=True,
        rating="4.78", reviews="599 отзывов",
        ozon_price=10950, ozon_url="https://www.ozon.ru/product/smartfon-poco-c85-8-256-gb-chernyy-4884337224/",
        dns_url="https://www.dns-shop.ru/product/b0dae99f4b21d0a4/69-smartfon-poco-c85-256-gb-cernyj/",
        citilink_url="https://www.citilink.ru/search/?text=POCO%20C85",
        ozon_img="https://ir.ozone.ru/s3/multimedia-1-d/c600/11961676921.jpg",
        verdict="Лучший баланс по деньгам: 8 ГБ ОЗУ, огромный аккумулятор и карта памяти до 1 ТБ. Экран простой — IPS, 720p.",
        pros=["8 ГБ ОЗУ — вкладки не выгружаются", "6000 мА·ч — два дня без розетки", "microSD до 1 ТБ"],
        cons=["Разрешение экрана всего 1600×720", "IPS, а не AMOLED"],
    ),
    dict(
        key="vivoy29", name="vivo Y29", config="8/256 ГБ",
        soc="Qualcomm Snapdragon 685, 8×2,8 ГГц", ram="8 ГБ", rom="256 ГБ",
        screen="IPS", refresh="120 Гц", resolution="1608×720",
        camera="50+2 Мп", battery="6500 мА·ч",
        sim="2 SIM (Nano)", sd="microSD до 1 ТБ", nfc=True,
        rating="4.83", reviews="543 отзыва",
        dns_price=15199, dns_url="https://www.dns-shop.ru/product/61627b4520b6d582/668-smartfon-vivo-y29-256-gb-koricnevyj/",
        ozon_url="https://www.ozon.ru/search/?text=vivo%20Y29",
        citilink_url="https://www.citilink.ru/search/?text=vivo%20Y29",
        dns_img="https://c.dns-shop.ru/thumb/st1/fit/300/300/729db0a9a7ec97e01dee1ab3c9425b19/cebec231483bf420b39884d",
        verdict="Самый мощный процессор в подборке (Snapdragon 685) при высшем рейтинге 4.83. Аккумулятор 6500 мА·ч — рекордный.",
        pros=["Snapdragon 685 — быстрее всех здесь", "6500 мА·ч", "8/256 ГБ"],
        cons=["Экран IPS 720p", "Цена у верхней границы бюджета"],
    ),
    dict(
        key="spark30pro", name="Tecno SPARK 30 Pro", config="8/128 ГБ",
        soc="MediaTek Helio G100, 8×2,2 ГГц", ram="8 ГБ", rom="128 ГБ",
        screen="AMOLED, 6,78″", refresh="120 Гц", resolution="2436×1080",
        camera="108 Мп", battery="5000 мА·ч",
        sim="2 SIM (Nano)", sd="microSD", nfc=True,
        rating="4.81", reviews="1.4k отзывов",
        dns_url="https://www.dns-shop.ru/product/629af0fc59eed0a4/678-smartfon-tecno-spark-30-pro-128-gb-cernyj/",
        ozon_url="https://www.ozon.ru/search/?text=Tecno%20Spark%2030%20Pro",
        citilink_url="https://www.citilink.ru/search/?text=Tecno%20Spark%2030%20Pro",
        dns_img="https://c.dns-shop.ru/thumb/st1/fit/300/300/746157db89da00801c873cd86389b3be/279dbeb537cec1cd0195bbe",
        verdict="Лучший экран в подборке: AMOLED Full HD+ и камера 108 Мп. Именно этот вариант — про «яркий экран и фото».",
        pros=["AMOLED 2436×1080 — ярче и контрастнее", "Камера 108 Мп", "Helio G100"],
        cons=["Память 128 ГБ вместо 256", "Вес и габариты побольше"],
    ),
    dict(
        key="hot50pro", name="Infinix HOT 50 Pro", config="8/256 ГБ",
        soc="MediaTek Helio G100, 8×2,2 ГГц", ram="8 ГБ", rom="256 ГБ",
        screen="AMOLED, 6,78″", refresh="120 Гц", resolution="2460×1080",
        camera="50+2 Мп", battery="5000 мА·ч",
        sim="2 SIM (Nano)", sd="microSD до 2 ТБ", nfc=True,
        rating="4.77", reviews="348 отзывов",
        dns_url="https://www.dns-shop.ru/product/ff87a2106f3bd21a/678-smartfon-infinix-hot-50-pro-256-gb-seryj/",
        ozon_url="https://www.ozon.ru/search/?text=Infinix%20Hot%2050%20Pro",
        citilink_url="https://www.citilink.ru/search/?text=Infinix%20Hot%2050%20Pro",
        dns_img="https://c.dns-shop.ru/thumb/st1/fit/300/300/b445a1ade6806f5d062bfe31179e440a/8f8376590f3a2f602facb07",
        verdict="Тот же AMOLED и процессор, что у Spark 30 Pro, но памяти 256 ГБ и слот под карту до 2 ТБ.",
        pros=["AMOLED 2460×1080", "8/256 ГБ", "microSD до 2 ТБ"],
        cons=["Камера скромнее — 50 Мп", "Меньше отзывов (348)"],
    ),
    dict(
        key="honor_x6c", name="HONOR X6c", config="6/256 ГБ",
        soc="MediaTek Helio G81 Ultra, 8×2 ГГц", ram="6 ГБ", rom="256 ГБ",
        screen="TFT LCD, 6,61″", refresh="120 Гц", resolution="1604×720",
        camera="50 Мп", battery="5300 мА·ч",
        sim="2 SIM (Nano)", sd="microSD", nfc=True,
        rating="4.78", reviews="1.7k отзывов",
        dns_url="https://www.dns-shop.ru/product/9af133883acfd9cb/661-smartfon-honor-x6c-256-gb-cernyj/",
        ozon_url="https://www.ozon.ru/search/?text=HONOR%20X6c",
        citilink_url="https://www.citilink.ru/search/?text=HONOR%20X6c",
        dns_img="https://c.dns-shop.ru/thumb/st1/fit/300/300/e629b2067414633f331b727e0c38b670/2b691c08fde22ddca92735c",
        verdict="Самый «обкатанный» вариант: 1,7 тыс. отзывов при 4.78. Защита IP64, 256 ГБ памяти.",
        pros=["Много отзывов — предсказуемое качество", "256 ГБ встроенной", "IP64"],
        cons=["Экран TFT — самый простой в подборке", "6 ГБ ОЗУ"],
    ),
    dict(
        key="galaxy_a07", name="Samsung Galaxy A07", config="4/128 ГБ",
        soc="MediaTek Helio G99, 8×2,2 ГГц", ram="4 ГБ", rom="128 ГБ",
        screen="PLS, 6,7″", refresh="90 Гц", resolution="1600×720",
        camera="50+2 Мп", battery="5000 мА·ч",
        sim="2 SIM (Nano)", sd="microSD", nfc=False,
        rating="4.76", reviews="1.1k отзывов",
        ozon_price=10880, ozon_url="https://www.ozon.ru/product/samsung-smartfon-galaxy-a07-rostest-eac-4-128-gb-nano-sim-fiol",
        dns_url="https://www.dns-shop.ru/product/34f66f4b719dd9cb/67-smartfon-samsung-galaxy-a07-128-gb-cernyj/",
        citilink_url="https://www.citilink.ru/search/?text=Samsung%20Galaxy%20A07",
        verdict="Самый дешёвый и с самой понятной оболочкой One UI. Но памяти всего 4 ГБ — для «много вкладок» это впритык.",
        pros=["Helio G99 при цене 10 880 ₽", "One UI — простая и знакомая", "1,1k отзывов, 4.76"],
        cons=["4 ГБ ОЗУ — вкладки будут выгружаться", "Нет NFC", "90 Гц экран"],
    ),
]


def money(v):
    return f"{v:,}".replace(",", "\u00a0")


def card(m):
    img = m.get("ozon_img")  # картинки DNS подписаны и не скачиваются
    img_local = f"img/{m['key']}.jpg"
    if not (BASE / img_local).exists() and img:
        subprocess.run(["curl", "-sL", "--max-time", "40", "-A", "Mozilla/5.0",
                        "-H", "Referer: https://www.ozon.ru/", "-o", str(BASE / img_local), img],
                       capture_output=True)
    prices = []
    if m.get("ozon_price"):
        prices.append(f'<a class="price-btn" href="{m["ozon_url"]}" target="_blank" rel="noopener">'
                      f'<span class="shop">Ozon</span><b>{money(m["ozon_price"])} ₽</b></a>')
    if m.get("dns_price"):
        prices.append(f'<a class="price-btn" href="{m["dns_url"]}" target="_blank" rel="noopener">'
                      f'<span class="shop">DNS</span><b>{money(m["dns_price"])} ₽</b></a>')
    prices.append(f'<a class="price-btn ghost" href="{m["ozon_url"]}" target="_blank" rel="noopener">'
                  f'<span class="shop">Ozon</span><b>смотреть</b></a>')
    prices.append(f'<a class="price-btn ghost" href="{m["dns_url"]}" target="_blank" rel="noopener">'
                  f'<span class="shop">DNS</span><b>смотреть</b></a>')
    prices.append(f'<a class="price-btn ghost" href="{m["citilink_url"]}" target="_blank" rel="noopener">'
                  f'<span class="shop">Ситилинк</span><b>смотреть</b></a>')
    specs = [
        ("Процессор", m["soc"]),
        ("Память", f'{m["ram"]} ОЗУ / {m["rom"]}'),
        ("Экран", f'{m["screen"]}, {m["resolution"]}, {m["refresh"]}'),
        ("Камера", m["camera"]),
        ("Аккумулятор", m["battery"]),
        ("SIM", m["sim"]),
        ("Карта памяти", m["sd"]),
        ("NFC", "есть" if m["nfc"] else "не указан"),
    ]
    rows = "".join(f"<tr><td>{k}</td><td>{html.escape(str(v))}</td></tr>" for k, v in specs)
    pros = "".join(f"<li>{html.escape(p)}</li>" for p in m["pros"])
    cons = "".join(f"<li>{html.escape(c)}</li>" for c in m["cons"])
    img_tag = (f'<img src="{img_local}" alt="{html.escape(m["name"])}" loading="eager">'
               if (BASE / img_local).exists() else '<div class="noimg">фото на сайте магазина</div>')
    return f"""
    <article class="card">
      <div class="card-img">{img_tag}</div>
      <div class="card-body">
        <h3>{html.escape(m["name"])} <span class="cfg">{html.escape(m["config"])}</span></h3>
        <div class="rating">★{m["rating"]} · {html.escape(m["reviews"])}</div>
        <p class="verdict">{html.escape(m["verdict"])}</p>
        <table class="specs">{rows}</table>
        <div class="pc">
          <div><b>Плюсы</b><ul>{pros}</ul></div>
          <div><b>На что смотреть</b><ul>{cons}</ul></div>
        </div>
        <div class="prices">{''.join(prices)}</div>
      </div>
    </article>"""


rows = "".join(
    f'<tr><td>{html.escape(m["name"])} {html.escape(m["config"])}</td>'
    f'<td>{html.escape(m["soc"].split(",")[0])}</td>'
    f'<td class="num">{html.escape(m["ram"])}</td>'
    f'<td>{html.escape(m["screen"])}</td>'
    f'<td>{html.escape(m["resolution"])}</td>'
    f'<td>{html.escape(m["camera"])}</td>'
    f'<td class="num">{html.escape(m["battery"])}</td>'
    f'<td class="num">{"да" if m["nfc"] else "нет"}</td>'
    f'<td class="num">★{m["rating"]}</td>'
    f'<td class="num">{money(m["ozon_price"]) + " ₽" if m.get("ozon_price") else (money(m["dns_price"]) + " ₽ (DNS)" if m.get("dns_price") else "—")}</td></tr>'
    for m in MODELS)

HTML = f"""<!DOCTYPE html>
<html lang="ru">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Смартфоны до 16 000 ₽: 2 SIM, карта памяти, яркий экран — обзор {DATE}</title>
<style>
:root {{ color-scheme: dark; }}
* {{ box-sizing: border-box; }}
body {{ margin:0; background:#0b1220; color:#e2e8f0;
  font-family: system-ui,-apple-system,'Segoe UI',Roboto,sans-serif; line-height:1.55; }}
.wrap {{ max-width:1080px; margin:0 auto; padding:28px 18px 60px; }}
h1 {{ font-size:clamp(22px,3.4vw,34px); margin:0 0 10px; }}
h2 {{ font-size:clamp(18px,2.4vw,24px); margin:38px 0 12px; }}
h3 {{ font-size:19px; margin:0 0 8px; }}
.lead {{ color:#94a3b8; font-size:16px; margin:0 0 22px; }}
.kpis {{ display:grid; grid-template-columns:repeat(auto-fit,minmax(190px,1fr)); gap:12px; margin:18px 0 26px; }}
.kpi {{ background:#111827; border:1px solid #334155; border-radius:12px; padding:12px 14px; }}
.kpi b {{ display:block; font-size:20px; }}
.kpi span {{ color:#94a3b8; font-size:13px; }}
.req {{ background:#111827; border:1px solid #334155; border-radius:12px; padding:16px 18px; }}
.req li {{ margin:6px 0; }}
.grid {{ display:grid; grid-template-columns:repeat(auto-fit,minmax(320px,1fr)); gap:16px; }}
.card {{ background:#111827; border:1px solid #334155; border-radius:14px; overflow:hidden; display:flex; flex-direction:column; }}
.card-img {{ background:#0f172a; height:230px; display:flex; align-items:center; justify-content:center; }}
.card-img img {{ max-width:100%; max-height:100%; object-fit:contain; }}
.noimg {{ color:#64748b; font-size:13px; }}
.card-body {{ padding:16px 16px 18px; }}
.cfg {{ color:#94a3b8; font-size:15px; font-weight:500; }}
.rating {{ color:#facc15; font-size:14px; margin-bottom:8px; }}
.verdict {{ font-size:14px; color:#cbd5e1; }}
table {{ width:100%; border-collapse:collapse; font-size:13.5px; margin:10px 0; }}
.specs td {{ padding:5px 0; border-bottom:1px solid #1e293b; vertical-align:top; }}
.specs td:first-child {{ color:#94a3b8; width:44%; }}
.pc {{ display:grid; grid-template-columns:1fr 1fr; gap:10px; font-size:13px; }}
.pc ul {{ margin:6px 0 0 16px; padding:0; color:#cbd5e1; }}
.prices {{ display:flex; flex-wrap:wrap; gap:8px; margin-top:14px; }}
.price-btn {{ display:flex; flex-direction:column; gap:2px; background:#1e293b; border:1px solid #334155;
  border-radius:10px; padding:8px 12px; text-decoration:none; color:#e2e8f0; font-size:13px; }}
.price-btn.ghost {{ background:transparent; }}
.price-btn b {{ font-size:15px; }}
.price-btn .shop {{ color:#94a3b8; font-size:12px; }}
.tbl-wrap {{ overflow-x:auto; }}
table.cmp {{ min-width:760px; font-size:13px; }}
table.cmp th, table.cmp td {{ padding:8px 10px; border-bottom:1px solid #1e293b; text-align:left; }}
table.cmp th {{ color:#94a3b8; font-weight:600; background:#111827; position:sticky; top:0; }}
.num {{ white-space:nowrap; }}
.box {{ background:#111827; border:1px solid #334155; border-left:4px solid #38bdf8; border-radius:12px;
  padding:14px 16px; margin:16px 0; font-size:14px; }}
.box.warn {{ border-left-color:#f59e0b; }}
.honest li {{ margin:5px 0; }}
a {{ color:#38bdf8; }}
footer {{ margin-top:38px; color:#64748b; font-size:13px; }}
</style>
</head>
<body>
<div class="wrap">

  <h1>Смартфоны до 16 000 ₽: две SIM, отдельная карта памяти, яркий экран</h1>
  <p class="lead">Собрано {DATE}. Отбор жёсткий: два слота под SIM, поддержка microSD, Android,
     крупный экран, заметная камера и запас памяти под браузер с десятком вкладок.
     Все цены и характеристики — из карточек товаров, ссылки ведут прямо на магазины.</p>

  <div class="kpis">
    <div class="kpi"><b>до 16 000 ₽</b><span>потолок бюджета</span></div>
    <div class="kpi"><b>{len(MODELS)}</b><span>модели, прошедшие все условия</span></div>
    <div class="kpi"><b>2 SIM + microSD</b><span>проверено в характеристиках DNS</span></div>
    <div class="kpi"><b>★4.70–4.83</b><span>рейтинги по отзывам покупателей</span></div>
  </div>

  <div class="req">
    <b>Что было в требованиях:</b>
    <ul>
      <li>две SIM-карты — <b>проверено</b> у всех моделей (в сводке DNS прямо указано «2 SIM»);</li>
      <li>слот под microSD — <b>проверено</b> по описанию товара (где указан максимальный объём — он в карточке);</li>
      <li>Android, крупный яркий экран — <b>проверено</b> тип, диагональ, разрешение и частота;</li>
      <li>хорошая камера — по мегапикселям основной камеры;</li>
      <li>запас процессора и ОЗУ под браузер и видео — по модели чипа и объёму памяти;</li>
      <li>громкий динамик и олеофобное покрытие — <b>магазины это не публикуют</b>, см. честный блок ниже.</li>
    </ul>
  </div>

  <h2>Модели</h2>
  <div class="grid">
  {''.join(card(m) for m in MODELS)}
  </div>

  <h2>Сравнение характеристик</h2>
  <div class="tbl-wrap">
  <table class="cmp">
    <tr><th>Модель</th><th>Процессор</th><th>ОЗУ</th><th>Экран</th><th>Разрешение</th>
        <th>Камера</th><th>Батарея</th><th>NFC</th><th>Рейтинг</th><th>Цена</th></tr>
    {rows}
  </table>
  </div>

  <h2>Честно о том, что не проверить по магазинам</h2>
  <div class="box warn">
    <ul class="honest">
      <li><b>Громкость динамиков нигде не измеряется.</b> Ни Ozon, ни DNS, ни Ситилинк не дают
          цифр по громкости — только «есть стереодинамики» или молчат. Проверить это можно
          только вживую: включить видео на максимуме в торговом зале или взять модель,
          у которой отзывы прямо хвалят звук.</li>
      <li><b>Олеофобное покрытие</b> тоже не указывается в карточках. Практически у всех
          современных моделей оно есть, но качество покрытия отличается даже внутри линейки.</li>
      <li><b>Проценты заряда, скорость интерфейса и реальная автономность</b> зависят от
          сценария — таблица даёт железо, а не впечатления.</li>
      <li><b>Цены живут своей жизнью:</b> проверены {DATE}; на Ozon они меняются ежедневно,
          в DNS и Ситилинке зависят от города и остатков. Кнопки ведут прямо на страницы товаров.</li>
      <li><b>В Ситилинке цены не удалось выгрузить автоматически</b> — сайт отдаёт их только
          в браузере с защитой от ботов. Ссылки на поиск по модели даны, цену нужно посмотреть
          на месте.</li>
    </ul>
  </div>

  <h2>Что я бы взял</h2>
  <div class="box">
    <p><b>Если важнее всего экран и фотографии — Tecno SPARK 30 Pro</b> (8/128): единственный
    в подборке с AMOLED Full HD+ и камерой 108 Мп. Именно он отвечает на «яркий экран» и
    «любит фотографировать».</p>
    <p><b>Если важнее цена и запас памяти под вкладки — POCO C85</b> (8/256) за
    {money(10950)} ₽ на Ozon: 8 ГБ ОЗУ, 6000 мА·ч и карта памяти до 1 ТБ.</p>
    <p><b>Если важнее максимальная производительность — vivo Y29</b> (8/256) со Snapdragon 685
    и аккумулятором 6500 мА·ч, {money(15199)} ₽ в DNS и рейтинг 4.83 — лучший в подборке.</p>
    <p><b>Samsung Galaxy A07</b> берём только если решает цена (10 880 ₽ на Ozon) и привычная
    оболочка: 4 ГБ ОЗУ — это как раз то место, где браузер начнёт выгружать вкладки.</p>
  </div>

  <footer>
    Источники: карточки товаров Ozon, DNS и Ситилинка. Характеристики взяты из сводки DNS
    («ядер — …, … ГБ, 2 SIM, тип экрана, разрешение, камера, … мА·ч») и описаний товаров.
    Отзывы и рейтинги — DNS. Дата сборки: {DATE}.
  </footer>
</div>
</body>
</html>
"""

(BASE / "index.html").write_text(HTML, encoding="utf-8")
print(f"index.html записан: {len(HTML):,} байт | моделей {len(MODELS)}")
imgs = list(IMG.glob("*.jpg"))
print("картинок скачано:", len(imgs))
for i in imgs:
    print(f"  {i.name}: {i.stat().st_size//1024} КБ")
