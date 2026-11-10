---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["4 semt.013.001.07 IntraPositionMovementInstructionV07", "5.3 Constraints"]
file_pages: [152]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.014.001.09"]
---

# 5.3 Constraints

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 152 to 152.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 152

```text
5.3 Constraints
C1 AdditionalReasonInforrmationRule
The AdditionalReasonInformation element must not contain information that can be provided in
a structured field unless bilaterally agreed.
C2 AnyBIC
Only a valid Business identifier code is allowed. Business identifier codes for financial or non-
financial institutions are registered and published by the ISO 9362 Registration Authority in the
ISO directory of BICs, and consists of eight (8) or eleven (11) contiguous characters.
C3 DescriptionPresenceRule
If Description is not present then either ISIN or at least one occurrence of OtherIdentification
must be present.
C4 DescriptionUsageRule
Description must be used alone as the last resort.
C5 DigitalTokenUnitUsageRule
DigitalTokenUnit format may only be used for instruments identified with a digital token
identifier.
C6 ISINGuideline
When an ISIN code exists, it is strongly recommended that the ISIN be used.
C7 ISINPresenceRule
If ISIN is not present then either Description or at least one occurrence of OtherIdentification
must be present.
C8 NoAccountOwnerTransactionIdentificationRule
If no reference is available for the AccountOwnerTransactionIdentification, for example, the
transaction was sent by fax, then the AccountOwnerTransactionIdentification must be
NONREF.
C9 OtherIdentificationPresenceRule
If OtherIdentification is not present then either ISIN or Description must be present.
C10 PendingToFailingRule
A pending transaction (PEND) becomes a failing transaction (PENF) on the settlement date
instructed in the message, during the end of day reporting.
C11 SafekeepingAccountOrBlockChainAddress1Rule
If SafekeepingAccount is present, BlockChainAddressOrWallet must be absent.
C12 SafekeepingAccountOrBlockChainAddress2Rule
If BlockChainAddressOrWallet is present, SafekeepingAccount must be absent.
C13 SafekeepingAccountOrBlockChainAddress3Rule
Either SafekeepingAccount or BlockChainAddressOrWallet must be present but not both.
Approved by the Securities SEG on 27 January 2026 semt.014.001.09
IntraPositionMovementStatusAdviceV09
Settlement And Reconciliation - Maintenance 2025 - 2026 152 March 2026
```

