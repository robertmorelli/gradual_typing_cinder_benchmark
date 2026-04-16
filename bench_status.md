# Benchmark Status

## Summary

- Benchmarks scanned: `30`
- All green: `11`
- Advanced-only failures: `2`
- Advanced + shallow failures: `4`
- Advanced + untyped failures: `0`
- Advanced + shallow + untyped failures: `7`
- Shallow-only failures: `0`
- Untyped-only failures: `0`
- Shallow + untyped failures: `0`
- Missing variants: `6`

## Needs Fixing Diff

### Advanced only

- meteor
- pidigits

### Advanced and shallow

- evolution
- go
- spectralnorm
- take5

### Advanced and untyped


### Advanced, shallow, and untyped

- espionage
- futen
- http2
- pythonflow
- sample_fsm
- slowsha
- stats

### Shallow only


### Untyped only


### Shallow and untyped


### Missing variants

- Benchmarks_Recreate_Paper_Results
- django
- django_sample
- held_karp
- wagtail
- zulip

### All green

- call_method
- call_method_slots
- call_simple
- chaos
- deltablue
- fannkuch
- float
- nbody
- nqueens
- pystone
- richards

## Per Benchmark

| benchmark | advanced | shallow fuzz | untyped |
| --- | --- | --- | --- |
| Benchmarks_Recreate_Paper_Results | missing | missing | missing |
| call_method | ok | ok | ok |
| call_method_slots | ok | ok | ok |
| call_simple | ok | ok | ok |
| chaos | ok | ok | ok |
| deltablue | ok | ok | ok |
| django | missing | missing | missing |
| django_sample | missing | missing | missing |
| espionage | failed | failed | failed |
| evolution | failed | failed | ok |
| fannkuch | ok | ok | ok |
| float | ok | ok | ok |
| futen | failed | failed | failed |
| go | failed | failed | ok |
| held_karp | ok | missing | missing |
| http2 | failed | failed | failed |
| meteor | failed | ok | ok |
| nbody | ok | ok | ok |
| nqueens | ok | ok | ok |
| pidigits | failed | ok | ok |
| pystone | ok | ok | ok |
| pythonflow | failed | failed | failed |
| richards | ok | ok | ok |
| sample_fsm | failed | failed | failed |
| slowsha | failed | failed | failed |
| spectralnorm | failed | failed | ok |
| stats | failed | failed | failed |
| take5 | failed | failed | ok |
| wagtail | missing | missing | missing |
| zulip | missing | missing | missing |

## Failure Details

### Benchmarks_Recreate_Paper_Results

- `untyped`: `missing` - missing advanced/main.py

### django

- `untyped`: `missing` - missing advanced/main.py

### django_sample

- `untyped`: `missing` - missing advanced/main.py

### espionage

- `advanced typed`: `failed` - Traceback (most recent call last):
- `advanced detyped`: `failed` - Traceback (most recent call last):
- `shallow k=0 sample=1`: `failed` - Traceback (most recent call last):
- `shallow k=1 sample=2`: `failed` - Traceback (most recent call last):
- `shallow k=1 sample=3`: `failed` - Traceback (most recent call last):
- `shallow k=3 sample=4`: `failed` - Traceback (most recent call last):
- `shallow k=3 sample=5`: `failed` - Traceback (most recent call last):
- `shallow k=5 sample=6`: `failed` - Traceback (most recent call last):
- `shallow k=5 sample=7`: `failed` - Traceback (most recent call last):
- `shallow k=6 sample=8`: `failed` - Traceback (most recent call last):
- `shallow k=6 sample=9`: `failed` - Traceback (most recent call last):
- `shallow k=7 sample=10`: `failed` - Traceback (most recent call last):
- `untyped`: `failed` - Traceback (most recent call last):

### evolution

- `advanced typed`: `failed` - Traceback (most recent call last):
- `advanced detyped`: `failed` - Traceback (most recent call last):
- `shallow k=0 sample=1`: `failed` - Traceback (most recent call last):
- `shallow k=1 sample=2`: `failed` - Traceback (most recent call last):
- `shallow k=1 sample=3`: `failed` - Traceback (most recent call last):
- `shallow k=2 sample=4`: `failed` - Traceback (most recent call last):
- `shallow k=2 sample=5`: `failed` - Traceback (most recent call last):
- `shallow k=3 sample=6`: `failed` - Traceback (most recent call last):

### futen

- `advanced typed`: `failed` - Traceback (most recent call last):
- `advanced detyped`: `failed` - Traceback (most recent call last):
- `shallow k=0 sample=1`: `failed` - Traceback (most recent call last):
- `shallow k=1 sample=2`: `failed` - Traceback (most recent call last):
- `untyped`: `failed` - Traceback (most recent call last):

### go

- `advanced typed`: `failed` - Traceback (most recent call last):
- `advanced detyped`: `failed` - Traceback (most recent call last):
- `shallow k=0 sample=1`: `failed` - Traceback (most recent call last):
- `shallow k=22 sample=2`: `failed` - Traceback (most recent call last):
- `shallow k=1 sample=3`: `failed` - Traceback (most recent call last):
- `shallow k=1 sample=4`: `failed` - Traceback (most recent call last):
- `shallow k=5 sample=5`: `failed` - Traceback (most recent call last):
- `shallow k=5 sample=6`: `failed` - Traceback (most recent call last):
- `shallow k=11 sample=7`: `failed` - Traceback (most recent call last):
- `shallow k=16 sample=8`: `failed` - Traceback (most recent call last):
- `shallow k=16 sample=9`: `failed` - Traceback (most recent call last):
- `shallow k=21 sample=10`: `failed` - Traceback (most recent call last):

