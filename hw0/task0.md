# CAP theorem

## Task
Проанализировать следующие СУБД согласно теореме CAP:
1) DragonFly
2) ScyllaDB
3) ArendataDB

## Solution
### Теор справка
Напомним, что о чем сама теорема. CAP заключает в себе [три свойства](https://habr.com/ru/companies/otus/articles/754514/):
1) **Согласованность (Consistency)**: Согласованность – это фундаментальный принцип, который требует, чтобы все копии данных в системе имели одинаковую информацию в любой момент времени.
В контексте распределенных систем это означает, что независимо от того, какой узел системы обрабатывает запрос, результат будет всегда согласован с остальными частями системы.
Это обеспечивает предсказуемость и консистентность данных, что важно для корректного функционирования многих приложений, таких как финансовые транзакции или системы учета.

2) **Доступность (Availability)**: Доступность – это способность системы отвечать на запросы пользователей в любое время, даже при наличии сбоев или неполадок в системе.
Она позволяет поддерживать работоспособность приложений даже при ограниченной доступности ресурсов. Для многих приложений, таких как онлайн-магазины или социальные сети,
доступность является критически важной характеристикой, поскольку простоев и недоступности пользователи могут воспринимать как серьезное разочарование.

3) **Устойчивость к разделению (Partition Tolerance)**: Устойчивость к разделению – это способность системы продолжать работу даже при потере связи между отдельными компонентами.
Распределенные системы могут столкнуться с сетевыми сбоями или разделением на части из-за проблем с сетью. Устойчивость к разделению гарантирует,
что система будет продолжать функционировать, сохраняя при этом согласованность и доступность в пределах возможного.

Сама же CAP теорема гласит, что любая СУБД может реализовывать лишь два свойства из данных трех. То есть одним из свойств всегда приходится жертвовать. Разберем на примерах

### DragonFly
Проанализировав статьи с [хабра](https://habr.com/ru/articles/745406/) и [opennet](https://www.opennet.ru/opennews/art.shtml?num=57279), я понял, что данная СУБД - 
переосмысление и улучшение популярной СУБД Redis. Одна из основных фишек - использование 2Q кэширования вместо LRU. На официальном сайте уже [указан](https://www.dragonflydb.io/faq/advantages-and-disadvantages-of-in-memory-database)
недостаток этой In-Memory database:"_The biggest disadvantage is that memory is volatile, which means if the system crashes or 
loses power, all data in memory can be lost._"

**ИТОГ**: на основе всей прочитанной информации делаем вывод, что DragonFly CA, но не P

### ScyllaDB
Как я понял, конкурент MongoDB и Касандры
Не смог найти что-то инересное про данное СУБД на независимых источниках, поэтому придется ссылаться на сайт самой СУБД, где [явно утверждается](https://www.scylladb.com/2018/08/28/scylla-fault-tolerance/), 
что данная СУБД  __chooses availability and partition tolerance over consistency, because it's impossible to be both consistent and highly available during a network partition and if we sacrifice consistency, we can be highly available__

**ИТОГ**: ScyllaDB AP и жертвует C

### ArendataDB
Arenadata DB (ADB) – распределенная СУБД, использующая концепцию MPP 
(massively parallel processing, массивно-параллельные вычисления) и основанная на СУБД с открытым исходным кодом – Greenplum.

Архитектура ADB – классический кластер: несколько серверов-сегментов, один сервер-мастер и один резервный, соединенные между собой быстрыми сетями (10G Ethernet или Infiniband). 
В каждом сервер-сегменте есть несколько сегментов (инстансов) PostgreSQL, содержащих данные. В случае отказа одного или нескольких сегментов они помечаются как сбойные и вместо них 
запускаются их зеркальные сегменты, репликация данных для которых происходит с помощью используемой в СУБД PostgreSQL технологии опережающей записи (Wright Ahead Log, WAL – 
все изменения таблиц и индексов записываются в файл только после их занесения в журнал). Почитав [документацию](https://docs.arenadata.io/adb/index.html) и 
[рекламный сайт](https://arenadata.tech/products/arenadata-db/) делаю вывод, точно есть C и P, но видимо нет A (хотя по ощущениям есть все 3, но просто A и C как бы делят в соотношении 20 на 80)

**ИТОГ**: Точно есть P, пункт C немного урезан в целях чтобы было A.