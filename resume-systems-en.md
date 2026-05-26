# Matheus Alves
**Systems & Low-Level Software Developer | C++ · Go · Graphics**

📧 matheus2ep@gmail.com
🔗 [linkedin.com/in/matheus-alves-dev](https://www.linkedin.com/in/matheus-alves-dev/)
🐙 [github.com/matpdev](https://github.com/matpdev)

---

## Summary

Software developer and Computer Science student specializing in systems programming, real-time graphics, and performance-critical software. Proficient in modern C++ (C++20/23), Go, and Vulkan 1.3. Experienced building game engines, CLI tooling, desktop applications with serial/hardware communication, and graphics pipelines from scratch. Strong focus on clean architecture, deterministic memory management, and developer tooling.

---

## Education

**B.Sc. Computer Science** — *In Progress (4th Semester)*

---

## Languages

- **Portuguese** — Native
- **English** — Professional Working Proficiency

---

## Technical Skills

### Languages
`C++ (C++20/23)` `Go` `Python` `QML`

### Graphics & Low-Level
`Vulkan 1.3` `OpenGL` `GLSL` `SPIR-V` `VMA (Vulkan Memory Allocator)` `vk-bootstrap` `SDL2`

### Systems & Tooling
`CMake (3.20+)` `vcpkg` `FetchContent` `Clangd LSP` `Clang-Format` `AddressSanitizer` `Homebrew`

### Desktop & Embedded
`Qt / QML` `Serial / UART` `TCP / Socket bridging` `Bluetooth / ESP32`

### DevOps
`Docker` `GitHub Actions`

---

## Professional Experience

### Software Developer — **Monaco.gg** *(Remote)*

- Built high-performance web gameroom supporting multiple mini-games (Runner, ShootEmUp, StackJump, Guess, Magus, Touch)
- Resolved critical production bugs: HTTPS redirect behind AWS ALB via `X-Forwarded-Proto`, `AudioBufferSourceNode` crashes on Android WebView, premature BLOCKED sessions
- Implemented a structured client-side logging pipeline with a defined database schema (`clientLogger`)
- Configured `readPreference: primaryPreferred` on MongoDB for read performance optimization
- Integrated `gameInstanceToken` across multiple game screens
- **Stack:** TypeScript, Next.js, Node.js, MongoDB, AWS

---

## Projects

### [cpp-gen](https://github.com/matpdev/cpp-gen) — C++ Project Scaffolding CLI
> *A modern CLI written in Go that scaffolds fully-configured C++ projects in seconds*

- Generates hierarchical CMake (3.20+) project structures via an interactive TUI in seconds
- Integrates package managers (vcpkg / FetchContent) and configures IDE environments (VS Code, CLion, Neovim)
- Automatically wires up Clangd LSP, Clang-Format, AddressSanitizer, and Git
- Includes a specialized Vulkan template with shader support, `vklib`, and vcpkg integration
- Distributed via **Homebrew** through [`matpdev/homebrew-tap`](https://github.com/matpdev/homebrew-tap)
- **Go**

---

### [fps-vulkan](https://github.com/matpdev/fps-vulkan) — FPS Game with Vulkan 1.3
> *FPS game built with Vulkan 1.3, using vk-bootstrap, VMA, SDL2 and dynamic rendering*

- Full FPS engine built from scratch with Vulkan 1.3 dynamic rendering, VMA, and SDL2
- **C++, Vulkan 1.3, CMake**

---

### [vulkan-template](https://github.com/matpdev/vulkan-template) / [Vulkan-first-hexagon](https://github.com/matpdev/Vulkan-first-hexagon) — Vulkan Engine Studies
- RAII wrapper library (`vklib`) for Vulkan with engine helpers for memory, pipelines, descriptors, and shader loading
- Uniform Buffer Objects (UBO) with full MVP transformation matrices and per-frame animation
- Texture loading via `stb_image` with staging buffers, layout transitions, and anisotropic sampling
- Indexed rendering with `vkCmdDrawIndexed`
- **C++, Vulkan 1.3, GLSL/SPIR-V**

---

### [detmag1](https://github.com/matpdev/detmag1) — Qt/QML Desktop App with Serial Communication
- Desktop C++/QML application with dependency injection via a centralized `ServiceContainer`
- Serial/UART communication bridged to TCP/Socket with device configuration mode
- Real-time diagnostics with `DiagnosticStats`, QtCharts graphs, and structured logging
- CMake + vcpkg build with parallel compilation presets
- **C++, QML, CMake**

---

### [0xDEADC0DE](https://github.com/matpdev/0xDEADC0DE) — Text-Based RPG with OpenGL
> *A modern text-based RPG with stunning OpenGL-powered text animations*

- Command-line RPG with text visual effects rendered via OpenGL
- **C++, OpenGL**

---

### [bluetooth-esp32](https://github.com/matpdev/bluetooth-esp32) — Embedded Bluetooth Communication
- Bluetooth communication bridge with ESP32 microcontroller
- **C++ (Embedded)**

---

### [StrafficSimulator](https://github.com/matpdev/StrafficSimulator) — Traffic Simulator
- Traffic simulation system in C++
- **C++**

---

### Algorithms & Graphics Demos

| Project | Description |
|---|---|
| [a-star-cpp](https://github.com/matpdev/a-star-cpp) | A* pathfinding implementation in C++ |
| [doom-fire-algorithm-cpp](https://github.com/matpdev/doom-fire-algorithm-cpp) | Doom fire effect algorithm |
| [pixel-trail-cpp](https://github.com/matpdev/pixel-trail-cpp) | Pixel trail visual effect |

---

### C++ Game Projects

| Project | Description |
|---|---|
| [cpp-game-engine](https://github.com/matpdev/cpp-game-engine) | Custom game engine in C++ |
| [brick-game](https://github.com/matpdev/brick-game) | Breakout-style game |
| [kart-game](https://github.com/matpdev/kart-game) | Kart racing game |
| [survive-game](https://github.com/matpdev/survive-game) | Survival game |
| [the-impale-game](https://github.com/matpdev/the-impale-game) | Action game |
| [kill-them](https://github.com/matpdev/kill-them) | Top-down action game |
| [wordle-game](https://github.com/matpdev/wordle-game) | Wordle clone |

---

*Last updated: May 2026*
