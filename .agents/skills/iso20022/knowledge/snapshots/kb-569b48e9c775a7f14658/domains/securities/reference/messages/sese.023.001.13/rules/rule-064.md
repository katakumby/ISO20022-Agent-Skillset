---
template: false
document_kind: "business-rule"
review_status: "needs-review"
title: "C64 SafekeepingPlaceGuideline"
domain: "securities"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_sets: ["settlement-and-reconciliation"]
updated: "2026-11-08"
message_ids: ["sese.023.001.13"]
rule_id: "C64"
source_locations: [{"source_id": "src-000197", "file_pages": [504, 505], "printed_pages": [504, 505], "heading": "17.3 Constraints", "constraint": "C64"}]
---

# C64 SafekeepingPlaceGuideline

Source wording: [src-000197](../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md), §17.3, file/printed page(s) 504, 505. Wrapped lines are retained. This MDR rule is distinct from XSD validation; it may specify cross-field, market-data or business conditions beyond the schema.

When used (see usage rule SafekeepingPlaceRule), unless special arrangements exist
between the account servicer and the account owner, it is recommended to use the place of
safekeeping field following the market practice described below:
• SafekeepingPlaceType/SharesHeldAtNCSD: a NCSD's BIC will be used for domestic and
NCSD to NCSD settlement instructions.
• SafekeepingPlaceType/SharesHeldAtICSD: an ICSD's BIC will be used for ICSD internal,
ICSD/local and ICSD to ICSD settlement instructions.
• SafekeepingPlaceType/SharesHeldAtLoaclCustodian: applicable, for instance, when the
account servicer is a global custodian and provides the account owner with a position reporting
at global custodian's agents' level. When instructing, the fund manager would therefore
mention, as a place of safekeeping, the BIC of the global custodian's agent on the market.
Absence of SafekeepingPlace means that:
• The SafekeepingPlace information is kept by the account servicer (SLA, account structure,
ETC.) and should not be provided by the account owner.
• The SafekeepingPlace is the counterparty's Depository. The transaction is therefore domestic
(to an NCSD) or internal to an ICSD.
For more details, see the relevant market practice document on www.smpg.info.

[Constraint index](../rules-business.md)
