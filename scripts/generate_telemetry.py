#!/usr/bin/env python3
"""Generate Bridges Chiral Telemetry SVG card for @matpdev."""

from __future__ import annotations

import datetime
import json
import os
import sys
import urllib.error
import urllib.request
from pathlib import Path

USERNAME = os.environ.get("GITHUB_REPOSITORY_OWNER", "matpdev")
TOKEN = os.environ.get("GITHUB_TOKEN", "")
OUT_PATH = Path(__file__).resolve().parent.parent / "assets" / "porter-telemetry.svg"

DEFAULT_TELEMETRY = {
    "public_repos": 28,
    "stars": 140,
    "contributions_year": 850,
    "languages": [
        ("C++ / C", 34, "#00D8FF"),
        ("Rust", 24, "#D4AF37"),
        ("Go", 16, "#38BDF8"),
        ("C# / .NET", 14, "#F5B041"),
        ("TS / Dart / Swift", 12, "#8B949E"),
    ],
}

LANG_COLORS = {
    "C++": "#00D8FF",
    "C": "#00D8FF",
    "Rust": "#D4AF37",
    "Go": "#38BDF8",
    "C#": "#F5B041",
    "TypeScript": "#60A5FA",
    "Dart": "#2DD4BF",
    "Swift": "#FB923C",
    "Kotlin": "#A78BFA",
    "Python": "#FBBF24",
}


def github_get(url: str) -> object:
    headers = {
        "Accept": "application/vnd.github+json",
        "User-Agent": "bridges-telemetry-generator",
    }
    if TOKEN:
        headers["Authorization"] = f"Bearer {TOKEN}"
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req, timeout=15) as resp:
        return json.loads(resp.read().decode("utf-8"))


def github_graphql(query: str, variables: dict[str, object]) -> dict[str, object]:
    headers = {
        "Accept": "application/vnd.github+json",
        "Content-Type": "application/json",
        "User-Agent": "bridges-telemetry-generator",
    }
    if TOKEN:
        headers["Authorization"] = f"Bearer {TOKEN}"
    payload = json.dumps({"query": query, "variables": variables}).encode("utf-8")
    req = urllib.request.Request("https://api.github.com/graphql", data=payload, headers=headers)
    with urllib.request.urlopen(req, timeout=15) as resp:
        return json.loads(resp.read().decode("utf-8"))


def fetch_telemetry() -> dict[str, object]:
    user = github_get(f"https://api.github.com/users/{USERNAME}")
    repos = github_get(f"https://api.github.com/users/{USERNAME}/repos?per_page=100&type=owner")

    if not isinstance(user, dict) or not isinstance(repos, list):
        return DEFAULT_TELEMETRY

    non_fork_repos = [r for r in repos if not r.get("fork")]
    stars = sum(int(r.get("stargazers_count", 0)) for r in non_fork_repos)
    public_repos = int(user.get("public_repos", len(non_fork_repos)))

    lang_counts: dict[str, int] = {}
    for repo in non_fork_repos:
        lang = repo.get("language")
        if lang:
            lang_counts[lang] = lang_counts.get(lang, 0) + 1

    total_lang = sum(lang_counts.values()) or 1
    sorted_langs = sorted(lang_counts.items(), key=lambda item: item[1], reverse=True)[:5]
    languages = []
    used_pct = 0
    for idx, (name, count) in enumerate(sorted_langs):
        if idx == len(sorted_langs) - 1:
            pct = max(1, 100 - used_pct)
        else:
            pct = max(1, round((count / total_lang) * 100))
            used_pct += pct
        languages.append((name, pct, LANG_COLORS.get(name, "#8B949E")))

    contributions_year = DEFAULT_TELEMETRY["contributions_year"]
    if TOKEN:
        gql = """
        query($login: String!) {
          user(login: $login) {
            contributionsCollection {
              contributionCalendar {
                totalContributions
              }
            }
          }
        }
        """
        data = github_graphql(gql, {"login": USERNAME})
        try:
            contributions_year = int(
                data["data"]["user"]["contributionsCollection"]["contributionCalendar"]["totalContributions"]  # type: ignore[index]
            )
        except (KeyError, TypeError, ValueError):
            pass

    return {
        "public_repos": public_repos,
        "stars": stars,
        "contributions_year": contributions_year,
        "languages": languages or DEFAULT_TELEMETRY["languages"],
    }


