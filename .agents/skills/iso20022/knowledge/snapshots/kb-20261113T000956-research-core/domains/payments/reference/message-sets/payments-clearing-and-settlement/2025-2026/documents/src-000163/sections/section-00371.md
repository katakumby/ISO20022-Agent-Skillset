---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000163"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["4 pacs.004.001.15 PaymentReturnV15", "4.4 Message Building Blocks", "4.4.1 GroupHeader <GrpHdr>", "4.4.3.27 OriginalTransactionReference <OrgnlTxRef>", "4.4.3.27.23 UnderlyingCustomerCreditTransfer <UndrlygCstmrCdtTrf>", "4.4.3.27.23.30 RemittanceInformation <RmtInf>", "4.4.3.27.23.30.2 Structured <Strd>", "4.4.3.27.23.30.2.6 TaxRemittance <TaxRmt>", "4.4.3.27.23.30.2.6.1 Creditor <Cdtr>"]
file_pages: [514]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pacs.004.001.15"]
---

# 4.4.3.27.23.30.2.6.1 Creditor <Cdtr>

Source: [src-000163](../../../../../../../../../evidence/omitted/0b754f3040fa67a0a084bf38.md). Locator: one-based file pages 514 to 514.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 514

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
     AdditionalInformation <AddtlInf> [0..1] Text 523
4.4.3.27.23.30.2.6.1  Creditor <Cdtr>
Presence: [0..1]
Definition: Party on the credit side of the transaction to which the tax applies.
Creditor <Cdtr> contains the following elements (see "TaxParty1" on page 1222 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   TaxIdentification <TaxId> [0..1] Text 1222
   RegistrationIdentification <RegnId> [0..1] Text 1222
   TaxType <TaxTp> [0..1] Text 1222
4.4.3.27.23.30.2.6.2  Debtor <Dbtr>
Presence: [0..1]
Definition: Party on the debit side of the transaction to which the tax applies.
Debtor <Dbtr> contains the following elements (see "TaxParty2" on page 1221 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   TaxIdentification <TaxId> [0..1] Text 1221
   RegistrationIdentification <RegnId> [0..1] Text 1221
   TaxType <TaxTp> [0..1] Text 1221
   Authorisation <Authstn> [0..1]  1221
     Title <Titl> [0..1] Text 1222
     Name <Nm> [0..1] Text 1222
4.4.3.27.23.30.2.6.3  UltimateDebtor <UltmtDbtr>
Presence: [0..1]
Definition: Ultimate party that owes an amount of money to the (ultimate) creditor, in this case, to the
taxing authority.
Approved by the Payments SEG on 12 January 2026 pacs.004.001.15 PaymentReturnV15
Payments Clearing and Settlement - Maintenance 2025 -
2026
514 March 2026
```

