---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["16 sese.022.001.08 SecuritiesStatusOrStatementQueryStatusAdviceV08", "16.4 Message Building Blocks"]
file_pages: [484]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.022.001.08"]
---

# 16.4 Message Building Blocks

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 484 to 484.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 484

```text
C3 ReferenceRule
The reference used to identify the transaction must be in line with the identification available for
the status advice requested by the SecuritiesTransactionStatusQuery. For example, a
SecuritiesTransactionStatusQuery must not request a
SecuritiesSettlementTransactionStatusAdvice using a CorporateActionEventIdentification.
C4 SafekeepingAccountOrBlockChainAddress1Rule
If SafekeepingAccount is present, BlockChainAddressOrWallet must be absent.
On Condition
    /SafekeepingAccount is present
Following Must be True
    /BlockChainAddressOrWallet Must be absent
This constraint is defined at the MessageDefinition level.
C5 SafekeepingAccountOrBlockChainAddress2Rule
If BlockChainAddressOrWallet is present, SafekeepingAccount must be absent.
On Condition
    /BlockChainAddressOrWallet is present
Following Must be True
    /SafekeepingAccount Must be absent
This constraint is defined at the MessageDefinition level.
C6 ShortLongNumberRule
ShortNumber must contain the FIN message type number of the linked message. LongNumber
must contain the XML message identifier of the linked message.
C7 SupplementaryDataRule
This component may not be used without the explicit approval of a SEG and submission to the
RA of ISO 20022 compliant structure(s) to be used in the Envelope element.
16.4 Message Building Blocks
This chapter describes the MessageBuildingBlocks of this MessageDefinition.
16.4.1 QueryDetails <QryDtls>
Presence: [1..1]
Definition: Unambiguous identification of the query as per the account owner.
QueryDetails <QryDtls> contains the following DocumentIdentification54 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   MessageNumber <MsgNb> [0..1] ± C6 484
   Reference <Ref> [1..1] Text 485
16.4.1.1  MessageNumber <MsgNb>
Presence: [0..1]
Definition: Message type number/message identifier of the message referenced in the linkage
sequence.
Approved by the Securities SEG on 27 January 2026 sese.022.001.08
SecuritiesStatusOrStatementQueryStatusAdviceV0
8
Settlement And Reconciliation - Maintenance 2025 - 2026 484 March 2026
```

