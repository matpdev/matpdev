# Matheus Alves
**Software Developer**

📧 matheus2ep@gmail.com
🔗 [linkedin.com/in/matheus-alves-dev](https://www.linkedin.com/in/matheus-alves-dev/)
🐙 [github.com/matpdev](https://github.com/matpdev)

---

## Sobre

Desenvolvedor de software cursando Ciência da Computação com sólida experiência em C++ moderno, desenvolvimento de jogos, gráficos em tempo real com Vulkan e OpenGL, desenvolvimento mobile com Flutter e Kotlin, e backends em C#, Go e Node.js. Experiência profissional comprovada em ambientes de produção, com histórico de resolução de bugs críticos, implementação de sistemas de logging e otimização de performance. Comprometido com código limpo, arquitetura bem definida e ferramentas que aceleram o desenvolvimento.

---

## Formação

**Ciência da Computação** — *Cursando 4º Semestre*

---

## Idiomas

- **Português** — Nativo
- **Inglês** — Avançado Profissional

---

## Habilidades Técnicas

### Linguagens
`C++ (C++20/23)` `Go` `C#` `Dart` `Kotlin` `Swift` `TypeScript` `JavaScript` `QML` `Python` `Ruby`

### Gráficos & Baixo Nível
`Vulkan 1.3` `OpenGL` `GLSL` `SPIR-V` `VMA` `vk-bootstrap` `SDL2`

### Frameworks & Bibliotecas
`Qt / QML` `ASP.NET Core` `Flutter` `Next.js` `Svelte` `Node.js` `Dio`

### Backend & Banco de Dados
`Go (net/http)` `ASP.NET Core` `MongoDB` `PostgreSQL`

### Mobile
`Flutter (Android/iOS)` `Kotlin (Android nativo)` `Swift (iOS/macOS)`

### Build & Ferramentas
`CMake (3.20+)` `vcpkg` `FetchContent` `Clangd LSP` `Clang-Format` `AddressSanitizer` `Homebrew`

### DevOps & Infra
`AWS ALB` `Docker` `GitHub Actions` `HTTPS/Redirects`

### Embedded & Protocolos
`Bluetooth / ESP32` `Serial / UART` `TCP / Socket bridging`

---

## Experiência Profissional

### Software Developer — **Monaco.gg** *(Remoto)*

> Repositórios: `monaco-gg/poseidon-gameroom` · `monaco-gg/vivo-embed-gameroom`

- Desenvolvimento de gameroom web de alta performance com múltiplos mini-games (Runner, ShootEmUp, StackJump, Guess, Magus, Touch)
- Implementação de sistema de logging client-side com pipeline estruturado e schema de banco de dados (`clientLogger`)
- Resolução de bugs críticos de produção: HTTPS redirect atrás de AWS ALB via `X-Forwarded-Proto`, erros de `AudioBufferSourceNode` em Android WebView e sessões BLOCKED prematuras
- Integração de sistema de `gameInstanceToken` em múltiplas telas de jogo
- Desenvolvimento de modal de erro de anúncio com mapeamento de mensagens de API, geração de códigos de suporte copiáveis e tratamento de falhas de reward
- Configuração de `readPreference: primaryPreferred` no MongoDB para otimização de leitura primária
- **Stack:** TypeScript, Next.js, Node.js, MongoDB, AWS

---

## Projetos

### [cpp-gen](https://github.com/matpdev/cpp-gen) — CLI Tool para scaffolding de projetos C++
> *A modern CLI tool written in Go that scaffolds fully-configured C++ projects in seconds*

- Gera projetos C++ com estrutura CMake hierárquica (3.20+) em segundos via CLI interativa (TUI)
- Integra gerenciadores de pacotes (vcpkg / FetchContent) e configura ambientes de IDE (VS Code, CLion, Neovim)
- Wires up Clangd LSP, Clang-Format, AddressSanitizer e Git automaticamente
- Suporte a templates especializados (incluindo template Vulkan com shaders, vklib e vcpkg)
- Disponível via **Homebrew** através do tap [`matpdev/homebrew-tap`](https://github.com/matpdev/homebrew-tap)
- **Go**

---

### [detmag1](https://github.com/matpdev/detmag1) — Aplicação Desktop Qt/QML com comunicação Serial
- Interface desktop C++/QML com injeção de dependência via `ServiceContainer` centralizado
- Comunicação Serial/UART com bridge para TCP/Socket e modo de configuração de dispositivo
- Diagnósticos em tempo real com `DiagnosticStats`, gráficos via QtCharts e logging estruturado
- Build com CMake + vcpkg e presets configurados para compilação paralela
- **C++, QML, CMake**

---

### [fps-vulkan](https://github.com/matpdev/fps-vulkan) — FPS com Vulkan 1.3
> *FPS game built with Vulkan 1.3, using vk-bootstrap, VMA, SDL2 and dynamic rendering*

- Engine FPS desenvolvido do zero com Vulkan 1.3, dynamic rendering, VMA e SDL2
- **C++, Vulkan, CMake**

---

### [vulkan-template](https://github.com/matpdev/vulkan-template) / [Vulkan-first-hexagon](https://github.com/matpdev/Vulkan-first-hexagon) — Estudos Vulkan
- Biblioteca wrapper RAII para Vulkan (`vklib`) com helpers de engine, memória, pipeline, descritores e shader loader
- Uniform Buffer Objects (UBO) com transformações MVP (model/view/proj) e animação por frame
- Carregamento de texturas via `stb_image` com staging buffer, transição de layout e sampler com anisotropia
- Renderização de hexágono indexada com `vkCmdDrawIndexed`
- **C++, Vulkan 1.3, GLSL/SPIR-V**

---

### [0xDEADC0DE](https://github.com/matpdev/0xDEADC0DE) — RPG Text-Based com OpenGL
> *A modern text-based RPG with stunning OpenGL-powered text animations*

- RPG de linha de comando com efeitos visuais de texto renderizados via OpenGL
- **C++, OpenGL**

---

### [resonance](https://github.com/matpdev/resonance) — HTTP Client multiplataforma
> *A high-performance, cross-platform HTTP client and request builder for developers*

- Alternativa ao Postman, cross-platform, focada em performance e experiência do desenvolvedor
- **Dart, Flutter, Dio**

---

### [TechWire](https://github.com/matpdev/TechWire) — RSS Reader nativo para macOS
> *Lightweight, high-performance RSS reader for macOS built natively in Swift*

- UI minimalista com sincronização rápida, voltado para desenvolvedores e entusiastas de tecnologia
- **Swift, macOS**

---

### [Tasknap](https://github.com/matpdev/Tasknap-backend) — App de tarefas Full-Stack
- Backend REST em **C# / ASP.NET Core** com app Android nativo em **Kotlin**

---

### Aplicativos Mobile (Flutter/Dart)
| Projeto | Descrição |
|---|---|
| [carlog_app](https://github.com/matpdev/carlog_app) | App de registro de veículos |
| [Runking-App](https://github.com/matpdev/Runking-App) | App de ranking/corrida |
| [Tremor-Checker](https://github.com/matpdev/Tremor-Checker) | App de checagem de tremores |

---

### Games em C++
| Projeto | Descrição |
|---|---|
| [cpp-game-engine](https://github.com/matpdev/cpp-game-engine) | Motor de jogos próprio em C++ |
| [brick-game](https://github.com/matpdev/brick-game) | Jogo estilo Breakout |
| [kart-game](https://github.com/matpdev/kart-game) | Jogo de kart |
| [survive-game](https://github.com/matpdev/survive-game) | Jogo de sobrevivência |
| [the-impale-game](https://github.com/matpdev/the-impale-game) | Jogo de ação |
| [kill-them](https://github.com/matpdev/kill-them) | Jogo de ação top-down |
| [wordle-game](https://github.com/matpdev/wordle-game) | Clone do Wordle |
| [doom-fire-algorithm-cpp](https://github.com/matpdev/doom-fire-algorithm-cpp) | Algoritmo de fogo do Doom |
| [a-star-cpp](https://github.com/matpdev/a-star-cpp) | Pathfinding A* em C++ |
| [pixel-trail-cpp](https://github.com/matpdev/pixel-trail-cpp) | Efeito visual de rastro de pixels |

---

### Outros Projetos
- [bluetooth-esp32](https://github.com/matpdev/bluetooth-esp32) — Comunicação Bluetooth com ESP32 (**C++ embedded**)
- [StrafficSimulator](https://github.com/matpdev/StrafficSimulator) — Simulador de tráfego (**C++**)
- [Caos-frontend](https://github.com/matpdev/Caos-frontend) — Frontend em **Svelte**
- [Hugin-backend](https://github.com/matpdev/Hugin-backend) — Backend em **Go**
- [lumi-backend](https://github.com/matpdev/lumi-backend) — Backend em **C#**
- [cpp-starter-project](https://github.com/matpdev/cpp-starter-project) — Starter template C++ com CMake

---

*Última atualização: Abril 2026*
