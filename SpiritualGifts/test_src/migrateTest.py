'''
Created on Sep 18, 2016

@author: joey
'''
import unittest

from util import migrate, constants
from model.results import Resultset
from util.utils import buildQuestionKey


class Test(unittest.TestCase):


    def testMigrate(self):
        data = ["Managing_with_Gods_principles_Faith_1,4","Managing_with_Gods_principles_Faith_2,4","Managing_with_Gods_principles_Faith_3,4","Managing_with_Gods_principles_Faith_4,3","Managing_with_Gods_principles_Faith_5,4","Displaying_Gods_authority_Healings_5,1","Displaying_Gods_authority_Distinguishing_of_Spirits_5,2","Displaying_Gods_authority_Distinguishing_of_Spirits_4,4","Displaying_Gods_authority_Distinguishing_of_Spirits_3,2","Displaying_Gods_authority_Distinguishing_of_Spirits_2,3","Displaying_Gods_authority_Distinguishing_of_Spirits_1,4","Displaying_Gods_authority_Healings_4,4","Displaying_Gods_love_Showing_Mercy_3,4","Displaying_Gods_love_Showing_Mercy_2,2","Displaying_Gods_love_Showing_Mercy_1,3","Displaying_Gods_love_Showing_Mercy_5,4","Displaying_Gods_love_Showing_Mercy_4,4","Communicating_Gods_mind_Teaching_2,4","Communicating_Gods_mind_Teaching_3,4","Displaying_Gods_love_Serving-Helps_4,4","Displaying_Gods_love_Serving-Helps_5,4","Displaying_Gods_love_Serving-Helps_1,1","Displaying_Gods_love_Serving-Helps_2,4","Displaying_Gods_love_Serving-Helps_3,4","Displaying_Gods_love_Hospitality_3,4","Displaying_Gods_love_Hospitality_2,4","Displaying_Gods_love_Hospitality_1,4","Displaying_Gods_love_Hospitality_5,4","Displaying_Gods_love_Hospitality_4,4","Managing_with_Gods_principles_Administration_1,2","Displaying_Gods_authority_Tongues_3,0","Managing_with_Gods_principles_Administration_3,1","Managing_with_Gods_principles_Administration_2,2","Managing_with_Gods_principles_Administration_5,2","Managing_with_Gods_principles_Administration_4,2","Displaying_Gods_authority_Tongues_4,0","Displaying_Gods_authority_Tongues_5,0","Managing_with_Gods_principles_Apostles_1,4","Managing_with_Gods_principles_Apostles_2,0","Managing_with_Gods_principles_Apostles_3,0","Managing_with_Gods_principles_Apostles_4,1","Managing_with_Gods_principles_Apostles_5,0","Managing_with_Gods_principles_Pastors_1,3","Managing_with_Gods_principles_Pastors_2,4","Managing_with_Gods_principles_Pastors_3,4","Managing_with_Gods_principles_Pastors_4,3","Managing_with_Gods_principles_Pastors_5,3","Communicating_Gods_mind_Wisdom_4,4","Communicating_Gods_mind_Wisdom_5,3","Communicating_Gods_mind_Prophecy_3,4","Communicating_Gods_mind_Prophecy_5,2","Communicating_Gods_mind_Prophecy_4,4","Communicating_Gods_mind_Wisdom_2,4","Communicating_Gods_mind_Prophecy_2,4","Communicating_Gods_mind_Prophecy_1,3","Communicating_Gods_mind_Wisdom_3,4","Displaying_Gods_love_Giving_4,4","Displaying_Gods_love_Giving_5,3","Communicating_Gods_mind_Wisdom_1,4","Displaying_Gods_love_Giving_1,0","Displaying_Gods_love_Giving_2,4","Displaying_Gods_love_Giving_3,2","Communicating_Gods_mind_Teaching_4,4","Communicating_Gods_mind_Teaching_5,3","Displaying_Gods_authority_Healings_1,2","Communicating_Gods_mind_Teaching_1,4","Displaying_Gods_authority_Healings_3,1","Displaying_Gods_authority_Healings_2,1","Displaying_Gods_authority_Tongues_2,0","Displaying_Gods_authority_Interpreting_Tongues_5,0","Displaying_Gods_authority_Interpreting_Tongues_4,0","Displaying_Gods_authority_Interpreting_Tongues_3,0","Displaying_Gods_authority_Interpreting_Tongues_2,0","Displaying_Gods_authority_Interpreting_Tongues_1,0","Displaying_Gods_authority_Tongues_1,0","Displaying_Gods_authority_Miracles_4,2","Displaying_Gods_authority_Miracles_5,2","Displaying_Gods_authority_Miracles_1,2","Displaying_Gods_authority_Miracles_2,3","Displaying_Gods_authority_Miracles_3,3","Managing_with_Gods_principles_Leadership-Oversight_2,4","Managing_with_Gods_principles_Leadership-Oversight_3,0","Managing_with_Gods_principles_Leadership-Oversight_1,1","Managing_with_Gods_principles_Leadership-Oversight_4,3","Managing_with_Gods_principles_Leadership-Oversight_5,4","Displaying_Gods_love_Encouraging_3,3","Displaying_Gods_love_Encouraging_2,2","Displaying_Gods_love_Encouraging_1,4","Displaying_Gods_love_Encouraging_5,3","Displaying_Gods_love_Encouraging_4,4","Communicating_Gods_mind_Knowledge_4,1","Communicating_Gods_mind_Knowledge_5,4","Communicating_Gods_mind_Knowledge_1,4","Communicating_Gods_mind_Knowledge_2,4","Communicating_Gods_mind_Knowledge_3,4","Communicating_Gods_mind_Evangelism_4,0","Communicating_Gods_mind_Evangelism_5,0","Communicating_Gods_mind_Evangelism_2,1","Communicating_Gods_mind_Evangelism_3,1","Communicating_Gods_mind_Evangelism_1,3"]
        resultset = Resultset()
        resultset.results = data
        resultset = migrate.addOne(resultset)
        resultset = migrate.updateKeys(resultset)
        resultDict = resultset.getResultsDict()
        for category in constants.categories:
            for gift in constants.gifting[category]:
                for i in range(1,6):
                    key = buildQuestionKey(category, gift, i)
                    print key
                    self.assertTrue(key in resultDict)
        

if __name__ == "__main__":
    unittest.main()