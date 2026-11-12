---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["53 setr.013.001.05 SwitchOrderV05", "53.4 Message Building Blocks", "53.4.5 SwitchOrderDetails <SwtchOrdrDtls>", "53.4.5.18 CashSettlementDetails <CshSttlmDtls>", "53.4.5.18.1 CashInOrOut <CshInOrOut>", "53.4.5.18.1.2 CashOutPaymentInstrument <CshOutPmtInstrm>", "53.4.5.18.1.2.1 CreditTransferDetails <CdtTrfDtls>", "53.4.5.18.1.2.1.9 IntermediaryAgent2Account <IntrmyAgt2Acct>", "53.4.5.18.1.2.1.9.1 Identification <Id>", "53.4.5.18.1.2.1.9.1.2 BlockChainCashWallet <BlckChainCshWllt>"]
file_pages: [3774]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.013.001.05"]
---

# 53.4.5.18.1.2.1.9.1.2 BlockChainCashWallet <BlckChainCshWllt>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 3774 to 3774.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3774

```text
Constraints
• IBAN
A valid IBAN consists of all three of the following components: Country Code, check digits and
BBAN.
53.4.5.18.1.2.1.9.1.2  BlockChainCashWallet <BlckChainCshWllt>
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
53.4.5.18.1.2.1.9.1.3  Other <Othr>
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
53.4.5.18.1.2.1.9.2  Name <Nm>
Presence: [0..1]
Definition: Name of the account. It provides an additional means of identification, and is designated by
the account servicer in agreement with the account owner.
Datatype: "Max35Text" on page 5403
53.4.5.18.1.2.1.10  CreditorAgent <CdtrAgt>
Presence: [1..1]
Definition: Financial institution servicing an account for the creditor.
Approved by the Securities SEG on 27 January 2026 setr.013.001.05 SwitchOrderV05
Investment Funds - Maintenance 2025 - 2026 3774 May 2026
```

