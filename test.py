my_list= [
            "Beautiful detailed portrait of an adorable day old elf baby by Jonathan Romeo, trending on artstation, instagram, octane render, unreal engine, realistic human eyes, piercing Heterochromia eyes, realistic human flesh:4",
            "text:-2",
            "glasses:-1",
            "color: 1"
        ]
#get the sum of all the numbers after the colon in my_list
print(sum(int(i.split(':')[1]) for i in my_list))