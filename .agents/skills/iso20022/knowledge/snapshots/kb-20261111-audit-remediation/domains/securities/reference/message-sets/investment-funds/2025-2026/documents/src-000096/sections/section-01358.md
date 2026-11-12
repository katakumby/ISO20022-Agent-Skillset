---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["37 sese.014.001.09 PortfolioTransferCancellationRequestV09", "41.4 Message Building Blocks", "41.4.4.12 BulkCashSettlementDetails <BlkCshSttlmDtls>", "41.4.4.12.1 PaymentInstrument <PmtInstrm>", "41.4.4.12.1.5 BlockChainCashWallet <BlckChainCshWllt>"]
file_pages: [1885]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.001.001.05"]
---

# 41.4.4.12.1.5 BlockChainCashWallet <BlckChainCshWllt>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 1885 to 1885.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1885

```text
Type <Tp> contains one of the following elements (see "InvestmentAccountType1Choice" on
page 4556 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 4556
Or}   Proprietary <Prtry> [1..1] ± 4556
41.4.4.12.1.5  BlockChainCashWallet <BlckChainCshWllt>
Presence: [1..1]
Definition: Block Chain Wallet where digital currencies are maintained. This is the equivalent of cash
account for digital currencies.
BlockChainCashWallet <BlckChainCshWllt> contains the following BlockChainAddressWallet14
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 1885
   Type <Tp> [0..1] ± 1885
   Name <Nm> [0..1] Text 1885
   DigitalLedgerIdentification <DgtlLdgrId> [1..1] IdentifierSet 1886
41.4.4.12.1.5.1  Identification <Id>
Presence: [1..1]
Definition: Unambiguous identification for the account between the account owner and the account
servicer.
Datatype: "Max140Text" on page 5402
41.4.4.12.1.5.2  Type <Tp>
Presence: [0..1]
Definition: Specifies the type of securities account.
Type <Tp> contains the following elements (see "GenericIdentification30" on page 4552 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 4552
   Issuer <Issr> [1..1] Text 4552
   SchemeName <SchmeNm> [0..1] Text 4553
41.4.4.12.1.5.3  Name <Nm>
Presence: [0..1]
Definition: Description of the account.
Datatype: "Max70Text" on page 5404
Approved by the Securities SEG on 27 January 2026 setr.001.001.05 RedemptionBulkOrderV05
Investment Funds - Maintenance 2025 - 2026 1885 May 2026
```