### held_karp

- `shallow fuzz`: `missing` - missing shallow/main.py
- `untyped`: `missing` - missing untyped/main.py

### http2

- `advanced typed`: `failed` - Traceback (most recent call last):
- `advanced detyped`: `failed` - Traceback (most recent call last):
- `shallow k=0 sample=1`: `failed` - Traceback (most recent call last):
- `shallow k=1 sample=2`: `failed` - Traceback (most recent call last):
- `untyped`: `failed` - Traceback (most recent call last):

### meteor

- `advanced detyped`: `failed` - Traceback (most recent call last):

### pidigits

- `advanced typed`: `failed` - Traceback (most recent call last):
- `advanced detyped`: `failed` - Traceback (most recent call last):

### pythonflow

- `advanced typed`: `failed` - Traceback (most recent call last):
- `advanced detyped`: `failed` - Traceback (most recent call last):
- `shallow k=0 sample=1`: `failed` - Traceback (most recent call last):
- `shallow k=10 sample=2`: `failed` - Traceback (most recent call last):
- `shallow k=1 sample=3`: `failed` - Traceback (most recent call last):
- `shallow k=1 sample=4`: `failed` - Traceback (most recent call last):
- `shallow k=2 sample=5`: `failed` - Traceback (most recent call last):
- `shallow k=2 sample=6`: `failed` - Traceback (most recent call last):
- `shallow k=5 sample=7`: `failed` - Traceback (most recent call last):
- `shallow k=7 sample=8`: `failed` - Traceback (most recent call last):
- `shallow k=7 sample=9`: `failed` - Traceback (most recent call last):
- `shallow k=9 sample=10`: `failed` - Traceback (most recent call last):
- `untyped`: `failed` - Traceback (most recent call last):

### sample_fsm

- `advanced typed`: `failed` - Traceback (most recent call last):
- `advanced detyped`: `failed` - Traceback (most recent call last):
- `shallow k=0 sample=1`: `failed` - Traceback (most recent call last):
- `shallow k=1 sample=2`: `failed` - Traceback (most recent call last):
- `shallow k=1 sample=3`: `failed` - Traceback (most recent call last):
- `shallow k=2 sample=4`: `failed` - Traceback (most recent call last):
- `shallow k=2 sample=5`: `failed` - Traceback (most recent call last):
- `shallow k=3 sample=6`: `failed` - Traceback (most recent call last):
- `untyped`: `failed` - Traceback (most recent call last):

### slowsha

- `advanced typed`: `failed` - Traceback (most recent call last):
- `advanced detyped`: `failed` - Traceback (most recent call last):
- `shallow k=0 sample=1`: `failed` - Traceback (most recent call last):
- `shallow k=1 sample=2`: `failed` - Traceback (most recent call last):
- `shallow k=1 sample=3`: `failed` - Traceback (most recent call last):
- `shallow k=2 sample=4`: `failed` - Traceback (most recent call last):
- `shallow k=2 sample=5`: `failed` - Traceback (most recent call last):
- `shallow k=3 sample=6`: `failed` - Traceback (most recent call last):
- `shallow k=3 sample=7`: `failed` - Traceback (most recent call last):
- `shallow k=4 sample=8`: `failed` - Traceback (most recent call last):
- `untyped`: `failed` - Traceback (most recent call last):

### spectralnorm

- `advanced typed`: `failed` - Traceback (most recent call last):
- `advanced detyped`: `failed` - Traceback (most recent call last):
- `shallow k=2 sample=4`: `failed` - Traceback (most recent call last):
- `shallow k=2 sample=5`: `failed` - Traceback (most recent call last):
- `shallow k=3 sample=6`: `failed` - Traceback (most recent call last):
- `shallow k=4 sample=9`: `failed` - Traceback (most recent call last):
- `shallow k=5 sample=10`: `failed` - Traceback (most recent call last):

### stats

- `advanced typed`: `failed` - Traceback (most recent call last):
- `advanced detyped`: `failed` - Traceback (most recent call last):
- `shallow k=0 sample=1`: `failed` - Traceback (most recent call last):
- `shallow k=1 sample=2`: `failed` - Traceback (most recent call last):
- `untyped`: `failed` - Traceback (most recent call last):

### take5

- `advanced typed`: `failed` - Traceback (most recent call last):
- `advanced detyped`: `failed` - Traceback (most recent call last):
- `shallow k=0 sample=1`: `failed` - Traceback (most recent call last):
- `shallow k=1 sample=2`: `failed` - Traceback (most recent call last):
- `shallow k=1 sample=3`: `failed` - Traceback (most recent call last):
- `shallow k=2 sample=4`: `failed` - Traceback (most recent call last):
- `shallow k=2 sample=5`: `failed` - Traceback (most recent call last):
- `shallow k=3 sample=6`: `failed` - Traceback (most recent call last):

### wagtail

- `untyped`: `missing` - missing advanced/main.py

### zulip

- `untyped`: `missing` - missing advanced/main.py
