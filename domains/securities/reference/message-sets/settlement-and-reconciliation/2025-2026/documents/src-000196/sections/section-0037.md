---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000196"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["Description of BusinessActivities", "Securities Financing Instruction", "Modification Process ", "Changes That Do Impact the Securities Position"]
content_origin: "source-transcription"
---

# Changes That Do Impact the Securities Position

Source: [src-000196](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart1_SettlementAndReconciliation_2025_2026_v2.docx). Locator: heading path Description of BusinessActivities / Securities Financing Instruction / Modification Process  / Changes That Do Impact the Securities Position.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P232** Changes That Do Impact the Securities Position

**P233** This model applies to changes impacting the securities position, for example, collateral substitutions, top-up and withdrawal.

**P234** In line with the SMPG current one message MP (for security financing recommending the usage of one message for both contract and the collateral), we use the existing process, that is, the use of settlement instructions (see activity diagrams described above in this document).

**P235** Indeed, substitutions, top-up and withdrawal are requests for position movements, and for such movements, settlement instructions are generally used:

**P236** For substitutions, a receive free linked to a delivery free should be the standard.

**P237** For top-up and withdrawal, as per the SMPG current MPs, a delivery or receive instruction is used and we believe there is no valid reason to change that standard.

**P238** Despite the fact that this will be a pure settlement movement, upon settlement of the change of positions not only a SettlementConfirmationAdvice will be sent out but also a SecuritiesFinancingStatusAdvice to advise of the position change impacting the SecuritiesFinancingTransaction.

