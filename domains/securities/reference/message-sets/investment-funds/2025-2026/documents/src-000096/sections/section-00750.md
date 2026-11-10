---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["35 sese.012.001.12 PortfolioTransferInstructionV12", "35.4 Message Building Blocks", "35.4.12 NomineeAccount <NmneeAcct>", "35.4.14.10 FinancialInstrumentAssetForTransfer <FinInstrmAsstForTrf>", "35.4.14.10.8 Conversion <Convs>", "35.4.14.10.8.1 TargetSecurity <TrgtScty>"]
file_pages: [1030]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.012.001.12"]
---

# 35.4.14.10.8.1 TargetSecurity <TrgtScty>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 1030 to 1030.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1030

```text
Conversion <Convs> contains the following Conversion5 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   TargetSecurity <TrgtScty> [1..1]  C28 1030
     Identification <Id> [1..1]  1031
{Or       ISIN <ISIN> [1..1] IdentifierSet 1032
Or       SEDOL <SEDOL> [1..1] IdentifierSet 1032
Or       CUSIP <CUSIP> [1..1] IdentifierSet 1033
Or       RIC <RIC> [1..1] IdentifierSet 1033
Or       TickerSymbol <TckrSymb> [1..1] IdentifierSet 1033
Or       Bloomberg <Blmbrg> [1..1] IdentifierSet 1033
Or       CTA <CTA> [1..1] IdentifierSet 1033
Or       QUICK <QUICK> [1..1] IdentifierSet 1033
Or       Wertpapier <Wrtppr> [1..1] IdentifierSet 1033
Or       Dutch <Dtch> [1..1] IdentifierSet 1034
Or       Valoren <Vlrn> [1..1] IdentifierSet 1034
Or       Sicovam <SCVM> [1..1] IdentifierSet 1034
Or       Belgian <Belgn> [1..1] IdentifierSet 1034
Or       Common <Cmon> [1..1] IdentifierSet 1034
Or       DTI <DTI> [1..1] IdentifierSet 1034
Or}       OtherProprietaryIdentification <OthrPrtryId> [1..1]  1034
         Identification <Id> [1..1] Text 1035
         IdentificationSource <IdSrc> [1..1] ± 1035
     Name <Nm> [0..1] Text 1035
     ShortName <ShrtNm> [0..1] Text 1035
   AdditionalInformation <AddtlInf> [0..*] ± 1035
35.4.14.10.8.1  TargetSecurity <TrgtScty>
Presence: [1..1]
Definition: Identification of the target security.
Impacted by: C28 "IdentificationGuideline"
Approved by the Securities SEG on 27 January 2026 sese.012.001.12 PortfolioTransferInstructionV12
Investment Funds - Maintenance 2025 - 2026 1030 May 2026
```

