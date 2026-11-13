---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["33 sese.010.001.07 TransferCancellationStatusReportV07", "34.4 Message Building Blocks", "34.4.4 StatusReport <StsRpt>", "34.4.4.21 DrawdownTranche <DrwdwnTrch>", "34.4.4.21.4 InvestorTaxReference <InvstrTaxRef>", "34.4.4.21.4.1 Type <Tp>", "34.4.4.21.4.1.1 Code <Cd>"]
file_pages: [931]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.011.001.10"]
---

# 34.4.4.21.4.1.1 Code <Cd>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 931 to 931.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 931

```text
Type <Tp> contains one of the following TaxReferenceType1Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 931
Or}   Proprietary <Prtry> [1..1] ± 931
34.4.4.21.4.1.1  Code <Cd>
Presence: [1..1]
Definition: Type of tax reference expressed as a code.
Datatype: "PersonIdentificationType7Code" on page 5341
CodeName Name Definition
ATIN AdoptionTaxpayerIdentificationNumber Temporary tax processing number (used
in the domestic adoption of a child).
GTIN GenericTaxIdentificationNumber Generic tax identification number.
ITIN IndividualTaxpayerIdentificationNumber Tax processing number.
34.4.4.21.4.1.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Type of tax reference expressed as a proprietary code.
Proprietary <Prtry> contains the following elements (see "GenericIdentification36" on page 4549 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 4549
   Issuer <Issr> [1..1] Text 4550
   SchemeName <SchmeNm> [0..1] Text 4550
34.4.4.21.4.2  Reference <Ref>
Presence: [1..1]
Definition: Pension scheme tax reference issued to the pension plan by a central organisation.
Datatype: "Max35Text" on page 5403
34.4.4.21.5  PercentageOfTotalTransferValue <PctgOfTtlTrfVal>
Presence: [0..1]
Definition: Percentage of the total transfer value covered by the drawdown.
Datatype: "PercentageRate" on page 5401
34.4.4.21.6  TotalAmountNetDrawdown <TtlAmtNetDrwdwn>
Presence: [0..1]
Definition: Amount that was originally designated for drawdown.
Approved by the Securities SEG on 27 January 2026 sese.011.001.10
TransferInstructionStatusReportV10
Investment Funds - Maintenance 2025 - 2026 931 May 2026
```

