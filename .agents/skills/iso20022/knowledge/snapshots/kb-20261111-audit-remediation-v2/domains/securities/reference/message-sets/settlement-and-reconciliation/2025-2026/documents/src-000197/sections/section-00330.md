---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["15 sese.021.001.08 SecuritiesTransactionStatusQueryV08", "15.4 Message Building Blocks"]
file_pages: [478]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.021.001.08"]
---

# 15.4 Message Building Blocks

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 478 to 478.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 478

```text
Following Must be True
    /SafekeepingAccount Must be absent
This constraint is defined at the MessageDefinition level.
C5 SafekeepingAccountOrBlockChainAddress3Rule
Either SafekeepingAccount or BlockChainAddressOrWallet must be present but not both.
Following Must be True
    /SafekeepingAccount Must be present
 Or    /BlockChainAddressOrWallet Must be present
This constraint is defined at the MessageDefinition level.
C6 ShortLongNumberRule
ShortNumber must contain the FIN message type number of the linked message. LongNumber
must contain the XML message identifier of the linked message.
C7 SupplementaryDataRule
This component may not be used without the explicit approval of a SEG and submission to the
RA of ISO 20022 compliant structure(s) to be used in the Envelope element.
15.4 Message Building Blocks
This chapter describes the MessageBuildingBlocks of this MessageDefinition.
15.4.1 StatusAdviceRequested <StsAdvcReqd>
Presence: [1..1]
Definition: Description of the status advice requested.
Impacted by: C2 "ReferenceRule"
StatusAdviceRequested <StsAdvcReqd> contains the following DocumentNumber22 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Number <Nb> [1..1] ± C6 478
   References <Refs> [1..*] ± 479
Constraints
• ReferenceRule
The reference used to identify the transaction must be in line with the identification available for the
status advice requested by the SecuritiesTransactionStatusQuery. For example, a
SecuritiesTransactionStatusQuery must not request a SecuritiesSettlementTransactionStatusAdvice
using a CorporateActionEventIdentification.
15.4.1.1  Number <Nb>
Presence: [1..1]
Definition: Number used to identify a message or document.
Impacted by: C6 "ShortLongNumberRule"
Approved by the Securities SEG on 27 January 2026 sese.021.001.08
SecuritiesTransactionStatusQueryV08
Settlement And Reconciliation - Maintenance 2025 - 2026 478 March 2026
```

