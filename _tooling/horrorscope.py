import types, math, sys, re, yaml, os, calendar, datetime, random

YearRange = range(2020,2033)
def main():

    f = open( "horrorscope/index.md", "w" )
    f.write( """---
permalink: /horrorscope
layout: horrorscopeindex
---
<center>
""")
    for yr in YearRange:
        f.write( calendar.HTMLCalendar().formatyear(yr) )
        f.write("\n")

    f.write("</center>")


    all_names = yaml.load(open("_data/names.yaml").read(),Loader=yaml.FullLoader)
    all_sayings = yaml.load(open("_data/sayings.yaml").read(),Loader=yaml.FullLoader)

    all_female_sayings = []
    all_male_sayings = []

    for idx in range(0, len(all_sayings)):
        if all_sayings[idx]["gender"] in ["d","m"]: all_male_sayings.append(idx)
        if all_sayings[idx]["gender"] in ["d","f"]: all_female_sayings.append(idx)

    first_day = datetime.date(YearRange[0],1,1)
    last_day = datetime.date(YearRange[-1]+1,1,1)
    td = datetime.timedelta(days=1)
    prev_day = None

    horrorscopes = {}

    while first_day < last_day:
        datestr = first_day.strftime("%Y%m%d")
        f = open( "horrorscope/{}.md".format(datestr), "w" )
        f.write( open( "horrorscope/_template.md", "r" ).read() )

        f.write("<table class='nav_links'><tr>")

        if prev_day:
            f.write("<td class='prev_link'><a href='{}'>Previous</a></td>".format(prev_day.strftime("%Y%m%d") ))
        else:
            f.write("<td></td>")

        f.write("<td class='calendar_link'><a href='/horrorscope'>Calendar</a></td>".format((first_day+td).strftime("%Y%m%d") ))

        if (first_day+td) != last_day:
            f.write("<td class='next_day'><a href='{}'>Next</a></td>".format((first_day+td).strftime("%Y%m%d") ))
        else:
            f.write("<td></td>")

        f.write("</tr></table>")

        f.close()

        horrorscopes[datestr] = [
            {
                "n": [ random.randrange( 0, len(all_names["female"]) ),
                       random.randrange( 0, len(all_names["male"]) ) ],
                "s": [ random.sample(all_female_sayings, k=1)[0],
                       random.sample(all_male_sayings, k=1)[0] ]
            } for n in range(1,13)]

        prev_day = first_day
        first_day += td

    with open(r'_data/horrorscope.yaml', 'w') as file:
        outputs = yaml.dump(horrorscopes, file)

if __name__ == '__main__':
    main()
