---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Initiation"
source_ids: ["src-000174"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["4 pain.007.001.13 CustomerPaymentReversalV13", "5.4 Message Building Blocks", "5.4.2.18 DirectDebitTransactionInformation <DrctDbtTxInf>", "5.4.2.18.5 DirectDebitTransaction <DrctDbtTx>", "5.4.2.18.5.1 MandateRelatedInformation <MndtRltdInf>", "5.4.2.18.5.1.1 MandateIdentification <MndtId>"]
file_pages: [450]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pain.008.001.12"]
---

# 5.4.2.18.5.1.1 MandateIdentification <MndtId>

Source: [src-000174](../../../../../../../../../raw-input/payments_initiation/ISO20022_MDRPart2_PaymentsInitiation_2025_2026_v1.pdf). Locator: one-based file pages 450 to 450.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 450

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
5.4.2.18.5.1.1  MandateIdentification <MndtId>
Presence: [0..1]
Definition: Unique identification, as assigned by the creditor, to unambiguously identify the mandate.
Datatype: "Max35Text" on page 609
5.4.2.18.5.1.2  DateOfSignature <DtOfSgntr>
Presence: [0..1]
Definition: Date on which the direct debit mandate has been signed by the debtor.
Datatype: "ISODate" on page 603
5.4.2.18.5.1.3  AmendmentIndicator <AmdmntInd>
Presence: [0..1]
Definition: Indicator notifying whether the underlying mandate is amended or not.
Datatype: One of the following values must be used (see "TrueFalseIndicator" on page 605):
• Meaning When True: True
• Meaning When False: False
5.4.2.18.5.1.4  AmendmentInformationDetails <AmdmntInfDtls>
Presence: [0..1]
Definition: List of mandate elements that have been modified.
Approved by the Payments SEG on 12 January 2026 pain.008.001.12 CustomerDirectDebitInitiationV12
Payments Initiation - Maintenance 2025 - 2026 450 March 2026
```

