# Livestock Health & Tracking System

**Module:** PROG211 Object-Oriented Programming 1 (Individual Assignment, Real-World Solutions under DPG Standards)
**Domain:** Agriculture

## The problem
Smallholder farmers often track animal health on paper, so vaccinations and checkups get missed. This
program gives a simple, free way to register animals, record treatments and see which animals are due
for a checkup.

## How to run
Requires Python 3.8+ and no extra libraries.

```
python main.py
```

## Project structure
| File | Purpose |
|------|---------|
| `models.py` | `Animal` and `Herd` classes (reusable in other projects) |
| `main.py` | Console menu, plus `add_record()` and `display_records()` functions |

## OOP concepts used
- **Classes and objects:** `Animal` and `Herd`; a `Herd` holds and interacts with many `Animal` objects.
- **Attributes:** tag_id, species, age_months, health_status, last_treatment, last_checkup.
- **Instance methods:** `update_record()`, `display_info()`, `needs_checkup()`, `days_since_checkup()`.
- **Class methods:** `Animal.from_string()` and `Animal.get_total_animals()`.
- **Static method:** `Animal.is_valid_tag()`.
- **Data structure (one only):** a dictionary `{tag_id: Animal}` inside `Herd`.
- **Tuples (optional):** `SPECIES` and `HEALTH_STATUSES` are fixed, unchangeable lists of allowed values.

## How this meets Digital Public Goods (DPG) standards
| Principle | How it is met |
|-----------|---------------|
| Open-source | Source code is published on GitHub for anyone to use, study and improve. |
| Inclusive and accessible | Plain-language prompts; numbered choices instead of typing exact words; clear error messages; no reliance on colour, images or sound; runs on low-spec computers with no internet. |
| Privacy-respecting | Only anonymous tag IDs are stored. No owner names, phone numbers, addresses or location data. |
| Modular and reusable | Data classes (`models.py`) are separate from the interface (`main.py`), so a web or mobile front end can reuse them. |

## Example usage
```
Choose an option (1-5): 1
Tag ID (e.g. COW-002): COW-002
Species:
  1. Cattle   2. Goat   3. Sheep   4. Pig   5. Chicken
Choose species number: 1
Age in months: 24
Animal registered.

Choose an option (1-5): 3
Tag ID: COW-002
New health status:
  1. Healthy   2. Needs Attention   3. Under Treatment   4. Recovering
Choose status number: 3
Treatment given (press Enter for none): Antibiotics
Record updated.

Choose an option (1-5): 2
--------------------------------
Tag ID        : COW-002
Species       : Cattle
Age (months)  : 24
Health status : Under Treatment
Last treatment: Antibiotics
Last checkup  : 2026-10-17
Checkup due   : No
--------------------------------
```

## Licence
MIT (open-source).
