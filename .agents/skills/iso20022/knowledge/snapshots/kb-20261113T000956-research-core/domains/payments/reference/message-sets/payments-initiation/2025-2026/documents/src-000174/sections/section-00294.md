---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Initiation"
source_ids: ["src-000174"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["4 pain.007.001.13 CustomerPaymentReversalV13", "5.4 Message Building Blocks", "5.4.2.1 PaymentInformationIdentification <PmtInfId>"]
file_pages: [426]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pain.008.001.12"]
---

# 5.4.2.1 PaymentInformationIdentification <PmtInfId>

Source: [src-000174](../../../../../../../../../evidence/omitted/577241d5215d98d6ed689f57.md). Locator: one-based file pages 426 to 426.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 426

```text
Following Must be True
    /DirectDebitTransactionInformation[*]/PaymentTypeInformation Must be absent
• UltimateCreditorGuideline
UltimateCreditor may only be present if different from Creditor.
• UltimateCreditorRule
If UltimateCreditor is present, then DirectDebitTransactionInformation/UltimateCreditor is not
allowed.
If DirectDebitTransactionInformation/UltimateCreditor is present, then UltimateCreditor is not
allowed.
DirectDebitTransactionInformation/UltimateCreditor and UltimateCreditor may both be absent.
Following Must be True
    /UltimateCreditor Must be absent
 Or    /DirectDebitTransactionInformation[*]/UltimateCreditor Must be absent
5.4.2.1  PaymentInformationIdentification <PmtInfId>
Presence: [1..1]
Definition: Unique identification, as assigned by a sending party, to unambiguously identify the payment
information group within the message.
Datatype: "Max35Text" on page 609
5.4.2.2  PaymentMethod <PmtMtd>
Presence: [1..1]
Definition: Specifies the means of payment that will be used to move the amount of money.
Datatype: "PaymentMethod2Code" on page 599
CodeName Name Definition
DD DirectDebit Collection of an amount of money from
the debtor's bank account by the
creditor. The amount of money and
dates of collections may vary.
5.4.2.3  RequestedAdviceType <ReqdAdvcTp>
Presence: [0..1]
Definition: Type of advice details requested.
Approved by the Payments SEG on 12 January 2026 pain.008.001.12 CustomerDirectDebitInitiationV12
Payments Initiation - Maintenance 2025 - 2026 426 March 2026
```

