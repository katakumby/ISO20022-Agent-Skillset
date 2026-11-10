---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["24 sese.001.001.10 TransferOutInstructionV10", "24.4 Message Building Blocks", "24.4.5 MasterReference <MstrRef>", "24.4.6.10 FinancialInstrumentDetails <FinInstrmDtls>"]
file_pages: [452]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.001.001.10"]
---

# 24.4.6.10 FinancialInstrumentDetails <FinInstrmDtls>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 452 to 452.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 452

```text
24.4.6.10  FinancialInstrumentDetails <FinInstrmDtls>
Presence: [1..1]
Definition: Information related to the financial instrument to be transferred.
Impacted by: C19 "IdentificationGuideline"
FinancialInstrumentDetails <FinInstrmDtls> contains the following FinancialInstrument116
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1]  453
{Or     ISIN <ISIN> [1..1] IdentifierSet 453
Or     SEDOL <SEDOL> [1..1] IdentifierSet 454
Or     CUSIP <CUSIP> [1..1] IdentifierSet 454
Or     RIC <RIC> [1..1] IdentifierSet 454
Or     TickerSymbol <TckrSymb> [1..1] IdentifierSet 454
Or     Bloomberg <Blmbrg> [1..1] IdentifierSet 454
Or     CTA <CTA> [1..1] IdentifierSet 454
Or     QUICK <QUICK> [1..1] IdentifierSet 454
Or     Wertpapier <Wrtppr> [1..1] IdentifierSet 455
Or     Dutch <Dtch> [1..1] IdentifierSet 455
Or     Valoren <Vlrn> [1..1] IdentifierSet 455
Or     Sicovam <SCVM> [1..1] IdentifierSet 455
Or     Belgian <Belgn> [1..1] IdentifierSet 455
Or     Common <Cmon> [1..1] IdentifierSet 455
Or     DTI <DTI> [1..1] IdentifierSet 455
Or}     OtherProprietaryIdentification <OthrPrtryId> [1..1]  455
       Identification <Id> [1..1] Text 456
       IdentificationSource <IdSrc> [1..1] ± 456
   Name <Nm> [0..1] Text 456
   ShortName <ShrtNm> [0..1] Text 456
   SupplementaryIdentification <SplmtryId> [0..1] Text 456
   ClassType <ClssTp> [0..1] Text 456
   SecuritiesForm <SctiesForm> [0..1] CodeSet 457
   DistributionPolicy <DstrbtnPlcy> [0..1] CodeSet 457
   DematerialisedIndicator <DmtrlsdInd> [0..1] Indicator 457
Approved by the Securities SEG on 27 January 2026 sese.001.001.10 TransferOutInstructionV10
Investment Funds - Maintenance 2025 - 2026 452 May 2026
```

