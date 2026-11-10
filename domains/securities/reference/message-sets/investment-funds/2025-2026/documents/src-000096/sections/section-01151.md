---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["37 sese.014.001.09 PortfolioTransferCancellationRequestV09", "40.4 Message Building Blocks", "40.4.14 Transferee <Trfee>", "40.4.15.11 FinancialInstrumentAssetForTransfer <FinInstrmAsstForTrf>", "40.4.15.11.9 Conversion <Convs>", "40.4.15.11.9.1 OriginalSecurity <OrgnlScty>"]
file_pages: [1608]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.043.001.02"]
---

# 40.4.15.11.9.1 OriginalSecurity <OrgnlScty>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 1608 to 1608.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1608

```text
Conversion <Convs> contains the following Conversion6 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   OriginalSecurity <OrgnlScty> [1..1]  C30 1608
     Identification <Id> [1..1]  1609
{Or       ISIN <ISIN> [1..1] IdentifierSet 1610
Or       SEDOL <SEDOL> [1..1] IdentifierSet 1610
Or       CUSIP <CUSIP> [1..1] IdentifierSet 1611
Or       RIC <RIC> [1..1] IdentifierSet 1611
Or       TickerSymbol <TckrSymb> [1..1] IdentifierSet 1611
Or       Bloomberg <Blmbrg> [1..1] IdentifierSet 1611
Or       CTA <CTA> [1..1] IdentifierSet 1611
Or       QUICK <QUICK> [1..1] IdentifierSet 1611
Or       Wertpapier <Wrtppr> [1..1] IdentifierSet 1611
Or       Dutch <Dtch> [1..1] IdentifierSet 1612
Or       Valoren <Vlrn> [1..1] IdentifierSet 1612
Or       Sicovam <SCVM> [1..1] IdentifierSet 1612
Or       Belgian <Belgn> [1..1] IdentifierSet 1612
Or       Common <Cmon> [1..1] IdentifierSet 1612
Or       DTI <DTI> [1..1] IdentifierSet 1612
Or}       OtherProprietaryIdentification <OthrPrtryId> [1..1]  1612
         Identification <Id> [1..1] Text 1613
         IdentificationSource <IdSrc> [1..1] ± 1613
     Name <Nm> [0..1] Text 1613
     ShortName <ShrtNm> [0..1] Text 1613
   AdditionalInformation <AddtlInf> [0..*] ± 1613
40.4.15.11.9.1  OriginalSecurity <OrgnlScty>
Presence: [1..1]
Definition: Identification of the original security.
Impacted by: C30 "IdentificationGuideline"
Approved by the Securities SEG on 27 January 2026 sese.043.001.02 PortfolioTransferCompletionV02
Investment Funds - Maintenance 2025 - 2026 1608 May 2026
```

