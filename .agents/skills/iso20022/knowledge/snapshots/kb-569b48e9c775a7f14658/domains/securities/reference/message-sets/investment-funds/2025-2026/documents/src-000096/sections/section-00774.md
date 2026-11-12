---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["35 sese.012.001.12 PortfolioTransferInstructionV12", "35.4 Message Building Blocks", "35.4.12 NomineeAccount <NmneeAcct>", "35.4.14.10 FinancialInstrumentAssetForTransfer <FinInstrmAsstForTrf>", "35.4.14.10.9 UnitsDetails <UnitsDtls>", "35.4.14.10.9.9 OtherAmount <OthrAmt>", "35.4.14.10.9.9.1 Type <Tp>"]
file_pages: [1058]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.012.001.12"]
---

# 35.4.14.10.9.9.1 Type <Tp>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 1058 to 1058.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1058

```text
OtherAmount <OthrAmt> contains the following OtherAmount1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Type <Tp> [1..1]  1058
{Or     Code <Cd> [1..1] CodeSet 1058
Or}     ProprietaryCode <PrtryCd> [1..1] ± 1058
   Amount <Amt> [1..1] Amount C1, C18 1058
35.4.14.10.9.9.1  Type <Tp>
Presence: [1..1]
Definition: Type of amount.
Type <Tp> contains one of the following OtherAmountType1Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 1058
Or}   ProprietaryCode <PrtryCd> [1..1] ± 1058
35.4.14.10.9.9.1.1  Code <Cd>
Presence: [1..1]
Definition: Type of amount expressed as a code.
Datatype: "OtherAmountType1Code" on page 5334
CodeName Name Definition
PINT PrepaidInterest Interest that was pre-paid.
SINT SettlementInterest Interest on the interest.
35.4.14.10.9.9.1.2  ProprietaryCode <PrtryCd>
Presence: [1..1]
Definition: Type of amount expressed as a proprietary code.
ProprietaryCode <PrtryCd> contains the following elements (see "GenericIdentification1" on
page 4552 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 4552
   SchemeName <SchmeNm> [0..1] Text 4552
   Issuer <Issr> [0..1] Text 4552
35.4.14.10.9.9.2  Amount <Amt>
Presence: [1..1]
Definition: Currency and amount.
Approved by the Securities SEG on 27 January 2026 sese.012.001.12 PortfolioTransferInstructionV12
Investment Funds - Maintenance 2025 - 2026 1058 May 2026
```

