"""
OpenAI O1 API統合スクリプトのテスト
"""

import os
import unittest
from unittest.mock import patch, MagicMock
import tempfile
import json
from datetime import datetime
from pathlib import Path

from src.call_openai_api import (
    get_latest_data_folder,
    read_prompt_file,
    read_markdown_file,
    call_openai_api,
    process_slack_data,
    process_github_data
)


class TestCallOpenAIAPI(unittest.TestCase):
    """OpenAI API統合スクリプトのテストクラス"""

    def setUp(self):
        """テスト前の準備"""
        self.temp_dir = tempfile.TemporaryDirectory()
        self.data_dir = Path(self.temp_dir.name)
        
        self.test_folder = self.data_dir / "2025-04-01_to_2025-04-07"
        self.test_folder.mkdir(parents=True, exist_ok=True)
        
        self.weekly_summary_path = self.test_folder / "weekly_summary.md"
        self.all_summary_path = self.test_folder / "all_summary.md"
        self.github_report_path = self.test_folder / "github_report-testrepo.md"
        
        with open(self.weekly_summary_path, 'w', encoding='utf-8') as f:
            f.write("# Weekly Summary\nTest content")
        
        with open(self.all_summary_path, 'w', encoding='utf-8') as f:
            f.write("# All Summary\nTest content")
        
        with open(self.github_report_path, 'w', encoding='utf-8') as f:
            f.write("# GitHub Report\nTest content")
        
        self.prompt_dir = self.data_dir / "src"
        self.slack_logger_dir = self.prompt_dir / "slack_logger"
        self.github_logger_dir = self.prompt_dir / "github_logger"
        
        self.slack_logger_dir.mkdir(parents=True, exist_ok=True)
        self.github_logger_dir.mkdir(parents=True, exist_ok=True)
        
        self.slack_prompt_path = self.slack_logger_dir / "prompt.txt"
        self.github_prompt_path = self.github_logger_dir / "prompt.txt"
        
        with open(self.slack_prompt_path, 'w', encoding='utf-8') as f:
            f.write("Slack prompt test")
        
        with open(self.github_prompt_path, 'w', encoding='utf-8') as f:
            f.write("GitHub prompt test")

    def tearDown(self):
        """テスト後のクリーンアップ"""
        self.temp_dir.cleanup()

    def test_get_latest_data_folder(self):
        """最新のデータフォルダを取得するテスト"""
        older_folder = self.data_dir / "2025-03-25_to_2025-03-31"
        older_folder.mkdir(parents=True, exist_ok=True)
        
        import time
        time.sleep(0.1)
        newer_folder = self.data_dir / "2025-04-08_to_2025-04-14"
        newer_folder.mkdir(parents=True, exist_ok=True)
        
        with patch('os.path.getctime', return_value=time.time()):
            latest = get_latest_data_folder(str(self.data_dir))
            self.assertEqual(os.path.basename(latest), "2025-04-08_to_2025-04-14")

    def test_read_prompt_file(self):
        """プロンプトファイルを読み込むテスト"""
        content = read_prompt_file(str(self.slack_prompt_path))
        self.assertEqual(content, "Slack prompt test")

    def test_read_markdown_file(self):
        """Markdownファイルを読み込むテスト"""
        content = read_markdown_file(str(self.weekly_summary_path))
        self.assertEqual(content, "# Weekly Summary\nTest content")

    @patch('openai.chat.completions.create')
    def test_call_openai_api(self, mock_create):
        """OpenAI APIを呼び出すテスト"""
        mock_response = MagicMock()
        mock_response.choices = [MagicMock()]
        mock_response.choices[0].message.content = "API response"
        mock_response.usage.prompt_tokens = 100
        mock_response.usage.completion_tokens = 50
        mock_create.return_value = mock_response
        
        response, cost = call_openai_api("Test prompt", "Test content")
        
        self.assertEqual(response, "API response")
        self.assertAlmostEqual(cost, 0.0045)  # 100 * 0.000015 + 50 * 0.000060 = 0.0045
        
        mock_create.assert_called_once_with(
            model="o1",
            messages=[
                {"role": "system", "content": "Test prompt"},
                {"role": "user", "content": "Test content"}
            ],
            temperature=0.7,
        )

    @patch('src.call_openai_api.call_openai_api')
    @patch('src.call_openai_api.read_prompt_file')
    @patch('src.call_openai_api.os.path.dirname')
    def test_process_slack_data(self, mock_dirname, mock_read_prompt, mock_call_api):
        """Slackデータを処理するテスト"""
        mock_dirname.return_value = str(self.data_dir)
        mock_read_prompt.return_value = "Test prompt"
        mock_call_api.return_value = ("API response", 0.0045)
        
        with patch('builtins.open'), \
             patch('datetime.now') as mock_now:
            mock_now.return_value = datetime(2025, 4, 4, 12, 0, 0)
            process_slack_data(
                data_dir=str(self.test_folder),
                output_dir=str(self.test_folder),
                use_all_summary=False,
                period=None
            )
        
        mock_read_prompt.assert_called_once()
        mock_call_api.assert_called_once()

    @patch('src.call_openai_api.call_openai_api')
    @patch('src.call_openai_api.read_prompt_file')
    @patch('src.call_openai_api.os.path.dirname')
    def test_process_github_data(self, mock_dirname, mock_read_prompt, mock_call_api):
        """GitHubデータを処理するテスト"""
        mock_dirname.return_value = str(self.data_dir)
        mock_read_prompt.return_value = "Test prompt"
        mock_call_api.return_value = ("API response", 0.0045)
        
        with patch('builtins.open'), \
             patch('datetime.now') as mock_now:
            mock_now.return_value = datetime(2025, 4, 4, 12, 0, 0)
            process_github_data(
                repo="owner/testrepo",
                data_dir=str(self.test_folder),
                output_dir=str(self.test_folder)
            )
        
        mock_read_prompt.assert_called_once()
        mock_call_api.assert_called_once()


if __name__ == '__main__':
    unittest.main()
