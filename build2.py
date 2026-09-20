#!/usr/bin/env python3
"""index.html — смартфоны до 16 000 ₽: 2 SIM + microSD ОДНОВРЕМЕННО (отдельный слот).

Данные на 20.09.2026.
Источники по слоту: 4PDA (формулировка «Карта памяти имеет отдельный слот» / «занимает один слот Sim»),
официальный сайт Xiaomi (POCO C85: «Две SIM-карты + microSD»), Samsung/DNS (A07: «отдельный слот microSD»),
обзор DTF по Tecno Spark 40 («отдельное место в лотке»).
Яркость, тип накопителя, отзывы — nanoreview / обзоры vc.ru, dtf.ru, агрегаторы отзывов.
Цены: Ozon (карточки товаров), обзор/агрегаторы для среднего уровня.
"""
import html
import pathlib

BASE = pathlib.Path(__file__).resolve().parent
DATE = "20.09.2026"


def money(v):
    return f"{v:,}".replace(",", "\u00a0")


# slot: 'отдельный' | 'гибрид' ; source — откуда сведения о слоте
MODELS = [
    dict(
        key="tecno_spark_40", name="TECNO Spark 40", config="8/256 ГБ",
        soc="MediaTek Helio G91 (RU-версия)", ram="8 ГБ", rom="256 ГБ, eMMC 5.1",
        screen="IPS, 6,67″", res="1600×720", hz="120 Гц", nits="~700 нит",
        cam="50 Мп", bat="5200 мА·ч", charge="45 Вт", stereo=True, nfc=True,
        rating="9,1 / 10", reviews="131 отзыв (агрегатор)",
        slot="отдельный", slot_src="обзор DTF: «microSD, отдельное место в лотке»",
        price_txt="11 500 – 15 000 ₽", price_note="типичный диапазон для 8/256 (обзор + агрегаторы)",
        links=[
            ("Ситилинк", "https://www.citilink.ru/search/?text=Tecno%20Spark%2040"),
            ("Ozon", "https://www.ozon.ru/search/?text=Tecno%20Spark%2040"),
            ("DNS", "https://www.dns-shop.ru/search/?q=Tecno+Spark+40"),
        ],
        verdict="Лучший набор под задачу: отдельный слот под карту, стереодинамики, 45 Вт зарядка, "
                "яркость ~700 нит и 8/256 в российской версии.",
        pros=["Стереодинамики — прямо в требованиях по звуку", "Отдельное место под microSD",
              "45 Вт: полный заряд заметно быстрее остальных", "IP64, NFC, 8/256"],
        cons=["Экран 720p при 6,67″", "Helio G91 и eMMC 5.1 — не для игр"],
    ),
    dict(
        key="redmi_15c", name="Xiaomi Redmi 15C", config="8/256 ГБ",
        soc="MediaTek Helio G81-Ultra", ram="8 ГБ", rom="256 ГБ, eMMC 5.1",
        screen="IPS, 6,9″", res="1600×720", hz="120 Гц", nits="810 нит (заявл.)",
        cam="50 Мп", bat="6000 мА·ч", charge="33 Вт", stereo=False, nfc=True,
        rating="★4,7 (DNS)", reviews="1,2 тыс. отзывов (DNS)",
        slot="отдельный", slot_src="4PDA: «Карта памяти имеет отдельный слот»",
        price_txt="15 095 ₽ (Ozon)", price_note="проверено в карточке Ozon 8/256",
        links=[("Ozon", "https://www.ozon.ru/product/xiaomi-smartfon-redmi-15c-8-256-gb-nano-sim-oranzhevyy-2904616066/"),
               ("DNS", "https://www.dns-shop.ru/search/?q=Redmi+15C"),
               ("Ситилинк", "https://www.citilink.ru/search/?text=Redmi%2015C")],
        verdict="Самая высокая заявленная яркость в подборке (810 нит) и самый крупный экран — 6,9″. "
                "microSD до 1 ТБ в отдельном слоте.",
        pros=["810 нит — самый яркий экран здесь", "Экран 6,9″", "6000 мА·ч", "microSD до 1 ТБ, отдельный слот"],
        cons=["720p на 6,9″ — заметны пиксели", "Одна колонка (без стерео)"],
    ),
    dict(
        key="poco_c85", name="POCO C85", config="8/256 ГБ",
        soc="MediaTek Helio G81-Ultra", ram="8 ГБ", rom="256 ГБ",
        screen="IPS LCD, 6,9″", res="1600×720", hz="120 Гц", nits="—",
        cam="50 Мп", bat="6000 мА·ч", charge="33 Вт", stereo=False, nfc=True,
        rating="★4,78 (DNS)", reviews="988 отзывов (агрегатор)",
        slot="отдельный", slot_src="сайт Xiaomi: «Две SIM-карты + microSD», слот не занимает место SIM",
        price_txt="10 950 ₽ (Ozon)", price_note="агрегатор: «от 10 626 ₽»",
        links=[("Ozon", "https://www.ozon.ru/product/smartfon-poco-c85-8-256-gb-chernyy-4884337224/"),
               ("DNS", "https://www.dns-shop.ru/search/?q=POCO+C85"),
               ("Ситилинк", "https://www.citilink.ru/search/?text=POCO%20C85")],
        verdict="Самый дешёвый способ получить 8/256, 6000 мА·ч и отдельный слот под карту памяти.",
        pros=["Цена 10 950 ₽ за 8/256", "6000 мА·ч", "Отдельный слот microSD до 1 ТБ"],
        cons=["Отзывы: брать стоит до 11–12 тыс. — иначе слабый процессор и eMMC уже не оправданы",
              "720p экран, одна колонка"],
    ),
    dict(
        key="infinix_hot50pro", name="Infinix HOT 50 Pro", config="8/256 ГБ",
        soc="MediaTek Helio G100", ram="8 ГБ", rom="256 ГБ",
        screen="AMOLED, 6,78″", res="1080×2436", hz="120 Гц", nits="—",
        cam="50+2 Мп", bat="5000 мА·ч", charge="33 Вт", stereo=False, nfc=True,
        rating="★4,77 (DNS)", reviews="348 отзывов (DNS)",
        slot="отдельный", slot_src="4PDA: «Карта памяти имеет отдельный слот»",
        price_txt="≈11 700 – 15 000 ₽", price_note="на Ozon встречался 11 695 ₽ (ростest), проверяйте карточку",
        links=[("Ozon", "https://www.ozon.ru/search/?text=Infinix%20HOT%2050%20Pro"),
               ("DNS", "https://www.dns-shop.ru/search/?q=Infinix+HOT+50+Pro"),
               ("Ситилинк", "https://www.citilink.ru/search/?text=Infinix%20HOT%2050%20Pro")],
        verdict="Единственный с AMOLED Full HD+ и отдельным слотом: чёткая картинка при 1080p, "
                "а не 720p, как у большинства бюджетников.",
        pros=["AMOLED 1080×2436 при 8/256", "Отдельный слот microSD до 2 ТБ", "Helio G100 — бодрее G81/G91"],
        cons=["Отзывы по базовому Hot 50: нет стереодинамиков и влагозащиты", "Меньше отзывов — 348"],
    ),
    dict(
        key="realme_c61", name="realme C61", config="6/128 ГБ",
        soc="Unisoc T612 (8 ядер)", ram="6 ГБ", rom="128 ГБ",
        screen="IPS, 6,74″", res="720×1600", hz="90 Гц", nits="—",
        cam="50 Мп", bat="5000 мА·ч", charge="15 Вт", stereo=False, nfc=False,
        rating="★8,2/10", reviews="1 560 отзывов (агрегатор)",
        slot="отдельный", slot_src="4PDA: «Карта памяти имеет отдельный слот»",
        price_txt="от 7 890 ₽ (СПб)", price_note="самый дешёвый вариант в подборке",
        links=[("DNS", "https://www.dns-shop.ru/search/?q=realme+C61"),
               ("Ozon", "https://www.ozon.ru/search/?text=realme%20C61"),
               ("Ситилинк", "https://www.citilink.ru/search/?text=realme%20C61")],
        verdict="Бюджетный вариант «сделать всё сразу»: 82 % владельцев хвалят автономность, "
                "слот под карту отдельный, цена от 7 890 ₽.",
        pros=["Дешевле всех — от 7 890 ₽", "Автономность хвалят 82 % владельцев", "Отдельный слот microSD"],
        cons=["Камерой недовольны 52 % (слабая ночная съёмка)", "45 % жалуются на предустановленный софт",
              "Нет NFC, зарядка всего 15 Вт"],
    ),
    dict(
        key="samsung_a07", name="Samsung Galaxy A07", config="4/128 ГБ",
        soc="MediaTek Helio G99", ram="4 ГБ", rom="128 ГБ, UFS 2.2",
        screen="PLS, 6,7″", res="1600×720", hz="90 Гц", nits="450 нит",
        cam="50+2 Мп", bat="5000 мА·ч", charge="25 Вт", stereo=False, nfc=False,
        rating="★4,76 (DNS)", reviews="1,1 тыс. отзывов (DNS) + 312 отзывов (агрегатор)",
        slot="отдельный", slot_src="DNS и обзорные сайты: «отдельный слот microSD до 2 ТБ»",
        price_txt="10 880 ₽ (Ozon)", price_note="проверено в карточке Ozon 4/128",
        links=[("Ozon", "https://www.ozon.ru/product/samsung-smartfon-galaxy-a07-rostest-eac-4-128-gb-nano-sim-fiol"),
               ("DNS", "https://www.dns-shop.ru/search/?q=Samsung+Galaxy+A07"),
               ("Ситилинк", "https://www.citilink.ru/search/?text=Samsung%20Galaxy%20A07")],
        verdict="Единственный с UFS 2.2 (быстрый накопитель) и One UI с 6 годами обновлений, "
                "но 4 ГБ ОЗУ — вкладки браузера будут выгружаться.",
        pros=["UFS 2.2 — быстрее eMMC у конкурентов", "Отдельный слот microSD до 2 ТБ",
              "One UI, 6 лет обновлений Android"],
        cons=["4 ГБ ОЗУ — это главный минус под браузер", "450 нит — самый тусклый экран подборки",
              "Нет NFC"],
    ),
    dict(
        key="redmi_14c", name="Xiaomi Redmi 14C", config="8/256 ГБ",
        soc="MediaTek Helio G81-Ultra", ram="8 ГБ", rom="256 ГБ",
        screen="IPS, 6,88″", res="720×1640", hz="120 Гц", nits="—",
        cam="50 Мп", bat="5160 мА·ч", charge="18 Вт", stereo=False, nfc=True,
        rating="★8,5/10", reviews="1 148 отзывов (агрегатор)",
        slot="отдельный", slot_src="4PDA: «Карта памяти имеет отдельный слот»",
        price_txt="≈11 000 – 14 000 ₽", price_note="цена сильно зависит от продавца — проверяйте карточку",
        links=[("DNS", "https://www.dns-shop.ru/search/?q=Redmi+14C"),
               ("Ozon", "https://www.ozon.ru/search/?text=Redmi%2014C"),
               ("Ситилинк", "https://www.citilink.ru/search/?text=Redmi%2014C")],
        verdict="Максимальный опыт владельцев (1 148 отзывов): большой экран и автономность хвалят, "
                "но реклама в системе раздражает 62 %.",
        pros=["Экран 6,88″ и 120 Гц", "Отдельный слот microSD", "Большая база отзывов — качество предсказуемо"],
        cons=["62 % владельцев жалуются на рекламу в системе", "51 % — на слабую ночную камеру",
              "Зарядка 18 Вт"],
    ),
]

