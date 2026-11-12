---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["37 sese.014.001.09 PortfolioTransferCancellationRequestV09", "46.4 Message Building Blocks", "46.4.5 MultipleExecutionDetails <MltplExctnDtls>", "46.4.5.10 IndividualExecutionDetails <IndvExctnDtls>", "46.4.5.10.33 CashSettlementDetails <CshSttlmDtls>", "46.4.5.10.33.1 PaymentInstrument <PmtInstrm>", "46.4.5.10.33.1.5 BlockChainCashWallet <BlckChainCshWllt>"]
file_pages: [2457]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.006.001.06"]
---

# 46.4.5.10.33.1.5 BlockChainCashWallet <BlckChainCshWllt>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 2457 to 2457.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2457

```text
Type <Tp> contains one of the following elements (see "InvestmentAccountType1Choice" on
page 4556 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 4556
Or}   Proprietary <Prtry> [1..1] ± 4556
46.4.5.10.33.1.5  BlockChainCashWallet <BlckChainCshWllt>
Presence: [1..1]
Definition: Block Chain Wallet where digital currencies are maintained. This is the equivalent of cash
account for digital currencies.
BlockChainCashWallet <BlckChainCshWllt> contains the following BlockChainAddressWallet14
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 2457
   Type <Tp> [0..1] ± 2457
   Name <Nm> [0..1] Text 2457
   DigitalLedgerIdentification <DgtlLdgrId> [1..1] IdentifierSet 2458
46.4.5.10.33.1.5.1  Identification <Id>
Presence: [1..1]
Definition: Unambiguous identification for the account between the account owner and the account
servicer.
Datatype: "Max140Text" on page 5402
46.4.5.10.33.1.5.2  Type <Tp>
Presence: [0..1]
Definition: Specifies the type of securities account.
Type <Tp> contains the following elements (see "GenericIdentification30" on page 4552 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 4552
   Issuer <Issr> [1..1] Text 4552
   SchemeName <SchmeNm> [0..1] Text 4553
46.4.5.10.33.1.5.3  Name <Nm>
Presence: [0..1]
Definition: Description of the account.
Datatype: "Max70Text" on page 5404
Approved by the Securities SEG on 27 January 2026 setr.006.001.06 RedemptionOrderConfirmationV06
Investment Funds - Maintenance 2025 - 2026 2457 May 2026
```

