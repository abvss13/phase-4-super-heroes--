from app import db, Hero, Power, HeroPower

if __name__ == "__main__":
    print("🦸‍♀️ Seeding powers...")
    powers = [
        Power(name="super strength", description="gives the wielder super-human strengths"),
        Power(name="flight", description="gives the wielder the ability to fly through the skies at supersonic speed"),
        Power(name="super human senses", description="allows the wielder to use her senses at a super-human level"),
        Power(name="elasticity", description="can stretch the human body to extreme lengths")
    ]
    db.session.bulk_save_objects(powers)
    db.session.commit()

    print("🦸‍♀️ Seeding heroes...")
    heroes = [
        Hero(name="Kamala Khan", super_name="Ms. Marvel"),
        Hero(name="Doreen Green", super_name="Squirrel Girl"),
        
    ]
    db.session.bulk_save_objects(heroes)
    db.session.commit()

    print("🦸‍♀️ Adding powers to heroes...")
    strengths = ["Strong", "Weak", "Average"]
    
    for hero in Hero.query.all():
        for _ in range(1, 4):  
            power = Power.query.order_by(db.func.random()).first()
            hero_power = HeroPower(hero=hero, power=power, strength=strengths[_ % 3])
            db.session.add(hero_power)
    
    db.session.commit()
    print("🦸‍♀️ Done seeding!")
