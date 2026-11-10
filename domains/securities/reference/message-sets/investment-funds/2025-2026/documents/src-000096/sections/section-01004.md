---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["37 sese.014.001.09 PortfolioTransferCancellationRequestV09", "38.4 Message Building Blocks", "38.4.10 SecondaryCorporateInvestor <ScndryCorpInvstr>", "38.4.15.8 FinancialInstrumentAssetForTransfer <FinInstrmAsstForTrf>", "38.4.15.8.2 Instrument <Instrm>", "38.4.15.8.2.1 Security <Scty>", "38.4.15.8.2.1.6 AlternateSecurity <AltrnScty>", "38.4.15.8.2.1.6.5 AlternateSecurityType <AltrnSctyTp>"]
file_pages: [1393]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.018.001.10"]
---

# 38.4.15.8.2.1.6.5 AlternateSecurityType <AltrnSctyTp>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 1393 to 1393.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1393

```text
ClassificationType <ClssfctnTp> contains one of the following elements (see
"ClassificationType32Choice" on page 4816 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   ClassificationFinancialInstrument <ClssfctnFinInstrm> [1..1] IdentifierSet 4816
Or}   AlternateClassification <AltrnClssfctn> [1..1] ± 4816
38.4.15.8.2.1.6.5  AlternateSecurityType <AltrnSctyTp>
Presence: [0..1]
Definition: Type of security offered in place of a restricted security, for example, common.
AlternateSecurityType <AltrnSctyTp> contains the following elements (see "GenericIdentification1"
on page 4552 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 4552
   SchemeName <SchmeNm> [0..1] Text 4552
   Issuer <Issr> [0..1] Text 4552
38.4.15.8.2.2  CashAsset <CshAsst>
Presence: [1..1]
Definition: Identification of the cash asset.
CashAsset <CshAsst> contains the following elements (see "CashAsset2" on page 4527 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   CashAssetType <CshAsstTp> [1..1]  4527
{Or     Code <Cd> [1..1] CodeSet 4527
Or}     Proprietary <Prtry> [1..1] ± 4528
   HoldingCurrency <HldgCcy> [1..1] CodeSet C1 4528
   AdditionalInformation <AddtlInf> [0..1] ± 4528
38.4.15.8.2.3  OtherAsset <OthrAsst>
Presence: [1..1]
Definition: Identification of another kind of asset in the holding that is not a security or cash.
Approved by the Securities SEG on 27 January 2026 sese.018.001.10 AccountHoldingInformationV10
Investment Funds - Maintenance 2025 - 2026 1393 May 2026
```

