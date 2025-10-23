# System Monitor

Lightweight interactive system-reporting script (system_monitor.py). Collects simple CPU/disk metrics, stores per-day reports under `reports/`, and provides an interactive menu to generate, view and list reports.

## Features
- Interactive CLI menu:
  - Monitor system (placeholder)
  - Generate a text report for a date
  - List report files (cross-platform)
  - Display in-memory reports
- Stores reports under `reports/<YYYY-MM-DD>/system_report.txt`
- Simple, human-readable report format

## Requirements
- Python 3.7+
- No external packages (uses standard library)

## Quick start (Windows)
1. Open PowerShell or cmd.
2. Run:
   ```powershell
   python c:\Users\DELL\system_monitor.py
   ```
3. Use the interactive menu:
   - `1` — Monitor System (calls monitor_system(); currently a placeholder)
   - `2` — Generate Report (writes `reports/<date>/system_report.txt`)
   - `3` — List Reports (prints directory listing)
   - `4` — View Reports (prints in-memory report objects)
   - `5` — Exit

## Report location & format
- Directory: `reports/<YYYY-MM-DD>/system_report.txt`
- Contents include:
  - Header with date
  - Total reports (count of in-memory report objects)
  - Each stored Report line (uses Report.__str__)
  - Average metrics snapshot

## Notes & recommended improvements
- monitor_system() is referenced but not implemented; implement sampling for CPU/disk and push Report instances into `self.reports`.
- Current `list_reports` used a shell `dir` call — updated to a safe `os.walk` approach in diagnostics recommendations to be cross-platform and avoid shell injection.
- `generate_report` had a hard-coded default date; prefer `datetime.date.today().isoformat()` when not provided.
- Consider persisting JSON or CSV for easier machine processing and add unit tests.
- For production use, avoid `shell=True` in subprocess calls and validate user input.

## Development
- Add metric collection (psutil recommended) for accurate CPU/disk stats:
  ```
  pip install psutil
  ```
- Add tests around file creation, listing, and report formatting.

## License
MIT — adapt as needed.
