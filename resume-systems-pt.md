# Matheus Alves
**Desenvolvedor de Software — Sistemas & Baixo Nível | C++ · Go · Gráficos**

📧 matheus2ep@gmail.com
🔗 [linkedin.com/in/matheus-alves-dev](https://www.linkedin.com/in/matheus-alves-dev/)
🐙 [github.com/matpdev](https://github.com/matpdev)

---

## Sobre

Desenvolvedor de software cursando Ciência da Computação, especializado em programação de sistemas, gráficos em tempo real e software crítico em performance. Proficiente em C++ moderno (C++20/23), Go e Vulkan 1.3. Experiente na construção de game engines, ferramentas CLI, aplicações desktop com comunicação serial/hardware e pipelines gráficos do zero. Foco em arquitetura limpa, gerenciamento determinístico de memória e ferramentas de desenvolvimento.

---

## Formação

**Bacharelado em Ciência da Computação** — *Cursando 4º Semestre*

---

## Idiomas

- **Português** — Nativo
- **Inglês** — Avançado Profissional

---

## Habilidades Técnicas

### Linguagens
`C++ (C++20/23)` `Go` `Python` `QML`

### Gráficos & Baixo Nível
`Vulkan 1.3` `OpenGL` `GLSL` `SPIR-V` `VMA (Vulkan Memory Allocator)` `vk-bootstrap` `SDL2`

### Sistemas & Ferramentas
`CMake (3.20+)` `vcpkg` `FetchContent` `Clangd LSP` `Clang-Format` `AddressSanitizer` `Homebrew`

### Desktop & Embarcado
`Qt / QML` `Serial / UART` `Ponte TCP / Socket` `Bluetooth / ESP32`

### DevOps
`Docker` `GitHub Actions`

---

## Experiência Profissional

### Software Developer — **Monaco.gg** *(Remoto)*

- Desenvolvimento de gameroom web de alta performance com múltiplos mini-games (Runner, ShootEmUp, StackJump, Guess, Magus, Touch)
- Resolução de bugs críticos de produção: redirect HTTPS atrás de AWS ALB via `X-Forwarded-Proto`, crashes de `AudioBufferSourceNode` no Android WebView e sessões BLOCKED prematuras
- Implementação de pipeline de logging client-side estruturado com schema de banco de dados definido (`clientLogger`)
- Configuração de `readPreference: primaryPreferred` no MongoDB para otimização de leitura
- Integração de `gameInstanceToken` em múltiplas telas de jogo
- **Stack:** TypeScript, Next.js, Node.js, MongoDB, AWS

---

## Projetos

### [cpp-gen](https://github.com/matpdev/cpp-gen) — CLI de Scaffolding para Projetos C++
> *Ferramenta CLI moderna escrita em Go que cria projetos C++ totalmente configurados em segundos*

- Gera estruturas de projeto CMake hierárquicas (3.20+) via TUI interativa em segundos
- Integra gerenciadores de pacotes (vcpkg / FetchContent) e configura ambientes de IDE (VS Code, CLion, Neovim)
- Configura automaticamente Clangd LSP, Clang-Format, AddressSanitizer e Git
- Inclui template especializado para Vulkan com suporte a shaders, `vklib` e vcpkg
- Distribuído via **Homebrew** pelo tap [`matpdev/homebrew-tap`](https://github.com/matpdev/homebrew-tap)
- **Go**

---

### [fps-vulkan](https://github.com/matpdev/fps-vulkan) — FPS com Vulkan 1.3
> *Jogo FPS desenvolvido com Vulkan 1.3, usando vk-bootstrap, VMA, SDL2 e dynamic rendering*

- Engine FPS construída do zero com Vulkan 1.3 dynamic rendering, VMA e SDL2
- **C++, Vulkan 1.3, CMake**

---

### [vulkan-template](https://github.com/matpdev/vulkan-template) / [Vulkan-first-hexagon](https://github.com/matpdev/Vulkan-first-hexagon) — Estudos de Engine Vulkan
- Biblioteca wrapper RAII (`vklib`) para Vulkan com helpers de engine para memória, pipelines, descritores e carregamento de shaders
- Uniform Buffer Objects (UBO) com matrizes de transformação MVP completas e animação por frame
- Carregamento de texturas via `stb_image` com staging buffers, transições de layout e amostragem anisotrópica
- Renderização indexada com `vkCmdDrawIndexed`
- **C++, Vulkan 1.3, GLSL/SPIR-V**

---

### [detmag1](https://github.com/matpdev/detmag1) — Aplicação Desktop Qt/QML com Comunicação Serial
- Aplicação desktop C++/QML com injeção de dependência via `ServiceContainer` centralizado
- Comunicação Serial/UART com bridge para TCP/Socket e modo de configuração de dispositivo
- Diagnósticos em tempo real com `DiagnosticStats`, gráficos via QtCharts e logging estruturado
- Build com CMake + vcpkg e presets para compilação paralela
- **C++, QML, CMake**

---

### [0xDEADC0DE](https://github.com/matpdev/0xDEADC0DE) — RPG Text-Based com OpenGL
> *RPG de linha de comando moderno com efeitos visuais de texto via OpenGL*

- RPG de linha de comando com efeitos visuais de texto renderizados via OpenGL
- **C++, OpenGL**

---

### [bluetooth-esp32](https://github.com/matpdev/bluetooth-esp32) — Comunicação Bluetooth Embarcado
- Bridge de comunicação Bluetooth com microcontrolador ESP32
- **C++ (Embarcado)**

---

### [StrafficSimulator](https://github.com/matpdev/StrafficSimulator) — Simulador de Tráfego
- Sistema de simulação de tráfego em C++
- **C++**

---

### Algoritmos & Demos Gráficos

| Projeto | Descrição |
|---|---|
| [a-star-cpp](https://github.com/matpdev/a-star-cpp) | Implementação do algoritmo A* em C++ |
| [doom-fire-algorithm-cpp](https://github.com/matpdev/doom-fire-algorithm-cpp) | Algoritmo de fogo do Doom |
| [pixel-trail-cpp](https://github.com/matpdev/pixel-trail-cpp) | Efeito visual de rastro de pixels |

---

### Projetos de Jogos em C++

| Projeto | Descrição |
|---|---|
| [cpp-game-engine](https://github.com/matpdev/cpp-game-engine) | Motor de jogos próprio em C++ |
| [brick-game](https://github.com/matpdev/brick-game) | Jogo estilo Breakout |
| [kart-game](https://github.com/matpdev/kart-game) | Jogo de kart |
| [survive-game](https://github.com/matpdev/survive-game) | Jogo de sobrevivência |
| [the-impale-game](https://github.com/matpdev/the-impale-game) | Jogo de ação |
| [kill-them](https://github.com/matpdev/kill-them) | Jogo de ação top-down |
| [wordle-game](https://github.com/matpdev/wordle-game) | Clone do Wordle |

---

*Última atualização: Maio 2026*
