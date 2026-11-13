---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Initiation"
source_ids: ["src-000174"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["2 pain.001.001.13 CustomerCreditTransferInitiationV13", "2.4 Message Building Blocks", "2.4.2 PaymentInformation <PmtInf>", "2.4.2.1 PaymentInformationIdentification <PmtInfId>"]
file_pages: [33]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pain.001.001.13"]
---

# 2.4.2.1 PaymentInformationIdentification <PmtInfId>

Source: [src-000174](../../../../../../../../../evidence/omitted/577241d5215d98d6ed689f57.md). Locator: one-based file pages 33 to 33.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 33

```text
• UltimateDebtorRule
If UltimateDebtor is present, then CreditTransferTransactionInformation/UltimateDebtor is not
allowed.
If CreditTransferTransactionInformation/UltimateDebtor is present, then UltimateDebtor is not
allowed.
CreditTransferTransactionInformation/UltimateDebtor and UltimateDebtor may both be absent.
Following Must be True
    /UltimateDebtor Must be absent
 Or    /CreditTransferTransactionInformation[*]/UltimateDebtor Must be absent
2.4.2.1  PaymentInformationIdentification <PmtInfId>
Presence: [1..1]
Definition: Unique identification, as assigned by a sending party, to unambiguously identify the payment
information group within the message.
Datatype: "Max35Text" on page 609
2.4.2.2  PaymentMethod <PmtMtd>
Presence: [1..1]
Definition: Specifies the means of payment that will be used to move the amount of money.
Datatype: "PaymentMethod3Code" on page 599
CodeName Name Definition
CHK Cheque Written order to a bank to pay a certain
amount of money from one person to
another person.
TRF CreditTransfer Transfer of an amount of money in the
books of the account servicer.
TRA TransferAdvice Transfer of an amount of money in the
books of the account servicer. An advice
should be sent back to the account
owner.
2.4.2.3  RequestedAdviceType <ReqdAdvcTp>
Presence: [0..1]
Definition: Type of advice details requested.
Approved by the Payments SEG on 12 January 2026 pain.001.001.13
CustomerCreditTransferInitiationV13
Payments Initiation - Maintenance 2025 - 2026 33 March 2026
```

