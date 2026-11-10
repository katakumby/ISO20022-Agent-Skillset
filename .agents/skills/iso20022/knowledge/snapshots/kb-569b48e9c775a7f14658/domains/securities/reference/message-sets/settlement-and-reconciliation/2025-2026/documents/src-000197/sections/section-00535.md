---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["25 sese.031.001.11 SecuritiesSettlementConditionModificationStatusAdviceV11", "25.3 Constraints"]
file_pages: [805]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.031.001.11"]
---

# 25.3 Constraints

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 805 to 805.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 805

```text
25.3 Constraints
C1 AdditionalReasonInforrmationRule
The AdditionalReasonInformation element must not contain information that can be provided in
a structured field unless bilaterally agreed.
C2 AnyBIC
Only a valid Business identifier code is allowed. Business identifier codes for financial or non-
financial institutions are registered and published by the ISO 9362 Registration Authority in the
ISO directory of BICs, and consists of eight (8) or eleven (11) contiguous characters.
C3 ModificationRequestPresenceRule
At least one securities settlement conditions modification request type must be present.
C4 OtherProcessingRule
If OtherProcessing is used, then its usage must be pre-agreed between the sender and
receiver.
C5 ReferencePresenceRule
At least one reference must be present.
C6 SafekeepingAccountOrBlockChainAddress1Rule
If SafekeepingAccount is present, BlockChainAddressOrWallet must be absent.
On Condition
    /SafekeepingAccount is present
Following Must be True
    /BlockChainAddressOrWallet Must be absent
This constraint is defined at the MessageDefinition level.
C7 SafekeepingAccountOrBlockChainAddress2Rule
If BlockChainAddressOrWallet is present, SafekeepingAccount must be absent.
On Condition
    /BlockChainAddressOrWallet is present
Following Must be True
    /SafekeepingAccount Must be absent
This constraint is defined at the MessageDefinition level.
C8 SettlementConditionModificationApplicabilityRule
All settlement condition modification request types do not apply to all account servicers.
C9 ShortLongNumberRule
ShortNumber must contain the FIN message type number of the linked message. LongNumber
must contain the XML message identifier of the linked message.
C10 SupplementaryDataRule
This component may not be used without the explicit approval of a SEG and submission to the
RA of ISO 20022 compliant structure(s) to be used in the Envelope element.
C11 WithLinkageRule
If Code WITH is used, then the one or more instruction which are linked become bound and
which must be executed together. Even if one single transactions/instructions/notifications can
Approved by the Securities SEG on 27 January 2026 sese.031.001.11
SecuritiesSettlementConditionModificationStatusAd
viceV11
Settlement And Reconciliation - Maintenance 2025 - 2026 805 March 2026
```