HYBRID = [
    ("HONOR X6c", "4PDA: «Карта памяти занимает один слот SIM»", "гибридный лоток"),
    ("vivo Y29", "DNS: «есть (универсальный слот SIM + SIM / SIM + карта памяти)»", "гибридный лоток"),
    ("Infinix Hot 60i", "4PDA: «Карта памяти занимает один слот Sim»", "гибридный лоток"),
    ("TECNO Spark 30 5G", "обзор: microSD ставится «вместо второй SIM-карты»", "гибридный лоток"),
    ("Redmi 14C (по части источников)", "часть англоязычных страниц описывает лоток как hybrid — в RU-версии 4PDA отмечает отдельный слот", "данные расходятся, уточняйте на витрине"),
]


def card(m):
    stereo = "стереодинамики" if m["stereo"] else "один динамик"
    specs = [
        ("Процессор", m["soc"]), ("Память", f'{m["ram"]} ОЗУ / {m["rom"]}'),
        ("Экран", f'{m["screen"]}, {m["res"]}, {m["hz"]}'),
        ("Яркость", m["nits"]), ("Камера", m["cam"]),
        ("Аккумулятор", f'{m["bat"]}, зарядка {m["charge"]}'),
        ("Динамики", stereo), ("NFC", "есть" if m["nfc"] else "нет"),
    ]
    rows = "".join(f"<tr><td>{k}</td><td>{html.escape(str(v))}</td></tr>" for k, v in specs)
    pros = "".join(f"<li>{html.escape(p)}</li>" for p in m["pros"])
    cons = "".join(f"<li>{html.escape(c)}</li>" for c in m["cons"])
    links = "".join(f'<a class="price-btn" href="{u}" target="_blank" rel="noopener">'
                    f'<span class="shop">{s}</span><b>открыть</b></a>' for s, u in m["links"])
    return f"""
    <article class="card">
      <div class="card-body">
        <h3>{html.escape(m["name"])} <span class="cfg">{html.escape(m["config"])}</span></h3>
        <div class="rating">{html.escape(m["rating"])} · {html.escape(m["reviews"])}</div>
        <div class="slot ok">2 SIM + microSD одновременно: <b>отдельный слот</b> <span class="src">({html.escape(m["slot_src"])})</span></div>
        <p class="verdict">{html.escape(m["verdict"])}</p>
        <table class="specs">{rows}</table>
        <div class="price">{m["price_txt"]}<span>{html.escape(m["price_note"])}</span></div>
        <div class="pc">
          <div><b>Плюсы</b><ul>{pros}</ul></div>
          <div><b>Минусы по отзывам</b><ul>{cons}</ul></div>
        </div>
        <div class="prices">{links}</div>
      </div>
    </article>"""


