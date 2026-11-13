---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SettlementRestrictions"
source_ids: ["src-000381"]
source_editions: ["september-2025"]
message_ids: []
heading_path: ["6 semt.032.001.01 SecuritiesTransactionCancellationRequestQueryV01", "6.3 Constraints"]
file_pages: [136]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.032.001.01"]
---

# 6.3 Constraints

Source: [src-000381](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SettlementRestrictions_MessageSet/ISO20022_MDRPart2_Target2Securities_SettlementRestrictions_v1.pdf`. Locator: one-based file pages 136 to 136.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 136

```text
6.3 Constraints
C1 AnyBIC
Only a valid Business identifier code is allowed. Business identifier codes for financial or non-
financial institutions are registered and published by the ISO 9362 Registration Authority in the
ISO directory of BICs, and consists of eight (8) or eleven (11) contiguous characters.
C2 Country
The code is checked against the list of country names obtained from the United Nations (ISO
3166, Alpha-2 code).
C3 SupplementaryDataRule
This component may not be used without the explicit approval of a SEG and submission to the
RA of ISO 20022 compliant structure(s) to be used in the Envelope element.
6.4 Message Building Blocks
This chapter describes the MessageBuildingBlocks of this MessageDefinition.
6.4.1 QueryDefinition <QryDef>
Presence: [1..1]
Definition: Defines the intra-position movement cancellation query criteria.
Approved by the Securities SEG on 21 August 2025 semt.032.001.01
SecuritiesTransactionCancellationRequestQueryV0
1
Target2-Securities - Settlement Restrictions 136 September 2025
```

