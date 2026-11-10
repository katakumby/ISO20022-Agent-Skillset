---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["55 setr.015.001.05 SwitchOrderConfirmationV05", "55.4 Message Building Blocks", "55.4.4 RelatedReference <RltdRef>", "55.4.5.21 CashSettlementDetails <CshSttlmDtls>", "55.4.5.21.1 CashInOrOut <CshInOrOut>", "55.4.5.21.1.2 CashOutPaymentInstrument <CshOutPmtInstrm>", "55.4.5.21.1.2.1 CreditTransferDetails <CdtTrfDtls>", "55.4.5.21.1.2.1.11 CreditorAgentAccount <CdtrAgtAcct>", "55.4.5.21.1.2.1.11.1 Identification <Id>", "55.4.5.21.1.2.1.11.1.2 BlockChainCashWallet <BlckChainCshWllt>"]
file_pages: [4092]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.015.001.05"]
---

# 55.4.5.21.1.2.1.11.1.2 BlockChainCashWallet <BlckChainCshWllt>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 4092 to 4092.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4092

```text
Constraints
• IBAN
A valid IBAN consists of all three of the following components: Country Code, check digits and
BBAN.
55.4.5.21.1.2.1.11.1.2  BlockChainCashWallet <BlckChainCshWllt>
Presence: [1..1]
Definition: Digital account where digital assets or digital tokens can be stored and where an entry is
made.
BlockChainCashWallet <BlckChainCshWllt> contains the following elements (see
"BlockChainAddressWallet3" on page 4846 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 4846
   Type <Tp> [0..1] ± 4846
   Name <Nm> [0..1] Text 4846
55.4.5.21.1.2.1.11.1.3  Other <Othr>
Presence: [1..1]
Definition: Unique identification of an account, as assigned by the account servicer, using an
identification scheme.
Other <Othr> contains the following elements (see "GenericAccountIdentification1" on page 4326 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 4326
   SchemeName <SchmeNm> [0..1]  4326
{Or     Code <Cd> [1..1] CodeSet 4326
Or}     Proprietary <Prtry> [1..1] Text 4326
   Issuer <Issr> [0..1] Text 4326
55.4.5.21.1.2.1.11.2  Name <Nm>
Presence: [0..1]
Definition: Name of the account. It provides an additional means of identification, and is designated by
the account servicer in agreement with the account owner.
Datatype: "Max35Text" on page 5403
55.4.5.21.1.2.1.12  Creditor <Cdtr>
Presence: [0..1]
Definition: Party that receives an amount of money from the debtor. In the context of the payment
model, the creditor is also the credit account owner.
Approved by the Securities SEG on 27 January 2026 setr.015.001.05 SwitchOrderConfirmationV05
Investment Funds - Maintenance 2025 - 2026 4092 May 2026
```

