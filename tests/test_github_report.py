"""
GitHub Report機能のテスト
"""

import unittest
from unittest.mock import patch, MagicMock
from src.github_logger.github_report import extract_github_data, generate_markdown


class TestGitHubReport(unittest.TestCase):
    """GitHub Report機能のテストクラス"""

    @patch('src.github_logger.github_report.get_github_token')
    @patch('src.github_logger.github_report.requests.get')
    @patch('src.github_logger.github_report.write_json_file')
    def test_closed_prs_not_in_updated(self, mock_write, mock_get, mock_token):
        """クローズされたPRが更新済みPRに含まれないことを確認"""
        mock_token.return_value = "test_token"
        
        # モックレスポンスを設定
        mock_responses = {
            'merged': {'items': []},
            'closed': {'items': [
                {
                    'id': 1,
                    'number': 10,
                    'title': 'Closed PR',
                    'user': {'login': 'testuser'},
                    'html_url': 'https://github.com/test/repo/pull/10',
                    'created_at': '2024-01-01T00:00:00Z',
                    'closed_at': '2024-01-02T00:00:00Z',
                    'body': 'Test closed PR'
                }
            ]},
            'created': {'items': []},
            'updated': {'items': []}
        }
        
        def mock_get_side_effect(url, headers=None, params=None):
            response = MagicMock()
            # /commitsを先にチェック（URLに基づく判定）
            if '/commits' in url:
                # コミット一覧のモック
                response.json.return_value = [
                    {
                        'commit': {
                            'message': 'Test commit message'
                        }
                    }
                ]
            elif '/pulls/' in url:
                # PR詳細のモック
                response.json.return_value = {
                    'additions': 10,
                    'deletions': 5,
                    'changed_files': 2,
                    'merged_at': None,
                    'body': 'Test body'
                }
            elif params and 'q' in params:
                query = params['q']
                if 'merged:' in query:
                    response.json.return_value = mock_responses['merged']
                elif 'closed:' in query and 'is:unmerged' in query:
                    response.json.return_value = mock_responses['closed']
                elif 'created:' in query and 'merged' not in query and 'updated' not in query:
                    response.json.return_value = mock_responses['created']
                elif 'updated:' in query:
                    response.json.return_value = mock_responses['updated']
                else:
                    response.json.return_value = {'items': []}
            else:
                response.json.return_value = {'items': []}
            return response
        
        mock_get.side_effect = mock_get_side_effect
        
        # extract_github_dataを実行
        result, json_file = extract_github_data(
            repo='test/repo',
            output_dir='/tmp/test_output',
            last_days=7,
            include_prs=True,
            timezone_str='UTC'
        )
        
        # 結果を検証
        self.assertIsNotNone(result)
        self.assertEqual(len(result['prs']), 1)
        self.assertEqual(result['prs'][0]['state'], 'closed')
        self.assertEqual(result['prs'][0]['number'], 10)

    def test_markdown_includes_closed_prs(self):
        """Markdownレポートにクローズ済みPRセクションが含まれることを確認"""
        items = [
            {
                'id': 1,
                'number': 10,
                'title': 'Closed PR',
                'state': 'closed',
                'html_url': 'https://github.com/test/repo/pull/10',
                'user': 'testuser',
                'created_at': '2024-01-01T00:00:00Z',
                'closed_at': '2024-01-02T00:00:00Z',
                'body': 'Test body',
                'type': 'pr',
                'additions': 10,
                'deletions': 5,
                'changed_files': 2
            },
            {
                'id': 2,
                'number': 20,
                'title': 'Merged PR',
                'state': 'merged',
                'html_url': 'https://github.com/test/repo/pull/20',
                'user': 'testuser',
                'created_at': '2024-01-01T00:00:00Z',
                'merged_at': '2024-01-03T00:00:00Z',
                'body': 'Test body',
                'type': 'pr',
                'additions': 20,
                'deletions': 10,
                'changed_files': 3
            }
        ]
        
        markdown = generate_markdown(
            items=items,
            repo='test/repo',
            start_date='2024-01-01',
            end_date='2024-01-07',
            output_file='/tmp/test_report.md'
        )
        
        # Markdownにクローズ済みPRセクションが含まれることを確認
        self.assertIn('クローズされたPR（マージなし）', markdown)
        self.assertIn('Closed PR', markdown)
        self.assertIn('クローズ日:', markdown)
        
        # マージ済みPRセクションも含まれることを確認
        self.assertIn('マージされたPR', markdown)
        self.assertIn('Merged PR', markdown)
        self.assertIn('マージ日:', markdown)


if __name__ == '__main__':
    unittest.main()
