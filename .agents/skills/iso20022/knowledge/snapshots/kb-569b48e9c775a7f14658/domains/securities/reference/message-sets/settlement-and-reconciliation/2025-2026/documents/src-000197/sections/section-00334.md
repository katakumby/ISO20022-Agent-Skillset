---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["16 sese.022.001.08 SecuritiesStatusOrStatementQueryStatusAdviceV08", "16.2 Structure"]
file_pages: [483]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.022.001.08"]
---

# 16.2 Structure

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 483 to 483.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 483

```text
F. ProcessingStatus
Provides details on the processing status of the request.
G. SupplementaryData
Additional information that cannot be captured in the structured elements and/or any other specific
block.
16.2 Structure
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Message root <Document> <SctiesStsOrStmtQryStsAdvc> [1..1]  C4, C5
   QueryDetails <QryDtls> [1..1]  484
     MessageNumber <MsgNb> [0..1] ± C6 484
     Reference <Ref> [1..1] Text 485
   AccountOwner <AcctOwnr> [0..1] ± 485
   SafekeepingAccount <SfkpgAcct> [0..1] ± 485
   BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 486
   StatusOrStatementRequested <StsOrStmtReqd> [0..1]  486
{Or     StatusAdvice <StsAdvc> [1..1]  C3 486
       Number <Nb> [1..1] ± C6 487
       References <Refs> [1..*] ± 487
Or}     Statement <Stmt> [1..1] ± 488
   ProcessingStatus <PrcgSts> [1..1]  488
{Or     AcknowledgedAccepted <AckdAccptd> [1..1] ± 489
Or     Rejected <Rjctd> [1..1] ± 489
Or}     Proprietary <Prtry> [1..1] ± 489
   SupplementaryData <SplmtryData> [0..*] ± C7 490
16.3 Constraints
C1 AdditionalReasonInforrmationRule
The AdditionalReasonInformation element must not contain information that can be provided in
a structured field unless bilaterally agreed.
C2 AnyBIC
Only a valid Business identifier code is allowed. Business identifier codes for financial or non-
financial institutions are registered and published by the ISO 9362 Registration Authority in the
ISO directory of BICs, and consists of eight (8) or eleven (11) contiguous characters.
Approved by the Securities SEG on 27 January 2026 sese.022.001.08
SecuritiesStatusOrStatementQueryStatusAdviceV0
8
Settlement And Reconciliation - Maintenance 2025 - 2026 483 March 2026
```

