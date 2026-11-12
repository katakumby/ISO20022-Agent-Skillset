# Embedded snapshot integration contract, version 1

This is an interface for a separately developed maintenance agent. This retrieval skill does not implement refresh, reload, conversion, configuration changes or rollback.

## Installed layout

- scripts/kb.py: standard-library, read-only retrieval CLI.
- knowledge/active.json: format_version 1 and snapshot_id.
- knowledge/snapshots/SNAPSHOT_ID/: immutable text snapshot.
- config.json: optional local defaults.
- evidence-packs/PACK_ID/: optional separately supplied evidence.

Paths are relative to the installed research skill, independent of working directory. Snapshot identifiers contain only ASCII letters, numbers, underscores and hyphens, at most 100 characters. Do not use symbolic links inside a snapshot.

## Snapshot files

manifest.json contains format_version, snapshot_id, label, corpus_sources_sha256, inventory, inventory_sha256, text_file_count, indexed_documents and file_count. inventory is files.json. files.json is an array of path, size, sha256 entries for every payload file, including index.sqlite. The manifest binds the inventory checksum. Neither file includes its own checksum recursively.

Source identity is independent of export identity. Preserve catalog/sources.json records, original source hashes, immutable original paths/archive-member names and exact locators. evidence/export-map.json records packaging transformations and original text fingerprints. Evidence/source availability pages identify omitted artifacts without changing semantic review status.

domains/, shared/ and catalog/ preserve canonical reference paths. Supporting text evidence and original XSD/JSON may be included at their historical relative paths. Binaries are not readable through the query helper.

## Search database

SQLite with FTS5, opened mode=ro and query_only:
- info(key,value): format_version and snapshot_id.
- files(path,sha256,size): packaged text-file membership.
- documents(id,path,title,kind,domain,message_id,family,metadata): metadata is JSON.
- tags(doc_id,key,value): kind/domain/message/family/namespace/collection/edition/source/status.
- search: contentless FTS5 columns title and body, rowid matching documents.id. The body column indexes the complete packaged text, including front matter: source qualifications and review limitations can appear only in metadata. Typed tags supplement this full-text coverage.

The index must be rebuilt as part of preparing a new snapshot, not on a research request. Validate source and file identity, links, and representative retrieval before activating it. Replace the small active.json pointer atomically only after staging and validation succeed; retain snapshots used by active readers. Retrieval commands pin snapshots with --snapshot ID. Unpinned calls validate the active pointer object, format_version and snapshot_id. Explicitly pinned calls validate the requested snapshot directly and do not consult the current active pointer.

## Configuration

config.json fields: retrieval_budget_chars (3000..60000, default 12000), default_collection (string or null), default_edition (string or null), evidence_pack (safe pack identifier or null). Defaults narrow search only when no explicit message, namespace, source or path scope is supplied; --all-scopes bypasses them. They never alter exact resolution.

## Optional evidence

evidence-packs/PACK_ID/evidence-manifest.json contains corpus_sources_sha256 and files, each with path, sha256, size, source_ids. Each selected entry must have verified byte size and SHA-256 and must match every listed registered source identity. The packaged catalog/sources.json must match corpus_sources_sha256.

An entry can contain the original source bytes (including an extracted archive member), or the registered ZIP container of an archive-member source. For a container, source verifies its registered archive fingerprint and the exact, uniquely named member's fingerprint without extraction. Returned local_original_evidence records preserve original occurrences, archive source identity and member name; local_originals remains a list of local paths. Wrong, missing, ambiguous or unsupported evidence is reported rather than treated as an original.

Hashing and archive-member verification authenticate bytes only. The helper does not render, execute or semantically interpret originals. Content inspection still requires an explicit user request.

## Compatibility

Target Python 3.10+ and SQLite FTS5 on Windows, macOS and Linux. Use UTF-8, portable relative paths, no network dependency, and read-only query connections. Do not change this format incompatibly under version 1.
