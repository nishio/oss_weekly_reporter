"""
設定管理モジュール

このモジュールは、OSS Weekly Reporterの設定を一元管理するためのクラスを提供します。
設定は以下の優先順位で読み込まれます：
1. コマンドライン引数
2. 環境変数
3. 設定ファイル
4. デフォルト値
"""

import os
import yaml
from pathlib import Path
from typing import Dict, List, Any, Optional, Union, TypedDict, cast


class OutputConfig(TypedDict, total=False):
    """出力設定の型定義"""
    default_dir: str
    timezone: str


class SlackConfig(TypedDict, total=False):
    """Slack設定の型定義"""
    token: str
    skip_channels: List[str]
    auto_join: bool


class GitHubConfig(TypedDict, total=False):
    """GitHub設定の型定義"""
    repos: List[str]


class OpenAIConfig(TypedDict, total=False):
    """OpenAI設定の型定義"""
    api_key: str
    model: str
    temperature: float


class ConfigDict(TypedDict, total=False):
    """設定辞書の型定義"""
    output: OutputConfig
    slack: SlackConfig
    github: GitHubConfig
    openai: OpenAIConfig
    skip_channels: List[str]  # 後方互換性のため
    auto_join: bool  # 後方互換性のため


class Config:
    """設定管理クラス"""

    def __init__(
        self,
        config_file: Optional[str] = None,
        env_prefix: str = "OSS_WEEKLY_REPORTER_",
        cli_args: Optional[Dict[str, Any]] = None
    ):
        """
        初期化

        Args:
            config_file: 設定ファイルのパス
            env_prefix: 環境変数のプレフィックス
            cli_args: コマンドライン引数
        """
        self._default_config = self._get_default_config()
        self._file_config = self._load_config_file(config_file)
        self._env_config = self._load_env_config(env_prefix)
        self._cli_config = cli_args or {}

        self._config = self._merge_configs()

        self._handle_backward_compatibility()

    def _get_default_config(self) -> ConfigDict:
        """デフォルト設定を取得"""
        return {
            "output": {
                "default_dir": "./data",
                "timezone": "UTC"
            },
            "slack": {
                "auto_join": True,
                "skip_channels": []
            },
            "github": {
                "repos": []
            },
            "openai": {
                "model": "o1",
                "temperature": 0.7
            }
        }

    def _load_config_file(self, config_file: Optional[str] = None) -> ConfigDict:
        """設定ファイルを読み込む"""
        if config_file and Path(config_file).exists():
            config_path = Path(config_file)
        else:
            config_paths = [
                Path("config.yaml"),  # カレントディレクトリ
                Path(__file__).parent.parent / "config.yaml",  # リポジトリルート
            ]
            
            config_path = None
            for path in config_paths:
                if path.exists():
                    config_path = path
                    break
        
        if config_path:
            try:
                with open(config_path, "r", encoding="utf-8") as f:
                    config = yaml.safe_load(f)
                print(f"設定ファイルを読み込みました: {config_path}")
                return cast(ConfigDict, config or {})
            except Exception as e:
                print(f"設定ファイルの読み込みに失敗しました: {e}")
        
        print("設定ファイルが見つからないか、読み込めませんでした。デフォルト設定を使用します。")
        return {}

    def _load_env_config(self, prefix: str) -> ConfigDict:
        """環境変数から設定を読み込む"""
        env_config: ConfigDict = {
            "output": {},
            "slack": {},
            "github": {},
            "openai": {}
        }
        
        if os.environ.get(f"{prefix}OUTPUT_DIR"):
            env_config["output"]["default_dir"] = os.environ[f"{prefix}OUTPUT_DIR"]
        
        if os.environ.get(f"{prefix}TIMEZONE"):
            env_config["output"]["timezone"] = os.environ[f"{prefix}TIMEZONE"]
        
        if os.environ.get("SLACK_TOKEN"):
            env_config["slack"]["token"] = os.environ["SLACK_TOKEN"]
        
        if os.environ.get(f"{prefix}SKIP_CHANNELS"):
            env_config["slack"]["skip_channels"] = os.environ[f"{prefix}SKIP_CHANNELS"].split(",")
        
        if os.environ.get(f"{prefix}AUTO_JOIN") is not None:
            env_config["slack"]["auto_join"] = os.environ[f"{prefix}AUTO_JOIN"].lower() in ("true", "1", "yes")
        
        if os.environ.get(f"{prefix}GITHUB_REPOS"):
            env_config["github"]["repos"] = os.environ[f"{prefix}GITHUB_REPOS"].split(",")
        
        if os.environ.get("OPENAI_API_KEY"):
            env_config["openai"]["api_key"] = os.environ["OPENAI_API_KEY"]
        
        if os.environ.get(f"{prefix}OPENAI_MODEL"):
            env_config["openai"]["model"] = os.environ[f"{prefix}OPENAI_MODEL"]
        
        if os.environ.get(f"{prefix}OPENAI_TEMPERATURE"):
            try:
                env_config["openai"]["temperature"] = float(os.environ[f"{prefix}OPENAI_TEMPERATURE"])
            except ValueError:
                pass
        
        return env_config

    def _merge_configs(self) -> ConfigDict:
        """設定をマージする（優先順位: CLI > 環境変数 > 設定ファイル > デフォルト）"""
        result: ConfigDict = {}
        
        for section, values in self._default_config.items():
            if isinstance(values, dict):
                result[section] = values.copy()
            else:
                result[section] = values
        
        for section, values in self._file_config.items():
            if section not in result:
                result[section] = {}
            
            if isinstance(values, dict) and isinstance(result[section], dict):
                result[section].update(values)
            else:
                result[section] = values
        
        for section, values in self._env_config.items():
            if section not in result:
                result[section] = {}
            
            if isinstance(values, dict) and isinstance(result[section], dict):
                result[section].update(values)
            else:
                result[section] = values
        
        for key, value in self._cli_config.items():
            if value is not None:  # Noneの場合は上書きしない
                parts = key.split(".")
                
                if len(parts) == 1:
                    result[key] = value
                elif len(parts) == 2:
                    section, option = parts
                    if section not in result:
                        result[section] = {}
                    
                    if isinstance(result[section], dict):
                        result[section][option] = value
        
        return result

    def _handle_backward_compatibility(self) -> None:
        """後方互換性のための処理"""
        if "skip_channels" in self._config:
            if "slack" not in self._config:
                self._config["slack"] = {}
            self._config["slack"]["skip_channels"] = self._config["skip_channels"]
        
        if "auto_join" in self._config:
            if "slack" not in self._config:
                self._config["slack"] = {}
            self._config["slack"]["auto_join"] = self._config["auto_join"]

    def get(self, key: str, default: Any = None) -> Any:
        """
        設定値を取得

        Args:
            key: 設定キー（例: "slack.token", "output.default_dir"）
            default: デフォルト値

        Returns:
            設定値
        """
        parts = key.split(".")
        
        if len(parts) == 1:
            return self._config.get(key, default)
        elif len(parts) == 2:
            section, option = parts
            section_config = self._config.get(section, {})
            
            if isinstance(section_config, dict):
                return section_config.get(option, default)
        
        return default

    def get_all(self) -> ConfigDict:
        """すべての設定を取得"""
        return self._config.copy()

    def get_section(self, section: str) -> Dict[str, Any]:
        """セクションの設定を取得"""
        return self._config.get(section, {}).copy()

    def update(self, key: str, value: Any) -> None:
        """
        設定値を更新

        Args:
            key: 設定キー（例: "slack.token", "output.default_dir"）
            value: 設定値
        """
        parts = key.split(".")
        
        if len(parts) == 1:
            self._config[key] = value
        elif len(parts) == 2:
            section, option = parts
            if section not in self._config:
                self._config[section] = {}
            
            if isinstance(self._config[section], dict):
                self._config[section][option] = value
