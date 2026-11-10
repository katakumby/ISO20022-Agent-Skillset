---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000163"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["3 pacs.003.001.12 FIToFICustomerDirectDebitV12", "3.4 Message Building Blocks", "3.4.2 DirectDebitTransactionInformation <DrctDbtTxInf>", "3.4.2.12 DirectDebitTransaction <DrctDbtTx>", "3.4.2.12.1 MandateRelatedInformation <MndtRltdInf>", "3.4.2.12.1.1 MandateIdentification <MndtId>"]
file_pages: [169]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pacs.003.001.12"]
---

# 3.4.2.12.1.1 MandateIdentification <MndtId>

Source: [src-000163](../../../../../../../../../raw-input/payments_clearing_and_settlement/ISO20022_MDRPart2_PaymentsClearingandSettlement_2025_2026_v1.pdf). Locator: one-based file pages 169 to 169.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 169

```text
Constraints
• AmendmentIndicatorFalseRule
If AmendmentIndicator is false, then AmendmentInformationDetails is not allowed.
On Condition
    /AmendmentIndicator is equal to value 'false'
Following Must be True
    /AmendmentInformationDetails Must be absent
• AmendmentIndicatorTrueRule
If AmendmentIndicator is true, then AmendmentInformationDetails must be present.
On Condition
    /AmendmentIndicator is equal to value 'true'
Following Must be True
    /AmendmentInformationDetails Must be present
3.4.2.12.1.1  MandateIdentification <MndtId>
Presence: [0..1]
Definition: Unique identification, as assigned by the creditor, to unambiguously identify the mandate.
Datatype: "Max35Text" on page 1246
3.4.2.12.1.2  DateOfSignature <DtOfSgntr>
Presence: [0..1]
Definition: Date on which the direct debit mandate has been signed by the debtor.
Datatype: "ISODate" on page 1239
3.4.2.12.1.3  AmendmentIndicator <AmdmntInd>
Presence: [0..1]
Definition: Indicator notifying whether the underlying mandate is amended or not.
Datatype: One of the following values must be used (see "TrueFalseIndicator" on page 1242):
• Meaning When True: True
• Meaning When False: False
3.4.2.12.1.4  AmendmentInformationDetails <AmdmntInfDtls>
Presence: [0..1]
Definition: List of mandate elements that have been modified.
Approved by the Payments SEG on 12 January 2026 pacs.003.001.12 FIToFICustomerDirectDebitV12
Payments Clearing and Settlement - Maintenance 2025 -
2026
169 March 2026
```

