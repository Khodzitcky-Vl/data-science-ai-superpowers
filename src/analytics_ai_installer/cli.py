from __future__ import annotations

import argparse
import os
import shutil
import subprocess
import sys

from analytics_ai_installer.bundles import BUNDLES


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="analytics-ai-installer",
        description="Install analytics skill bundles via Skilz",
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    install_parser = subparsers.add_parser("install", help="Install a named bundle")
    install_parser.add_argument("bundle", choices=sorted(BUNDLES))
    install_parser.add_argument("--agent", required=True, choices=["codex", "claude"])
    install_parser.add_argument("--project", action="store_true")
    install_parser.add_argument(
        "--repo",
        help="Skill repository in owner/repo format. Defaults to ANALYTICS_AI_SKILLS_REPO.",
    )

    subparsers.add_parser("list-bundles", help="List available bundles")

    list_skills_parser = subparsers.add_parser(
        "list-skills", help="List skills in a bundle"
    )
    list_skills_parser.add_argument("bundle", choices=sorted(BUNDLES))

    return parser


def resolve_skills_repo(repo: str | None) -> str:
    if repo:
        return repo

    repo_from_env = os.getenv("ANALYTICS_AI_SKILLS_REPO")
    if repo_from_env:
        return repo_from_env

    print(
        "Error: skill repository is not set. Pass --repo owner/repo or set ANALYTICS_AI_SKILLS_REPO.",
        file=sys.stderr,
    )
    raise SystemExit(1)


def require_skilz() -> None:
    if shutil.which("skilz") is None:
        print("Error: 'skilz' is not installed or not in PATH.", file=sys.stderr)
        print("Install it first: pip install skilz", file=sys.stderr)
        raise SystemExit(1)


def install_bundle(bundle: str, agent: str, project: bool, repo: str) -> int:
    require_skilz()

    git_url = f"https://github.com/{repo}"
    for skill in BUNDLES[bundle]:
        cmd = ["skilz", "-y", "install", "--git", git_url, "--skill", skill, "--agent", agent]
        if project:
            cmd.append("--project")

        print(f"Installing {skill} from {git_url}")
        result = subprocess.run(cmd)
        if result.returncode != 0:
            print(f"Failed to install {skill}", file=sys.stderr)
            return result.returncode

    print(f"Bundle '{bundle}' installed successfully for agent '{agent}'")
    return 0


def list_bundles() -> int:
    for bundle_name, skills in BUNDLES.items():
        print(f"{bundle_name}: {len(skills)} skills")
    return 0


def list_skills(bundle: str) -> int:
    for skill in BUNDLES[bundle]:
        print(skill)
    return 0


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()

    if args.command == "install":
        repo = resolve_skills_repo(args.repo)
        return install_bundle(args.bundle, args.agent, args.project, repo)
    if args.command == "list-bundles":
        return list_bundles()
    if args.command == "list-skills":
        return list_skills(args.bundle)

    parser.print_help()
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
