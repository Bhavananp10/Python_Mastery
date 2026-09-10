"""
Module 6 practice — Nested dictionaries & the full "person" worked example.
Notes: 03-nested-dictionaries-and-worked-example.md
Author: Bhavana
"""


def demo_nested_access():
    print("== Nested dictionaries & lists ==")
    person = {
        "name": "Bhavana",
        "address": {"street": "Space street", "zipcode": "02210"},
        "skills": ["JavaScript", "React", "Node", "MongoDB", "Python"],
    }
    print("address.street:", person["address"]["street"])
    print("skills[0]:      ", person["skills"][0])
    print("middle skill:   ", person["skills"][len(person["skills"]) // 2])

    data = {"users": [{"name": "Bhavana", "age": 22}, {"name": "Anu", "age": 24}]}
    print("data['users'][0]['name']:", data["users"][0]["name"])


def demo_shallow_copy_trap():
    print("\n== copy() is shallow — nested data is still shared ==")
    person = {"name": "Bhavana", "skills": ["Python"]}
    copy = person.copy()
    copy["skills"].append("SQL")
    print("person['skills'] also changed:", person["skills"])


PERSON = {
    "first_name": "Bhavana",
    "last_name": "Buddha",
    "age": 22,
    "country": "Finland",
    "is_married": True,
    "skills": ["JavaScript", "React", "Node", "MongoDB", "Python"],
    "address": {"street": "Space street", "zipcode": "02210"},
}


def middle_skill(person):
    if "skills" not in person:
        return None
    skills = person["skills"]
    return skills[len(skills) // 2]


def knows_python(person):
    return "Python" in person.get("skills", [])


def classify_developer(person):
    skills = set(person.get("skills", []))
    if {"React", "Node", "MongoDB"}.issubset(skills):
        return "fullstack developer"
    if {"Node", "Python", "MongoDB"}.issubset(skills):
        return "backend developer"
    if skills == {"JavaScript", "React"}:
        return "frontend developer"
    return "unknown title"


def describe_marriage_and_country(person):
    if person["is_married"] and person["country"] == "Finland":
        full_name = person["first_name"] + " " + person["last_name"]
        return f"{full_name} lives in {person['country']}. They are married."
    return None


def demo_worked_example():
    print("\n== Worked example: the person record ==")
    print("Middle skill:", middle_skill(PERSON))
    print("Knows Python:", knows_python(PERSON))
    print("Classification:", classify_developer(PERSON))
    print(describe_marriage_and_country(PERSON))


if __name__ == "__main__":
    demo_nested_access()
    demo_shallow_copy_trap()
    demo_worked_example()
