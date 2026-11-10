---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["35 sese.012.001.12 PortfolioTransferInstructionV12", "36.4 Message Building Blocks", "36.4.12 TransferorAccount <TrfrAcct>", "36.4.15.11 FinancialInstrumentAssetForTransfer <FinInstrmAsstForTrf>", "36.4.15.11.26 PaymentDetails <PmtDtls>", "36.4.15.11.26.2 CreditTransferDetails <CdtTrfDtls>", "36.4.15.11.26.2.12 CreditorAccount <CdtrAcct>", "36.4.15.11.26.2.12.3 BlockChainCashWallet <BlckChainCshWllt>"]
file_pages: [1287]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.013.001.12"]
---

# 36.4.15.11.26.2.12.3 BlockChainCashWallet <BlckChainCshWllt>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 1287 to 1287.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1287

```text
Constraints
• IBAN
A valid IBAN consists of all three of the following components: Country Code, check digits and
BBAN.
36.4.15.11.26.2.12.3  BlockChainCashWallet <BlckChainCshWllt>
Presence: [0..1]
Definition: Block Chain Wallet where digital currencies are maintained. This is the equivalent of cash
account for digital currencies.
BlockChainCashWallet <BlckChainCshWllt> contains the following elements (see
"BlockChainAddressWallet3" on page 4846 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 4846
   Type <Tp> [0..1] ± 4846
   Name <Nm> [0..1] Text 4846
36.4.15.11.26.2.12.4  Other <Othr>
Presence: [0..1]
Definition: Unique identification of the account, as assigned by the account servicer, using an
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
36.4.15.11.27  CrystallisationDetails <CrstllstnDtls>
Presence: [0..*]
Definition: Number of units that have been received (crystallised) or not yet received (uncrystallised)
from the fund. This is typically relevant to a pension fund.
Approved by the Securities SEG on 27 January 2026 sese.013.001.12 PortfolioTransferConfirmationV12
Investment Funds - Maintenance 2025 - 2026 1287 May 2026
```

