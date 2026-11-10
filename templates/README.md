# Template guide

These files are reusable scaffolds, not ISO 20022 reference content. Each template file has `template: true` and `review_status: template`. Its placeholders are scaffolding only. Populated references and their actual review status are reached through the [catalog](../catalog/README.md).

## Templates and destinations

| Template | Destination within its owning reference folder | Purpose |
| --- | --- | --- |
| [Message index](message-index.md) | `index.md` in a full-message-ID folder | Curated purpose, actors, usage, and navigation |
| [Message-set index](message-set-index.md) | `index.md` in a message-set edition folder | Shared roles, processes, models, and message membership |
| [Message structure](message-structure.md) | `structure.md` in a message folder | Roots, schema dependencies, ordering, and type navigation |
| [Schema type](schema-type.md) | `types/type-NNNN.md` in a message folder | Full definition of one named or anonymous schema type |
| [Rules](rules.md) | `rules.md` in a message or message-set folder | Source-grounded business rules and separate schema constraints |
| [Table](table.md) | `tables/tbl-NNNN.md` in a message or message-set folder | Complete table content and provenance |
| [Diagram](diagram.md) | `diagrams/fig-NNNN.md` in a message or message-set folder | Original evidence, Mermaid, and semantic explanation |
| [Diagram index](diagram-index.md) | `diagrams/index.md` in a message or message-set folder | Important models first, then the complete diagram inventory |
| [Coverage](coverage.md) | `coverage.md` in the owning message-set edition or standalone message folder | Source-to-output reconciliation and review evidence |
| [Code-set index](code-set-index.md) | `index.md` in a shared code-publication edition folder | Versioned code-set context and links to complete code tables |

## Typical output layout

Read originals from the message-set collections under [raw-input/](../raw-input/) and follow the [collection routing map](../catalog/README.md#collection-routing) into the separate domain/shared output areas. Never write conversion output into the raw input folders.

Create output folders only when their sources are processed. A message-set edition normally owns shared business material and a coverage inventory:

```text
reference/message-sets/<set-slug>/<edition>/
  index.md
  coverage.md
  rules.md
  tables/
  diagrams/
    index.md
  flows/
  participants.md
  documents/<source-id>/
    tables/
    diagrams/
```

Each exact message definition owns one canonical reference; schema pages exist when its schema is supplied:

```text
reference/messages/<full-message-id>/
  index.md
  structure.md
  rules.md
  types/
  tables/
  diagrams/
    index.md
```

Create a local coverage page for a standalone message that has no owning message-set inventory. Otherwise, link to the shared coverage page and identify the message's relevant items. Shared tables and diagrams live once within the owning source/message-set scope; message indexes link to them. Source evidence pages under `documents/<source-id>/` retain occurrences and point to curated reconstructions where applicable.

Canonical participants live in `shared/reference/participants/`. Message-set participant indexes link to these scoped definitions. Reusable flows live in the owning set edition and link participants, messages, source activities and diagrams in both directions. Labels alone do not justify merging roles. Participant and flow conventions are illustrated by the maintained [participant](../catalog/participants.md) and [flow](../catalog/flows.md) indexes.

Code publications use `shared/reference/code-sets/<publication>/<edition>/`, an index, a coverage page, and linked complete tables. Their edition is independent of a message's version.

Do not create empty output pages to simulate progress. If a required section is inapplicable, state why; if it is unknown, record the missing evidence.

## Instantiate a template

1. Copy the appropriate template into the actual output folder.
2. Change `template: true` to `template: false` and `review_status: template` to `review_status: draft`.
3. Fill metadata from registered evidence and replace every `{{placeholder}}`.
4. Remove the template-only guidance and this template's navigation link.
5. Turn link placeholders into real relative links, computed from the output file's location. Do not leave nonexistent placeholder destinations.
6. Add source IDs and precise locators. Link the source register and relevant local sources, canonical pages, coverage, and issues.
7. Set review metadata only after the required checks actually pass.

Use YAML null for truly inapplicable fields and an empty list for no applicable list entries. Missing required evidence must be explained and tracked; null is not a substitute for identifying a gap.

## Metadata and naming

- Preserve exact full message identifiers, XML names, code values, namespace URIs, and edition labels.
- Page metadata records domain, business area when applicable, source IDs, edition, origin where relevant, and review status.
- Named and anonymous types receive stable local `type-NNNN` page IDs. Metadata holds the exact QName or containing schema path; page filenames do not assume local names are unique across namespaces.
- Table and diagram IDs are local to their owning source/reference folder. Source ID, locator, and scope disambiguate repeated occurrences.
- Use short descriptive headings and focused pages. Link to canonical content instead of copying shared material.
- Use standard Markdown tables. Do not use merged HTML cells to preserve a spreadsheet layout; make header context explicit in Markdown.
- Escape literal table pipes and preserve leading zeros. Keep original-language technical labels when translation would change their meaning.

## Diagram policy

Origins are `source-reconstruction` and `xsd-derived`. Native use cases use `usecase-beta` with Mermaid 12 or newer. Record the exact renderer version used to validate each diagram.

The diagram template deliberately has no fabricated diagram or executable placeholder Mermaid block. Insert a real fenced `mermaid` block during conversion. For derived diagrams, the original-image field is inapplicable; cite schema declarations instead.

Use cases and data/entity/class models are high priority and require visual review. A textual description complements Mermaid and identifies semantics that cannot be drawn faithfully.

## Navigation

[Workspace guide](../README.md) · [Conversion instructions](../AGENTS.md) · [Source register](../tracking/source-register.md) · [Conversion status](../tracking/conversion-status.md) · [Issues](../tracking/issues.md)
