---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["30 sese.007.001.10 TransferInConfirmationV10", "30.4 Message Building Blocks", "30.4.4 RelatedReference <RltdRef>", "30.4.7.16 UnitsDetails <UnitsDtls>", "30.4.7.16.9 OtherAmount <OthrAmt>", "30.4.7.16.9.1 Type <Tp>"]
file_pages: [745]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.007.001.10"]
---

# 30.4.7.16.9.1 Type <Tp>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 745 to 745.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 745

```text
OtherAmount <OthrAmt> contains the following OtherAmount1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Type <Tp> [1..1]  745
{Or     Code <Cd> [1..1] CodeSet 745
Or}     ProprietaryCode <PrtryCd> [1..1] ± 745
   Amount <Amt> [1..1] Amount C1, C10 745
30.4.7.16.9.1  Type <Tp>
Presence: [1..1]
Definition: Type of amount.
Type <Tp> contains one of the following OtherAmountType1Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 745
Or}   ProprietaryCode <PrtryCd> [1..1] ± 745
30.4.7.16.9.1.1  Code <Cd>
Presence: [1..1]
Definition: Type of amount expressed as a code.
Datatype: "OtherAmountType1Code" on page 5334
CodeName Name Definition
PINT PrepaidInterest Interest that was pre-paid.
SINT SettlementInterest Interest on the interest.
30.4.7.16.9.1.2  ProprietaryCode <PrtryCd>
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
30.4.7.16.9.2  Amount <Amt>
Presence: [1..1]
Definition: Currency and amount.
Approved by the Securities SEG on 27 January 2026 sese.007.001.10 TransferInConfirmationV10
Investment Funds - Maintenance 2025 - 2026 745 May 2026
```

