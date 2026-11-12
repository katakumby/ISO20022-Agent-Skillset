---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["16 sese.022.001.08 SecuritiesStatusOrStatementQueryStatusAdviceV08", "16.4 Message Building Blocks", "16.4.4 BlockChainAddressOrWallet <BlckChainAdrOrWllt>"]
file_pages: [486]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.022.001.08"]
---

# 16.4.4 BlockChainAddressOrWallet <BlckChainAdrOrWllt>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 486 to 486.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 486

```text
16.4.4 BlockChainAddressOrWallet <BlckChainAdrOrWllt>
Presence: [0..1]
Definition: Blockchain address or wallet where digital assets are maintained. This is the equivalent of
safekeeping account for digital assets.
BlockChainAddressOrWallet <BlckChainAdrOrWllt> contains the following elements (see
"BlockChainAddressWallet3" on page 1572 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 1572
   Type <Tp> [0..1] ± 1572
   Name <Nm> [0..1] Text 1572
16.4.5 StatusOrStatementRequested <StsOrStmtReqd>
Presence: [0..1]
Definition: Details of the request.
StatusOrStatementRequested <StsOrStmtReqd> contains one of the following
StatusOrStatement14Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   StatusAdvice <StsAdvc> [1..1]  C3 486
     Number <Nb> [1..1] ± C6 487
     References <Refs> [1..*] ± 487
Or}   Statement <Stmt> [1..1] ± 488
16.4.5.1  StatusAdvice <StsAdvc>
Presence: [1..1]
Definition: Identifies the status advice and the transaction for which the status advice was requested.
Impacted by: C3 "ReferenceRule"
StatusAdvice <StsAdvc> contains the following DocumentNumber22 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Number <Nb> [1..1] ± C6 487
   References <Refs> [1..*] ± 487
Constraints
• ReferenceRule
The reference used to identify the transaction must be in line with the identification available for the
status advice requested by the SecuritiesTransactionStatusQuery. For example, a
Approved by the Securities SEG on 27 January 2026 sese.022.001.08
SecuritiesStatusOrStatementQueryStatusAdviceV0
8
Settlement And Reconciliation - Maintenance 2025 - 2026 486 March 2026
```

