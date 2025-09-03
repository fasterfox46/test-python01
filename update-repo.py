from dulwich.repo import Repo
from dulwich.client import get_transport_and_path
from dulwich import index

def refresh_repo(repo_path: str, remote_url: str = None):
    print(f"🔄 Refreshing repo at: {repo_path}")
    repo = Repo(repo_path)

    # Use remote from config if not provided
    if remote_url is None:
        remote_url = repo.get_config_stack().get((b'remote "origin"', b'url')).decode()

    # Fetch updates from remote
    client, remote_path = get_transport_and_path(remote_url)
    fetch_result = client.fetch(remote_path, repo)

    # Detect default branch from HEAD or fallback to 'main'
    ref_candidates = [
        b'refs/heads/main',
        b'refs/heads/master',
        b'refs/remotes/origin/main',
        b'refs/remotes/origin/master',
        b'HEAD'
    ]

    latest_commit = None
    for ref in ref_candidates:
        if ref in fetch_result.refs:
            latest_commit = fetch_result.refs[ref]
            print(f"📌 Found latest commit from ref: {ref.decode()}")
            break

    if not latest_commit:
        raise ValueError("❌ Could not resolve latest commit from remote refs.")

    # Rebuild working tree from latest commit
    tree = repo[latest_commit].tree
    index.build_index_from_tree(repo.path, repo.index_path(), repo.object_store, tree)

    print(f"✅ Repo refreshed to commit: {latest_commit.decode('utf-8', 'ignore')}")

# Example usage
if __name__ == "__main__":
    refresh_repo("/usr/local/projects/myrepo")
