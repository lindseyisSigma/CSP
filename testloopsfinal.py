gold = ["1", "2", "3"]
got_gold1="1"
got_gold2="2"
got_gold3="3"
got_gold4="4"
got_gold5="5"

gold: list[str]
for gold in gold:
    print(f"You now have {gold}!")
Golds = 3
text = "Gold" + str(Golds)

live_remaning = ["1", "2", "3"]
live_remaning: list[str]
for live_remaning in live_remaning:
    print(f"You now have {live_remaning}HP!")
lives_remaning = 3
text = "Lives" + str(lives_remaning)