def render_svg(data: dict[str, object]) -> str:
    now_utc = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    public_repos = int(data["public_repos"])  # type: ignore[arg-type]
    stars = int(data["stars"])  # type: ignore[arg-type]
    contributions = int(data["contributions_year"])  # type: ignore[arg-type]
    languages: list[tuple[str, int, str]] = data["languages"]  # type: ignore[assignment]

    lang_rows = []
    for idx, (name, pct, color) in enumerate(languages[:5]):
        y = 78 + idx * 26
        bar_w = max(8, round(290 * (pct / 100.0)))
        lang_rows.append(
            f'''  <g transform="translate(460, {y})">
    <text x="0" y="12" fill="#E6EDF3" font-family="'JetBrains Mono', Consolas, monospace" font-size="11">{name}</text>
    <rect x="135" y="3" width="240" height="8" rx="1" fill="#16202A"/>
    <rect x="135" y="3" width="{bar_w}" height="8" rx="1" fill="{color}">
      <animate attributeName="width" from="0" to="{bar_w}" dur="1.1s" fill="freeze"/>
    </rect>
    <text x="385" y="11" fill="#8B949E" font-family="'JetBrains Mono', Consolas, monospace" font-size="10.5">{pct}%</text>
  </g>'''
        )

    lang_block = "\n".join(lang_rows)

    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 220" width="900" height="220" role="img" aria-label="Bridges Porter Telemetry for {USERNAME}">
  <defs>
    <linearGradient id="tBg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#090C10"/>
      <stop offset="100%" stop-color="#0D1218"/>
    </linearGradient>
    <pattern id="tGrid" width="24" height="24" patternUnits="userSpaceOnUse">
      <path d="M 24 0 L 0 0 0 24" fill="none" stroke="#151E28" stroke-width="0.6"/>
    </pattern>
  </defs>

  <polygon points="14,4 886,4 896,14 896,206 886,216 14,216 4,206 4,14" fill="url(#tBg)" stroke="#1E2D3D" stroke-width="1.3"/>
  <polygon points="14,4 886,4 896,14 896,206 886,216 14,216 4,206 4,14" fill="url(#tGrid)" opacity="0.5"/>

  <polyline points="4,28 4,14 14,4 38,4" fill="none" stroke="#00D8FF" stroke-width="2"/>
  <polyline points="862,4 886,4 896,14 896,28" fill="none" stroke="#00D8FF" stroke-width="2"/>
  <polyline points="4,192 4,206 14,216 38,216" fill="none" stroke="#D4AF37" stroke-width="2"/>
  <polyline points="862,216 886,216 896,206 896,192" fill="none" stroke="#D4AF37" stroke-width="2"/>

  <!-- Header -->
  <text x="26" y="28" fill="#00D8FF" font-family="'JetBrains Mono', Consolas, monospace" font-size="11" font-weight="700" letter-spacing="1.8">
    CUFF LINK TELEMETRY // PORTER GRADE: S-RANK
  </text>
  <text x="874" y="28" text-anchor="end" fill="#6E7681" font-family="'JetBrains Mono', Consolas, monospace" font-size="10">
    SYNCED: {now_utc}
  </text>
  <line x1="24" y1="38" x2="876" y2="38" stroke="#1B2836" stroke-width="1"/>

  <!-- Left KPI Cards -->
  <g transform="translate(26, 56)">
    <rect x="0" y="0" width="126" height="68" fill="#0E141B" stroke="#1E2D3D" stroke-width="1"/>
    <text x="12" y="22" fill="#8B949E" font-family="'JetBrains Mono', Consolas, monospace" font-size="9.5" letter-spacing="1">DELIVERIES</text>
    <text x="12" y="50" fill="#F0F6FC" font-family="'JetBrains Mono', Consolas, monospace" font-size="24" font-weight="700">{public_repos}</text>
    <text x="86" y="50" fill="#00D8FF" font-family="'JetBrains Mono', Consolas, monospace" font-size="9.5">REPOS</text>

    <rect x="138" y="0" width="126" height="68" fill="#0E141B" stroke="#1E2D3D" stroke-width="1"/>
    <text x="150" y="22" fill="#8B949E" font-family="'JetBrains Mono', Consolas, monospace" font-size="9.5" letter-spacing="1">LIKES RECEIVED</text>
    <text x="150" y="50" fill="#D4AF37" font-family="'JetBrains Mono', Consolas, monospace" font-size="24" font-weight="700">{stars}</text>
    <text x="226" y="50" fill="#D4AF37" font-family="'JetBrains Mono', Consolas, monospace" font-size="9.5">STARS</text>

    <rect x="276" y="0" width="136" height="68" fill="#0E141B" stroke="#1E2D3D" stroke-width="1"/>
    <text x="288" y="22" fill="#8B949E" font-family="'JetBrains Mono', Consolas, monospace" font-size="9.5" letter-spacing="1">CHIRAL SIGNALS</text>
    <text x="288" y="50" fill="#00D8FF" font-family="'JetBrains Mono', Consolas, monospace" font-size="24" font-weight="700">{contributions}</text>
    <text x="366" y="50" fill="#8B949E" font-family="'JetBrains Mono', Consolas, monospace" font-size="9.5">/YR</text>
  </g>

  <!-- Left Footer Status -->
  <g transform="translate(26, 140)">
    <rect x="0" y="0" width="412" height="54" fill="#0E141B" stroke="#1E2D3D" stroke-width="1"/>
    <text x="14" y="21" fill="#8B949E" font-family="'JetBrains Mono', Consolas, monospace" font-size="10" letter-spacing="1.2">
      PRIMARY DOMAINS: <tspan fill="#E6EDF3">SYSTEMS · BACKEND · EMBEDDED · GRAPHICS</tspan>
    </text>
    <text x="14" y="40" fill="#8B949E" font-family="'JetBrains Mono', Consolas, monospace" font-size="10" letter-spacing="1.2">
      STRAND STATUS: <tspan fill="#00D8FF">CONNECTED</tspan>   //   <tspan fill="#D4AF37">KEEP ON KEEPING ON</tspan>
    </text>
  </g>

  <!-- Right Language Bandwidth -->
  <text x="460" y="64" fill="#8B949E" font-family="'JetBrains Mono', Consolas, monospace" font-size="10.5" letter-spacing="1.4">
    CHIRAL BANDWIDTH DISTRIBUTION
  </text>
{lang_block}
</svg>
'''


def main() -> int:
    try:
        data = fetch_telemetry()
    except (urllib.error.URLError, TimeoutError, json.JSONDecodeError) as exc:
        print(f"Network/API unavailable ({exc}); using baseline telemetry.", file=sys.stderr)
        data = DEFAULT_TELEMETRY

    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUT_PATH.write_text(render_svg(data), encoding="utf-8")
    print(f"Wrote {OUT_PATH}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
