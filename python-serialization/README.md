# Python — Serialization

A deep dive into marshaling and serialization: how data is transformed, stored, and transmitted across systems and networks.

---

## Background

Modern applications constantly need to move data — between processes, across networks, into databases, and out of files. Two fundamental techniques make this possible:

**Marshaling** is the process of transforming in-memory objects into a portable format suitable for storage or transmission. It packages complex objects and their attributes into a simpler representation (often binary) so they can be reconstructed on another system or platform.

**Serialization** is closely related — it specifically converts data structures or object states into a format that can be saved to a file or sent over a network. The key goal is preserving object state so it can be recreated identically elsewhere. This is essential for data persistence, distributed computing, and inter-process communication.

While the two terms are often used interchangeably, marshaling typically implies transmitting across a network or between processes, whereas serialization focuses more broadly on any form of persistent representation.

---

## Learning Objectives

By the end of this project, you should be able to explain and demonstrate:

- The differences and similarities between marshaling and serialization
- How to implement serialization in a practical programming context
- How serialized data is used in web applications, databases, and network communication
- The performance trade-offs between serialization formats — JSON, XML, and binary

---

## Serialization Formats Covered

| Format | Use case | Python module |
|---|---|---|
| JSON | Human-readable data exchange, web APIs | `json` |
| CSV | Tabular data, spreadsheets, data pipelines | `csv` |
| XML | Structured documents, legacy systems | `xml.etree.ElementTree` |
| Binary (Pickle) | Python-native object persistence | `pickle` |

---

## Requirements

- Python 3.8.5 on Ubuntu 20.04 LTS
- First line of every file: `#!/usr/bin/python3`
- Code must follow `pycodestyle` (version 2.7.*)
- All files must be executable and end with a newline

---

## AUTHOR

- Ian Aviles - [GitHub](https://github.com/IanAvi15)