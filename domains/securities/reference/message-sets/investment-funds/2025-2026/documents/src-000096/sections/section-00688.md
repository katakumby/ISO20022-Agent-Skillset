---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["33 sese.010.001.07 TransferCancellationStatusReportV07", "34.4 Message Building Blocks", "34.4.4 StatusReport <StsRpt>", "34.4.4.21 DrawdownTranche <DrwdwnTrch>", "34.4.4.21.3 ApplicableRules <AplblRules>", "34.4.4.21.3.1 Code <Cd>"]
file_pages: [930]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.011.001.10"]
---

# 34.4.4.21.3.1 Code <Cd>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 930 to 930.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 930

```text
ApplicableRules <AplblRules> contains one of the following ApplicableRules1Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 930
Or}   Proprietary <Prtry> [1..1] ± 930
34.4.4.21.3.1  Code <Cd>
Presence: [1..1]
Definition: Applicable rules expressed as a code.
Datatype: "ApplicableRules1Code" on page 5277
CodeName Name Definition
NPRE NotPreADay Pre A Day rules do not apply.
YPRE PreADay Pre A Day rules applies.
34.4.4.21.3.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Applicable rules expressed as a proprietary code.
Proprietary <Prtry> contains the following elements (see "GenericIdentification36" on page 4549 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 4549
   Issuer <Issr> [1..1] Text 4550
   SchemeName <SchmeNm> [0..1] Text 4550
34.4.4.21.4  InvestorTaxReference <InvstrTaxRef>
Presence: [0..1]
Definition: Identification of the investor as assigned by a tax authority.
InvestorTaxReference <InvstrTaxRef> contains the following TaxReference2 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Type <Tp> [0..1]  930
{Or     Code <Cd> [1..1] CodeSet 931
Or}     Proprietary <Prtry> [1..1] ± 931
   Reference <Ref> [1..1] Text 931
34.4.4.21.4.1  Type <Tp>
Presence: [0..1]
Definition: Type of tax reference.
Approved by the Securities SEG on 27 January 2026 sese.011.001.10
TransferInstructionStatusReportV10
Investment Funds - Maintenance 2025 - 2026 930 May 2026
```

