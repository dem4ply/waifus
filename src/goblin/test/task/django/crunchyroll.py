from unittest import TestCase
from unittest.mock import patch, Mock
from goblin.task.django.crunchyroll import save_newspaper

class Crunchyroll_test( TestCase ):
    @patch( 'requests.post' )
    def test_save_newspaper( self, requests_post ):
        item_test = {
            'test': 'test'
        }
        save_newspaper.apply( item_test )
        self.assertTrue( requests_post.called )
