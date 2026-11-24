<div align="center">
  <img src="./assets/bridges-header.svg" alt="Bridges Chiral Network Terminal — Matheus Alves (@matpdev)" width="100%" />

  <br />

  [![Sidequest Lab](https://img.shields.io/badge/SIDEQUESTLAB.DEV-0B0E11?style=flat-square&logo=astro&logoColor=00D8FF&labelColor=0B0E11&color=00D8FF)](https://sidequestlab.dev)
  [![Resume](https://img.shields.io/badge/PORTER_DOSSIER-RESUME.MD-0B0E11?style=flat-square&logo=read-the-docs&logoColor=D4AF37&labelColor=0B0E11&color=D4AF37)](./resume.md)
  [![LinkedIn](https://img.shields.io/badge/LINKEDIN-MATHEUS--ALVES--DEV-0B0E11?style=flat-square&logo=linkedin&logoColor=00D8FF&labelColor=0B0E11&color=1E2D3D)](https://www.linkedin.com/in/matheus-alves-dev/)
  [![Email](https://img.shields.io/badge/COMMS-MATHEUS2EP%40GMAIL.COM-0B0E11?style=flat-square&logo=gmail&logoColor=D4AF37&labelColor=0B0E11&color=1E2D3D)](mailto:matheus2ep@gmail.com)
</div>

<br />

```text
> CONNECTING TO UCA NODE: BR-NE // MACAÍBA
> AUTHENTICATING CUFF LINK... [OK]
> ROLE: SYSTEMS & BACKEND ENGINEER  |  PRODUCT BUILDER
> MISSION: CONNECTING SILICON, CONCURRENT SYSTEMS & PRODUCTION CLOUD
```

I build **low-level, high-throughput, and resilient software** — from static PS2 recompilation and **Vulkan / C++23** engines to **Rust / Go / .NET** distributed backends, embedded **TCP/UDP** telemetry pipelines, and local-first **Flutter / SwiftUI / Kotlin** apps.

<div align="center">
  <img src="./assets/chiral-divider.svg" alt="Chiral Divider" width="100%" />
</div>

## `// CHIRAL NETWORK TOPOLOGY`

```mermaid
flowchart LR
    HW["HARDWARE & EMBEDDED\nSTM32 · ESP32 · MIPS · Serial"] -->|"TCP/UDP · FFI"| SYS["SYSTEMS & GRAPHICS\nC++23 · Rust · Vulkan · Boost.ASIO"]
    SYS -->|"Queues · gRPC"| CLOUD["BACKEND & CLOUD\nGo · .NET 8 · AWS SQS/ECS · MongoDB · PG"]
    CLOUD -->|"APIs · Offline Sync"| CLIENT["CLIENT & DEV TOOLING\nFlutter · SwiftUI · Kotlin · Next.js · LSP/CLI"]

    style HW fill:#0D1218,stroke:#D4AF37,color:#E6EDF3,stroke-width:1.5px
    style SYS fill:#0D1218,stroke:#00D8FF,color:#E6EDF3,stroke-width:1.5px
    style CLOUD fill:#0D1218,stroke:#00D8FF,color:#E6EDF3,stroke-width:1.5px
    style CLIENT fill:#0D1218,stroke:#D4AF37,color:#E6EDF3,stroke-width:1.5px
```

<div align="center">
  <img src="./assets/chiral-divider.svg" alt="Chiral Divider" width="100%" />
</div>

## `// CARGO MANIFEST — PERSONAL & OPEN SOURCE`

<table>
  <tr>
    <td width="50%" valign="top">
      <h3><code>[RECOMP]</code> <a href="https://github.com/matpdev/SaintSeiyaRecomp">SaintSeiyaRecomp</a></h3>
      <p><strong>Native PC port &amp; static recompilation of Saint Seiya: The Hades (PS2)</strong></p>
      <p>Translates all <strong>13,855 MIPS R5900 functions</strong> to native C for Linux &amp; Windows, paired with a custom <strong>Vulkan</strong> renderer and an emulated <strong>SPU2</strong> running the original audio driver.</p>
      <p><code>C</code> · <code>Python</code> · <code>Vulkan</code> · <code>MIPS</code></p>
    </td>
    <td width="50%" valign="top">
      <h3><code>[AI-LAW]</code> <a href="https://github.com/matpdev/tinstar">Tinstar</a></h3>
      <p><strong>The law in your repo — deterministic checks from plain-language rules</strong></p>
      <p>Compiles rules written in <code>AGENTS.md</code> / <code>CLAUDE.md</code> into fast checks that run <strong>without an LLM</strong> in the terminal, Zed/editor LSP, CI, and AI agent loops.</p>
      <p><code>Rust</code> · <code>ast-grep</code> · <code>LSP</code> · <code>MCP</code></p>
    </td>
  </tr>
  <tr>
    <td width="50%" valign="top">
      <h3><code>[CLI]</code> <a href="https://github.com/matpdev/cpp-gen">cpp-gen</a></h3>
      <p><strong>Modern C++ project scaffolder distributed via Homebrew &amp; AUR</strong></p>
      <p>Native Go CLI/TUI that generates CMake 3.20+ presets, <code>vcpkg</code> / <code>FetchContent</code>, Clangd LSP, AddressSanitizer, and Vulkan/IDE templates in seconds.</p>
      <p><code>Go</code> · <code>Cobra</code> · <code>CMake</code> · <code>Clangd</code></p>
    </td>
    <td width="50%" valign="top">
      <h3><code>[PHYSICS]</code> <a href="https://codeberg.org/l0gic_br4in/parking-simulator">Car Physics &amp; Parking Simulator</a></h3>
      <p><strong>Manual transmission &amp; tire dynamics simulation from scratch</strong></p>
      <p>Models an engine torque curve, slipping clutch, 5-speed gearbox + reverse, load transfer, and <strong>Pacejka tire physics</strong> with real-time telemetry.</p>
      <p><code>C++23</code> · <code>raylib</code> · <code>Dear ImGui</code> · <code>CMake</code></p>
    </td>
  </tr>
  <tr>
    <td width="50%" valign="top">
      <h3><code>[AIOPS]</code> SentinelAI</h3>
      <p><strong>Event-driven AIOps &amp; automated incident diagnosis copilot</strong></p>
      <p>Ingests production telemetry through <strong>AWS SQS + S3</strong> and <strong>PostgreSQL/Dapper</strong>, with PII sanitization, <code>Microsoft.Extensions.AI</code>, OpenTelemetry, Grafana, and Testcontainers + BDD.</p>
      <p><code>.NET</code> · <code>AWS SQS/S3</code> · <code>PostgreSQL</code> · <code>OpenTelemetry</code></p>
    </td>
    <td width="50%" valign="top">
      <h3><code>[PROTOCOL]</code> Foco (Mac + Guard)</h3>
      <p><strong>Cross-device focus ecosystem without root or lock-in</strong></p>
      <p>A <strong>SwiftUI</strong> macOS study/roadmap app paired with a <strong>Kotlin + Shizuku</strong> Android blocker communicating over a custom local-network protocol signed with <strong>HMAC + Bonjour</strong>.</p>
      <p><code>SwiftUI</code> · <code>Kotlin</code> · <code>Shizuku</code> · <code>HMAC</code></p>
    </td>
  </tr>
</table>

<details>
  <summary><strong><code>[+] OPEN SECONDARY CARGO LOG (MORE SIDEQUESTS &amp; LABS)</code></strong></summary>
  <br />
  <table>
    <tr>
      <th align="left">Codename</th>
      <th align="left">Mission Scope</th>
      <th align="left">Loadout</th>
    </tr>
    <tr>
      <td><strong>docs-lsp</strong></td>
      <td>Offline hover Language Server for Vulkan docs, cppreference, man pages, and GLSL qualifiers running alongside <code>clangd</code>.</td>
      <td><code>LSP</code> · <code>Vulkan</code> · <code>C++</code> · <code>GLSL</code></td>
    </tr>
    <tr>
      <td><strong>El Recrutador</strong></td>
      <td>Local-first job triage &amp; 1-page ATS CV generator using embedded Typst, DeepSeek JSON mode, and SQLite.</td>
      <td><code>Flutter</code> · <code>Rust FFI</code> · <code>Typst</code> · <code>SQLite</code></td>
    </tr>
    <tr>
      <td><strong>Conta Certa</strong></td>
      <td>100% offline shopping list with real-time calculator and spending cap powered by a Rust core.</td>
      <td><code>Flutter</code> · <code>Rust FFI</code> · <code>SQLite</code></td>
    </tr>
    <tr>
      <td><strong>Vulkan &amp; Game Labs</strong></td>
      <td>Experimental 2D/3D engines, dynamic rendering, VMA, RAII Vulkan wrappers (<code>vklib</code>), and ESP-IDF/PlatformIO hardware experiments.</td>
      <td><code>C++20/23</code> · <code>Vulkan 1.3</code> · <code>ESP32</code></td>
    </tr>
  </table>
</details>

<div align="center">
  <img src="./assets/chiral-divider.svg" alt="Chiral Divider" width="100%" />
</div>

## `// STRAND CONTRACTS — FIELD EXPERIENCE`

| Period | Contract | Role | Key Impact |
| :--- | :--- | :--- | :--- |
| **Aug 2025 — Present** | **Monaco.gg** | Software Engineer / Product Builder | Core backend &amp; real-time fraud detection for carrier-billed gaming platforms (Claro, Vivo, TIM); async **AWS SQS/SNS/ECS** queues and **MongoDB** replicas stable under traffic bursts (`Go`, `FastAPI`, `Next.js`, `SvelteKit`). |
| **2024 — Present** | **Techmobi Tecnologia** | Software Engineer (Contract) | Eliminated race conditions in weigh-in-motion (WIM) sensor diagnostics (**Qt6/C++20**, **Boost.ASIO**) reaching **100% field stability**; modeled **40+ domain entities** in **.NET 8 DDD/CQRS**; built **Rust + Tokio + Flutter FFI** hardware simulators &amp; relays. |
| **2023 — 2025** | **Runking** | Backend &amp; Mobile Engineer | Engineered an offline-first sync engine (**SQLite + Rust FFI**) and **WebRTC over UDP** telemetry streaming for **zero data loss** during live marathons. |
| **Feb 2022 — Aug 2025** | **Pinó** | Full Stack / Frontend Engineer | Led frontend architecture for enterprise portals and high-traffic apps (`React`, `Next.js`, `Vue`, `React Native`, `Flutter`) backed by Node.js APIs on AWS. |

<div align="center">
  <img src="./assets/chiral-divider.svg" alt="Chiral Divider" width="100%" />
</div>

## `// ODRADEK EQUIPMENT LOADOUT`

<details open>
  <summary><strong><code>[+] INSPECT FULL TECH ARSENAL</code></strong></summary>
  <br />

  - **Core Languages**: `C++ (20/23)` · `Rust` · `Go` · `C# (.NET 8)` · `TypeScript` · `Python` · `Kotlin` · `Swift` · `Dart` · `SQL`
  - **Systems, Graphics &amp; Embedded**: `Linux Systems` · `Vulkan 1.3 (VMA)` · `OpenGL` · `GLSL` · `Qt6` · `Boost.ASIO` · `POSIX Threads` · `TCP/UDP` · `WebRTC` · `STM32 / ESP32`
  - **Backend, Cloud &amp; Data**: `AWS (SQS, SNS, ECS, S3, ALB)` · `Docker` · `PostgreSQL` · `MongoDB` · `Redis` · `SQLite` · `OpenTelemetry` · `Grafana`
  - **Mobile, Web &amp; Tooling**: `Flutter (flutter_rust_bridge)` · `SwiftUI` · `Next.js` · `SvelteKit` · `CMake` · `LSP / MCP` · `GitHub Actions`

</details>

<div align="center">
  <img src="./assets/chiral-divider.svg" alt="Chiral Divider" width="100%" />
</div>

## `// CUFF LINK TELEMETRY`

<div align="center">
  <img src="./assets/porter-telemetry.svg" alt="Bridges Porter Telemetry" width="100%" />
  <br /><br />
  <sub>
    <code>"Keep on keeping on."</code> — Automated daily via <a href="./.github/workflows/update-telemetry.yml">GitHub Actions</a> · More engineering logs at <a href="https://sidequestlab.dev">sidequestlab.dev</a>
  </sub>
</div>
