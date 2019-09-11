import unittest

from run_app import app

class TestRoutes(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_index(self):
        response = self.app.get('/')
        self.assertEqual(200, response.status_code)
        self.assertEqual('text/html; charset=utf-8', response.content_type)

        response_str = response.data.decode('utf-8')
        self.assertIn('<td>Spider-Man</td>', str(response_str))
        self.assertIn('<td>Bitten by a radioactive spider, high school student Peter Parker gained the speed, strength and powers of a spider. Adopting the name Spider-Man, Peter hoped to start a career using his new abilities. Taught that with great power comes great responsibility, Spidey has vowed to use his powers to help people.</td>', str(response_str))
        self.assertIn('<td><a href = "/stories/1009610?character_name=Spider-Man">Read more...</a></td>', str(response_str))

        self.assertIn('<td>Fantastic Four</td>', str(response_str))
        self.assertIn('<td>After being exposed to cosmic rays, Reed Richards, Susan Storm, Ben Grimm and Johnny Storm found they had amazing new powers. Reed Richards found he has the ability to stretch his body in any way he wanted, while Susan Storm can turn herself, objects and other people invisible. Ben Grimm transformed into a rocky, super-strong behemoth and Johnny Storm has the ability to set himself on fire. Dubbed the Fantastic Four, Mr. Fantastic, Invisible Woman, Thing and the Human Torch are Marvel&#39;s First Family.</td>', str(response_str))
        self.assertIn('<td><a href = "/stories/1009299?character_name=Fantastic+Four">Read more...</a></td>', str(response_str))

        self.assertIn('<td>Wolverine</td>', str(response_str))
        self.assertIn('<td>Born with super-human senses and the power to heal from almost any wound, Wolverine was captured by a secret Canadian organization and given an unbreakable skeleton and claws. Treated like an animal, it took years for him to control himself. Now, he&#39;s a premiere member of both the X-Men and the Avengers.</td>', str(response_str))
        self.assertIn('<td><a href = "/stories/1009718?character_name=Wolverine">Read more...</a></td>', str(response_str))

    def test_index_bootstrap_css(self):
        response = self.app.get('/')
        response_str = response.data.decode('utf-8')
        self.assertIn('bootstrap.min.css', response_str)

    def test_view_stories(self):
        response = self.app.get('/stories/1009610?character_name=Spider-Man')
        self.assertEqual(200, response.status_code)
        self.assertEqual('text/html; charset=utf-8', response.content_type)

        response_str = response.data.decode('utf-8')
        self.assertIn('<td>Cover #486</td>', str(response_str))
        self.assertIn('<td>Interior #487</td>', str(response_str))
        self.assertIn('<td>SENSATIONAL SPIDER-MAN (2006) #23</td>', str(response_str))
        self.assertIn('<td>Interior #499</td>', str(response_str))
        self.assertIn('<td>Interior #599</td>', str(response_str))

    def test_view_bootstrap_css(self):
        response = self.app.get('/stories/1009610?character_name=Spider-Man')
        response_str = response.data.decode('utf-8')
        self.assertIn('bootstrap.min.css', response_str)

if __name__ == '__main__':
    unittest.main()
