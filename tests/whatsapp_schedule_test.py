import unittest
import sys

sys.path.append("..")
from App.inputs import phonenumber_check,whatsapp_schedule_message,date_time


class TestScheduleclass(unittest.TestCase):

    def test_time_format(self):
       self.assertTrue ( phonenumber_check.check_phone_number("254704563911") )

    def test_choice(self):
       self.assertTrue (phonenumber_check.check_options("1") )

    def test_schedule_message(self):
       self.assertIsNone (whatsapp_schedule_message.schedule_message("hello",254704563911))
      
    def test_date_format(self):
       self.assertTrue (date_time.check_date_format("2/07/2021"))

    def test_get_todays_date(self):
     self.assertTrue (date_time.get_todays_date())

    def test_get_time_now(self):
     self.assertTrue(date_time.get_time_now())

    def test_check_date_not_passed(self):
     self.assertTrue (date_time.check_date_not_passed("2/07/2021", "3/07/2021"))

    def test_countdown_timer(self):
     self.assertTrue  (date_time.check_date_time_not_passed("2/07/2021 00:00", "3/07/2021 00:00"))


    
   



   

   
   

