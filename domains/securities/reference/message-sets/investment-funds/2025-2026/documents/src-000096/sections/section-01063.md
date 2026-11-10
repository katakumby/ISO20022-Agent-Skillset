---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["37 sese.014.001.09 PortfolioTransferCancellationRequestV09", "39.4 Message Building Blocks", "39.4.7 SecondaryIndividualInvestor <ScndryIndvInvstr>", "39.4.15.4 FinancialInstrumentAssetForTransfer <FinInstrmAsstForTrf>", "39.4.15.4.2 Instrument <Instrm>", "39.4.15.4.2.1 Security <Scty>", "39.4.15.4.2.1.1 Identification <Id>"]
file_pages: [1470]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.019.001.09"]
---

# 39.4.15.4.2.1.1 Identification <Id>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 1470 to 1470.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1470

```text
Security <Scty> contains the following FinancialInstrumentIdentification11 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1]  1470
{Or     ISIN <ISIN> [1..1] IdentifierSet 1471
Or     SEDOL <SEDOL> [1..1] IdentifierSet 1471
Or     CUSIP <CUSIP> [1..1] IdentifierSet 1472
Or     RIC <RIC> [1..1] IdentifierSet 1472
Or     TickerSymbol <TckrSymb> [1..1] IdentifierSet 1472
Or     Bloomberg <Blmbrg> [1..1] IdentifierSet 1472
Or     CTA <CTA> [1..1] IdentifierSet 1472
Or     QUICK <QUICK> [1..1] IdentifierSet 1472
Or     Wertpapier <Wrtppr> [1..1] IdentifierSet 1472
Or     Dutch <Dtch> [1..1] IdentifierSet 1473
Or     Valoren <Vlrn> [1..1] IdentifierSet 1473
Or     Sicovam <SCVM> [1..1] IdentifierSet 1473
Or     Belgian <Belgn> [1..1] IdentifierSet 1473
Or     Common <Cmon> [1..1] IdentifierSet 1473
Or     DTI <DTI> [1..1] IdentifierSet 1473
Or}     OtherProprietaryIdentification <OthrPrtryId> [1..1]  1473
       Identification <Id> [1..1] Text 1474
       IdentificationSource <IdSrc> [1..1] ± 1474
   Name <Nm> [0..1] Text 1474
   ShortName <ShrtNm> [0..1] Text 1474
   ClassificationType <ClssfctnTp> [0..1] ± 1474
Constraints
• IdentificationGuideline
When an ISIN code exists, it is strongly recommended that the ISIN be used.
39.4.15.4.2.1.1  Identification <Id>
Presence: [1..1]
Definition: Unique and unambiguous identifier of a security, assigned under a formal or proprietary
identification scheme.
Approved by the Securities SEG on 27 January 2026 sese.019.001.09
AccountHoldingInformationRequestV09
Investment Funds - Maintenance 2025 - 2026 1470 May 2026
```

