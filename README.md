# termui

A keyboard-driven terminal UI for [termio](https://github.com/dcwestra/termio) — the POSIX SSH connection manager.

termui wraps the termio CLI in a visual interface built with [Textual](https://github.com/Textualize/textual), giving you a live alias list, detail panel, and quick access to every termio feature without leaving your terminal.

![Tokyo Night themed TUI with alias list, detail panel, and key hint bar](.github/screenshot.png)

---

## Requirements

- **[termio](https://github.com/dcwestra/termio)** installed at `/usr/local/bin/termio`
- Python 3.11+
- Textual 0.89+

---

## Install

```sh
pip install --user git+https://github.com/dcwestra/termui.git
termui
```

Or clone and install in editable mode for development:

```sh
git clone https://github.com/dcwestra/termui.git
pip install --user -e termui/
termui
```

---

## Features

| Screen | Key | Description |
|--------|-----|-------------|
| Home | *(default)* | Alias list with live ping, detail panel, all alias actions |
| SFTP | `f` | Dual-pane file browser (upload / download) |
| Add / Edit | `a` / `e` | Guided alias form |
| Tunnels | `t` | Named port-forward profiles — start / stop |
| Snippets | `s` | Reusable remote commands — run on alias or group |
| SSH Agent | `G` | Key list — add / remove / clear |
| Log | `l` | Connection history with alias filter |
| Backups | `b` | Config backup list + one-click restore |
| Templates | `m` | Saved alias templates |
| Bootstrap | `B` | Install / sync snippet widget (`Ctrl+X s`) on remote hosts |

### Home screen actions (right panel)

| Key | Action |
|-----|--------|
| `↵` | Connect |
| `P` | Connect with ephemeral profile |
| `f` | SFTP browser |
| `e` | Edit alias |
| `k` | Rotate SSH key |
| `p` | Pin / unpin |
| `n` | Rename |
| `C` | Clone |
| `g` | Add / remove group tag |
| `x` | Run one-off remote command |
| `w` | Wake-on-LAN |
| `B` | Snippet sync (bootstrap) |
| `D` | Delete |

---

## Design

- **Tokyo Night** colour palette throughout
- All mutations go through the `termio` CLI — termui never writes config files directly
- Blocking terminal ops (connect, SFTP, rotate) use `app.suspend()` so the TUI cleanly hands the terminal over and reclaims it on exit
- Read-only config parsing (aliases, tunnels, snippets, history) done directly in Python for speed

---

## License

MIT — see [LICENSE](LICENSE)
