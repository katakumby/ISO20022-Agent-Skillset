---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000163"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["3 pacs.003.001.12 FIToFICustomerDirectDebitV12", "3.4 Message Building Blocks", "3.4.2 DirectDebitTransactionInformation <DrctDbtTxInf>", "3.4.2.35 RemittanceInformation <RmtInf>", "3.4.2.35.2 Structured <Strd>", "3.4.2.35.2.3 CreditorReferenceInformation <CdtrRefInf>", "3.4.2.35.2.3.1 Type <Tp>", "3.4.2.35.2.3.1.2 Issuer <Issr>"]
file_pages: [225]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pacs.003.001.12"]
---

# 3.4.2.35.2.3.1.2 Issuer <Issr>

Source: [src-000163](../../../../../../../../../raw-input/payments_clearing_and_settlement/ISO20022_MDRPart2_PaymentsClearingandSettlement_2025_2026_v1.pdf). Locator: one-based file pages 225 to 225.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 225

```text
Definition: Type of creditor reference, in a proprietary form.
Datatype: "Max35Text" on page 1246
3.4.2.35.2.3.1.2  Issuer <Issr>
Presence: [0..1]
Definition: Entity that assigns the credit reference type.
Datatype: "Max35Text" on page 1246
3.4.2.35.2.3.2  Reference <Ref>
Presence: [0..1]
Definition: Unique reference, as assigned by the creditor, to unambiguously refer to the payment
transaction.
Usage: If available, the initiating party should provide this reference in the structured remittance
information, to enable reconciliation by the creditor upon receipt of the amount of money.
If the business context requires the use of a creditor reference or a payment remit identification, and
only one identifier can be passed through the end-to-end chain, the creditor's reference or payment
remittance identification should be quoted in the end-to-end transaction identification.
Datatype: "Max35Text" on page 1246
3.4.2.35.2.4  Invoicer <Invcr>
Presence: [0..1]
Definition: Identification of the organisation issuing the invoice, when it is different from the creditor or
ultimate creditor.
Approved by the Payments SEG on 12 January 2026 pacs.003.001.12 FIToFICustomerDirectDebitV12
Payments Clearing and Settlement - Maintenance 2025 -
2026
225 March 2026
```

