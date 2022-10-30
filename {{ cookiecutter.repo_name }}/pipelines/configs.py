from pathlib import Path
import dbutils

PIPELINE_ROOT = Path(__file__).resolve()
REPO_ROOT = PIPELINE_ROOT.parents[1]
USER_ROOT = REPO_ROOT.parents[1]
WORKSPACE_ROOT = USER_ROOT.parents[1]

DBRICKS_TOKEN = dbutils.secrets.get(scope="scope", key="key")