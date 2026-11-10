---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["16 sese.022.001.08 SecuritiesStatusOrStatementQueryStatusAdviceV08", "16.4 Message Building Blocks", "16.4.5 StatusOrStatementRequested <StsOrStmtReqd>", "16.4.5.1 StatusAdvice <StsAdvc>", "16.4.5.1.1 Number <Nb>"]
file_pages: [487]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.022.001.08"]
---

# 16.4.5.1.1 Number <Nb>

Source: [src-000197](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf). Locator: one-based file pages 487 to 487.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 487

```text
SecuritiesTransactionStatusQuery must not request a SecuritiesSettlementTransactionStatusAdvice
using a CorporateActionEventIdentification.
16.4.5.1.1  Number <Nb>
Presence: [1..1]
Definition: Number used to identify a message or document.
Impacted by: C6 "ShortLongNumberRule"
Number <Nb> contains one of the following elements (see "DocumentNumber5Choice" on page 1444
for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   ShortNumber <ShrtNb> [1..1] Text 1444
Or   LongNumber <LngNb> [1..1] Text 1445
Or}   ProprietaryNumber <PrtryNb> [1..1] ± 1445
Constraints
• ShortLongNumberRule
ShortNumber must contain the FIN message type number of the linked message. LongNumber must
contain the XML message identifier of the linked message.
16.4.5.1.2  References <Refs>
Presence: [1..*]
Definition: References of transaction for which the status is requested.
Approved by the Securities SEG on 27 January 2026 sese.022.001.08
SecuritiesStatusOrStatementQueryStatusAdviceV0
8
Settlement And Reconciliation - Maintenance 2025 - 2026 487 March 2026
```

