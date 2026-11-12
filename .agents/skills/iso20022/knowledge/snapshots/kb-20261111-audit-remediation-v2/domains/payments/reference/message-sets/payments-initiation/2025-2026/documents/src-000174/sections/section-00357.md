---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Initiation"
source_ids: ["src-000174"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["4 pain.007.001.13 CustomerPaymentReversalV13", "5.4 Message Building Blocks", "5.4.2.18 DirectDebitTransactionInformation <DrctDbtTxInf>", "5.4.2.18.17 RemittanceInformation <RmtInf>", "5.4.2.18.17.2 Structured <Strd>", "5.4.2.18.17.2.3 CreditorReferenceInformation <CdtrRefInf>", "5.4.2.18.17.2.3.1 Type <Tp>", "5.4.2.18.17.2.3.1.2 Issuer <Issr>"]
file_pages: [506]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pain.008.001.12"]
---

# 5.4.2.18.17.2.3.1.2 Issuer <Issr>

Source: [src-000174](../../../../../../../../../evidence/omitted/577241d5215d98d6ed689f57.md). Locator: one-based file pages 506 to 506.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 506

```text
Definition: Type of creditor reference, in a proprietary form.
Datatype: "Max35Text" on page 609
5.4.2.18.17.2.3.1.2  Issuer <Issr>
Presence: [0..1]
Definition: Entity that assigns the credit reference type.
Datatype: "Max35Text" on page 609
5.4.2.18.17.2.3.2  Reference <Ref>
Presence: [0..1]
Definition: Unique reference, as assigned by the creditor, to unambiguously refer to the payment
transaction.
Usage: If available, the initiating party should provide this reference in the structured remittance
information, to enable reconciliation by the creditor upon receipt of the amount of money.
If the business context requires the use of a creditor reference or a payment remit identification, and
only one identifier can be passed through the end-to-end chain, the creditor's reference or payment
remittance identification should be quoted in the end-to-end transaction identification.
Datatype: "Max35Text" on page 609
5.4.2.18.17.2.4  Invoicer <Invcr>
Presence: [0..1]
Definition: Identification of the organisation issuing the invoice, when it is different from the creditor or
ultimate creditor.
Approved by the Payments SEG on 12 January 2026 pain.008.001.12 CustomerDirectDebitInitiationV12
Payments Initiation - Maintenance 2025 - 2026 506 March 2026
```

