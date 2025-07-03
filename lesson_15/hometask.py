import sys
import os
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

import unittest
from unittest.mock import patch
from log_event_module import log_event

class TestLogEvent(unittest.TestCase):

    @patch("log_event_module.logger")
    def test_log_success(self, mock_logger):
        log_event("user1", "success")
        mock_logger.info.assert_called_once_with("Login event - Username: user1, Status: success")

    @patch("log_event_module.logger")
    def test_log_expired(self, mock_logger):
        log_event("user2", "expired")
        mock_logger.warning.assert_called_once_with("Login event - Username: user2, Status: expired")

    @patch("log_event_module.logger")
    def test_log_failed(self, mock_logger):
        log_event("user3", "failed")
        mock_logger.error.assert_called_once_with("Login event - Username: user3, Status: failed")

    @patch("log_event_module.logger")
    def test_log_unknown_status(self, mock_logger):
        log_event("user4", "locked")
        mock_logger.error.assert_called_once_with("Login event - Username: user4, Status: locked")

if __name__ == "__main__":
    unittest.main()