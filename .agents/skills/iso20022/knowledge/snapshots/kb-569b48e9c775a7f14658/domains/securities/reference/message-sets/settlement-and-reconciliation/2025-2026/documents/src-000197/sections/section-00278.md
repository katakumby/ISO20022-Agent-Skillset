---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["11 semt.020.001.07 SecuritiesMessageCancellationAdviceV07", "12.3 Constraints"]
file_pages: [415]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.021.001.09"]
---

# 12.3 Constraints

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 415 to 415.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 415

```text
12.3 Constraints
C1 AnyBIC
Only a valid Business identifier code is allowed. Business identifier codes for financial or non-
financial institutions are registered and published by the ISO 9362 Registration Authority in the
ISO directory of BICs, and consists of eight (8) or eleven (11) contiguous characters.
C2 DescriptionPresenceRule
If Description is not present then either ISIN or at least one occurrence of OtherIdentification
must be present.
C3 DescriptionUsageRule
Description must be used alone as the last resort.
C4 ISINGuideline
When an ISIN code exists, it is strongly recommended that the ISIN be used.
C5 ISINPresenceRule
If ISIN is not present then either Description or at least one occurrence of OtherIdentification
must be present.
C6 OtherIdentificationPresenceRule
If OtherIdentification is not present then either ISIN or Description must be present.
C7 ReasonRule
If the reason is requested, then it must be in line with the reasons available for the message
type requested.
C8 SafekeepingAccountOrBlockChainAddress1Rule
If SafekeepingAccount is present, BlockChainAddressOrWallet must be absent.
On Condition
    /SafekeepingAccount is present
Following Must be True
    /BlockChainAddressOrWallet Must be absent
This constraint is defined at the MessageDefinition level.
C9 SafekeepingAccountOrBlockChainAddress2Rule
If BlockChainAddressOrWallet is present, SafekeepingAccount must be absent.
On Condition
    /BlockChainAddressOrWallet is present
Following Must be True
    /SafekeepingAccount Must be absent
This constraint is defined at the MessageDefinition level.
C10 SafekeepingAccountOrBlockChainAddress3Rule
Either SafekeepingAccount or BlockChainAddressOrWallet must be present but not both.
Following Must be True
    /SafekeepingAccount Must be present
 Or    /BlockChainAddressOrWallet Must be present
This constraint is defined at the MessageDefinition level.
Approved by the Securities SEG on 27 January 2026 semt.021.001.09 SecuritiesStatementQueryV09
Settlement And Reconciliation - Maintenance 2025 - 2026 415 March 2026
```

