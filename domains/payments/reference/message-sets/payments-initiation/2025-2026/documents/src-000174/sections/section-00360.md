---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Initiation"
source_ids: ["src-000174"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["4 pain.007.001.13 CustomerPaymentReversalV13", "5.4 Message Building Blocks", "5.4.2.18 DirectDebitTransactionInformation <DrctDbtTxInf>", "5.4.2.18.17 RemittanceInformation <RmtInf>", "5.4.2.18.17.2 Structured <Strd>", "5.4.2.18.17.2.6 TaxRemittance <TaxRmt>", "5.4.2.18.17.2.6.1 Creditor <Cdtr>"]
file_pages: [510]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pain.008.001.12"]
---

# 5.4.2.18.17.2.6.1 Creditor <Cdtr>

Source: [src-000174](../../../../../../../../../raw-input/payments_initiation/ISO20022_MDRPart2_PaymentsInitiation_2025_2026_v1.pdf). Locator: one-based file pages 510 to 510.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 510

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
     AdditionalInformation <AddtlInf> [0..1] Text 519
5.4.2.18.17.2.6.1  Creditor <Cdtr>
Presence: [0..1]
Definition: Party on the credit side of the transaction to which the tax applies.
Creditor <Cdtr> contains the following elements (see "TaxParty1" on page 584 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   TaxIdentification <TaxId> [0..1] Text 584
   RegistrationIdentification <RegnId> [0..1] Text 584
   TaxType <TaxTp> [0..1] Text 584
5.4.2.18.17.2.6.2  Debtor <Dbtr>
Presence: [0..1]
Definition: Party on the debit side of the transaction to which the tax applies.
Debtor <Dbtr> contains the following elements (see "TaxParty2" on page 583 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   TaxIdentification <TaxId> [0..1] Text 583
   RegistrationIdentification <RegnId> [0..1] Text 583
   TaxType <TaxTp> [0..1] Text 583
   Authorisation <Authstn> [0..1]  584
     Title <Titl> [0..1] Text 584
     Name <Nm> [0..1] Text 584
5.4.2.18.17.2.6.3  UltimateDebtor <UltmtDbtr>
Presence: [0..1]
Definition: Ultimate party that owes an amount of money to the (ultimate) creditor, in this case, to the
taxing authority.
Approved by the Payments SEG on 12 January 2026 pain.008.001.12 CustomerDirectDebitInitiationV12
Payments Initiation - Maintenance 2025 - 2026 510 March 2026
```

