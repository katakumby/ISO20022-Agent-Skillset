---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["37 sese.014.001.09 PortfolioTransferCancellationRequestV09", "40.4 Message Building Blocks", "40.4.14 Transferee <Trfee>", "40.4.15.11 FinancialInstrumentAssetForTransfer <FinInstrmAsstForTrf>", "40.4.15.11.2 Instrument <Instrm>", "40.4.15.11.2.1 Security <Scty>"]
file_pages: [1598]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.043.001.02"]
---

# 40.4.15.11.2.1 Security <Scty>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 1598 to 1598.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1598

```text
Instrument <Instrm> contains one of the following FinancialInstrument103Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Security <Scty> [1..1]  C29 1598
     Identification <Id> [1..1]  1599
{Or       ISIN <ISIN> [1..1] IdentifierSet 1600
Or       SEDOL <SEDOL> [1..1] IdentifierSet 1600
Or       CUSIP <CUSIP> [1..1] IdentifierSet 1601
Or       RIC <RIC> [1..1] IdentifierSet 1601
Or       TickerSymbol <TckrSymb> [1..1] IdentifierSet 1601
Or       Bloomberg <Blmbrg> [1..1] IdentifierSet 1601
Or       CTA <CTA> [1..1] IdentifierSet 1601
Or       QUICK <QUICK> [1..1] IdentifierSet 1601
Or       Wertpapier <Wrtppr> [1..1] IdentifierSet 1601
Or       Dutch <Dtch> [1..1] IdentifierSet 1602
Or       Valoren <Vlrn> [1..1] IdentifierSet 1602
Or       Sicovam <SCVM> [1..1] IdentifierSet 1602
Or       Belgian <Belgn> [1..1] IdentifierSet 1602
Or       Common <Cmon> [1..1] IdentifierSet 1602
Or       DTI <DTI> [1..1] IdentifierSet 1602
Or}       OtherProprietaryIdentification <OthrPrtryId> [1..1]  1602
         Identification <Id> [1..1] Text 1603
         IdentificationSource <IdSrc> [1..1] ± 1603
     Name <Nm> [0..1] Text 1603
     ShortName <ShrtNm> [0..1] Text 1603
     ClassificationType <ClssfctnTp> [0..1] ± 1603
Or   CashAsset <CshAsst> [1..1] ± C27 1603
Or}   OtherAsset <OthrAsst> [1..1] ± 1604
40.4.15.11.2.1  Security <Scty>
Presence: [1..1]
Definition: Identification of the security.
Impacted by: C29 "IdentificationGuideline"
Approved by the Securities SEG on 27 January 2026 sese.043.001.02 PortfolioTransferCompletionV02
Investment Funds - Maintenance 2025 - 2026 1598 May 2026
```

