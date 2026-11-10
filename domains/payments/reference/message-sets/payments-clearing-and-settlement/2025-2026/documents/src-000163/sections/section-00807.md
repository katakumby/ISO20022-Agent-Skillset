---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000163"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["8 pacs.010.001.06 FinancialInstitutionDirectDebitV06", "9.4 Message Building Blocks", "9.4.1 GroupHeader <GrpHdr>", "9.4.3.11 OriginalTransactionReference <OrgnlTxRef>", "9.4.3.11.10 MandateRelatedInformation <MndtRltdInf>", "9.4.3.11.10.1 DirectDebitMandate <DrctDbtMndt>", "9.4.3.11.10.1.1 MandateIdentification <MndtId>"]
file_pages: [1093]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pacs.028.001.07"]
---

# 9.4.3.11.10.1.1 MandateIdentification <MndtId>

Source: [src-000163](../../../../../../../../../raw-input/payments_clearing_and_settlement/ISO20022_MDRPart2_PaymentsClearingandSettlement_2025_2026_v1.pdf). Locator: one-based file pages 1093 to 1093.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1093

```text
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
9.4.3.11.10.1.1  MandateIdentification <MndtId>
Presence: [0..1]
Definition: Unique identification, as assigned by the creditor, to unambiguously identify the mandate.
Datatype: "Max35Text" on page 1246
9.4.3.11.10.1.2  DateOfSignature <DtOfSgntr>
Presence: [0..1]
Definition: Date on which the direct debit mandate has been signed by the debtor.
Datatype: "ISODate" on page 1239
9.4.3.11.10.1.3  AmendmentIndicator <AmdmntInd>
Presence: [0..1]
Definition: Indicator notifying whether the underlying mandate is amended or not.
Datatype: One of the following values must be used (see "TrueFalseIndicator" on page 1242):
• Meaning When True: True
• Meaning When False: False
9.4.3.11.10.1.4  AmendmentInformationDetails <AmdmntInfDtls>
Presence: [0..1]
Definition: List of mandate elements that have been modified.
Approved by the Payments SEG on 12 January 2026 pacs.028.001.07 FIToFIPaymentStatusRequestV07
Payments Clearing and Settlement - Maintenance 2025 -
2026
1093 March 2026
```

