---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["72 semt.027.001.01 SecuritiesSettlementTransactionQueryResponseV01", "72.4 Message Building Blocks"]
file_pages: [2486]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.027.001.01"]
preceding_topic_continuations: [{"constraint_ids": ["C39"], "until_heading": "72.4 Message Building Blocks", "scope": "Text before the named heading on this one-based file page.", "file_page": 2486, "topic": "72.3 Constraints", "reference_path": "domains/securities/reference/message-sets/t2s/august-2026/documents/src-000233/sections/section-01810.md"}]
---

# 72.4 Message Building Blocks

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 2486 to 2486.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

<!-- PDF-TOPIC-NAV-START -->
## Topic continuation

On file page 2486, C39 before **72.4 Message Building Blocks** continue [72.3 Constraints](section-01810.md). They belong to the preceding Constraints topic; the full source page is retained below without rearranging its text.
<!-- PDF-TOPIC-NAV-END -->

## File page 2486

```text
SettlementParameters/SecuritiesTransactionType: CollateralIn (COLI)
Collateral (taker) In Return
SecuritiesMovementType: Delivery (DELI)
SettlementParameters/SecuritiesTransactionType: CollateralIn (COLI).
C39 WithLinkageRule
If Code WITH is used, then the one or more instruction which are linked become bound and
which must be executed together. Even if one single transactions/instructions/notifications can
not be executed, then all the other transactions/instructions/notifications must also be kept
pending. Therefore the use of code WITH must be limited to combine up to 2 or 3 transactions/
instructions/notifications.
72.4 Message Building Blocks
This chapter describes the MessageBuildingBlocks of this MessageDefinition.
72.4.1 Pagination <Pgntn>
Presence: [1..1]
Definition: Pagination of the message.
Pagination <Pgntn> contains the following elements (see "Pagination1" on page 2980 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PageNumber <PgNb> [1..1] Text 2980
   LastPageIndicator <LastPgInd> [1..1] Indicator 2980
72.4.2 ReportGeneralDetails <RptGnlDtls>
Presence: [1..1]
Definition: General characteristics related to the report information.
Impacted by: C29 "ReportIdentificationRule"
ReportGeneralDetails <RptGnlDtls> contains the following SecuritiesReport2 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ReportIdentification <RptId> [0..1] Text 2487
   QueryReference <QryRef> [0..1] Text 2487
   QueryType <QryTp> [1..1] CodeSet 2487
   ActivityIndicator <ActvtyInd> [1..1] Indicator 2487
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
semt.027.001.01
SecuritiesSettlementTransactionQueryResponseV0
1
Target2-Securities 2486 August 2026
```

