'''
Created on Oct 19, 2010

@author: joeykblack
'''

categories = []
gifting = {}

def fix(name):
    return name.replace('-', '/').replace('_', ' ').replace('Gods', "God's")

def unfix(name):
    return name.replace('/', '-').replace(' ', '_').replace("God's", "Gods")

# Init Categories
categories.append("Displaying_Gods_love")
categories.append("Communicating_Gods_mind")
categories.append("Managing_with_Gods_principles")
categories.append("Displaying_Gods_authority")


# Init Giftings

# NOTE: order corresponds to order in narratives.csv
# not really a good solution

#Serving/Helps, Showing Mercy, Hospitality, Encouraging, Giving 
gifting[categories[0]] = ["Serving-Helps","Showing_Mercy","Hospitality","Encouraging","Giving"]

#Wisdom, Knowledge, Prophecy, Teaching, Evangelism
gifting[categories[1]] = ["Wisdom","Knowledge","Prophecy","Teaching","Evangelism"]

#Administration, Leadership, Pastors, Apostles, Faith
gifting[categories[2]] = []
gifting[categories[2]].append("Administration")
gifting[categories[2]].append("Leadership-Oversight")
gifting[categories[2]].append("Pastors")
gifting[categories[2]].append("Apostles")
gifting[categories[2]].append("Faith")

#Healings, Miracles, Distinguishing of Spirits, Tongues, Interpreting Tongues
gifting[categories[3]] = []
gifting[categories[3]].append("Healings")
gifting[categories[3]].append("Miracles")
gifting[categories[3]].append("Distinguishing_of_Spirits")
gifting[categories[3]].append("Tongues")
gifting[categories[3]].append("Interpreting_Tongues")


#specialO = iconv("UTF-8", "ISO-8859-2#TRANSLIT", "o")



# NOTE: must be in order as above

#A.Displaying God's love
definitions={}
definitions[ gifting[categories[0]] [0] ] = ["Serving/Helps", "(1 Corinthians, Romans, 1 Peter) diakonia - Meeting charitable needs by command or voluntary service."]
definitions[ gifting[categories[0]] [1] ] = ["Showing mercy", "(Romans) eleeo - Helping those that are afflicted or seeking aid."]
definitions[ gifting[categories[0]] [2] ] = ["Hospitality", "(1 Peter) diakoneo - To provide food, drink and the necessities of life to guests."]
definitions[ gifting[categories[0]] [3] ] = ["Encouraging", "(Romans) parakaleo - To summon, speak to, console and encourage by strengthening the individual"]
definitions[ gifting[categories[0]] [4] ] = ["Giving", "(Romans) metadidomi - To freely grant, supply or furnish what is necessary as if it was their due."]

#Communicating God's mind
definitions[ gifting[categories[1]] [0] ] = ["Wisdom", "(1 Corinthians) Sophia - Supreme intelligence acquired by divine insight, experience and application in many diverse matters."]
definitions[ gifting[categories[1]] [1] ] = ["Knowledge", "(1 Corinthians) gnosis - General intelligence, understanding of what is moral and right living."]
definitions[ gifting[categories[1]] [2] ] = ["Prophecy", "(1 Corinthians, Romans, Ephesians) prophetes - Someone moved by the Spirit to proclaim a cause or event relevant to growth, development or salvation. "]
definitions[ gifting[categories[1]] [3] ] = ["Teaching", "(Romans, Ephesians, 1 Peter)  didasko - To instruct, expound, explain and instill doctrine"]
definitions[ gifting[categories[1]] [4] ] = ["Evangelists", "(Ephesians) euaggelistes - Someone who brings good tidings (of the gospel), simply and plainly who are not apostles."]

#Managing with God's principles 
definitions[ gifting[categories[2]] [0] ] = ["Administration", "(1 Peter) oikonomos - A manager or supervisor trusted with the management of all day to day operations."]
definitions[ gifting[categories[2]] [1] ] = ["Leadership/Oversight", "(Romans) proistemi - A protector, guardian or one given oversight of others."]
definitions[ gifting[categories[2]] [2] ] = ["Pastors", "(Ephesians) poimen -A herdsman who oversees the care and control of others, as an overseer of Christian assemblies."]
definitions[ gifting[categories[2]] [3] ] = ["Apostles", "(Ephesians) apostolos - One sent with divine orders and direction, referring specifically to the 12 or generally to eminent Christian teachers."]
definitions[ gifting[categories[2]] [4] ] = ["Faith", "(1 Corinthians) pistis - Trust and conviction of the truth regarding man's relationship with God and divine things."]

#Displaying God's authority
definitions[ gifting[categories[3]] [0] ] = ["Healings", "(1 Corinthians) iama - To cure, make physically and/or spiritually whole and remove errors (or sin, bringing about salvation)."]
definitions[ gifting[categories[3]] [1] ] = ["Miraculous powers", "(1 Corinthians) dynamis - To have the power, resources or ability to do something strong or very significant as a sighn for salvation/increased faith."]
definitions[ gifting[categories[3]] [2] ] = ["Distinguishing between spirits", "(1 Corinthians) diakrisis - Be able to judge, separate, discriminate or distinguish differences in spirits."]
definitions[ gifting[categories[3]] [3] ] = ["Speaking in different kinds of tongues/languages", "(1 Corinthians) glossa - The dialect that identifies or distinguishes a distinct people."]
definitions[ gifting[categories[3]] [4] ] = ["Interpretation of tongues/languages", "(1 Corinthians) hermeneia - Identifying, explaining or expounding communication that is obscure to others."]



#title prefix
heading = []
heading.append("Your greatest gifting is found in ")
heading.append("Your second greatest gifting is found in ")
heading.append("Your third greatest gifting is found in ")
heading.append("Your fourth greatest gifting is found in ")



