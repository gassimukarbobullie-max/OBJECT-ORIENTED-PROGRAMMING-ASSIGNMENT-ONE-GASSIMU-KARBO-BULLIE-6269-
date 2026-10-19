from datetime import date

SPECIES = ("Cattle", "Goat", "Sheep", "Pig", "Chicken")
HEALTH_STATUSES = ("Healthy", "Needs Attention", "Under Treatment", "Recovering")

class Animal:

    total_animals = 0

    def __init__(self, tag_id, species, age_months, health_status="Healthy"):
        if not Animal.is_valid_tag(tag_id):
            raise ValueError("Tag ID must be 3-12 letters, numbers or hyphens.")
        if species.title() not in SPECIES:
            raise ValueError("Species must be one of: " + ", ".join(SPECIES))
        if age_months < 0:
            raise ValueError("Age cannot be negative.")
        if health_status not in HEALTH_STATUSES:
            raise ValueError("Invalid health status.")

        self.tag_id = tag_id.strip().upper()
        self.species = species.title()
        self.age_months = age_months
        self.health_status = health_status
        self.last_checkup = date.today()
        self.last_treatment = "None"
        Animal.total_animals += 1


    def update_record(self, health_status, treatment="None"):
        if health_status not in HEALTH_STATUSES:
            raise ValueError("Invalid health status.")
        self.health_status = health_status
        self.last_treatment = treatment.strip() or "None"
        self.last_checkup = date.today()

    def days_since_checkup(self, today=None):
        return ((today or date.today()) - self.last_checkup).days

    def needs_checkup(self, interval_days=90):
        return self.days_since_checkup() >= interval_days

    def display_info(self):
        due = "YES - CHECKUP DUE" if self.needs_checkup() else "No"
        print(f"Tag ID        : {self.tag_id}")
        print(f"Species       : {self.species}")
        print(f"Age (months)  : {self.age_months}")
        print(f"Health status : {self.health_status}")
        print(f"Last treatment: {self.last_treatment}")
        print(f"Last checkup  : {self.last_checkup.isoformat()}")
        print(f"Checkup due   : {due}")

    @classmethod
    def from_string(cls, text):
        tag, species, age = [part.strip() for part in text.split(",")]
        return cls(tag, species, int(age))

    @classmethod
    def get_total_animals(cls):
        return cls.total_animals

    @staticmethod
    def is_valid_tag(tag):
        tag = tag.strip()
        return 3 <= len(tag) <= 12 and tag.replace("-", "").isalnum()


class Herd:

    def __init__(self, farm_code):
        self.farm_code = farm_code  # a code such as "FARM-001", not a person's name
        self._animals = {}          # {tag_id: Animal}

    def add_animal(self, animal):
        if animal.tag_id in self._animals:
            raise ValueError(f"Tag {animal.tag_id} is already registered.")
        self._animals[animal.tag_id] = animal

    def get_animal(self, tag_id):
        return self._animals.get(tag_id.strip().upper())

    def all_animals(self):
        return self._animals.values()

    def __len__(self):
        return len(self._animals)