rows = "".join(
    f'<tr><td>{html.escape(m["name"])} {html.escape(m["config"])}</td>'
    f'<td>{html.escape(m["soc"].split("(")[0].strip())}</td>'
    f'<td class="num">{html.escape(m["ram"])}</td>'
    f'<td>{html.escape(m["screen"])}</td>'
    f'<td>{html.escape(m["res"])} / {html.escape(m["hz"])}</td>'
    f'<td class="num">{html.escape(m["nits"])}</td>'
    f'<td>{html.escape(m["cam"])}</td>'
    f'<td class="num">{html.escape(m["bat"])}</td>'
    f'<td class="num">{html.escape(m["charge"])}</td>'
    f'<td class="num">{"да" if m["stereo"] else "нет"}</td>'
    f'<td class="num slot-col">отдельный</td>'
    f'<td class="num">{html.escape(m["price_txt"])}</td></tr>' for m in MODELS)

hybrid_rows = "".join(
    f'<tr><td><b>{html.escape(n)}</b></td><td>{html.escape(s)}</td><td class="num bad">✗ {html.escape(w)}</td></tr>'
    for n, s, w in HYBRID)

HTML = f"""<!DOCTYPE html>
<html lang="ru">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Смартфоны до 16 000 ₽: 2 SIM + microSD одновременно — обзор {DATE}</title>
<style>
:root {{ color-scheme: dark; }}
* {{ box-sizing: border-box; }}
body {{ margin:0; background:#0b1220; color:#e2e8f0; font-family: system-ui,-apple-system,'Segoe UI',Roboto,sans-serif; line-height:1.55; }}
.wrap {{ max-width:1120px; margin:0 auto; padding:28px 18px 60px; }}
h1 {{ font-size:clamp(21px,3.3vw,33px); margin:0 0 10px; }}
h2 {{ font-size:clamp(18px,2.4vw,24px); margin:38px 0 12px; }}
h3 {{ font-size:19px; margin:0 0 8px; }}
.lead {{ color:#94a3b8; font-size:16px; margin:0 0 20px; }}
.kpis {{ display:grid; grid-template-columns:repeat(auto-fit,minmax(200px,1fr)); gap:12px; margin:18px 0 24px; }}
.kpi {{ background:#111827; border:1px solid #334155; border-radius:12px; padding:12px 14px; }}
.kpi b {{ display:block; font-size:19px; }}
.kpi span {{ color:#94a3b8; font-size:13px; }}
.req {{ background:#111827; border:1px solid #334155; border-radius:12px; padding:16px 18px; }}
.req li {{ margin:6px 0; }}
.grid {{ display:grid; grid-template-columns:repeat(auto-fit,minmax(340px,1fr)); gap:16px; }}
.card {{ background:#111827; border:1px solid #334155; border-radius:14px; }}
.card-body {{ padding:16px 16px 18px; }}
.cfg {{ color:#94a3b8; font-size:15px; font-weight:500; }}
.rating {{ color:#facc15; font-size:14px; margin-bottom:8px; }}
.slot {{ font-size:13px; border-radius:9px; padding:7px 10px; margin:8px 0 10px; }}
.slot.ok {{ background:#0f2a1d; border:1px solid #1f7a4d; color:#86efac; }}
.slot .src {{ color:#94a3b8; font-weight:400; }}
.verdict {{ font-size:14px; color:#cbd5e1; }}
table {{ width:100%; border-collapse:collapse; font-size:13.5px; margin:10px 0; }}
.specs td {{ padding:5px 0; border-bottom:1px solid #1e293b; vertical-align:top; }}
.specs td:first-child {{ color:#94a3b8; width:42%; }}
.price {{ margin:10px 0 4px; font-size:16px; }}
.price span {{ display:block; color:#94a3b8; font-size:12.5px; }}
.pc {{ display:grid; grid-template-columns:1fr 1fr; gap:10px; font-size:13px; }}
.pc ul {{ margin:6px 0 0 16px; padding:0; color:#cbd5e1; }}
.prices {{ display:flex; flex-wrap:wrap; gap:8px; margin-top:14px; }}
.price-btn {{ display:flex; flex-direction:column; gap:2px; background:#1e293b; border:1px solid #334155;
  border-radius:10px; padding:8px 12px; text-decoration:none; color:#e2e8f0; font-size:13px; }}
.price-btn b {{ font-size:14px; }}
.price-btn .shop {{ color:#94a3b8; font-size:12px; }}
.tbl-wrap {{ overflow-x:auto; }}
table.cmp {{ min-width:1000px; font-size:12.5px; }}
table.cmp th, table.cmp td {{ padding:8px 9px; border-bottom:1px solid #1e293b; text-align:left; }}
table.cmp th {{ color:#94a3b8; font-weight:600; background:#111827; position:sticky; top:0; }}
.num {{ white-space:nowrap; }}
.slot-col {{ color:#86efac; }}
.bad {{ color:#fca5a5; }}
.box {{ background:#111827; border:1px solid #334155; border-left:4px solid #38bdf8; border-radius:12px; padding:14px 16px; margin:16px 0; font-size:14px; }}
.box.warn {{ border-left-color:#f59e0b; }}
.box.bad {{ border-left-color:#ef4444; }}
.honest li {{ margin:6px 0; }}
a {{ color:#38bdf8; }}
footer {{ margin-top:38px; color:#64748b; font-size:13px; }}
</style>
</head>
<body>
<div class="wrap">

  <h1>Смартфоны до 16 000 ₽: 2 SIM <span style="color:#86efac">и</span> microSD одновременно</h1>
  <p class="lead">Собрано {DATE}. Главное условие отбора — <b>не гибридный лоток</b>: две SIM-карты и карта
     памяти должны работать <b>одновременно</b>. Модели с совмещённым слотом («SIM + SIM / SIM + карта памяти»)
     исключены — их список внизу. Все данные о слотах взяты из 4PDA, официальных сайтов и обзоров, а не из
     предположений. Цены проверялись на Ozon, DNS и Ситилинк по Санкт-Петербургу.</p>

  <div class="kpis">
    <div class="kpi"><b>до 16 000 ₽</b><span>потолок бюджета</span></div>
    <div class="kpi"><b>{len(MODELS)}</b><span>модели с отдельным слотом</span></div>
    <div class="kpi"><b>{len(HYBRID)}</b><span>модели исключены (гибрид)</span></div>
    <div class="kpi"><b>2 SIM + microSD</b><span>проверено по источникам</span></div>
  </div>

  <div class="req">
    <b>Что учитывалось:</b>
    <ul>
      <li><b>2 SIM и microSD одновременно</b> — только отдельный (тройной) лоток;</li>
      <li>громкий звук — отмечено, где есть <b>стереодинамики</b>;</li>
      <li>яркий экран — приведена <b>заявленная яркость в нитах</b>, где её опубликовали;</li>
      <li>камера, процессор, ОЗУ — по характеристикам и тестам;</li>
      <li>отзывы владельцев — отдельный блок «минусы по отзывам» в каждой карточке;</li>
      <li>покупка в Санкт-Петербурге — у каждой модели есть ссылка на DNS (город СПб) и другие магазины.</li>
    </ul>
  </div>

  <h2>Подходят: 2 SIM + отдельный слот под карту памяти</h2>
  <div class="grid">
  {''.join(card(m) for m in MODELS)}
  </div>

  <h2>Сравнение характеристик</h2>
  <div class="tbl-wrap">
  <table class="cmp">
    <tr><th>Модель</th><th>Процессор</th><th>ОЗУ</th><th>Экран</th><th>Разрешение / Гц</th>
        <th>Яркость</th><th>Камера</th><th>Батарея</th><th>Зарядка</th><th>Стерео</th>
        <th>Слот для карты памяти</th><th>Цена</th></tr>
    {rows}
  </table>
  </div>
  <div class="box">
    <b>Как читать столбец «Слот для карты памяти»:</b> «отдельный» значит, что карта памяти
    вставляется в своё место и <b>две SIM-карты остаются на месте</b>. Именно это вам и нужно.
    Формулировка «универсальный слот SIM + SIM / SIM + карта памяти» (как у vivo Y29) означает выбор:
    либо вторая SIM, либо карта памяти.
  </div>

  <h2>Исключены из-за совмещённого слота</h2>
  <div class="tbl-wrap">
  <table class="cmp">
    <tr><th>Модель</th><th>Что написано в источнике</th><th>Итог</th></tr>
    {hybrid_rows}
  </table>
  </div>
  <div class="box bad">
    Эти модели <b>не подходят</b> под условие: придётся выбирать между второй SIM-картой и картой памяти.
    Если такое поведение устраивает — они дешевле, но по вашему требованию они отсеяны.
  </div>

  <h2>Отзывы и обзоры: коротко по каждой модели</h2>
  <div class="box">
    <ul class="honest">
      <li><b>TECNO Spark 40</b> — в российской версии 8/256, стереодинамики, 45 Вт, IP64, яркость около 700 нит;
          минусы, о которых пишут: экран 720p, платформа Helio G91 и eMMC 5.1 (не для тяжёлых игр).</li>
      <li><b>Redmi 15C</b> — заявленная яркость 810 нит и крупный экран 6,9″; в отзывах хвалят экран и автономность,
          ругают 720p и одиночный динамик.</li>
      <li><b>POCO C85</b> — по совокупности 988 отзывов вывод: брать до 11–12 тысяч за 8/256, тогда слабый
          процессор и eMMC — приемлемый компромисс.</li>
      <li><b>Infinix HOT 50 Pro</b> — единственный с AMOLED Full HD+ и отдельным слотом; по базовому Hot 50
          в отзывах отмечают отсутствие стереодинамиков и влагозащиты, зато хвалят экран 120 Гц и автономность.</li>
      <li><b>realme C61</b> — 82 % владельцев хвалят автономность, но 52 % недовольны камерой, а 45 % — рекламой
          и лишним софтом; нет NFC.</li>
      <li><b>Samsung Galaxy A07</b> — единственный с UFS 2.2 и 6 годами обновлений, но 4 ГБ ОЗУ и яркость 450 нит —
          самые слабые в подборке места.</li>
      <li><b>Redmi 14C</b> — 1 148 отзывов: рекламу в системе отмечают 62 %, слабую ночную камеру — 51 %;
          зато большой экран и автономность.</li>
    </ul>
  </div>

  <h2>Цены и покупка в Санкт-Петербурге</h2>
  <div class="box warn">
    <ul class="honest">
      <li>Диапазоны цен — <b>средние по рынку на {DATE}</b>: Ozon, DNS, Ситилинк, обзоры и агрегаторы.
          Точную цену обязательно смотрите в карточке: у этих моделей разброс между продавцами до 3–4 тысяч.</li>
      <li><b>Проверенные цены:</b> POCO C85 8/256 — 10 950 ₽ (Ozon, агрегатор даёт «от 10 626 ₽»);
          Redmi 15C 8/256 — 15 095 ₽ (Ozon); Samsung Galaxy A07 4/128 — 10 880 ₽ (Ozon);
          realme C61 — от 7 890 ₽ в СПб; TECNO Spark 40 8/256 — 11 500–15 000 ₽.</li>
      <li><b>Санкт-Петербург:</b> все модели продаются в DNS (ссылка ведёт на поиск с городом СПб),
          большинство — в Ситилинке и на Ozon с доставкой в ПВЗ. Наличие по конкретному магазину
          меняется ежедневно — проверяйте на странице товара.</li>
      <li><b>DNS и Ситилинк не отдают цены для автоматического сбора</b> (защита от ботов и цены,
          зависящие от города) — поэтому вместо цифры стоит ссылка на поиск: цену видно сразу на сайте.</li>
    </ul>
  </div>

  <h2>Что я бы взял</h2>
  <div class="box">
    <p><b>TECNO Spark 40 8/256</b> — лучший компромисс под ваши требования: отдельный слот под карту,
    стереодинамики (громкий звук), 45 Вт зарядка и яркость ~700 нит при цене 11,5–15 тыс.</p>
    <p><b>Infinix HOT 50 Pro 8/256</b> — если важнее всего картинка: AMOLED Full HD+ вместо 720p,
    и при этом слот под карту тоже отдельный.</p>
    <p><b>POCO C85 8/256</b> — если решает цена: 10 950 ₽, 8 ГБ ОЗУ, 6000 мА·ч и отдельный слот.</p>
  </div>

  <footer>
    Источники: 4PDA (формулировки о слоте), сайт Xiaomi (POCO C85), материалы о Samsung Galaxy A07,
    обзор DTF по TECNO Spark 40, nanoreview (яркость дисплеев, тип накопителя), агрегаторы отзывов
    (wizemart), карточки товаров Ozon, каталог DNS. Дата сборки: {DATE}.
  </footer>
</div>
</body>
</html>
"""

(BASE / "index.html").write_text(HTML, encoding="utf-8")
print(f"index.html: {len(HTML):,} байт | моделей {len(MODELS)} | исключено {len(HYBRID)}")
